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
    WiseFilter = CatWiseFilter(request.GET,queryset=CatWise.objects.all())
    context = {
        "Filter":WiseFilter,
        "WiseObjects": WiseFilter.qs.order_by('RA')[0:50]
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
            form.save()
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
            form.save()
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