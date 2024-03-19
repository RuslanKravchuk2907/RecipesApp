from django.shortcuts import render, HttpResponse

recipes = [
  {
    'author': 'Dom',
    'title': 'meatball',
    'directions': 'combaine all ingredients',
    'date_posted': 'May 19, 2024'
  },
  {
    'author': 'Dom',
    'title': 'ham',
    'directions': 'combaine all ingredients',
    'date_posted': 'May 10, 2024'
  },
  {
    'author': 'Dom',
    'title': 'BBQ',
    'directions': 'combaine all ingredients',
    'date_posted': 'May 4, 2024'
  },
  {
    'author': 'Dom',
    'title': 'Nuggets',
    'directions': 'combaine all ingredients',
    'date_posted': 'May 11, 2024'
  },
]

# Create your views here.
def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)

def about(request):

    return render(request, "recipes/about.html", {'title':'About us page'})
