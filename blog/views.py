from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Page, Comment
from .forms import PageForm, CommentForm


def page_list(request):
    pages = Page.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/page_list.html', {'pages': pages})


def page_detail(request, pk):
	page = get_object_or_404(Page, pk=pk)
	return render(request, 'blog/page_detail.html', {'page': page})


@login_required
def page_new(request):
	if request.method == "POST":
		form = PageForm(request.POST)
		if form.is_valid():
			page = form.save(commit=False)
			page.author = request.user
			# page.published_date = timezone.now()
			page.save()
			return redirect('page_detail', pk=page.pk)
	else:
		form = PageForm()
	return render(request, 'blog/page_edit.html', {'form': form})


@login_required
def page_edit(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == "POST":
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            # page.published_date = timezone.now()
            page.save()
            return redirect('page_detail', pk=page.pk)
    else:
        form = PageForm(instance=page)
    return render(request, 'blog/page_edit.html', {'form': form})


@login_required
def page_draft_list(request):
    pages = Page.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/page_draft_list.html', {'pages': pages})


@login_required
def page_publish(request, pk):
    page = get_object_or_404(Page, pk=pk)
    page.publish()
    return redirect('page_detail', pk=pk)


@login_required
def page_remove(request, pk):
	page = get_object_or_404(Page, pk=pk)
	page.delete()
	return redirect('page_list')


def add_comment_to_page(request, pk):
	page = get_object_or_404(Page, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.page = page
			comment.save()
			return redirect('page_detail', pk=page.pk)
	else:
		form = CommentForm()
	return render(request, 'blog/add_comment_to_page.html', {'form': form})


@login_required
def comment_approve(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.approve()
	return redirect('page_detail', pk=comment.page.pk)


@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	page_pk = comment.page.pk
	comment.delete()
	return redirect('page_detail', pk=page.pk)


