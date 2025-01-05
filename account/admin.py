from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from account.models import Profession, Service, Website

UserModel = get_user_model()


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    # Add 'introduction' to the fieldsets dynamically
    UserAdmin.fieldsets += (
        ("About Page Text", {"fields": ("introduction",)}),
        ("Photo", {"fields": ("photo",)}),
        ("Can be contacted?", {"fields": ("can_be_contacted",)}),
        ("can data be shared?", {"fields": ("can_data_be_shared",)}),
        ("Professions", {"fields": ("professions",)}),
        ("Services", {"fields": ("services",)}),
        ("Websites", {"fields": ("websites",)}),
    )


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ["name", "publish", "created", "updated"]
    list_filter = ["name", "publish", "created", "updated"]
    search_fields = ["name", "publish", "created", "updated"]
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "created"
    ordering = ["name", "publish"]
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "publish", "created", "updated"]
    list_filter = ["name", "publish", "created", "updated"]
    search_fields = ["name", "publish", "created", "updated"]
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "created"
    ordering = ["name", "publish"]
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ["name", "publish", "created", "updated"]
    list_filter = ["name", "publish", "created", "updated"]
    search_fields = ["name", "publish", "created", "updated"]
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "created"
    ordering = ["name", "publish"]
    show_facets = admin.ShowFacets.ALWAYS
