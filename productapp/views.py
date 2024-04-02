# from django.shortcuts import redirect, render
# from .models import Member
# from .forms import MemberForm

# def index(request):
#     members = Member.objects.all()
#     return render(request, 'index.html', {'members': members})

# def add(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = MemberForm()
#     return render(request, 'add.html', {'form': form})

# def addrec(request):
#     w=request.POST['image']
#     x=request.POST['name']
#     y=request.POST['quantity']
#     z=request.POST['price']
#     mem=Member(name=x, quantity=y, price=z, image=w)
#     mem.save()
#     return redirect("/")

# def delete(request, id):
#     member = Member.objects.get(id=id)
#     member.delete()
#     return redirect("/")

# def update(request, id):
#     member = Member.objects.get(id=id)
#     if request.method == 'POST':
#         form = MemberForm(request.POST, instance=member)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = MemberForm(instance=member)
#     return render(request, 'update.html', {'form': form})

# def uprec(request,id):
#     w=request.POST['image']
#     x=request.POST['name']
#     y=request.POST['quantity']
#     z=request.POST['price']
#     mem=Member.objects.get(id=id)
#     mem.image=w
#     mem.name=x
#     mem.quantity=y
#     mem.price=z
#     mem.save()
#     return redirect("/")
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm

def main_home(request):
    return render(request, 'main_home.html')

def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dealer_home')
    else:
        form = ProductForm()
    return render(request, 'add.html', {'form': form})

def delete(request, id):
    member = Product.objects.get(id=id)
    member.delete()
    return redirect('dealer_home')

def update(request, id):
    Product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=Product)
        if form.is_valid():
            form.save()
            return redirect('dealer_home')
    else:
        form = ProductForm(instance=Product)
    return render(request, 'update.html', {'form': form})

def uprec(request, id):
    Product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=Product)
        if form.is_valid():
            form.save()
            return redirect('dealer_home')
    return redirect('user_home')
