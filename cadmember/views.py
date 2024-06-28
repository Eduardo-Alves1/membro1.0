from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cadmember.models import Member
from cadmember.forms import MemberForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, CreateView


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
#O código selecionado na classe `MembersListView` é responsável por lidar com a funcionalidade de pesquisa no aplicativo Django.

#No método `get_queryset`, ele primeiro recupera todos os objetos `Member` do banco de dados usando o método `super().get_queryset()`. Em seguida, ele ordena os membros pelo nome usando o método `order_by('name')`.

#Depois, ele verifica se uma consulta de pesquisa é fornecida nos parâmetros GET da solicitação. Se uma consulta de pesquisa for encontrada, ele filtra os membros com base no nome usando o método `filter(name__icontains=search)`. O lookup `icontains` executa uma pesquisa case-insensitive para a consulta de pesquisa fornecida dentro dos nomes dos membros.

#Por fim, ele retorna os membros filtrados ou ordenados como o queryset para a ListView. Isso permite que a ListView exiba os resultados da pesquisa ou a lista completa de membros com base na consulta de pesquisa.
          


class NewMemberView(View):
    def get(self, request):
        new_member_form = MemberForm()
        return render(request, 'new_member.html', {'new_member_form': new_member_form})
    
    def post(self, request):
         new_member_form = MemberForm(request.POST)
         if new_member_form.is_valid():
                 new_member_form.save()
                 return redirect('members_list')
         return render(request, 'new_member.html', {'new_member_form': new_member_form})
    
class NewMemberCreateView(CreateView):
     model = Member
     form_class = MemberForm
     template_name = 'new_member.html'    
     success_url = '/members/'
         
      