# Tugas 4 PBP - README
Nama : Marietha Asnat Nauli Sitompul <br />
NPM : 2106752413 <br />
Kelas : PBP - B <br />
Kode Asdos : BI
#### [Link Aplikasi Heroku](https://tugas2pbpasnat.herokuapp.com/todolist/)

## Kegunaan `{% csrf_token %}` pada Elemen Form
#### Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
`{% csrf_token %}` merupakan sebuah tag acak atau _random_ yang dibuat oleh Django dan merupakan sebuah built-in template pada elemen `<form>`. Tag ini memiliki fungsi untuk melindungi Cross Site Request Forgery (CSRF) dari serangan, terutama Cross Site Request Forgery _attack_. Token ini memiliki nilai acak dan mengandung nilai yang berbeda setiap sesinya. Sistem kerja dari `{% csrf_token %}` pada elemen `<form>` adalah ia akan memberikan token CSRF unik untuk setiap sesi pengguna, token ini kemudian dimasukkan ke dalam parameter tersembunyi dari form HTML. kemudian setelah itu dikirim ke browser klien. <br />
Apabila tidak terdapat kode `{% csrf_token %}` pada elemen `<form>`, maka CSRF tidak akan ada yang melindungi sehingga sangat memungkinkan terjadinya serangan atau _attack_. Selain itu, akan muncul error ketika berusaha submit elemen `<form>` tanpa token `{% csrf_token %}`. <br />

## Pembuatan Elemen Form Secara Manual
#### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Kita dapat membuat elemen `<form>` secara manual tanpa menggunakan generator seperti `{{ form.as_table }}`. Cara membuatnya adalah dengan menggunakan tag `<form>` pada html sebagai berikut : <br />
```
    <form action=[URL DESTINATION] method=[METHOD]>
        <input type="text" name="title" placeholder="Title" class="form-control">
        ....
    </form>
```
Dengan URL DESTINATION merupakan posting data ke URL endpoint, METHOD merupakan method untuk passing variabel ke URL DESTINATION (menggunakan GET atau POST), dan INPUT TYPE merupakan input data dari pengguna. HTML memiliki minimal 1 tag input (tipe apapun) dan 1 tag tipe submit. Contoh penerapan nya adalah `<input type="submit" name="submit" value="Create New"/>` untuk membuat sebuah task baru. <br />

## Proses Alur Data pada Form 
#### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Secara singkat alur data tersebut dimulai dari user akan mengisi seluruh data yang ada pada form dan melakukan submit --> Kemudian data tersebut akan dikirim HTTP Request dari html ke `views.py` --> Kemudian data akan diolah pada file `views.py` dan disimpan dalam database --> Kemudian data tersebut dapat dilihat kapanpun html tersebut dibuka atau dipanggil.  <br />
Contoh dari proses tersebut pada tugas 4 ini adalah pada form add new task atau membuat task baru. Setelah form diisi oleh pengguna, maka ada request berupa POST yang akan dikirim beserta dengan data pada form tersebut. Jika data benar, maka data tersebut akan diambil dan dimasukkan ke dalam database.  <br />

## Implementasi Poin 1 - 9
#### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.
**Poin 1 : Membuat suatu aplikasi baru bernama todolist** <br />
> Dibuat di proyek Django Tugas 2 pekan lalu. <br />

Menjalankan virtual environment lalu menjalankan perintah `python manage.py startapp todolist`. <br />

**Poin 2 : Menambahkan path todolist** <br />
> Sehingga pengguna dapat mengakses https://localhost:8000/todolist. <br />

Menambahkan path todolist pada bagian `urlpatterns` di file `project_django/urls.py` dengan format `path('todolist/', include('todolist.urls')),`. <br />

Menambahkan `todolist` pada bagian `INSTALLED_APPS` di file `project_django/settings.py`. <br />

**Poin 3 : Membuat sebuah model todolist yang memiliki empat atribut** <br />
> user (untuk menghubungkan _task_ dengan pengguna yang membuat), date (untuk mendeskripsikan tanggal pembuatan _task_), title(untuk mendeskripsikan judul _task_), dan description (untuk mendeskripsikan deskripsi _task_). <br />

Membuat model pada `todolist/models.py` dengan atribut `user`, `date`, `title`, dan `description`. Kemudian melakukan migrasi dengan menjalankan `python manage.py makemigration` dan `python manage.py migrate`. <br />

**Poin 4 :  Mengimplementasikan form registrasi, login, dan logout** <br />
> Sehingga pengguna dapat menggunakan todolist dengan baik. <br />

Membuat fungsi `register`, `login_user`, dan `logout_user` di file `todolist/views.py`. Kemudian membuat berkas HTML untuk masing - masing fungsi, yaitu `register.html`, `login.html`, `logout.html` pada folder `todolist/templates`. Setelah itu, saya juga membuat routing untuk masing - masing fungsi, contohnya, untuk routing fungsi register saya menuliskan kode sebagai berikut `path('register/', register, name='register'),`. <br />

**Poin 5 : Membuat halaman utama todolist** <br />
> Berisi username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task. <br />

Membuat sebuah fungsi `show_todolist` pada file `todolist/views.py`, dimana fungsi tersebut akan me-render ke halaman utama. Pada fungsi tersebut saya mencantumkan elemen - elemen yang data nya akan di passing, seperti username, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task. Kemudian saya membuat `todolist.html` pada folder `todolist/templates` untuk menampilkan elemen - elemen tersebut. <br />

**Poin 6 : Membuat halaman form untuk pembuatan task** <br />
> Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task. <br />

Membuat sebuah file bernama `forms.py` yang berisi form yang akan digunakan untuk mengambil data, dimana terdapat 2 atribut, yaitu judul dan deskripsi task. Membuat sebuah fungsi `new_todolist` pada file `todolist/views.py`, dimana fungsi tersebut akan me-render ke halaman pembuatan task baru dan passing form pada file forms.py. Kemudian saya membuat `newtodolist.html` pada folder `todolist/templates` untuk menampilkan form. Selain itu saya juga membuat handle untuk penambahan task. <br />

**Poin 7 : Membuat routing sehingga beberapa fungsi dapat diakses** <br />
> Melalui URL login, register, create-task, logout, main (utama nya). <br />

Menambahkan path pada bagian `urlpatterns` di file `todolist/urls.py` seperti berikut :<br />
```
    path('', show_todolist, name = 'show_todolist'), 
    path('register/', register, name = 'register'),
    path('login/', login_user, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('create-task/', new_todolist, name = 'new_todolist'),
```

**Poin 8 :  Melakukan deployment ke Heroku** <br />
Langkah pertama yang saya lakukan adalah mengupload berkas - berkas tugas 4 ke repo di github dengan memanfaatkan git add, commit, dan push. Kemudian saya menjalan workflow atau action yang gagal agar aplikasi mywatchlist dapat ter-deploy di aplikasi Heroku. <br />

**Poin 9 : Membuat dua akun pengguna dan tiga dummy data** <br />
> Menggunakan model Task pada akun masing - masing di situs web Heroku. <br />

Menggunakan fitur registrasi dan login akun untuk membuat 2 akun pengguna. Kemudian pada masing - masing akun membuat 3 buah data atau to do list menggunakan fitur `New To Do List`.
