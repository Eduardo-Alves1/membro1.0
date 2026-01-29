from django.contrib import admin
from django.urls import path
from cadmember.views import (
    MembersListView,
    NewMemberCreateView,
    MemberUpdateView,
    MemberDeleteView,
    MemberDetailView,
    exporta_excel,
)

urlpatterns = [
    path("members/", MembersListView.as_view(), name="members_list"),
    path("new_member/", NewMemberCreateView.as_view(), name="new_member"),
    path("member/<int:pk>/update", MemberUpdateView.as_view(), name="member_update"),
    path("member/<int:pk>/", MemberDetailView.as_view(), name="member_detail"),
    path("member/<int:pk>/delete", MemberDeleteView.as_view(), name="member_delete"),
    path("exportar-excel/", exporta_excel, name="exportar_excel"),
]
