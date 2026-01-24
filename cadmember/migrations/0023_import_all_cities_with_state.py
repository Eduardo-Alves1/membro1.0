from django.db import migrations


IBGE_MUNICIPIOS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios?orderBy=nome"


def import_cities(apps, schema_editor):
    """
    Importa todos os municípios do Brasil a partir da API do IBGE e vincula ao Estado.
    Idempotente: usa get_or_create por (city, state).
    Se não houver acesso à internet, a migration não falha; apenas registra a situação.
    """
    State = apps.get_model("cadmember", "State")
    City = apps.get_model("cadmember", "City")

    try:
        import json
        from urllib.request import urlopen
        from urllib.error import URLError, HTTPError

        with urlopen(IBGE_MUNICIPIOS_URL, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except (TimeoutError, URLError, HTTPError, Exception):
        # Sem internet ou erro inesperado: não falhar a migration.
        print("[IBGE] Não foi possível consultar a API durante a migration. Pulei a importação de municípios.")
        return

    total = 0
    criados = 0
    atualizados = 0

    for m in data:
        # Estrutura esperada: m["nome"], m["microrregiao"]["mesorregiao"]["UF"]["nome"]
        try:
            city_name = m.get("nome")
            uf = (
                m.get("microrregiao", {})
                .get("mesorregiao", {})
                .get("UF", {})
                .get("nome")
            )
        except Exception:
            continue

        if not city_name or not uf:
            continue

        state = State.objects.filter(state=uf).first()
        if not state:
            # Estado não encontrado (deveria existir pela seed anterior)
            continue

        total += 1

        # Tentar vincular caso já exista cidade homônima sem estado
        existing_unlinked = City.objects.filter(city=city_name, state__isnull=True).first()
        if existing_unlinked:
            existing_unlinked.state = state
            existing_unlinked.save(update_fields=["state"])
            atualizados += 1
            continue

        # Criar se não existir a combinação (city, state)
        obj, created = City.objects.get_or_create(city=city_name, state=state)
        if created:
            criados += 1

    print(f"[IBGE] Municípios processados: {total}, criados: {criados}, atualizados: {atualizados}")


class Migration(migrations.Migration):
    dependencies = [
        ("cadmember", "0022_link_capitals_to_states"),
    ]

    operations = [
        migrations.RunPython(import_cities, migrations.RunPython.noop),
    ]

