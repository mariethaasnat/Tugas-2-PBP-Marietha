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


# Tugas 5 PBP - README
#### [Link Aplikasi Heroku](https://tugas2pbpasnat.herokuapp.com/todolist/)

## Perbedaan serta Kelebihan - Kekurangan dari Inline, Internal, dan External CSS
#### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
**Inline Style** <br />
Berisikan properti Cascading Style Sheet (CSS) pada bagian body yang dilampirkan atau di-attached dengan elemen. Penerapannya bersifat unik terhadap satu elemen HTML. Inline Style menggunakan atribut ‘style’ di dalam elemen HTML. <br />
-- Kelebihan : Tidak perlu membuat dan mengunggah dokumen terpisah seperti pada External Style. Selain itu, Inline Style dapat dengan mudah dan cepat membuat properti CSS ke dalam halaman HTML. <br />
-- Kekurangan : Styling beberapa elemen dapat mempengaruhi ukuran halaman HTML dan waktu download nya. Selain itu, menambahkan properti CSS ke setiap elemen HTML akan membuat struktur nya berantakan dan memakan waktu yang cukup lama. <br />
**Internal Style** <br />
Berisikan properti Cascading Style Sheet (CSS) di dalam file HTML pada bagian head dimana properti CSS menempel di dalam file HTML tersebut. Penerapannya bersifat untuk satu halaman HTML. Internal Style menggunakan elemen ‘<style>’ pada bagian ‘<head>’. <br />
-- Kelebihan : Karena properti CSS berada pada file HTML yang sama, maka tidak perlu mengunggah banyak file. Selain itu, Inline Style dapat menggunakan class dan ID selector. <br />
-- Kekurangan : Menambahkan kode atau property ke dokumen HTML dapat meningkatkan ukuran halaman dan waktu loading web. Selain itu, karena Inline Style memiliki prioritas yang lebih tinggi, semua style yang berada pada Internal Style akan di-override oleh Inline Style. <br />
**External Style** <br />
Berisikan file CSS yang terpisah yang hanya berisi properti style dengan bantuan tag atribut. Properti CSS ditulis dalam file terpisah yang memiliki ekstensi .css yang kemudian di-link ke dokumen HTML menggunakan tag link. Untuk setiap elemen, style hanya dapat diatur sekali dan akan diterapkan di seluruh halaman web. Penerapannya bersifat untuk banyak halaman HTML. External Style menggunakan elemen ‘<link>’ untuk me-link¬ ke sebuah eksternal file CSS. <br />
-- Kelebihan : Karena properti CSS berada pada file yang terpisah, file HTML akan memiliki struktur yang lebih bersih dan berukuran lebih kecil. Selain itu, External Style dapat menggunakan file .css yang sama untuk beberapa halaman web. <br />
-- Kekurangan : Karena Inline dan Internal Style memiliki prioritas yang lebih tinggi, semua style yang berada pada External Style akan di-override oleh Inline dan Internal Style. Selain itu, mengunggah atau menautkan beberapa file CSS dapat meningkatkan waktu download web. Halaman web juga mungkin tidak di render dengan benar sampai CSS eksternal dimuat. <br />

