from django.contrib import admin
from cadmember.models import Member, City, State

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','cpf', 'address',)
    search_fields = ('cpf', 'name',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('city',)
    search_fields = ('city',)

class StateAdmin(admin.ModelAdmin):
    list_display = ('state',)
    search_fields = ('state',)

admin.site.register(Member, MemberAdmin)

admin.site.register(City, CityAdmin)

admin.site.register(State, StateAdmin)