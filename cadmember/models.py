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
    date_baptism = models.DateField(
        null=False, blank=False, verbose_name="Data de Batismo"
    )
    address = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Endereço"
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

class Contribution(models.Model):
    TYPE_CHOICES = [
        ("DIZ", "Dízimo"),
        ("OFE", "Oferta Geral"),
        ("ESP", "Oferta Especial"),
    ]
    PAYMENT_CHOICES = [
        ("DIN", "Dinheiro"),
        ("PIX", "PIX"),
        ("CAR", "Cartão de Débito/Crédito"),
    ]

    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(
        Member,
        on_delete=models.PROTECT,
        verbose_name="Membro",
        related_name="contributions",
    )
    value = models.DecimalField(
        verbose_name="Valor", max_digits=10, decimal_places=2
    )
    date = models.DateField(verbose_name="Data da contribuição")
    type = models.CharField(
        max_length=3, choices=TYPE_CHOICES, verbose_name="Tipo de contribuição"
    )
    payment_method = models.CharField(
        max_length=3, choices=PAYMENT_CHOICES, verbose_name="Meio de pagamento"
    )
    notes = models.TextField(verbose_name="Observações", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Contribuição"
        verbose_name_plural = "Contribuições"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.member.name} - {self.get_type_display()} - R$ {self.value}"