## Tag HTML5
#### Jelaskan tag HTML5 yang kamu ketahui.
`<a>` : Mendefinisikan Hyperlink <br />
`<abbr>` : Mendefinisikan bentuk singkatan suatu kata atau frase yang lebih panjang <br />
`<address>` : Menspesifikasikan informasi kontak author <br />
`<area>` : Mendefinsikan sebuah spesifik area dalam image map <br />
`<article>` : Mendefinisikan sebuah artikel <br />
`<aside>` : Mendefinisikan beberapa konten yang berhubungan dengan konten halaman web <br />
`<audio>` : Memasukkan sound atau audio dalam dokumen HTML <br />
`<b>` : Menampilkan teks dalam style tebal atau bold <br />
`<base>` : Mendefiniskan URL dasar untuk semua URL relatif dalam dokumen <br />
`<bdi>` : Merepresentasikan teks yang terisolasi dengan tujuan text formatting <br />
`<bdo>` : Override teks direction <br />
`<blockquote>` : Merepresentasikan sebuah bagian yang diambil dari sumber lain <br />
`<body>` : Mendefinisikan bagian body suatu dokumen <br />
`<br>` : Menghasilkan sebuah line break <br />
`<button>` : Membuat sebuah tombol yang dapat di klik <br />
`<canvas>` : Mendefinisikan bagian atau wilayah dalam dokumen <br />
`<caption>` : Mendefinisikan caption atau judul suatu tabel <br />
`<cite>` : Menunjukkan kutipan atau referensi ke sumber lain <br />
`<code>` : Menspesifikasikan teks sebagai kode komputer <br />
`<col>` : Mendefinsikan nilai atribut untuk satu atau lebih kolom dalam tabel <br />
`<colgroup>` : Menentukan atribut untuk beberapa kolom dalam tabel <br />
`<data>` : Meletakkan konten yang memiliki terjemahan yang machine-readable <br />
`<datalist>` : Merepresentasikan set opsi yang telah ditentukan untuk suatu elemen input <br />
`<dd>` : Menspesifikasikan deskripsi pada dt dan dl <br />
`<del>` : Merepresentasikan teks yang telah dihapus dari dokumen <br />
`<details>` : Merepresentasikan widget dimana user dapat memperoleh informasi <br />
`<dfn>` : Menspesifikasikan sebuah definisi <br />
`<dialog>` : Mendefinsikan sebuah dialog box atau subwindow <br />
`<div>` : Menspesifikasikan sebuah bagian atau divisi dalam dokumen <br />
`<dl>` : Mendefinisikan sebuah list deskripsi <br />
`<dt>` : Mendefinsikan sebuah item pada list deskripsi <br />
`<em>` : Mendefinisikan teks yang ditekankan <br />
`<embed>` : Meletakkan aplikasi eksternal seperti konten media ke dalam dokumen HTML <br />
`<fieldset>` : Menentukan sebuah set mengenai form <br />
`<figcaption>` : Mendefinisikan sebuah keterangan atau legend untuk gambar <br />
`<figure>` : Merepresentasikan gambar yang diilustrasikan <br />
`<footer>` : Merepresentasikan footer sebuah dokumen atau bagian <br />
`<form>` : Mendefinisikan sebuah form HTML untuk input user <br />
`<head>` : Mendefinsikan bagian head dokumen seperti judul <br />
`<header>` : Merepresentasikan heade sebuah dokumen atau bagian <br />
`<hgroup>` : Mendefinsikan grup yang berisi header <br />
`<h1>` to `<h6>` : Mendefinisikan header HTML <br />
`<hr>` : Menghasilkan sebuah garis mendatar atau horizontal <br />
`<html>` : Mendefinisikan root dari suatu dokumen HTML <br />
`<i>` : Menampilkan teks dalam style miring atau italic <br />
`<iframe>` : Menampilkan sebuah url dalam Inline frame <br />
`<img>` : Merepresentasikan suatu gambar <br />
`<input>` : Mendefinisikan sebuah kontrol input <br />
`<ins>` : Mendefinisikan sebuah blok teks yang telah dimasukkan ke dalam dokumen <br />
`<kbd>` : Menentukan teks sebagai input keyboard <br />
`<keygen>` : Merepresentasikan kontrol untuk public-private key <br />
`<label>` : mendefinisikan sebuah label untuk kontrol input <br />
`<legend>` : Mendefinisikan caption untuk elemen fieldset <br />
`<li>` : Mendefiniskan sebuah list <br />
`<link>` : Mendefinisikan hubungan antara dokumen dan sumber eksternal <br />
`<main>` : Merepresentasikan bagian utama atau main dari program <br />
`<map>` : Mendefinisikan peta gambar dari sisi user <br />
`<mark>` : Merepresentasikan teks yang di-highlight untuk tujuan referensi <br />
`<menu>` : Merepresentasikan sebuah list commands <br />
`<menuitem>` : Mendefinsikan sebuah list commands yang dapat dilakukan oleh user <br />
`<meta>` : Menyediakan metadata terstruktur mengenai konten dalam dokumen <br />
`<meter>` : Merepresentasikan pengukuran skalaran dalam suatu range <br />
`<nav>` : Mendefinsikan sebuah bagian mengenai link navigasi <br />
`<noscript>` : Mendefinisikan konten alternative yang tidak mensupport frames <br />
`<object>` : Mendefinisikan sebuah object <br />
`<ol>` : Mendefinisikan list yang sudah terurut <br />
`<optgroup>` : Mendefinsikan sebuah kelompok yang berisi opsi yang saling berhubungan dalam section list <br />
`<option>` : Mendefinisikan opsi dalam selection list <br />
`<output>` : Merepresentasikan hasil dari suatu perhitungan <br />
`<p>` : Mendefinisikan paragraf <br />
`<param>` : Mendefinisikan sebuah parameter untuk suatu object <br />
`<picture>` : Mendefinisikan tempat untuk beberapa gambar <br />
`<pre>` : Mendefinisikan teks yang telah diformat <br />
`<progress>` : Merepresentasikan kemajuan penyelesaian suatu task <br />
`<q>` : Mendefinisikan kutipan Inline pendek <br />
`<rp>` : Menyediakan fall-bak parenthesis untuk browser yang tidak mensupport anotasi ruby <br />
`<rt>` : Mendefinisikan pengucapan suatu karakter yang direpresentasikan dalam anotasi ruby <br />
`<ruby>` : Mewakili anotasi ruby <br />
`<s>` : Mewakili konten yang sudah tidak akurat atau relevan <br />
`<samp>` : Menentukan teks sebagai output sampel dari suatu program <br />
`<script>` : Menempatkan skrip dalam dokumen untuk pemrosesan dari sisi klien <br />
`<section>` : Mendefinisikan bagian – bagian dari dokumen HTML <br />
`<select>` : Mendefinisikan daftar yang dipilih dalam suatu formulir <br />
`<small>` : Menampilkan teks dalam ukuran yang lebih kecil <br />
`<source>` : Mendefinisikan sumber media alternatif untuk elemen media <br />
`<span>` : Mendefinisikan bagian Inline Style <br />
`<strong>` : Menunjukkan teks yang ingin ditekankan <br />
`<tyle>` : Merepresentasikan informasi style ke dalam head dokumen <br />
`<sub>` : Mendefinisikan teks subscript <br />
`<summary>` : Mendefinisikan ringkasan untuk elemen details <br />
`<sup>` : Mendefinisikan teks superscript <br />
`<svg>` : Meletakkan konten SVG dalam dokumen HTML <br />
`<table>` : Mendefinisikan sebuah tabel <br />
`<tbody>` : Mengelompokkan sekumpulan baris yang mendefinisikan isi utama tabel <br />
`<td>` : Mendefinisikan cell dalam tabel <br />
`<template>` : Mendefinisikan elemen yang harus disembunyikan saat halaman HTML digunakan <br />
`<textarea>` : Mendefinisikan multi-line input teks <br />
`<tfoot>` : Mengelompokkan sekumpulan baris yang meringkas kolom tabel <br />
`<th>` : Mendefinisikan cell paling atas dalam tabel <br />
`<thead>` : Mengelompokkan sekumpulan baris yang menjelaskan kolom tabel <br />
`<time>` : Merepresentasikan waktu dan/atau tanggal <br />
`<title>` : Mendefinisikan judul untuk dokumen HTML <br />
`<tr>` : Mendefinisikan baris atau row dalam tabel <br />
`<track>` : Mendefinisikan text track dari elemen media <br />
`<u>` : Menampilkan teks dengan garis bawah <br />
`<ul>` : Mendefinisikan daftar yang tidak berurutan <br />
`<var>` : Mendefinisikan sebuah variabel <br />
`<video>` : Meletakkan video dalam dokumen HTML <br />
`<wbr>` : Merepresentasikan peluang sebuah line break <br />

