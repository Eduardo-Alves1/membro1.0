"""
Script para inserir múltiplos membros via Django ORM
Mais seguro e recomendado que SQL puro
"""

import os
import django
import csv
from datetime import datetime

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from cadmember.models import Member


def bulk_insert_from_csv(csv_file_path):
    """
    Insere membros a partir de um arquivo CSV

    Formato esperado do CSV:
    name,cpf,date_birth,city_birth,state_birth,date_baptism,address,cep,bairro,city,state,dizimista,telephone
    """
    members = []

    try:
        with open(csv_file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row_num, row in enumerate(reader, start=2):  # Começa em 2 (header é 1)
                try:
                    # Converter valores
                    dizimista = row["dizimista"].lower() in ("true", "1", "sim", "yes")

                    member = Member(
                        name=row["name"],
                        cpf=row["cpf"],
                        date_birth=datetime.strptime(
                            row["date_birth"], "%Y-%m-%d"
                        ).date(),
                        city_birth=row.get("city_birth") or None,
                        state_birth=row.get("state_birth") or None,
                        date_baptism=datetime.strptime(
                            row["date_baptism"], "%Y-%m-%d"
                        ).date(),
                        address=row["address"],
                        cep=row["cep"],
                        bairro=row.get("bairro") or None,
                        city=row.get("city") or None,
                        state=row.get("state") or None,
                        dizimista=dizimista,
                        telephone=row.get("telephone") or None,
                    )
                    members.append(member)

                except Exception as e:
                    print(f"❌ Erro na linha {row_num}: {e}")
                    continue

        # Inserir em lote
        if members:
            Member.objects.bulk_create(members, ignore_conflicts=True)
            print(f"✅ {len(members)} membros inseridos com sucesso!")
        else:
            print("⚠️  Nenhum membro foi inserido.")

    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {csv_file_path}")
    except Exception as e:
        print(f"❌ Erro geral: {e}")


def bulk_insert_hardcoded():
    """
    Insere membros usando dados hardcoded
    """
    members_data = [
        {
            "name": "João Silva Santos",
            "cpf": "12345678901",
            "date_birth": "1980-05-15",
            "city_birth": "São Paulo",
            "state_birth": "SP",
            "date_baptism": "1995-08-20",
            "address": "Rua das Flores, 123",
            "cep": "01310100",
            "bairro": "Centro",
            "city": "São Paulo",
            "state": "SP",
            "dizimista": True,
            "telephone": "11987654321",
        },
        {
            "name": "Maria Oliveira Costa",
            "cpf": "98765432101",
            "date_birth": "1985-09-22",
            "city_birth": "Rio de Janeiro",
            "state_birth": "RJ",
            "date_baptism": "2000-11-10",
            "address": "Avenida Paulista, 500",
            "cep": "01310200",
            "bairro": "Bela Vista",
            "city": "São Paulo",
            "state": "SP",
            "dizimista": True,
            "telephone": "11988776655",
        },
        {
            "name": "Carlos Mendes Ferreira",
            "cpf": "55544433322",
            "date_birth": "1990-03-10",
            "city_birth": "Belo Horizonte",
            "state_birth": "MG",
            "date_baptism": "2005-06-15",
            "address": "Rua das Pedras, 789",
            "cep": "30130100",
            "bairro": "Funcionários",
            "city": "Belo Horizonte",
            "state": "MG",
            "dizimista": False,
            "telephone": "31987654321",
        },
    ]

    members = [Member(**data) for data in members_data]

    try:
        created = Member.objects.bulk_create(members, ignore_conflicts=True)
        print(f"✅ {len(created)} membros inseridos com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao inserir membros: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("Script de Inserção em Lote de Membros")
    print("=" * 60)

    # Opção 1: Inserir do arquivo CSV
    csv_path = "bulk_members.csv"
    # bulk_insert_from_csv(csv_path)

    # Opção 2: Inserir dados hardcoded
    bulk_insert_hardcoded()
