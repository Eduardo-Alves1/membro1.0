from django.shortcuts import render, redirect
from cadmember.models import Member
from cadmember.forms import MemberForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def members_view(request):
    members = Member.objects.all().order_by('name')
    search = request.GET.get('search')
    if search:
        members = members.filter(name__icontains=search)
    return render(request, 'members.html', {'members': members})

@login_required(login_url='/login')
def new_member_view(request):
        if request.method == 'POST':
             new_member_form = MemberForm(request.POST)
             if new_member_form.is_valid():
                 new_member_form.save()
                 return redirect('members_list')
        else:
             new_member_form = MemberForm()
        return render(request, 'new_member.html', {'new_member_form': new_member_form})
             