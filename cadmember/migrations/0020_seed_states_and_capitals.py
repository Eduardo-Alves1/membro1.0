from django.db import migrations


STATES = [
    "Acre",
    "Alagoas",
    "Amapá",
    "Amazonas",
    "Bahia",
    "Ceará",
    "Distrito Federal",
    "Espírito Santo",
    "Goiás",
    "Maranhão",
    "Mato Grosso",
    "Mato Grosso do Sul",
    "Minas Gerais",
    "Pará",
    "Paraíba",
    "Paraná",
    "Pernambuco",
    "Piauí",
    "Rio de Janeiro",
    "Rio Grande do Norte",
    "Rio Grande do Sul",
    "Rondônia",
    "Roraima",
    "Santa Catarina",
    "São Paulo",
    "Sergipe",
    "Tocantins",
]

CAPITALS = [
    "Rio Branco",
    "Maceió",
    "Macapá",
    "Manaus",
    "Salvador",
    "Fortaleza",
    "Brasília",
    "Vitória",
    "Goiânia",
    "São Luís",
    "Cuiabá",
    "Campo Grande",
    "Belo Horizonte",
    "Belém",
    "João Pessoa",
    "Curitiba",
    "Recife",
    "Teresina",
    "Rio de Janeiro",
    "Natal",
    "Porto Alegre",
    "Porto Velho",
    "Boa Vista",
    "Florianópolis",
    "São Paulo",
    "Aracaju",
    "Palmas",
]


def seed_states_and_capitals(apps, schema_editor):
    State = apps.get_model("cadmember", "State")
    City = apps.get_model("cadmember", "City")

    # Popular Estados
    for state_name in STATES:
        State.objects.get_or_create(state=state_name)

    # Popular capitais (mínimo para que City tenha dados úteis imediatamente)
    for city_name in CAPITALS:
        City.objects.get_or_create(city=city_name)


def undo_seed(apps, schema_editor):
    State = apps.get_model("cadmember", "State")
    City = apps.get_model("cadmember", "City")

    State.objects.filter(state__in=STATES).delete()
    City.objects.filter(city__in=CAPITALS).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("cadmember", "0019_alter_member_created_at_alter_member_updated_at"),
    ]

    operations = [
        migrations.RunPython(seed_states_and_capitals, undo_seed),
    ]

