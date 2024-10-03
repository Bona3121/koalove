from django.shortcuts import render, redirect , reverse 
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@login_required(login_url='/login')
# Create your views here.
def show_main(request):
    query = request.GET.get('q')
   
    #query untuk handle cari barangnya blm di atur
    
    context = {
       
    }
    return render(request, 'main.html', context)

def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST.get('description', '')
        image = request.FILES.get('image')  # Handle image upload

        if not name or not price:
            messages.error(request, 'Product name and price are required!')
            return redirect('main:create_product')

        product = Product(name=name, price=price, description=description, image=image, user=request.user)
        product.save()
        messages.success(request, 'Product added successfully!')
        return redirect('main:show_main')

    return render(request, 'create_product.html')


def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah digunakan.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registrasi berhasil! Silakan login.')
            return redirect('main:login')  # Ubah sesuai URL login Anda
            
    return render(request, 'register.html') 

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Mencari produk berdasarkan ID
    product = Product.objects.filter(pk=id).first()  # Mengambil produk atau None jika tidak ditemukan

    if not product:
        # Jika produk tidak ditemukan, tampilkan pesan error
        messages.error(request, 'Produk tidak ditemukan.')
        return redirect('main:show_main')

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')  # Mengambil file gambar jika ada

        if not name or not price:
            # Menampilkan pesan error jika field kosong
            messages.error(request, 'Silakan isi semua field terlebih dahulu.')
        else:
            # Memperbarui produk jika semua field diisi
            product.name = name
            product.price = price
            
            # Periksa apakah gambar baru diunggah
            if image:
                product.image = image

            product.save()
            messages.success(request, 'Produk berhasil diperbarui.')
            return redirect('main:show_main')

    # Mengirim data produk ke template untuk mengisi form dengan nilai lama
    context = {
        'product': product
    }
    return render(request, 'edit_product.html', context)


def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    image = request.FILES.get('image')  # Make sure this retrieves a single file, not a list
    user = request.user

    new_product = Product(
        name=name, price=price, image=image,  
        user=user
    )
    new_product.save()  # Save the product
    return HttpResponse(b"CREATED", status=201)