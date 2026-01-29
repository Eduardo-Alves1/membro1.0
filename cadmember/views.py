import openpyxl
from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from cadmember.models import Member
from finance.models import Contribution
from cadmember.forms import MemberForm
from finance.forms import ContributionForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.messages.views import SuccessMessageMixin


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
class NewMemberCreateView(SuccessMessageMixin, CreateView):
    model = Member
    form_class = MemberForm
    template_name = "new_member.html"
    success_url = "/members/"
    success_message = "Cadastro realizado com sucesso!"


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


# --- Contribution Views ---


@method_decorator(login_required(login_url="login"), name="dispatch")
class ContributionListView(ListView):
    model = Contribution
    template_name = "contributions_list.html"
    context_object_name = "contributions"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by("-date")
        search_member = self.request.GET.get("search_member")
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")

        if search_member:
            queryset = queryset.filter(member__name__icontains=search_member)
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        return queryset


@method_decorator(login_required(login_url="login"), name="dispatch")
class ContributionCreateView(CreateView):
    model = Contribution
    form_class = ContributionForm
    template_name = "contribution_form.html"
    success_url = "/contributions/"


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
