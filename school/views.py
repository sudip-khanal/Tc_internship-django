from django.http import HttpResponse
from django.shortcuts import render
from school.models import Author
# Create your views here.
def get_student(request):
    context={}
    context= Author.objects.all()
    return HttpResponse("all Authors:")