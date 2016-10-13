from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Page 


def page_list(request):
    pages = Page.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/page_list.html', {'pages': pages})


def page_detail(request, pk):
	page = get_object_or_404(Page, pk=pk)
	return render(request, 'blog/page_detail.html', {'page': page})


