from django.contrib import admin

from .models import Curriculum, Resource


class CurriculumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("subject",)}

admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(Resource)
