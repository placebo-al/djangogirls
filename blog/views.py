from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Page
from .forms import PageForm


def page_list(request):
    pages = Page.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/page_list.html', {'pages': pages})


def page_detail(request, pk):
	page = get_object_or_404(Page, pk=pk)
	return render(request, 'blog/page_detail.html', {'page': page})


def page_new(request):
	if request.method == "POST":
		form = PageForm(request.POST)
		if form.is_valid():
			page = form.save(commit=False)
			page.author = request.user
			page.published_date = timezone.now()
			page.save()
			return redirect('page_detail', pk=page.pk)
	else:
		form = PageForm()
	return render(request, 'blog/page_edit.html', {'form': form})


def page_edit(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == "POST":
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.published_date = timezone.now()
            page.save()
            return redirect('page_detail', pk=page.pk)
    else:
        form = PageForm(instance=page)
    return render(request, 'blog/page_edit.html', {'form': form})


