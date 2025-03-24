import pandas as pd
import openpyxl
from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from cadmember.models import Member
from cadmember.forms import MemberForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)


@method_decorator(login_required(login_url="login"), name="dispatch")
class MembersListView(ListView):
    model = Member
    template_name = "members.html"
    context_object_name = "members"

    def get_queryset(self):
        members = super().get_queryset().order_by("name")
        search = self.request.GET.get("search")
        if search:
            members = members.filter(name__icontains=search)
        return members


@method_decorator(login_required(login_url="login"), name="dispatch")
class NewMemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    template_name = "new_member.html"
    success_url = "/members/"


@method_decorator(login_required(login_url="login"), name="dispatch")
class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = "member_update.html"
    success_url = "/members/"


@method_decorator(login_required(login_url="login"), name="dispatch")
class MemberDeleteView(DeleteView):
    model = Member
    template_name = "member_delete.html"
    success_url = "/members/"


@method_decorator(login_required(login_url="login"), name="dispatch")
class MemberDetailView(DetailView):
    model = Member
    template_name = "member_detail.html"


def exporta_excel(request):
    members = Member.objects.all().order_by("name")
    wb = openpyxl.Workbook()
    ws = wb.active
    # Titulo da planilha
    ws.title = "Membros"

    headers = [
        "ID",
        "NOME",
        "CPF",
        "Data de Nascimento",
        "Cidade de Nascimento",
        "Estado Nascimento",
        "Data de Batismo",
        "Endereço",
        "CEP",
        "TELEFONE",
        "DIZIMISTA",
    ]

    ws.append(headers)

    for m in members:
        ws.append(
            [
                m.id,
                m.name,
                m.cpf,
                m.date_birth.strftime("%d/%m/%Y"),
                m.city_birth.city,
                m.state_birth.state,
                m.date_baptism.strftime("%d/%m/%Y"),
                m.address,
                m.cep,
                m.telephone,
                m.dizimista,
            ]
        )

    # Configurando a resposta para fazer o download como um arquivo Excel
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="membros.xlsx"'

    # Salvando o workbook no buffer da resposta
    wb.save(response)

    return response
