# admin.py
from django.contrib import admin
from .models import FeatureTab,PortfolioItem, TeamMember

admin.site.register(FeatureTab)
admin.site.register(PortfolioItem)

admin.site.register(TeamMember)
