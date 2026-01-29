from django.urls import path
from finance.views import (
    ContributionListView,
    ContributionCreateView,
    ExpenseListView,
    ExpenseCreateView,
    FinanceDashboardView,
    FinanceReportView,
    export_finance_report,
)

urlpatterns = [
    path(
        "contributions/",
        ContributionListView.as_view(),
        name="contributions_list",
    ),
    path(
        "contributions/new/",
        ContributionCreateView.as_view(),
        name="contribution_new",
    ),
    path(
        "expenses/",
        ExpenseListView.as_view(),
        name="expenses_list",
    ),
    path(
        "expenses/new/",
        ExpenseCreateView.as_view(),
        name="expense_new",
    ),
    path(
        "finance/dashboard/",
        FinanceDashboardView.as_view(),
        name="finance_dashboard",
    ),
    path(
        "finance/report/",
        FinanceReportView.as_view(),
        name="finance_report",
    ),
    path(
        "finance/report/export/",
        export_finance_report,
        name="finance_report_export",
    ),
]
