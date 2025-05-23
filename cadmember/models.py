from django.db import models


class City(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100, name="city")

    def __str__(self):
        return self.city


class State(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=100, name="state")

    def __str__(self):
        return self.state


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="nome"
    )
    cpf = models.CharField(
        max_length=11, unique=True, blank=False, null=True, verbose_name="cpf"
    )
    date_birth = models.DateField(
        null=False, blank=False, verbose_name="data_nascimento", default=" "
    )
    city_birth = models.ForeignKey(
        City, on_delete=models.PROTECT, related_name="cidade_nascimento", null=True
    )
    state_birth = models.ForeignKey(
        State, on_delete=models.PROTECT, related_name="estado_nascimento", null=True
    )
    date_baptism = models.DateField(
        null=False, blank=False, verbose_name="data_batismo"
    )
    address = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="endereço"
    )
    cep = models.CharField(max_length=8, blank=False, null=False, verbose_name="cep")

    dizimista = models.BooleanField(default=False, verbose_name="dizimista", null=False)

    telephone = models.CharField(
        max_length=11, blank=True, null=True, verbose_name="telefone"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

    def __str__(self) -> str:
        return self.name
