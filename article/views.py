from django.core.files.base import equals_lf
from django.db import reset_queries
from article.forms import ArticleForm
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404,reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from article.models import Article, Commet
from django.core.exceptions import ValidationError



# Create your views here.
def index(request):

    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
@login_required(login_url="login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }


    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addarticle(request):
    
    form = ArticleForm(request.POST or None,request.FILES or None)
    context={
        "form":form
    }
    try:
        if form.is_valid():
            article=form.instance
            article.author=request.user
            if  not str(article.articleImage).endswith(("png","jpg")):
                raise ValidationError('Empty URL')
            article.save()
            messages.success(request,"Makale basariyla olusturuldu")
            return redirect("dashboard")

    except ValidationError as err:
        print(err)
        messages.info(request,"Lutfen bir resim dosyasi secin") 
    return render(request,"addarticle.html",context)




        
def readarticle(request,id):
   # article = Article.objects.get(id=id)
    article=get_object_or_404(Article,id=id)
    commets=article.commet.all()
    context={
        "article":article,
        "commets":commets
    }


    return render(request,"readarticle.html",context)

@login_required(login_url="user:login")

def update(request,id):
    article=get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        form.save()
        messages.success(request,"Makale basariyla guncellendi")
        return redirect("dashboard")
    context ={

        "form":form
    }

    return render(request,"update.html",context)
def delete (request,id):
    article=get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"basairlya silindi")
    return redirect("dashboard")
def article (request):
    def findArticles():
        if(keyword:=(request.GET.get("keyword"))):
            return Article.objects.filter(title__contains=keyword)
        else:
            return Article.objects.all()
   
    context={
        "articles":findArticles()
    }
    return render(request,"article.html",context)

def commet(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        content=request.POST.get("content")
        author=request.POST.get("title")
        newCommet = Commet(content=content,author=author)
        newCommet.article=article
        newCommet.save()
    return redirect(reverse("readarticle",kwargs={"id":id}))





