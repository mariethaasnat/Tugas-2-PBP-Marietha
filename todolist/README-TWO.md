# Tugas 6 PBP - README
Nama : Marietha Asnat Nauli Sitompul <br />
NPM : 2106752413 <br />
Kelas : PBP - B <br />
Kode Asdos : BI
#### [Link Aplikasi Heroku](https://tugas2pbpasnat.herokuapp.com/todolist/)

## Perbedaan _Asynchronous Programming_ dan _Synchronous Programming_
#### Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_.
**Asynchronous Programming** <br />
Model _programming multithreaded_ (dapat digunakan oleh lebih dari satu user tanpa membutuhkan duplikasi dari program yang sedang dijalankan) yang paling sering diaplikasikan pada jaringan dan komunikasi. _Asynchronous_ bersifat _non-blocking_ yang berarti model ini tidak memblokir eksekusi lebih lanjut saat satu atau lebih operasi sedang berlangsung, sehingga beberapa operasi yang berhubungan dapat dijalakan secara bersamaan tanpa menunggu _task_ lain untuk diselesaikan. Salah satu contoh _Asynchronous Programming_ adalah SMS, dimana saat satu orang mengirim pesan teks dan penerima belum merespon teks tersebut, pengirim dapat melakukan hal lain selagi menunggu jawaban dari penerima. <br />
**Synchronous Programming** <br />
Model _programming single-thread_ (hanya dapat menjalankan satu eksekusi setiap waktunya) dan ideal untuk pemrograman yang bersifat reaktif. _Synchronous_ bersifat _blocking_ yang berarti model ini akan mengikuti rangkaian operasi yang akan dieksekusi dan setiap operasi atau eksekusi dilakukan satu per satu, sehingga saat suatu operasi dijalankan, operasi lainnya diblokir dan tidak dapat dijalankan. Penyelesaian suatu operasi akan memicu operasi berikutnya dan seterusnya hingga selesai. Salah satu contoh _Synchronous Programming_ adalah telepon, dimana saat satu orang berbicara, orang yang satunya mendengarkan, dan saat orang pertama selesai, orang kedua cenderung segera merespons orang pertama tersebut. <br />
**Perbedaan _Asynchronous Programming_ dan _Synchronous Programming_** <br />
| Asynchronous Programming | Synchronous Programming |
| --- | --- |
| Bersifat _non-blocking_ sehingga eksekusi suatu task tidak bergantung pada task lain (dapat mengirim beberapa request sekaligus ke server) | Bersifat _blocking_ sehingga eksekusi setiap operasi bergantung kepada penyelesaian operasi yang sebelumnya (hanya dapat mengirim satu request) |
| Bersifat _multi-thread_ sehingga operasi dapat dijalankan secara paralel | Bersifat _single-thread_ sehingga hanya satu operasi yang dapat dijalankan pada satu waktu |
| Meningkatkan _throughput_ karena beberapa oprasi dapat dijalankan secara bersamaan | Berjalan lebih lambat dan lebih _methodical_ |
| Digunakan untuk _task_ yang bersifat independen, dimana ia memainkan peran penting | Digunakan untuk _task_ yang bersifat dependen, lebih mudah untuk digunakan dan tidak memerlukan pengukuran alur prosesnya |

## Penerapan _Event-Driven Programming_ dalam JavaScript dan AJAX serta Contoh Penerapannya
#### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma _Event-Driven Programming_. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
_Event-Driven Programming_ adalah sebuah paradigma dimana objek, _services_, dan lain sebagainya, berkomunikasi secara tidak langsung dengan mengirimkan pesan ke satu sama lain melalui suatu perantara. Dalam kata lain, alur dari program bergantung pada event yang dilakukan antara _user_ dan _client_. Salah satu contohnya adalah saat sebuah button diklik dimana program ini menerapkan konsep _Asynchronous Programming_. Contoh penerapan _Event-Driven Programming_ pada tugas ini adalah saat melakukan AJAX POST. AJAX POST dipanggil saat user membuat task baru, yaitu saat button “create new task” diklik, fungsi AJAX POST tersebut akan dijalankan dan mengirimkan data ke server. <br />

## Penerapan _Asynchronous Programming_ pada AJAX
#### Jelaskan penerapan _asynchronous programming_ pada AJAX.
Pada AJAX, salah satu bentuk penerapan _Asynchronous Programming_ adalah saat terjadi sedikit perubahan data dalam pembuatan website, tidak perlu dilakukan reload. Seperti yang telah disebutkan sebelumnya, _event-driven programming_ merupakan salah satu penerapan _Asynchronous Programming_ pada AJAX. Selain AJAX POST, AJAX GET juga merupakan salah satu implementasi dari _Asynchronous Programming_. Data yang ditangkap akan dikirim ke dalam server tanpa melalui browser reload. AJAX akan menangkap operasi yang akan dijalankan dan mengirimnya ke dalam server agar datanya diubah menjadi _Asynchronous_. <br />

## Implementasi Poin 1 - 2
#### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.
**Poin 1 : Implementasi AJAX GET** <br />
Menambahkan sebuah fungsi baru pada file `views.py` yang akan mengembalikan _task_ sesuai dengan user log in dalam bentuk JSON. Kemudian saya membuat sebuah routing `/json` pada file `urls.py` agar dapat diakses oleh user. Lalu saya melakukan pemanggilan AJAX GET untuk mengambil task dalam bentuk JSON kemudian disimpan ke dalam tabel. <br />

**Poin 2 : Implementasi AJAX POST** <br />
Membuat sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task dengan cara mengubah direct yang sebelumnya menuju `todolist/newtodolist` menjadi memunculkan sebuah modal. Menambahkan sebuah fungsi baru pada file `views.py` yang akan menambahkan _task_ baru ke dalam database. Kemudian saya membuat sebuah routing `/add` pada file `urls.py` yang mengarah ke view yang baru. Modal tersebut akan memunculkan sebuah form yang akan diisi task baru. Kemudian dilakukan pemanggilan AJAX POST dimana data tersebut akan dikirim ke server atau database kemudian diproses. Jika berhasil membuat sebuah task baru, maka akan terjadi pemanggilan fungsi kembali (fungsi AJAX POST) dan menutup modal tersebut. 
