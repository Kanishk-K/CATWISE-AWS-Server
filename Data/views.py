from django import contrib
from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from djqscsv.djqscsv import render_to_csv_response
from .forms import CatWiseForm
from .models import CatWise
from .filters import CatWiseFilter
from django.contrib import messages


# Create your views here.
@login_required
def index(request):
    return redirect('Data:page_index', page=1)

@login_required
def page_index(request,page):
    WiseFilter = CatWiseFilter(request.GET,queryset=CatWise.objects.all())
    QuerySet = WiseFilter.qs
    context = {
        "Filter":WiseFilter,
        "WiseObjects":QuerySet.order_by('RA')[50*(page-1):(50*(page-1))+50],
        "TotalFound":len(QuerySet),
        "PagesBefore":[i for i in range(page-5,len(QuerySet)//50 + 2) if i > 0 and i<page],
        "CurrentPage":page,
        "PagesAfter": [i for i in range(page,page+6) if i < len(QuerySet)//50 + 2 and i>page],
        "MaxPage":len(QuerySet)//50 + 1,
    }
    return render(request,"Data/index.html",context=context)

@login_required
def render_csv(request):
    WiseFilter = CatWiseFilter(request.GET,queryset=CatWise.objects.all())
    WiseObjects = WiseFilter.qs
    return render_to_csv_response(WiseObjects,filename="CatWise_Data")

@login_required
def view_data(request,id):
    context = {
        "WiseObject":CatWise.objects.get(pk=id)
    }
    return render(request,"Data/view.html",context=context)

@staff_member_required
def add_data(request):
    if request.method == "POST":
        form = CatWiseForm(data=request.POST)
        if form.is_valid():
            CATWISE = form.save(commit=False)
            CATWISE.last_modified = request.user
            CATWISE.save()
            return redirect('Data:index')
        else:
            context = {
                'form':form,
            }
            messages.warning(request, 'Data inserted into the form was not valid', extra_tags=['warning',"fas fa-fa-upload"])
            return render(request, "Data/add.html",context=context)
    else:
        context = {
            'form':CatWiseForm(),
        }
        return render(request,'Data/add.html',context=context)

@staff_member_required
def edit_data(request,id):
    if request.method == "POST":
        form = CatWiseForm(data=request.POST,instance=CatWise.objects.get(id=id))
        if form.is_valid():
            CATWISE = form.save(commit=False)
            CATWISE.last_modified = request.user
            CATWISE.save()
            return redirect('Data:index')
        else:
            context = {
                'form':form,
            }
            messages.warning(request, 'Data inserted into the form was not valid', extra_tags=['warning',"fas fa-fa-upload"])
            return render(request, "Data/add.html",context=context)
    else:
        context = {
            'form':CatWiseForm(instance=CatWise.objects.get(id=id)),
        }
        return render(request,'Data/add.html',context=context)

@staff_member_required
def delete_data(request,id):
    CatWise.objects.get(id=id).delete()
    return redirect('Data:index')