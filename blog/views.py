from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .forms import ContactForm, CommentForm
from .bot import send_message
from .models import Article, Portfolio,Comment

def home_view(request):

    articles = Article.objects.all()
    portfolios = Portfolio.objects.all().order_by("-id")
    
   

    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            description = form.cleaned_data["description"]

            send_message(name, email, phone_number, description)


            form.save()

            form = ContactForm()

            messages.success(request, 'Your message has been sent successfully.')
            return HttpResponseRedirect(reverse('home-page'))
        else:
            messages.error(request, 'Please correct the errors below.')

    context = {
        "form": form,
        "articles": articles,
        "portfolios": portfolios,
    }

    return render(request, "theme-particle.html", context)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Article, Comment
from .forms import CommentForm

def blog_view(request, id):
    article = get_object_or_404(Article, id=id)

    # Faqat GET so‘rovida view_count oshiriladi
    if request.method == 'GET':
        article.view_count += 1
        article.save()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.rating = request.POST.get("rating", 3)  # Default to 3 if not selected
            comment.save()
            messages.success(request, 'Izoh yuborildi')
            return HttpResponseRedirect(reverse("blog-page", args=[id]))

    comments = Comment.objects.filter(article=article).order_by("-create_date")
    form = CommentForm()
    context = {
        "article": article,
        "comments": comments,
        "form": form
    }
    return render(request, "blog.html", context)
