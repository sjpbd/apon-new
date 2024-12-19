# home/models.py
from django.db import models
from tinymce.models import HTMLField

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.alt_text or f"Image {self.id}"


class AboutUs(models.Model):
    title = models.CharField(max_length=255, default="About Us")
    short_description = HTMLField(help_text="This will be shown on the home page.")
    long_description = HTMLField(help_text="This will be shown on the detailed page.")
    infrastructure = HTMLField("Infrastructure of APON")
    membership_affiliation = HTMLField("Membership & Affiliation")
    awards = HTMLField("Awards")
    goal = HTMLField("Goal")
    objectives = HTMLField("Objectives of APON")
    program_activities = HTMLField("Program Activities")

    main_image = models.ImageField(
        upload_to='about_us/', 
        default='path/to/default/main_image.jpg', 
        help_text="Main image for the home page."
    )
    additional_images = models.ImageField(
        upload_to='about_us/', 
        blank=True, 
        null=True, 
        help_text="Additional images for the detailed page."
    )

    class Meta:
        verbose_name = 'About Us Section'
        verbose_name_plural = 'About Us Section'

    def __str__(self):
        return self.title



class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    full_description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    published_date = models.DateField()
    
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    short_description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Fact(models.Model):
    icon = models.CharField(max_length=100, help_text="Name of the Material Icon (e.g., event, people).")
    number = models.CharField(max_length=100, help_text="Number to display, e.g., '26', '1500+', etc.")
    label = models.CharField(max_length=100, help_text="Label for the fact (e.g., 'YEARS').")

    def __str__(self):
        return self.label





