from django.contrib import admin
from cadmember.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','cpf', 'address',)
    search_fields = ('cpf', 'name',)


admin.site.register(Member, MemberAdmin)