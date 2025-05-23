# # views.py
# from django.shortcuts import render
# from .utils import fetch_live_news
# from .models import NewsItem

# def news_list(request):
#     news = NewsItem.objects.order_by('-published_date')
#     return render(request, 'news/news_list.html', {'news': news})

# # news/views.py
# def live_news_view(request):
#     news = fetch_live_news()
#     print("Fetched news:", news)  # DEBUG
#     return render(request, 'news/news_list.html', {'news': news})
# views.py
# news/views.py
# news/views.py
######################################################
# from django.shortcuts import render

# def news_list(request):
    
#     return render(request, 'news/news_list.html')
#############################################################

# news/views.py
from django.shortcuts import render, get_object_or_404
from .models import News


def news_list(request):
    news_items = News.objects.all()  # Sare news items fetch karo
    return render(request, 'news/news_list.html', {'news_items': news_items})
#######################################################################################
def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news_item})

############################################################################################
def news_list(request):
   news = News.objects.all().order_by('published_date')  # Correct field
   return render(request, 'news/news_list.html', {'news': news})








