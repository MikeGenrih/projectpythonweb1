from django.shortcuts import render, redirect
from django.http import HttpResponse
from unicodedata import category

from .models import  Products, Category, Comment
from .forms import CommentForm


def home(request, category):

    context = {

        "category": Category.objects.all(),
    }
    if category == 'home':
        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                product = Products.objects.get(id=form.cleaned_data['id'])
                new_comment = Comment.objects.create(
                    product=product,
                    text=form.cleaned_data['text'],
                )

                context['comment_form'] = form

                context['comment_list'] = Comment.objects.all()

        else:
            form = CommentForm()
            context['comment_form'] = form
            context['comment_list'] = Comment.objects.all()

        context['products'] =  Products.objects.all()

    else:
        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():

                product = Products.objects.get(id=form.cleaned_data['id'])
                new_comment = Comment.objects.create(
                    product=product,
                    text=form.cleaned_data['text'],
                )

                context['comment_form'] = form

                # comment = form.save(commit=False)
                # comment.product = Products.objects.get(id=product_id)
                # comment.save()

                context['comment_list'] = Comment.objects.all()
        else:
            form = CommentForm()
            context['comment_form'] = form
            context['comment_list'] = Comment.objects.all()

        context['products'] = Products.objects.filter(category__title=category)

    return render(request, 'books/home.html', context=context,)


