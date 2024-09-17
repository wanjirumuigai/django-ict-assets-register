from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Asset, Issue_Assets, Request, Staff
from .forms import AssetForm, RequestForm
from django.contrib.auth.models import User
from django.contrib import messages
from users.forms import CreateUserForm
# Create your views here.

@login_required(login_url='user-login')
def index(request):

    requests = Request.objects.all() 

    requests_count = requests.count()
    workers_count = Staff.objects.all().count()
    assets_count = Asset.objects.all().count()    
     

    if request.method == 'POST':
        form = RequestForm(request.POST)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.order_by = request.user
            instance.save()
            return redirect('index')
    else:
        form = RequestForm()

  
    categories = ['Desktops','Laptops','Servers', 'Network','UPS','Audio/Visual']
    items = []
    status = ['Working', 'Faulty', 'Obsolete', 'Lost', 'Disposed']
    conditions = []

    for item in status:
        status_count = Asset.objects.filter(status=item).count()
        conditions.append({'status':item, 'count':status_count})

       
    for category in categories:


        category_count = Asset.objects.filter(category=category).count()
        items.append({'category': category, 'count':category_count})
    context = {
        'requests': requests,
        'form': form,
        'items': items,
        'statuses': conditions,   
        'requests_count': requests_count,
        'workers_count': workers_count,
        'assets_count': assets_count,
        
    }
  
     
    return render(request, 'dashboard/index.html', context=context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    items_requested = Request.objects.all()

    requests_count = items_requested.count()
    all_assets = Asset.objects.all()
    assets_count = all_assets.count()

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('first_name')
            messages.success(request, f'{user_name} has been added')
            return redirect('staff')
            
    else:
        form = CreateUserForm()
    
    context = {
        'workers': workers,
        'workers_count': workers_count,   
        'requests_count': requests_count,  
        'assets_count': assets_count,  
        'form': form, 
    }
    return render(request, 'dashboard/staff.html', context=context)

@login_required(login_url='user-login')
def staff_detail(request, pk):
    worker = User.objects.get(id=pk)

    context = {
        'worker': worker,
    }

    return render(request, 'dashboard/staff_detail.html', context=context)

@login_required(login_url='user-login')

def assets(request):
    all_assets = Asset.objects.all()
    assets_count = all_assets.count()

    workers_count = User.objects.all().count()
    items_requested = Request.objects.all()

    requests_count = items_requested.count()

   
   
    if request.method=='POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('model')
            messages.success(request, f'{product_name} has been added')
            return redirect('assets')
            
    else:
        form = AssetForm()
    
    context = {
        'assets': all_assets,
        'form': form,
        'assets_count': assets_count,
        'workers_count': workers_count,
        'requests_count': requests_count,

    }
    return render(request, 'dashboard/assets.html', context=context)

@login_required(login_url='user-login')
def asset_delete(request, pk):
    item = Asset.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('assets')

    return render(request, 'dashboard/asset_delete.html')

@login_required(login_url='user-login')
def asset_edit(request,pk):
    item = Asset.objects.get(id=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('assets')
    else:
        form = AssetForm(instance=item)
  

    
    context = {
        'form': form,

    }
    return render(request, 'dashboard/asset_edit.html', context=context)
@login_required(login_url='user-login')
def requests(request):
    workers_count = User.objects.all().count()

    items_requested = Request.objects.all()

    requests_count = items_requested.count()

    all_assets = Asset.objects.all()
    assets_count = all_assets.count()
    

    context = {
        'items': items_requested,
        'requests_count': requests_count,
        'workers_count': workers_count,
        'assets_count': assets_count, 
    }

    return render(request, 'dashboard/requests.html', context=context)



@login_required(login_url='user-login')
def desktops(request):

    return render(request, 'dashboard/desktops.html')
@login_required(login_url='user-login')
def laptops(request):

    return render(request, 'dashboard/laptops.html')
@login_required(login_url='user-login')
def licenses(request):

    return render(request, 'dashboard/licenses.html')

@login_required(login_url='user-login')
def obsolete(request):

    return render(request, 'dashboard/obsolete.html')

@login_required(login_url='user-login')
def all_assets(request):
    categories = ['Desktops','Laptops','Servers', 'Network','UPS','Audio/Visual']
    items = []

    for category in categories:


        category_count = Asset.objects.filter(category=category).count()
        items.append({'category': category, 'count':category_count})
    context = {
        'items': items,
        
        
        
    }

   

    return render(request, 'dashboard/index.html', context=context)
