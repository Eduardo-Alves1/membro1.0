from django.shortcuts import render
from cadmember.models import Member

def members_view(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})
