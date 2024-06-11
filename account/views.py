from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
import json
from .models import *
from .forms import ArticleForm,ReporterForm
# Create your views here.
# def get_article(request):
#     a=Article.objects.all()
#     print(a)
   
def create_reporter(request):
    if request.method == 'POST':
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Reporter Created Successfully .....")
            return redirect('get_article')
    else:
        form = ReporterForm()
    return render(request, 'create_reporter.html', {'form': form})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request, "Article Created Successfully .....")
            return redirect('get_article')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

def get_article(request):
    articles=Article.objects.all()
    return render(request,'all_articles.html',{'articles':articles})


def delete_article(request,pk):
      obj = Article.objects.get(id=pk)
      obj.delete()
      messages.warning(request, "Article Deleted Successfully .....")
      return redirect('get_article')

  
# def update_article(request,pk):
#         current_record = Article.objects.get(id=pk)
#         form = ArticleUpdateForm(request.POST or None, instance=current_record)
#         if form.is_valid():
#             form.save()
#             messages.info(request, "Article Updated Successfully .....")
#             return redirect('get_article')
    