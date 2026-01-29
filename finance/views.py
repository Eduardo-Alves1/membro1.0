import json
import openpyxl
import calendar
from datetime import date, datetime, timedelta
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    CreateView,
    TemplateView,
)

from finance.forms import ContributionForm, ExpenseForm
from finance.models import Contribution, Expense


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


@method_decorator(login_required(login_url="login"), name="dispatch")
class ExpenseListView(ListView):
    model = Expense
    template_name = "expenses_list.html"
    context_object_name = "expenses"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by("-date")
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")
        category = self.request.GET.get("category")

        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        if category:
            queryset = queryset.filter(category=category)
        return queryset


@method_decorator(login_required(login_url="login"), name="dispatch")
class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "expense_form.html"
    success_url = "/expenses/"


@method_decorator(login_required(login_url="login"), name="dispatch")
class FinanceDashboardView(TemplateView):
    template_name = "finance_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        period = self.request.GET.get("period", "year")
        year = int(self.request.GET.get("year", today.year))
        month_value = self.request.GET.get("month")
        start_value = self.request.GET.get("start_date")
        end_value = self.request.GET.get("end_date")

        def aggregate_totals(entries, exits):
            total_entries = (
                entries.aggregate(total=Sum("value")).get("total") or Decimal("0.00")
            )
            total_exits = (
                exits.aggregate(total=Sum("value")).get("total") or Decimal("0.00")
            )
            return total_entries, total_exits, total_entries - total_exits

        def series_by_day(start_date, end_date, label_format):
            entries = Contribution.objects.filter(date__gte=start_date, date__lte=end_date)
            exits = Expense.objects.filter(date__gte=start_date, date__lte=end_date)

            entries_by_day = (
                entries.annotate(day=TruncDay("date"))
                .values("day")
                .annotate(total=Sum("value"))
                .order_by("day")
            )
            exits_by_day = (
                exits.annotate(day=TruncDay("date"))
                .values("day")
                .annotate(total=Sum("value"))
                .order_by("day")
            )

            entries_map = {item["day"]: item["total"] for item in entries_by_day}
            exits_map = {item["day"]: item["total"] for item in exits_by_day}

            labels = []
            entries_values = []
            exits_values = []
            current_day = start_date
            while current_day <= end_date:
                labels.append(current_day.strftime(label_format))
                entries_values.append(float(entries_map.get(current_day) or 0))
                exits_values.append(float(exits_map.get(current_day) or 0))
                current_day += timedelta(days=1)

            total_entries, total_exits, balance = aggregate_totals(entries, exits)
            return labels, entries_values, exits_values, total_entries, total_exits, balance

        if period == "month":
            try:
                month_date = datetime.strptime(month_value or "", "%Y-%m").date()
            except ValueError:
                month_date = today
            year = month_date.year
            month = month_date.month
            start_date = date(year, month, 1)
            last_day = calendar.monthrange(year, month)[1]
            end_date = date(year, month, last_day)
            label_suffix = month_date.strftime("%Y-%m")
            month_value = month_date.strftime("%Y-%m")
            day_labels, entries_values, exits_values, total_entries, total_exits, balance = series_by_day(
                start_date,
                end_date,
                "%d %b",
            )
            chart_title = f"Entradas x Saidas por dia ({label_suffix})"
        elif period == "range":
            try:
                start_date = datetime.strptime(start_value or "", "%Y-%m-%d").date()
            except ValueError:
                start_date = date(year, 1, 1)
            try:
                end_date = datetime.strptime(end_value or "", "%Y-%m-%d").date()
            except ValueError:
                end_date = today
            if end_date < start_date:
                start_date, end_date = end_date, start_date

            label_suffix = f"{start_date.strftime('%Y-%m-%d')} a {end_date.strftime('%Y-%m-%d')}"
            day_labels, entries_values, exits_values, total_entries, total_exits, balance = series_by_day(
                start_date,
                end_date,
                "%d %b",
            )
            chart_title = f"Entradas x Saidas por dia ({label_suffix})"
        else:
            start_date = date(year, 1, 1)
            end_date = date(year, 12, 31)
            label_suffix = str(year)

            entries = Contribution.objects.filter(date__gte=start_date, date__lte=end_date)
            exits = Expense.objects.filter(date__gte=start_date, date__lte=end_date)

            entries_by_month = (
                entries.annotate(month=TruncMonth("date"))
                .values("month")
                .annotate(total=Sum("value"))
                .order_by("month")
            )
            exits_by_month = (
                exits.annotate(month=TruncMonth("date"))
                .values("month")
                .annotate(total=Sum("value"))
                .order_by("month")
            )

            month_labels = []
            entries_values = []
            exits_values = []
            exits_map = {item["month"]: item["total"] for item in exits_by_month}
            entries_map = {item["month"]: item["total"] for item in entries_by_month}

            for month in range(1, 13):
                current_month = date(year, month, 1)
                month_labels.append(calendar.month_abbr[month])
                entries_values.append(float(entries_map.get(current_month) or 0))
                exits_values.append(float(exits_map.get(current_month) or 0))
            chart_title = f"Entradas x Saidas por mes ({label_suffix})"

            total_entries, total_exits, balance = aggregate_totals(entries, exits)

        context.update(
            {
                "total_entries": total_entries,
                "total_exits": total_exits,
                "balance": balance,
                "chart_labels": json.dumps(
                    day_labels if period in ["month", "range"] else month_labels
                ),
                "chart_entries": json.dumps(entries_values),
                "chart_exits": json.dumps(exits_values),
                "chart_title": chart_title,
                "period": period,
                "year": year,
                "month": month_value or "",
                "start_date": start_value or "",
                "end_date": end_value or "",
            }
        )
        return context


