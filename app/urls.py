
from django.contrib import admin
from django.urls import path
from cadmember.views import MembersListView, NewMemberCreateView, MemberUpdateView,MemberDeleteView
from accounts.views import register_view, login_view,logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', MembersListView.as_view(), name='members_list'),
    path('new_member/',NewMemberCreateView.as_view(), name='new_member'),
    path('member/<int:pk>/update',MemberUpdateView.as_view(), name='member_update'),
    path('member/<int:pk>/delete',MemberDeleteView.as_view(), name='member_delete'),
    path('register/', register_view, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name='logout'),  # from django.contrib.auth.views
]
