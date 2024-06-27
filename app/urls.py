
from django.contrib import admin
from django.urls import path
from cadmember.views import members_view,new_member_view
from accounts.views import register_view, login_view,logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/',members_view, name='members_list'),
    path('new_member/',new_member_view, name='new_member'),
    path('register/', register_view, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name='logout'),  # from django.contrib.auth.views
]
