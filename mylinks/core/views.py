from django.shortcuts import render
from .models import Link
# Create your views here.

def links(request):

    all_links = Link.objects.all()
    context = {"links" : all_links}
    return render(request, 'core/templates/links.html', context)


def click_link(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    link.clicks += 1
    link.save()
    return redirect(link.url)