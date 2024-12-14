from django.db import models

# Create your models here.
# models.py
from django.db import models

# models.py
from django.db import models

class FeatureTab(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    additional_description = models.TextField(blank=True, null=True)  # for the second paragraph or italic text
    image_url = models.URLField()
    
    def __str__(self):
        return self.title
    


class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# models.py
from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name





