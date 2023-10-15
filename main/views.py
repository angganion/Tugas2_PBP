from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from .models import Item
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import requests
import random
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound

def add_zero(a):
    kode = str(a)
    if len(kode) < 8:
        kode = ("0"*(8-len(kode))) + str(a)
    return kode

@login_required(login_url='main:login')
def show_main(request):
    item = Item.objects.filter(user=request.user)
    context = {
        'name' : request.user.username,
        'class' : 'PBP D',
        'random_image' : 'https://cataas.com/cat/says/hello%20world!',
        'random' : 'https://94.131.113.17/wp-content/uploads/2023/06/okep.gif',
        'gacor' : add_zero(random.choice(range(1000, 10000000))),
        'products': item,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def show_random_image(request):
    r = requests.get('http://thecatapi.com/api/images/get?format=src&type=png')
    return HttpResponse( r.content, content_type="image/png")

def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
def show_html(request):
    data = Item.objects.all()
    return render(request, 'items.html', {'data': data})
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def delete_product(request, id):
    try:
        # Temukan produk yang akan dihapus berdasarkan ID
        item = get_object_or_404(Item, pk=id)

        # Hapus produk dari database
        item.delete()

        # Respon JSON yang menandakan penghapusan berhasil
        return JsonResponse({'message': 'Produk berhasil dihapus'}, status=204)

    except Item.DoesNotExist:
        # Respon JSON yang menandakan bahwa produk tidak ditemukan
        return JsonResponse({'message': 'Produk tidak ditemukan'}, status=404)

    except Exception as e:
        # Respon JSON yang menandakan kesalahan server
        return JsonResponse({'message': 'Terjadi kesalahan server'}, status=500)

def increase_product_quantity(request, id):
    # Temukan produk yang akan ditambahkan berdasarkan ID
    item = get_object_or_404(Item, pk=id)


    # Tambahkan jumlah produk
    item.amount += 1
    item.save()

    # Redirect ke halaman lain setelah menambah jumlah produk, misalnya, kembali ke halaman daftar produk
    return redirect('main:show_main')

def decrease_product_quantity(request, id):
    # Temukan produk yang akan dikurangkan berdasarkan ID
    item = get_object_or_404(Item, pk=id)

    # Pastikan jumlah produk tidak menjadi negatif
    # Kurangkan jumlah produk
    item.amount -= 1
    item.save()

    if item.amount == 0:
        item.delete()
    return redirect('main:show_main')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
@login_required
def add_product_ajax(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("amount")
        description = request.POST.get("description")
        rarity = request.POST.get("rarity")
        user = request.user

        new_product = Item(name=name, amount=price, description=description, rarity=rarity, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

