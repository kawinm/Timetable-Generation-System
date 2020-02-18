from django.contrib import admin

from .models import Staff, Group, Subject

admin.site.register(Staff)
admin.site.register(Group)
admin.site.register(Subject)