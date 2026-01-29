from django.db import models
from cadmember.models import Member


class Contribution(models.Model):
    TYPE_CHOICES = [
        ("DIZ", "Dizimo"),
        ("OFE", "Oferta Geral"),
        ("ESP", "Oferta Especial"),
    ]
    PAYMENT_CHOICES = [
        ("DIN", "Dinheiro"),
        ("PIX", "PIX"),
        ("CAR", "Cartao de Debito/Credito"),
    ]

    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(
        Member,
        on_delete=models.PROTECT,
        verbose_name="Membro",
        related_name="contributions",
    )
    value = models.DecimalField(verbose_name="Valor", max_digits=10, decimal_places=2)
    date = models.DateField(verbose_name="Data da contribuicao")
    type = models.CharField(
        max_length=3, choices=TYPE_CHOICES, verbose_name="Tipo de contribuicao"
    )
    payment_method = models.CharField(
        max_length=3, choices=PAYMENT_CHOICES, verbose_name="Meio de pagamento"
    )
    notes = models.TextField(verbose_name="Observacoes", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Contribuicao"
        verbose_name_plural = "Contribuicoes"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.member.name} - {self.type} - {self.value} em {self.date}"


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("MAN", "Manutencao"),
        ("MIS", "Missoes"),
        ("SOC", "Social"),
        ("ADM", "Administrativo"),
        ("OUT", "Outros"),
    ]
    PAYMENT_CHOICES = Contribution.PAYMENT_CHOICES

    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, verbose_name="Descricao")
    category = models.CharField(
        max_length=3, choices=CATEGORY_CHOICES, verbose_name="Categoria"
    )
    value = models.DecimalField(verbose_name="Valor", max_digits=10, decimal_places=2)
    date = models.DateField(verbose_name="Data da saida")
    payment_method = models.CharField(
        max_length=3, choices=PAYMENT_CHOICES, verbose_name="Meio de pagamento"
    )
    notes = models.TextField(verbose_name="Observacoes", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Saida"
        verbose_name_plural = "Saidas"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.description} - {self.value} em {self.date}"
