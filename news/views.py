from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from .utils import login_required

def news_list(request):
    news_items = News.objects.all().order_by('-pub_date')
    return render(request, 'news/news_list.html', {'news_items': news_items})

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})