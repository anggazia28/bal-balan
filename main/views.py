from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_toko' : 'Bal balan',
        'npm' : '2406495943',
        'name': 'Angga Ziaurrohchman',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
