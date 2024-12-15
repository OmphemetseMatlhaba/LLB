from django.shortcuts import render
from .models import FeatureTab, PortfolioItem, TeamMember


# Create your views here.

def index(request):
        tabs = FeatureTab.objects.all() 
        portfolio_items = PortfolioItem.objects.all() # Fetch all tab data
        team_members = TeamMember.objects.all()  # Fetch all team members
        return render(request, 'index.html', {'tabs': tabs ,'portfolio_items': portfolio_items, 'team_members': team_members})
# views.py
def portfolio_detail(request, id):
    portfolio_item = PortfolioItem.objects.get(id=id)
    return render(request, 'portfolio_detail.html', {'item': portfolio_item})



def about(request):
 return render(request, 'about.html')