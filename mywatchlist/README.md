# Tugas 3 PBP - README
Nama : Marietha Asnat Nauli Sitompul <br />
NPM : 2106752413 <br />
Kelas : PBP - B <br />
Kode Asdos : BI
#### [Link Aplikasi Heroku](https://tugas2pbpasnat.herokuapp.com/mywatchlist/)

## Perbedaan Antara JSON, XML, dan HTML
#### Jelaskan perbedaan antara JSON, XML, dan HTML!
**JSON (JavaScript Object Notation)** <br />
JSON digunakan untuk menyimpan dan mengirimkan data yang sering digunakan pada banyak aplikasi web ataupun _mobile_. JSON sangat mudah untuk dimengerti dan dipahami karena JSON didesain menjadi _self-describing_. Sintaks JSON merupakan turunan dari _Object_ JavaScript, akan tetapi formatnya berbentuk teks, sehingga kode JSON terdapat di banyak bahasa pemrograman. Beberapa keunggulan JSON adalah JSON tidak menggunakan _end tag_, lebih singkat dibandingkan lainnya, bisa menggunakan array, dan lebih cepat untuk dibaca dan ditulis. <br />
**XML (eXtensible Markup Language)** <br />
XML digunakan untuk menyimpan dan mengirimkan data yang sering digunakan pada banyak aplikasi web ataupun _mobile_. Pada XML, kita perlu menulis program untuk mengirim, menerima, menyimpan, maupun menampilkan informasi – informasi yang dibungkus di dalam tag. XML di desain menjadi _self-descriptive_ dimana kita bisa membaca dan mengerti dengan mudah informasi apa yang disampaikan pada data yang tertulis. Salah satu perbedaan JSON dan XML adalah XML harus di-parse menggunakan XML parser, sementara JSON dapat di-parse menggunakaan function JavaScript biasa. <br />
**HTML (HyperText Markup Language)** <br />
HTML adalah salah satu _markup language_ yang digunakan untuk membuat web dimana HTML menggambarkan struktur halaman dari web tersebut. HTML terdiri dari serangkaian elemen dimana elemen – elemen tersebut akan memberi tahu web bagaimana cara menampilkan konten dari web tersebut dan tampilannya juga dapat di kustomisasi. <br />

## _Data Delivery_ dalam Pengimplementasian Sebuah Platform
#### Jelaskan mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?
Dalam pengimplentasian sebuah platform, dibutuhkan _data delivery_ untuk mempermudah pertukaran data antara _client_ dan _server_. _Data delivery_ tersebut akan memudahkan kita untuk mengirim dan mengambil data sehingga data tersebut dapat dimengerti dengan mudah, baik oleh manusia maupun mesin. Data yang telah diperoleh tersebut akan diolah menjadi sesuatu yang bermanfaat. Untuk melakukan _data delivery_, dapat digunakan format tertentu seperti HTML, JSON, dan XML.

## Implementasi Poin 1 - 7
#### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.
**Poin 1 : Membuat suatu aplikasi baru bernama mywatchlist** <br />
> Dibuat di proyek Django Tugas 2 pekan lalu. <br />

Menjalankan virtual environment lalu menjalankan perintah `python manage.py startapp mywatchlist`. <br />

**Poin 2 : Menambahkan path mywatchlist** <br />
> Sehingga pengguna dapat mengakses https://localhost:8000/mywatchlist. <br />

Menambahkan path mywatchlist pada bagian `urlpatterns` di file `project_django/urls.py` dengan format `path('mywatchlist/', include('mywatchlist.urls')),`. <br />

Menambahkan `mywatchlist` pada bagian `INSTALLED_APPS` di file `project_django/settings.py`. <br />

**Poin 3 : Membuat sebuah model mywatchlist yang memiliki lima atribut** <br />
> Watched (untuk mendeskripsikan film tersebut sudah ditonton atau belum), title (untuk mendeskripsikan judul film), rating(untuk mendeskripsikan rating film rentang 1 sampai dengan 5), release_date (untuk mendeskripsikan kapan film dirilis), dan review (untuk mendeskripsikan review untuk film tersebut). <br />

Membuat model pada `mywatchlist/models.py` dengan atribut `watched`, `title`, `rating`, `release_date`, dan `review`. Kemudian melakukan migrasi dengan menjalankan `python manage.py makemigration` dan `python manage.py migrate`. <br />

**Poin 4 :  Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas** <br />
Menambahkan 12 data berupa JSON pada file `fixtures/initial_mywatchlist_data.json`. <br />

**Poin 5 : Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya** <br />
> Disajikan dalam tiga format, yaitu HTML, XML, JSON. <br />

Membuat fungsi untuk menampilkan data dalam bentuk format HTML, XML, dan JSON pada `mywatchlist/views.py`. Fungsi yang menampilkan dalam format HTML saya beri nama `show_mywatchlist`. Fungsi yang menampilkan dalam format JSON saya beri nama `show_mywatchlist_json` dan `show_mywatchlist_json_by_id`. Fungsi yang menampilkan dalam format XML daya beri nama `show_mywatchlist_xml` dan `show_mywatchlist_xml_by_id`. <br />

**Poin 6 : Membuat routing sehingga data di atas dapat diakses** <br />
Menambahkan path mywatchlist pada bagian `urlpatterns` di file `mywatchlist/urls.py`. Sebagai contoh, untuk path HTML, saya menambahkan `path('html/', show_mywatchlist, name='show_mywatchlist')`. Kemudian saya juga melakukan hal yang sama pada XML dan JSON. <br />

**Poin 7 : Melakukan deployment ke Heroku** <br />
Langkah pertama yang saya lakukan adalah menambahkan '&& python manage.py loaddata movies_catalog.json' di baris pertama 'Procfile'. Kemudian saya mengupload berkas - berkas tersebut ke repo di github dengan memanfaatkan git add, commit, dan push. Kemudian saya menjalan workflow atau action yang gagal agar aplikasi mywatchlist dapat ter-deploy di aplikasi Heroku. <br />

## Postman
#### Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md
**HTML Format** <br />
![Postman - HTML Format](https://user-images.githubusercontent.com/112157528/191540428-bced0689-1173-408c-8238-02d945239fa5.png)

**XML Format** <br />
![Postman - XML Format](https://user-images.githubusercontent.com/112157528/191540788-cd583a70-9d63-4341-80b8-7265da4f5066.png)

**JSON Format** <br />
![Postman - JSON Format](https://user-images.githubusercontent.com/112157528/191540955-73771196-6867-44fd-af7c-d6d0ad050c8e.png)
