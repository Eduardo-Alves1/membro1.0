from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegisterForm, UserPermissionsForm, GroupForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

@login_required
def register_view(request):
    if not request.user.is_superuser:
        return redirect('members_list')

    # VERIFICA O POST DO USURIO SE É VALIDO
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            if username and User.objects.filter(username__iexact=username).exists():
                form.add_error("username", "Nome de usuario ja existe.")
            else:
                try:
                    form.save()
                    return redirect("members_list")
                except IntegrityError:
                    form.add_error("username", "Nome de usuario ja existe.")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("members_list")
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, "login.html", {"login_form": login_form})


def logout_view(request):
    logout(request)
    return redirect("login")


def _superuser_only(request):
    if not request.user.is_superuser:
        return False
    return True


@login_required
def users_list_view(request):
    if not _superuser_only(request):
        return redirect("members_list")

    search = request.GET.get("search", "")
    users = User.objects.all().order_by("username")
    if search:
        users = users.filter(username__icontains=search)
    return render(request, "users_list.html", {"users": users, "search": search})


@login_required
def user_permissions_view(request, user_id):
    if not _superuser_only(request):
        return redirect("members_list")

    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        form = UserPermissionsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users_list")
    else:
        form = UserPermissionsForm(instance=user)
    return render(request, "user_permissions.html", {"form": form, "user_obj": user})


@login_required
def groups_list_view(request):
    if not _superuser_only(request):
        return redirect("members_list")

    groups = Group.objects.all().order_by("name")
    return render(request, "groups_list.html", {"groups": groups})


@login_required
def group_create_view(request):
    if not _superuser_only(request):
        return redirect("members_list")

    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("groups_list")
    else:
        form = GroupForm()
    return render(request, "group_form.html", {"form": form, "title": "Novo Grupo"})


@login_required
def group_update_view(request, group_id):
    if not _superuser_only(request):
        return redirect("members_list")

    group = get_object_or_404(Group, pk=group_id)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("groups_list")
    else:
        form = GroupForm(instance=group)
    return render(
        request, "group_form.html", {"form": form, "title": "Editar Grupo"}
    )
