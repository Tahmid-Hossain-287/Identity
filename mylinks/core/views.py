from django.shortcuts import render
from .models import Link
# Create your views here.

def links(request):

    all_links = Link.objects.all()
    context = {"links" : all_links}
    return render(request, 'core/templates/links.html', context)