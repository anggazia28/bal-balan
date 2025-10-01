# Tugas Individu PBP

## - Name : Angga Ziaurrohchman
## - NPM : 2406495943
## - Kelas : PBP E

## Link pws :https://angga-ziaurrohchman-balbalan.pbp.cs.ui.ac.id/ 

## Link Dokumentasi Tugas
### [Tugas 2](../../wiki/[README]-Tugas-Individu-2)
### [Tugas 3](../../wiki/[README]-Tugas-Individu-3)
### [Tugas 4](../../wiki/[README]-Tugas-Individu-4)

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut! 
Pada prioritas pertama adalah <!important> yang diikuti oleh inline style <style="> lalu <#id>, <.class> <[attr]> <:hover>, dan yang terakhir adalah urutan baris. Prioritas akan dilihat dari yang pertama, apabila sama sama prioritas misal sama sama important maka penentunya akan ada pada inline style nya, jika sama lalu id dan seterusnya. 
//

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Karena kita tidak selalu bisa memastikan user akan mengakses web dari device apa ? apakah android, IOS, desktop atau yang lainnya, sehingga jika kita tidak menerapkan responsive design maka tampilan web bisa saja rusak atau tidak sesuai dengan yang kita harapkan ketika itu dibuka pada device tertentu. Jika demikian maka user experience akan terganggu karena layout web yang tidak dapat menyesuaikan ukuran layar akan membuat keterbacaan teks, estetika, dan kemudahan penggunaan menjadi berkurang. 

Contoh aplikasi yang sudah menerapkan adalah Instagram Web yang dapat menyesuaikan layoutnya ketika dibuka pada desktop
Contoh aplikasi yang belum menerapkan adalah Website pemerintah dan web berita (namun sekarang aplikasi serupa jarang ditemukan)

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah area kosong di sekitar border untuk memisahkan 1 elemen dengan elemen lain, border adalah garis tepi yang membungkus konten dan paddingnya, sementara padding sendiri adalah area kosong di sektiar konten yang menjadi jarak dari inti konten ke border

Cara mengimplementasikannya ialah dapat diatur pada CSS dengan menambahkan margin, jika hanya 1 maka akan berlaku untuk semua sisi, 2 untuk vertikal dan horizontal dan jika ditentukan misal margin-top brti diatur bagian atas nya. Border dan Padding pun sama

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dirancang untuk mengatur satu dimensi antar item sehingga dapat diatur posisi horizontal ataupun vertikalnya dengan gap yang sama besar sementara Grid layout berarti membagi atau menjadikan posisinya dengan format baris dan kolom secara eksplisit. Misal dalam satu tampilan ada beberapa item yang saling sejajar, maka dapat digunakan grid dengan kolom yang sama, 

### Implementasi

#### Fungsi delete dan edit Product
Membuat function baru yaitu edit dan delete pada <views.py> lalu membuat template untuk edit dan import function pada <urls.py> serta menambahkannya ke path. Terakhir tentu saja menambahkan tombol edit dan delete pada template utama yaitu main dan menghubungkannya dengan href. 

#### Kustomisasi halaman login, register, tambah product, edit product, dan detail
Pertama perlu dimasukan script cdn di base html agar template django dapat terhubung dengan tailwind. Selanjutnya karena akan dikustomisasi tampilannya melalui tailwind css maka harus dikonfigurasi terlebih dahulu untuk static file pada aplikasi. 

Selanjutnya adalah menambahkan file global.css pada folder static dan dihubungkan dengan base.html dengan link rel. Sisanya adalah custom styling pada file css dan html sesuai yang diinginkan dengan menambahkan border, color, bg dll.

#### Kustomisasi halaman daftar produk 
##### Ada pesan belum ada produk
Menaruh foto pada direktori static/image dan menambahkan kode pada main.html dengan if else jika produk tidak ada maka akan menampilkan teks dan foto tadi (ditautkan dengan img src)

##### Terdapat card product
Membuat template card product lalu menambahkan kode inlcude card pada main.html agar bagian itu dapat diisi oleh tampilan card dengan jumlah sesuai card atau product yg ada

#### Card product dengan button edit dan delete
Menambahkan button atau teks di template card dan menyambungkannya ke urls edit dan delete dengan href.

#### Navigation Bar
Membuat template untuk navigation bar folder template aplikasi kemudian ditautkan pada <main.html> dengan <include>. 