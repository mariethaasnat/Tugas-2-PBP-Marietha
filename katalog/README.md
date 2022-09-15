# Tugas 2 PBP - README
Nama : Marietha Asnat Nauli Sitompul <br />
NPM : 2106752413 <br />
Kelas : PBP - B <br />
Kode Asdos : BI
#### [Link Aplikasi Heroku](https://tugas2pbpasnat.herokuapp.com/katalog/)

## Bagan
#### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Tugas 2 PBP drawio](https://user-images.githubusercontent.com/112157528/190302596-5f167843-9411-4dc8-84bf-680c8c5073c2.png)

Aplikasi katalog ini akan memproses request dari user dengan cara mencari url yang menyimpan informasi yang diinginkan oleh client pada file urls.py. Setelah url yang diinginkan oleh client ditemukan, maka urls.py akan memanggil fungsi view pada file views.py. Kemudian fungsi view akan mengambil data atau query dari file models.py dimana nantinya data tersebtu akan ditampilkan. Kemudian fungsi tersebtu akan mereturn suatu fungsi render yang akan membaca katalog.html. Pada katalog.html, terdapat informasi yang akan menentukan bagaimana data tersebut akan ditampilkan. Kemudian data tersebut ditampilkan kepada client.

## Virtual Environment
#### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
_Virtual_ Environment atau _VirtualEnv_ adalah suatu ruang lingkup virtual atau suatu wadah yang terisolasi dari _dependencies_ utama yang berguna saat dibutuhkan _dependencies_ yang berbeda-beda antara project satu dengan yang lainnya, yang berjalan pada satu system operasi yang sama. Penggunaan virtual environment diterapkan agar saat terjadi perubahan - perubahan dalam suatu ruang lingkup, data lain yang terdapat pada project yang berbeda tidak terpengaruhi perubahan tersebut. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi hal tersebut tidak dianjurkan karena sangat memungkinkan timbulnya banyak masalah akibat penggunaan oleh banyak pengguna. Selain itu, aplikasi web tersebut akan lebih susah untuk dipelihara atau _maintain_. <br />

## Implementasi Poin 1 - 4
#### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
**1. Membuat sebuah fungsi pada views.py** <br />
> Fungsi yang dibuat dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML. <br />

Dengan menggunakan template yang sudah diberikan, saya membuat sebuah fungsi `katalog_view`, tetapi sebelumnya saya melakukan immport CatalogItem dari models.py dengan cara : `from katalog.models import CatalogItem`. <br />

Fungsi ini akan menerima parameter request dan mengembalikan suatu fungsi render. Fungsi render tersebut nantinya akan menampilkan html yang berisi data - data yang telah diambil pada fungsi, kemudian data tersebut akan disimpan di variabel `katalog_item`. <br />

![views.py](https://user-images.githubusercontent.com/112157528/190294241-6f3fe572-9ee5-49ae-9149-5dd39ebde4b4.png)
 
**2. Membuat sebuah routing pada views.py** <br />
> Routing dibuat untuk memetakan fungsi yang telah dibuat sebelumnya. <br />

Untuk dapat mengakses aplikasi katalog ini, saya menambahkan `path('katalog/', include('katalog.urls')),` pada file project_django\urls.py agar aplikasi katalog dapat mengambil data yang sesuai dengan request client. <br />

Untuk membuat sebuah routing, saya melakukan import fungsi yang sudah dibuat di views.py sebelumnya, sehingga fungsi tersebut akan dipanggil ketika url ini diakses.

![routing views.py](https://user-images.githubusercontent.com/112157528/190295907-17addbd1-bf94-427f-8016-ab8208556649.png)

**3. Memetakan data yang didapatkan ke dalam HTML** <br />
> Pemetakan data dilakukan dengan sintaks dari Django untuk pemetaan data template. <br />

Dengan mengikuti langkah - langkah pada tutorial, saya mengubah bagian **fill me** dalam file `katalog.html` menjadi

![Screenshot (4029)](https://user-images.githubusercontent.com/112157528/190296428-7417ceb7-622a-401c-b7c2-18cd096eb206.png)

dengan begitu nama dan student id saya dapat ditampilkan dalam url. Kemudian saya menambahkan sebuah _loop_, yaitu for loop untuk menampilkan field setiap instance dari data yang didapatkan, sehingga setiap field yang ditulis dari objek `list_item` dapat dituliskan.

![Screenshot (4028)](https://user-images.githubusercontent.com/112157528/190296855-e4740e43-dd14-4a3a-b541-c0212e9e0471.png)

**4. Melakukan deployment ke Heroku** <br />
Langkah pertama yang saya lakukan adalah mengupload berkas - berkas tersebut ke repo di github dengan memanfaatkan git add, commit, dan push. Kemudian saya membuat sebuah aplikasi baru pada herokuapp yang saya beri nama tugas2pbpasnat. Kemudian saya menambahkan 2 variabel Repository Secret seperti langkah - langkah pada tutorial sebelumnya. Dan terakhir saya melakukan _deploy_ ulang repo milik saya yang ada di github.
