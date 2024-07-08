import pandas as pd
from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from cadmember.models import Member
from cadmember.forms import MemberForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


@method_decorator(login_required(login_url='login'), name='dispatch')
class MembersListView(ListView):
    model = Member
    template_name ='members.html'
    context_object_name ='members'
    def get_queryset(self):
        members = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        if search:
             members = members.filter(name__icontains=search)
        return members


    
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewMemberCreateView(CreateView):
     model = Member
     form_class = MemberForm
     template_name = 'new_member.html'    
     success_url = '/members/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class MemberUpdateView(UpdateView):
     model = Member
     form_class = MemberForm
     template_name = 'member_update.html'
     success_url = '/members/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class MemberDeleteView(DeleteView):
     model = Member
     template_name ='member_delete.html'
     success_url = '/members/'
     
@method_decorator(login_required(login_url='login'), name='dispatch')
class MemberDetailView(DetailView):
     model = Member
     template_name ='member_detail.html'

def exporta_excel(request):
     members = Member.objects.all()
     df = pd.DataFrame(members.values('name','cpf', 'date_birth', 'city_birth', 'state_birth', 'date_baptism', 'address', 'cep'))
     response = HttpResponse(content_type='application/ms-excel')
     response['Content-Disposition'] = 'attachment; filename=members.xlsx'
     df.to_excel(response, index=False)
     return response

