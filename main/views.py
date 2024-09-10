from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'Koalove',
        'name': 'Marla Marlena',
        'class': 'PBP C',
    }

    return render(request, "main.html", context)
