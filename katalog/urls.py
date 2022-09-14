# Nama : Marietha Asnat Nauli Sitompul
# NPM : 2106752413
# Kelas : PBP - B
# Kode Asdos : BI

from django.urls import path
from katalog.views import katalog_view

# TODO: Implement Routings Here
app_name = 'katalog'

urlpatterns = [
    path('', katalog_view, name = 'katalog_view'),
]