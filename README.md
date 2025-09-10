# Tugas Individu 2 PBP

## - Name : Angga Ziaurrohchman
## - NPM : 2406495943
## - Kelas : PBP E

#Link :https://angga-ziaurrohchman-balbalan.pbp.cs.ui.ac.id/# 

### Cara Implementasi checklist step by step

#### 1. Membuat proyek Django baru
Siapkan direktori yang akan digunakan untuk proyek lalu aktifkan environment. Instal semua dependencies proyek lalu tinggal menjalankan django-admin startproject <nama_proyek> yang akan membuat struktur direktori proyek django secara otomatis. Jika struktur direktori sudah selesai dibuat maka tinggal meengatur agar local host dan host lain dapat mengakses aplikasi dengan mengaturnya di setting.py.

#### 2. Cara membuat aplikasi
Membuat aplikasi memakai python manage.py startapp main lalu mendaftarkannya di installed app.

#### 3. Melakukan routing pada proyek
Setelah proyek berhasil dibuat, tambahkan rute pada <urls.py> untuk mengarahkan request ke aplikasi, pada hal ini adalah main melalui <show_main>

#### 4. Membuat model pada aplikasi main 
Pada file <models.py> didalam aplikasi main, buat model <Product> yang memiliki atribut <name>,<price>,<thumbnail>,<category>,<is_featured>, dan atribut tambahan lain yang digunakan sebagai penyimpanan data produk ke dalam database

#### 5. Fungsi pada views.py 
Pada <views.py> buat context sbg isian data yang akan dikirimkan ke tampilan html atau yang kita sebut template dlm hal ini, jadi html sbg template dan views sbg isi yang akan ditampilkan dalam template nya

#### 6. Routing pada urls.py aplikasi main untuk memetakan fungsi 
Di <urls.py> pada aplikasi main, tambah impor fungsi include lalu tambah rute url di path pada bagian urlpattern agar dapat mengarahkan tampilan ke main

#### 7. Melakukan deployment ke PWS 
Setelah semua langkah sudah dilakukan, lakukan deployment ke PWS dengan membuat proyek baru pada PWS dan mengkonfigurasikan environment, memberikan akses host di <setting.py> lalu push dan login menggunakan credential

#### 8. Membuat <README.md> yang berisi tautan menuju aplikasi PWS dan jawaban pertanyaan
Buat file baru di direktori utama proyek dengan nama <README.md> dan isi dengan jawaban

### Bagan request client ke web aplikasi berbasis Django serta kaitan antara <urls.py>, <views.py>, <models.py>, dan berkahs <html>
!["bagan"](https://drive.google.com/uc?export=view&id=1S2qUuFF2JsCjEW5vKEQsRgYrPFK1sa40)

User melalui web browser mengirimkan request dengan HTTP ke server lalu melalui manage.py akan diproses dan mengarahkan ke urls.py dimana di urls.py akan mencocokan URL dengan daftar yg ada. Jika ditemukan kecocokan maka akan dilanjutkan ke view.py dan jika tidak akan mengembalikan 404 Not Found. Pada views.py request akan diproses dan jika membutuhkan data dari database maka akan melibatkan models.py untuk mengambil data dari database. Di views ini ada data yang akan dimasukan ke template(html) lalu setelah digabungkan dan dirender, hasilnya akan dikembalikan ke user.

- urls.py = mencari atau mengarahkan request ke aplikasi yang tersedia
- views.py = memproses logika tampilan dan data
- models.py = menghubungkan ke database dan menyediakan data apabila dibutuhkan
- html = tampilan yang dikembalikan ke user

### Peran setting.py
setting.py adalah pusat kendali dalam proyek Django karena semua konfigurasi inti ada dan diatur oleh setting.py. Hal hal yang biasanya diatur adalah database apa saja yang perlu dipakai, aplikasi mana yang aktif, mekanisme request, dan lokasi tiap file, template, dan data. 

### Cara kerja migrasi data
Migrasi database pada Django adalah mekanisme untuk menjaga konsistensi antara definisi model pada models.py dengan struktur database yang sebenarnya. Dimulai dengan perintah makemigrations, yang menghasilkan berkas migrasi berisi catatan perubahan model. Selanjutnya, perintah migrate akan mengeksekusi berkas tersebut menjadi instruksi SQL untuk membuat atau mengubah tabel di database. Sistem migrasi ini juga menyimpan riwayat perubahan sehingga pengembang dapat melakukan sinkronisasi maupun rollback bila diperlukan.

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Karena Django menyediakan hampir seluruh kebutuhan dasar pengembangan aplikasi web secara terintegrasi, seperti ORM, autentikasi, sistem templating, dan panel administrasi yang memudahkan mahasiswa  untuk memahami konsep arsitektur perangkat lunak modern, mulai dari pemisahan lapisan (URL, view, model, template), pengelolaan basis data, hingga aspek keamanan. 