
from django.contrib import admin
from django.urls import path
from cadmember.views import members_view,new_member_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/',members_view, name='members_list'),
    path('new_member/',new_member_view, name='new_member'),
]
