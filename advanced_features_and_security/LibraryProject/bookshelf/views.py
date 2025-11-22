from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .forms import ArticleForm
from .models import Article

# Create your views here.


#create article
@permission_required("bookshelf.can_create", raise_exception= True)
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("articles")
    else:
        form = ArticleForm()
    
    return render(request, "bookshelf/create-article.html", {"form": form})

@permission_required("bookshelf.can_view", raise_exception= True)
def view_article(request):
    articles = ArticleForm.objects.all()
    return render(request, "bookshelf/articles.html", {"articles": articles})

@permission_required("bookshelf.can_edit", raise_exception= True)
def edit_article(request):
    article_id = request.POST.get("id")
    article = Article.objects.get(id= article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance= article)
        if form.is_valid():
            form.save()
            redirect("articles")
    else:
        form = ArticleForm(instance= article)
    
    return render(request, "bookshelf/edit-article.html", {"form": form})

@permission_required("bookshelf.can_delete", raise_exception= True)
def delete_article(request):
    article_id = request.POST.get("id")
    article = Article.objects.get(id= article_id)
    article.delete()
    redirect("articles")