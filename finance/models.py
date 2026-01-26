from django.db import models
from cadmember.models import Member

# Create your models here.


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
    value = models.DecimalField(verbose_name="Valor", max_digits=10, decimal_places=2)
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
        return f"{self.member.name} - {self.type} - {self.value} em {self.date}"
