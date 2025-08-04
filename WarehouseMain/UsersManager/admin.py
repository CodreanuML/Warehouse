from django.contrib import admin

from .models import (
	Profile,
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user","role","id_number",)
    search_fields = ("user",)



