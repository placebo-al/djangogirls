from django.shortcuts import render
from django.utils import timezone
from .models import Page 


def page_list(request):
    pages = Page.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/page_list.html', {'pages': pages})