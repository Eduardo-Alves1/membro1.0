from django.urls import path
from accounts.views import (
    register_view,
    login_view,
    logout_view,
    users_list_view,
    user_permissions_view,
    groups_list_view,
    group_create_view,
    group_update_view,
)

urlpatterns = [
    path("register/", register_view, name="register"),
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("users/", users_list_view, name="users_list"),
    path("users/<int:user_id>/permissions/", user_permissions_view, name="user_permissions"),
    path("groups/", groups_list_view, name="groups_list"),
    path("groups/new/", group_create_view, name="group_new"),
    path("groups/<int:group_id>/edit/", group_update_view, name="group_edit"),
]
