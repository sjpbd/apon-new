# home/admin.py
from django.contrib import admin
from .models import CarouselImage
from .models import AboutUs
from tinymce.widgets import TinyMCE
from django.db import models
from .models import NewsArticle, Service, TeamMember, FAQ, Fact

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['alt_text', 'image']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    list_display = ['title']


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')
    search_fields = ('title', 'description')
    list_filter = ('title',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)


@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'icon')