@method_decorator(login_required(login_url="login"), name="dispatch")
class FinanceReportView(TemplateView):
    template_name = "finance_report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")

        contributions = Contribution.objects.all()
        expenses = Expense.objects.all()

        if start_date:
            contributions = contributions.filter(date__gte=start_date)
            expenses = expenses.filter(date__gte=start_date)
        if end_date:
            contributions = contributions.filter(date__lte=end_date)
            expenses = expenses.filter(date__lte=end_date)

        contributions_total = contributions.aggregate(total=Sum("value")).get("total") or Decimal("0.00")
        expenses_total = expenses.aggregate(total=Sum("value")).get("total") or Decimal("0.00")
        balance = contributions_total - expenses_total

        by_type_raw = (
            contributions.values("type")
            .annotate(total=Sum("value"))
            .order_by("type")
        )
        type_labels = dict(Contribution.TYPE_CHOICES)
        by_type = [
            {"type": type_labels.get(row["type"], row["type"]), "total": row["total"]}
            for row in by_type_raw
        ]

        context.update(
            {
                "contributions_total": contributions_total,
                "expenses_total": expenses_total,
                "balance": balance,
                "by_type": by_type,
                "start_date": start_date or "",
                "end_date": end_date or "",
            }
        )
        return context


@login_required(login_url="login")
def export_finance_report(request):
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    contributions = Contribution.objects.all()
    expenses = Expense.objects.all()

    if start_date:
        contributions = contributions.filter(date__gte=start_date)
        expenses = expenses.filter(date__gte=start_date)
    if end_date:
        contributions = contributions.filter(date__lte=end_date)
        expenses = expenses.filter(date__lte=end_date)

    wb = openpyxl.Workbook()
    ws_entries = wb.active
    ws_entries.title = "Entradas"
    ws_entries.append(["Data", "Membro", "Tipo", "Valor", "Pagamento", "Notas"])

    for c in contributions:
        ws_entries.append(
            [
                c.date.strftime("%d/%m/%Y"),
                c.member.name,
                c.get_type_display(),
                float(c.value),
                c.get_payment_method_display(),
                c.notes or "",
            ]
        )

    ws_exits = wb.create_sheet(title="Saidas")
    ws_exits.append(["Data", "Descricao", "Categoria", "Valor", "Pagamento", "Notas"])

    for e in expenses:
        ws_exits.append(
            [
                e.date.strftime("%d/%m/%Y"),
                e.description,
                e.get_category_display(),
                float(e.value),
                e.get_payment_method_display(),
                e.notes or "",
            ]
        )

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="financeiro.xlsx"'
    wb.save(response)
    return response
