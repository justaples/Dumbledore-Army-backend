from django.contrib import admin
from .models import Member, Spell, Meeting

# Register your models here.
admin.site.register(Member)
admin.site.register(Spell)
admin.site.register(Meeting)