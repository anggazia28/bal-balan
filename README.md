# Tugas Individu PBP

## - Name : Angga Ziaurrohchman
## - NPM : 2406495943
## - Kelas : PBP E

## Link pws :https://angga-ziaurrohchman-balbalan.pbp.cs.ui.ac.id/ 
## Link Dokumentasi Tugas
### [Tugas 2](../../wiki/[README]-Tugas-Individu-2)

### Mengapa kita perlu data delivery dalam pengimplementaian sebuah plaform

Data delivery berguna agar data di platform kita yang ada pada database dapat dikirim ke sistem lain dan data dapat diakses dengan lebih cepat dan aman tanpa harus masuk ke sistem database terlebih dahulu, Selain itu dapat digunakan dengan API delivery

### Mana yang lebih baik antara XML dan JSON? mengapa JSON lebih populer dibandingkan XML

Karena kebanyakan scripting language itu javascript dan JSON lebih kompatibel ke javascript, berbeda dengan XML yang lebih strict. JSON juga punya kelebihan seperti lebih ringan dan sintaks lebih gampang (ringkas) dibaca.

JSON lebih populer karena ukurannya lebih kecil daripada XML sehingga transfer data akan lebih cepat. Struktur JSON juga seperti dictionary (key:value) sehingga lebih mudah dipakai. Dalam integrasi web, JSON bisa diparse oleh JavaScript tanpa tambahan Library.

### Fungsi <is_valid()> pada form Django

<is_valid()> digunakan untuk mengecek data yang disubmit sesuai validation rules yang ada seperti nama produk dibatasi hingga 100 karakter, maka jika lebih dari itu akan menampilkan pesan eror

### Mengapa kita membutuhkan <csrf_token> saat membuat form di Django? dan bagaimana jika tidak ? apakah itu dapat dimanfaatkan oleh penyerang?

Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya. Ini berguna agar yang dapat mengakses request POST (dalam konteks tugas ini berarti membuat news atau menambahakan produk) web hanyalah domain yang kita izinkan dalam CSRF_TRUSTED_ORIGINS

Jika tidak menggunakan ini maka server akan menerima semua request sehingga nanti penyerang dapat mendapatkan akses seperti user

### Implementasi

#### Menambahkan 4 fungsi views
Menambahkan/Menuliskan fungsi baru (def) pada file views.py dengan return yang diinginkan, pada konteks ini salah satu contohnya adalah <HttpResponse(xml_data, content_type="application/xml")> yang akan memberikan respon berupa file xml yang berisi data dari produk baik semua atau yang berdasarkan id

#### Membuat routing URL untuk masing masing views
Menambahkan nama function di import file urls.py agar dapat function dapat dikenali dan nantinya dapat diarahkan ke function yang sesuai lalu menamnbahkan path url ke urlpattern agar terdaftar, jadi setiap ada request dengan path tersebut bisa langsung diarahkan (karena udh ada di path jalurnya) ke function yang terdaftar tadi

#### Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" dan "Detail"
Mengedit file main.html pada templates pada aplikasi dengan menambahkan tombol/button yang dapat berpindah ketika dipencet ke link/url yang disiapkan melalui <href="{% url 'main:add_product' %}"> (format djanglo template)
Dalam hal ini digunakan for loop agar semua item yang ada dapat ditampilkan

Juga menyiapkan file html lain yang merupakan tujuan dari button tersebut, dlm tugas ini ada 2 yaitu detail dan add

#### Membuat halaman form untuk menambahkan objek model 
menambah file html lain yang sudah disebutkan tadi yaitu add dengan menyambungkannya dengan file forms.py yg berisi atribut apa saja yang akan digunakan 

#### Membuat halaman yang menampilkan detail dari setiap data 
menambah file html lain yang sudah disebutkan juga yaitu detail, berisi sebuah atribut/data dari produk yang ingin ditampilkan beserta tombol back yang mengarah ke halaman utama (main.html)

### Screenshoot Postman
![alt text](<Screenshot 2025-09-17 105512.png>) 
![alt text](<Screenshot 2025-09-17 103808.png>) 
![alt text](<Screenshot 2025-09-17 103831.png>) 
![alt text](<Screenshot 2025-09-17 105441.png>)