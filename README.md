# Tugas Individu PBP

## - Name : Angga Ziaurrohchman
## - NPM : 2406495943
## - Kelas : PBP E

## Link pws :https://angga-ziaurrohchman-balbalan.pbp.cs.ui.ac.id/ 

## Link Dokumentasi Tugas
### [Tugas 2](../../wiki/[README]-Tugas-Individu-2)
### [Tugas 3](../../wiki/[README]-Tugas-Individu-3)

### Apa itu Django AuthenticationForm? apa kelebihan dan kekurangannya 
Modul bawaan dari django yang memungkinkan/menyiapkan proses login user yang sudah berisi field username dan password beserta validasi input serta autentikasi ke database.

Kelebihannya lebih praktis, kita tidak perlu membangun proses login dari awal dan hanya tinggal memakai/menerapkan modul yg sudah ada. Selain itu modul ini juga dapat dikustomisasi sehingga lebih fleksibel. 
Kekurangannya ada pada sifat generiknya sehingga kita masih perlu menyiapkan field baru agar laman login lebih proper

### Apa perbedaan antara autentikasi dan ototrisasi dan Bagaimana Django mengimplementasikan kedua konsep tersebut
Autentikasi adalah proses mencocokan/mengecek apakah user/data yang masuk atau login ini benar benar ada sebelumnya pada database, sementara otorisasi adalah memberikan akses untuk user yang login kepada fitur fitur yg sesuai dengan role nya. 

Pada proses autentikasi, django sudah punya sistem bawaan yaitu contrib.auth yang jika digunakan akan memudahkan kita karena proses autentikasi backend (seperti memverifikasi, menyimpan informasi session) akan secara otomatis dilakukan oleh django, tanpa harus disetting secara manual. Pada proses otorisasi, django menerapkan flag khusus untuk tiap user, jadi objek user punya atribut seperti grup yang nantinya dalam grup itu bisa kita tentukan akses/permission apa saja yang diberikan. Dalam function function yang akan diberikan pembatasan berdasarkan grup, dpat diberikan decorator diatas functionnya. 

### Apa kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Cookies lebih sederhana karena bisa langsung dibaca via HTTP header, data yang disimpan tidak terlalu banyak, namun kapasitas maksimal 4kb, kurang aman karena data disimpan di browser, dan dapat membebani request.

Session lebih aman karena data tidak disimpan di browser melainkan di server, kapasitas lebih besar, dan lebih mudah dikontrol karena admin web dapat menghapus session. Akan tetapi semakin banyak user, semakin besar pula storage manajemen session di server

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai ? Bagaimana Django menangani hal tersebut?
Tergantung, dapat dikatakan cookies cukup namun bukan berarti aman absolut by default karena banyak potensi potensi risiko yang bisa muncul seperti Injection XSS yaitu pencurian data dalam cookies jika peretas berhasil melakukan injeksi kode Javascript yang akan dieksekusi oleh client dan mencuri cookies. Selain itu terdapat potensi data dalam cookie bisa dilihat di jaringan jika tanpa HTTPS dan masih banyak potensi resiko lain. 

Penanganan Django untuk hal hal tersebut adalah seperti menyimpan data di session dan id session di cookies, rotasi session key, CSRF, 

### Implementasi tugas secara step by step

#### Mengimplementasikan fungsi registrasi, login, dan logout 
Mengimport method bawaan dari Django seperti UserCreationForm, Login, Logout, dari django.contrib.auth dan auth.forms. Lalu membuat function register, login, dan logout. Membuat template html dari login dan register, menambahkan button logout di main.html, dan menghubungkannya lewat urls.py dengan cara mengimport function yang sudah dibuat lalu menuliskan/memasukan path nya ke urlpatterns

#### Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal
Mendaftar akun dengan register lalu add product masing masing akun 3 product

![alt text](<Screenshot 2025-09-22 225054.png>) 
![alt text](<Screenshot 2025-09-22 225125.png>) 
![alt text](<Screenshot 2025-09-22 225137.png>) 
![alt text](<Screenshot 2025-09-22 225149.png>) 
![alt text](<Screenshot 2025-09-22 225204.png>) 
![alt text](<Screenshot 2025-09-22 225222.png>) 

#### Menghubungkan model Product dengan User
Mengimpor method User dan menambahkan atribut user dengan datatype foreignKey pada Class Product di models.py lalu migration

#### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi
Mengimpor method yg dibutuhkan lalu menambahkan kode untuk mendaftarkan cookie last login dengan isi timestamp terkini agar dapat ditampilkan. Pada function show main ditambahkan item context baru yaitu last login untuk mengambil cookies last login sebelumnya/terakhir.

Modifikasi template yaitu main.html untuk menampilkan last login dan mengubah context name menjadi username dari client/request yang sedang aktif
