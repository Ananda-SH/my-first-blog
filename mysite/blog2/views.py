# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from blog2.forms import RegisForm
from blog2.models import Registration


def home_page(request):
    if request.method == 'POST':
        print('post method called')
        form = RegisForm(request.POST)
        print('regisform', request.POST['name'])
        print('regisform', request.POST['number'])
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            print('saved')
            return redirect('details_page')
    else:
        print('add method is called')
    return render(request, 'blog2/home.html', {'form':RegisForm})


def details_page(request):
    print('sending to the details page')
    details = Registration.objects.all()
    print('details', details.values())
    return render(request, 'blog2/details.html', {'posts': details})


def details_edit(request, pk):
    print('details_edit', request, pk)
    post = get_object_or_404(Registration, pk=pk)
    form = RegisForm(request.POST)
    if request.method == 'POST':
        print('saving edited data')
        if form.is_valid:
            post = form.save(commit=False)
            post.save()
            return redirect('details_page')
    else:
        print('sending for editing')
        form = RegisForm(instance=post)
        return render(request, 'blog2/edit_reg.html', {'form':form})




# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})