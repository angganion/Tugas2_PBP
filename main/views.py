from django.shortcuts import render

# Create your views here.\
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

    }

    return render(request, "main.html", context)
