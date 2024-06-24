
from django.contrib import admin
from django.urls import path
from cadmember.views import members_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/',members_view, name='members_list')
]
