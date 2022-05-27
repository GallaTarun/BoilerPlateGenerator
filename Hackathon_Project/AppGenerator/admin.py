from django.contrib import admin
from .models import Project, Frontend, Backend

# Register your models here.
admin.site.register(Project)
admin.site.register(Frontend)
admin.site.register(Backend)
