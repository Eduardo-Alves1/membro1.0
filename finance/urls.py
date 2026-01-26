from django.contrib import admin
from django.urls import path
from cadmember.views import (
    ContributionListView,
    ContributionCreateView,

)
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    # Contribution URLs
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
]
