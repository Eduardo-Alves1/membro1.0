import openpyxl
from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from cadmember.models import Member, Contribution
from finance.forms import MemberForm, ContributionForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    CreateView,
)

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