## Tipe - Tipe CSS Selector
#### Jelaskan tipe-tipe CSS selector yang kamu ketahui.
**a. Simple Selector** : Memilih elemen berdasarkan nama, id, atau class. <br />
= Element selector (element) (Memilih elemen HTML berdasarkan nama elemennya), ID selector (#id) (Menggunakan atribut id suatu elemen HTML yang bersifat unik untuk memilih satu elemen spesifik), Class selector (.class atau element.class) (Memilih elemen HTML dengan spesifik atribut class tertentu), Universal selector (`*`) (Memilih semua elemen HTML pada halaman web), Grouping selector (element, element, …) (Memilih semua elemen HTML dengan definisi style yang sama). <br />
**b. Combinator Selector** : Memilih elemen berdasarkan hubungan spesifik antar elemen. <br />
= Descendant selector (element element (space)) (Memilih semua elemen yang merupakan turunan dari elemen tertentu), Child selector (element>element (>)) (Memilih semua elemen yang merupakan anak dari elemen tertentu), Adjacent Sibling selector (element+element (+)) (Memilih elemen yang berada di posisi langsung setelah elemen tertentu dan harus memiliki elemen parent yang sama), General Sibling selector (element1`~`element2) (Memilih semua elemen yang merupakan sibling berikutnya dari elemen tertentu). <br />
**c. Pseudo-class Selector** : Memilih elemen berdasarkan keadaan tertentu. <br />
= :active (Memilih link aktif), :checked (Memilih semua elemen input yang sudah dicek), :disabled (Memilih semua elemen input yang dinonaktifkan), :empty (Memilih semua elemen p yang tidak memiliki anak), :enabled (Memilih semua elemen input yang diaktifkan), :first-child (Memilih semua elemen p yang merupakan anak pertama dari parentnya), :first-of-type (Memilih semua elemen p yang merupakan elemen p pertama dari parentnya), :focus (Memilih elemen input yang memiliki focus), :hover (Memilih link yang berada di bawah kursor mouse), :in-range (Memilih semua elemen input dengan nilai pada range tertentu), :invalid (Memilih semua elemen input dengan nilai tidak valid), :lang(language) (Memilih semua elemen p yang memiliki atribut lang), :last-child (Memilih semua elemen p yang merupakan anak terakhir dari parentnya), :last-of-type (Memilih semua elemen p yang merupakan elemen p terakhir dari parentnya), :link (Memilih semua link yang belum pernah dikunjungi), :not(selector) (Memilih semua elemen yang bukan merupakan elemen p), :nth-child(n) (Memilih semua elemen p yang merupakan anak ke-n dari parentnya), :nth-last-child(n) (Memilih semua elemen p yang merupakan anak ke-n terakhir dari parentnya), :nth-last-of-type(n) (Memilih semua elemen p yang merupakan elemen p ke-n terakhir dari parentnya), :nth-of-type(n) (Memilih semua elemen p yang merupakan elemen p ke-n parentnya), :only-of-type (Memilih semua elemen p yang merupakan satu – satunya elemen p dari parentnya), :only-child (Memilih semua elemen p yang merupakan satu – satunya anak dari parentnya), :optional (Memilih semua elemen input yang tidak memiliki spesifik atribut required), :out-of-range (Memilih semua elemen input dengan nilai di luar range), :read-only (Memilih semua elemen input yang memiliki atribut readonly), :read-write (Memilih semua elemen input yang tidak ada atribut readonly), :required (Memilih semua elemen input dengan spesifik atribut required), :root (Memilih elemen root milik dokumen), :target (Memilih element yang sedang aktif yang berisi nama target nya), :valid (Memilih semua elemen input dengan nilai valid), :visited (Memilih semua link yang sudah pernah dikunjungi). <br />
**d. Pseudo-elements Selector** : Memilih dan styling sebuah bagian dari suatu elemen. <br />
= : :after (Menyisipkan beberapa konten setelah konten suatu elemen), : :before (Menyisipkan beberapa konten sebelum konten suatu elemen), : :first-letter (Menambahkan style khusus ke huruf pertama sebuah teks), : :first-line (Menambahkan style khusus ke baris pertama sebuah teks), : :marker (Memilih marker dari daftar item), : :selection (Memilih porsi tertentu dari suatu elemen yang sedang dipilih oleh user). <br />
**e. Attribute Selector** : Memilih elemen berdasarkan atribut atau nilai atributnya. <br />
= [attribute] selector ([attribute]) (Memilih elemen dengan atribut tertentu), [attribute=”value”] selector ([attribute=value]) (Memilih elemen dengan atribut dan nilai tertentu), [attribute~=”value”] selector ([attribute~=value]) (Memilih elemen dengan nilai atribut yang mengandung kata tertentu), [attribute|=”value”] selector ([attribute|=value]) (Memilih elemen dengan atribut yang ditentukan, dimana nilai yang ditentukan sama persis dengan nilainya), [attribute^=”value”] selector ([attribute^=value]) (Memilih elemen dengan atribut yang ditentukan, dimana nilainya dimulai dari nilai yang ditentukan), [attribute$=”value”] selector ([attribute$=value]) (Memilih elemen yang nilai atributnya diakhiri dengan nilai tertentu), [attribute*=”value”] selector ([attribute*=value]) (Memilih elemen yang nilai atributnya mengandung nilai tertentu). <br />

## Implementasi Poin 1-2
#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
> Kustomisasi templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma). <br />
> Ketentuan 1 : Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin. <br />
> Ketentuan 2 : Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task). <br />
> Membuat keempat halaman yang dikustomisasi menjadi responsive. <br />

Saya menggunakan bantuan CSS framework Bootstrap untuk melakukan kustomisasi templat halaman login, register, create-task, dan halaman utama to do list. Langkah pertama yang saya lakukan adalah menambahkan link bootsrap pada file `base.html`. Kemudian saya melakukan perubahan pada style dan hal - hal lain pada elemen - elemen HTML tersebut. Kemudian saya membuat keempat halaman yang sudah saya kustomisasi tersebut menjadi responsive. Hal terakhir yang saya lakukan ada melakukan add, commit, dan push ke Github. <br />
