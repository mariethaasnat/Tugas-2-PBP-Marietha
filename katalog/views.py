# Nama : Marietha Asnat Nauli Sitompul
# NPM : 2106752413
# Kelas : PBP - B
# Kode Asdos : BI

from django.shortcuts import render
from katalog.models import CatalogItem

# TODO : Create your views here.
def katalog_view (request):
    katalog_item = CatalogItem.objects.all()
    context = {
    'list_item': katalog_item,
    'Nama': 'Marietha Asnat Nauli Sitompul',
    'ID': '2106752413'
    }
    return render(request, "katalog.html", context)