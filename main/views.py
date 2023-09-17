from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from .models import Item
from django.http import HttpResponse
from django.core import serializers
import requests
import random

def add_zero(a):
    kode = str(a)
    if len(kode) < 8:
        kode = ("0"*(8-len(kode))) + str(a)
    return kode

def show_main(request):
    item = Item.objects.all()
    context = {
        'name' : 'Wahyu Ridho Anggoro',
        'class' : 'PBP D',
        'random_image' : 'https://cataas.com/cat/says/hello%20world!',
        'random' : 'https://94.131.113.17/wp-content/uploads/2023/06/okep.gif',
        'gacor' : add_zero(random.choice(range(1000, 10000000))),
        'products': item
    }

    return render(request, "main.html", context)

def show_random_image(request):
    r = requests.get('http://thecatapi.com/api/images/get?format=src&type=png')
    return HttpResponse( r.content, content_type="image/png")

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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
    # Temukan produk yang akan dihapus berdasarkan ID
    item = Item.objects.filter(pk=id)

    # Hapus produk dari database
    if item.exists():
        # Hapus item
        item.delete()

    # Redirect ke halaman lain setelah menghapus produk, misalnya, kembali ke halaman daftar produk
    return redirect('main:show_main')
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