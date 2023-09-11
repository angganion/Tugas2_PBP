from django.shortcuts import render
import requests
from django.http import HttpResponse
import random
# Create your views here.\

def add_zero(a):
    kode = str(a)
    if len(kode) < 8:
        kode = ("0"*(8-len(kode))) + str(a)
    return kode

def show_main(request):
    context = {
        'name1': 'orang1',
        'deskripsi1': 'baarang mahal',
        'total1' : 0,
        'name2' : 'orang2',
        'deskripsi2' : 'barang bagus',
        'total2' : 0,
        'name3' : 'orang3',
        'deskripsi3' : 'barang murah',
        'total3' : 0,
        'random_image' : requests.get('https://cataas.com/cat/says/hello%20world!').url,
        'gacor' : add_zero(random.choice(range(1000, 10000000)))
    }

    return render(request, "main.html", context)

def show_random_image(request):
    r = requests.get('http://thecatapi.com/api/images/get?format=src&type=png')
    return HttpResponse( r.content, content_type="image/png")
