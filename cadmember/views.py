from django.shortcuts import render, redirect
from cadmember.models import Member
from cadmember.forms import MemberForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View


class MemberListView(View):
      def get(self, request,):
            members = Member.objects.all().order_by('name')
            search = request.GET.get('search')
            if search:
                members = members.filter(name__icontains=search)
            return render(request,'members.html', {'members': members})
          


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
         
      