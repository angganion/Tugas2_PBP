from django.shortcuts import render

# Create your views here.\
def show_main(request):
    context = {
        'name1': 'orang1',
        'barang1': 'barang1',
        'total1' : 0,
        'orang2' : 'orang2',
        'barang2' : 'barang2',
        'total2' : 0,
        'orang3' : 'orang3',
        'barang3' : 'barang3',
        'total3' : 0,

    }

    return render(request, "main.html", context)
