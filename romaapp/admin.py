from django.contrib import admin

from romaapp.forms import ContactForm
from .models import Contact, Home, About, Profile, Category, Skills, Portfolio

# Register your models here.

# HOME
admin.site.register(Home)


# ABOUT
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]


# SKILLS
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]


# PORTFOILO
admin.site.register(Portfolio)

# CONTACT
admin.site.register(Contact)
class ContactAdmin(admin.TabularInline):
    inlines = [
        ContactForm,
    ]