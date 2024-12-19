# home/views.py
from django.shortcuts import render, get_object_or_404
from .models import CarouselImage, AboutUs, NewsArticle, Service, TeamMember, FAQ, Fact
from django.views.generic import TemplateView

def home(request):
    images = CarouselImage.objects.all()
    about_us = AboutUs.objects.first()
    news_articles = NewsArticle.objects.all().order_by('-published_date')[:4]  # Get the latest 4 news articles
    faqs = FAQ.objects.all()
    facts = Fact.objects.all()

    context = {
        'images': images,
        'image_count': images.count(),
        'about_us': about_us,
        'news_articles': news_articles,
        'faqs': faqs,
        'facts': facts,
    }

    return render(request, 'home/home.html', context)

def about_us_detail(request):
    about_us = AboutUs.objects.first()
    return render(request, 'home/about_detail.html', {'about_us': about_us})

def news_list(request):
    news_articles = NewsArticle.objects.all().order_by('-published_date')
    return render(request, 'home/news_list.html', {'news_articles': news_articles})

def news_detail(request, pk):
    news_article = get_object_or_404(NewsArticle, pk=pk)
    latest_news = NewsArticle.objects.exclude(pk=pk).order_by('-published_date')[:5]
    return render(request, 'home/news_detail.html', {'news_article': news_article, 'latest_news': latest_news})

def services_list(request):
    services = Service.objects.all()  
    return render(request, 'home/service_detail.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'home/service_detail.html', {'service': service})

def treatment_view(request):
    return render(request, 'home/treatment.html')

def contact(request):
    return render(request, 'home/contact.html')


def program(request):
    return render(request, 'home/program.html')

def team_view(request):
    team_members = TeamMember.objects.all()
    return render(request, 'home/team.html', {'team_members': team_members})


def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'home/faq.html', {'faqs': faqs})


class FactsView(TemplateView):
    template_name = 'home/facts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['facts'] = Fact.objects.all()
        return context
