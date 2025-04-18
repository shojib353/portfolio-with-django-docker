from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Project,Certificates

def index(request):

    
    

    projects = Project.objects.all()
    certificates=Certificates.objects.all()

    context = {
        'projects': projects,
        'certificates':certificates,
    }
    return render(request,"portfolio_app/index.html",context=context)



def get_date(request):
    today = date.today()
    template = "<html>" \
                "Today's date is {}" \
               "</html>".format(today)
    return HttpResponse(content=template)