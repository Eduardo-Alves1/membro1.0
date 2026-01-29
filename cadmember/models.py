from django.db import models


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Nome"
    )
    cpf = models.CharField(
        max_length=11, unique=True, blank=False, null=True, verbose_name="CPF"
    )
    date_birth = models.DateField(
        null=False, blank=False, verbose_name="Data de Nascimento", default=" "
    )
    city_birth = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Cidade de Nascimento",
    )
    state_birth = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Estado de Nascimento",
    )
    birth_cep = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        verbose_name="CEP de Nascimento",
    )
    birth_address = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Endereco de Nascimento",
    )
    birth_address_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Numero Nascimento",
    )
    birth_bairro = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Bairro de Nascimento",
    )
    date_baptism = models.DateField(
        null=False, blank=False, verbose_name="Data de Batismo"
    )
    address = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Endereço"
    )
    address_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Numero",
    )
    cep = models.CharField(max_length=8, blank=False, null=False, verbose_name="CEP")
    bairro = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Bairro"
    )
    city = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Cidade"
    )
    state = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Estado"
    )

    dizimista = models.BooleanField(default=False, verbose_name="É Dizimista?", null=False)

    telephone = models.CharField(
        max_length=11, blank=True, null=True, verbose_name="Telefone"
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
