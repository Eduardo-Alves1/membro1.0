from django.db import migrations


CAPITALS_BY_STATE = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas",
}


def link_capitals(apps, schema_editor):
    State = apps.get_model("cadmember", "State")
    City = apps.get_model("cadmember", "City")

    for state_name, capital_name in CAPITALS_BY_STATE.items():
        try:
            state = State.objects.get(state=state_name)
        except State.DoesNotExist:
            continue
        
        # Pode haver mais de uma cidade com o mesmo nome; tentamos vincular a capital sem ambiguidades.
        cities = City.objects.filter(city=capital_name)
        if cities.count() == 1:
            city = cities.first()
            if city.state_id is None:
                city.state = state
                city.save(update_fields=["state"])
        else:
            # Como fallback, se houver mais de uma, preferimos a que ainda não tenha estado.
            city = cities.filter(state__isnull=True).first()
            if city:
                city.state = state
                city.save(update_fields=["state"])


def unlink_capitals(apps, schema_editor):
    City = apps.get_model("cadmember", "City")
    City.objects.filter(state__isnull=False, city__in=CAPITALS_BY_STATE.values()).update(state=None)


class Migration(migrations.Migration):
    dependencies = [
        ("cadmember", "0021_city_state"),
    ]

    operations = [
        migrations.RunPython(link_capitals, unlink_capitals),
    ]

