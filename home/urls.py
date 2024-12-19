from django.urls import path
from . import views
from .views import treatment_view, team_view, FactsView

app_name = 'home'

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about_us_detail, name='about_us_detail'),
    path('news/', views.news_list, name='news_list'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('services/', views.services_list, name='services_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('treatment/', treatment_view, name='treatment'),
    path('contact/', views.contact, name='contact'),
    path('program/', views.program, name='program'),
    path('team/', team_view, name='team'),
    path('faqs/', views.faq, name='faq'),
    path('facts/', FactsView.as_view(), name='facts'),

]

