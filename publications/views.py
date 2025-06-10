from django.shortcuts import render, redirect
from .models import Publication
from .forms import PublicationForm

def publication_list(request):
    publications = Publication.objects.all().order_by('-year')
    category = request.GET.get('category')
    author = request.GET.get('author')
    year = request.GET.get('year')
    topic = request.GET.get('topic')

    if category:
        publications = publications.filter(category=category)
    if author:
        publications = publications.filter(authors__icontains=author)
    if year:
        publications = publications.filter(year=year)
    if topic:
        publications = publications.filter(topic__icontains=topic)

    return render(request, "publications/publications.html", {"publications": publications})

def add_publication(request):
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publication_list')
    else:
        form = PublicationForm()
    return render(request, "publications/add_publication.html", {"form": form})