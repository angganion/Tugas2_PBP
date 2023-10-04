# Tugas2_PBP


1. dalam mengerjakan tugas ini hal pertama yang saya lakukan adalah membuat sebuah repo di gthub dan mnambahakan readme.md beserta .gitignore, setelah selesai membuat repo tersebut saya mengcloning repo tersebut ke dalam directory local saya dengan git clone. setelah selesai memiliki repo git untuk tugas ini kemudia saya membuat virtual environment di dalam folder tersebut dan melakukan instalasi terhadapa semua requirents yang di butuhkan dengan melakukan command pip install requirments.txt. setelah itu saya menjalankan perintah "django-admin startproject inventory_gacor" untuk memulai project django. kemudian membuat app dengan "django-admin startapp main". kemudian saya menambahkan file urls.py dan mengisinya dengan beberapa line agar app main dapart dijangkau oleh user. kemudian saya membuat kelas item di models dan mengisinya dengan ketentuan yang ada. setelah itu saya mengisi views.py dan html nya

2. ![image](https://github.com/angganion/Tugas2_PBP/assets/120027733/9c978e79-76f8-481b-b222-497e72b0fc79)


3. Virtual Env di gunakan unntuk memepermudah kita saat melakukan pengerjaan project, karena dengan menggunakan env kita bisa menginstall banyak modul atau package yang tidak terhubung dengan komputer kita, dengan hal tersebut kita tidak perlu takut akan terjadi bentrok antara 1 package dengan package yang lain karena mungkin suatu saaat kita akan membuat 2 projrect dengan package yang sama namun dengan versi yang berbeda dan virtual env dapat mengatasi masalah seperti itu. jadi virtual env sebenarnya bukanlah hal yang wajib dan benar benar diperlukan saar membuat project django, namun itu adalah suatu langkah yang akan sangat mempermudah kita saat mengerjakan beberapa project bersaamaan yang berbeda

4. MVC, MVT, dan MVVM adalah tiga arsitektur desain yang umum digunakan dalam pengembangan perangkat lunak. Mereka membagi aplikasi menjadi tiga komponen utama: Model, View, dan penghubung antara keduanya.

---MVC (Model-View-Controller)---

Model: Ini adalah komponen yang menyimpan data dan berisi logika bisnis. Model ini independen dari View dan Controller.

View: Bagian ini bertanggung jawab untuk menampilkan data kepada pengguna. Dalam MVC, View berfungsi sebagai antarmuka pengguna.

Controller: Controller berfungsi sebagai perantara antara Model dan View. Ini menerima input dari pengguna, memanipulasi Model sesuai input tersebut, dan kemudian memberitahu View untuk memperbarui tampilan dengan data yang diperbarui.

---MVT (Model-View-Template)---

Model: Mirip dengan MVC, Model di MVT menyimpan data dan logika bisnis.

View: View dalam MVT juga bertanggung jawab untuk menampilkan data kepada pengguna, mirip dengan MVC.

*Template: Template menggantikan peran Controller yang ada di MVC. Dalam MVT, View berperan dalam menerima input dari pengguna, memanipulasi Model sesuai input, dan menampilkan data yang diperbarui. Template adalah bagian yang mengatur bagaimana data ditampilkan dalam View.

---MVVM (Model-View-ViewModel)---

Model: Sama seperti dalam MVC dan MVT, Model di MVVM berisi data dan logika bisnis.

View: View dalam MVVM bertanggung jawab untuk menampilkan data kepada pengguna. Namun, dalam MVVM, View sangat pasif dan hanya berfokus pada tampilan.

*ViewModel: ViewModel adalah komponen yang menjembatani Model dan View. ViewModel mengelola data dari Model dan mengonversinya ke dalam format yang mudah ditampilkan oleh View. ViewModel juga menangani logika tampilan, sehingga View hanya perlu fokus pada tampilan dan interaksi dengan pengguna. ViewModel 
memungkinkan isolasi antara Model dan View.

Jadi, perbedaan utama antara ketiga arsitektur ini adalah bagaimana penghubung antara Model dan View diatur. MVC menggunakan Controller, MVT menggunakan Template, sedangkan MVVM menggunakan ViewModel untuk menjaga isolasi dan pemisahan yang lebih baik antara komponen-komponen aplikasi

# Tugas3_PBP
1. Apa perbedaan antara form POST dan form GET dalam Django?

form post berguna untuk mengirim data form ke dalam database server, sedangkan form get digunakan untuk mendapaatkan form dari user

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

XML adalah bahasa markup yang digunakan untuk menyimpan dan mengangkut data, JSON adalah format pertukaran data yang ringan, HTML adalah bahasa markup yang digunakan untuk membuat halaman web

Dalam konteks pengiriman data, perbedaan utama antara ketiga format ini adalah cara mereka merepresentasikan data. HTML digunakan untuk merepresentasikan konten web, seperti teks, gambar, dan video. XML digunakan untuk merepresentasikan data terstruktur, seperti informasi produk atau informasi pelanggan. JSON juga digunakan untuk merepresentasikan data terstruktur, tetapi lebih sering digunakan dalam aplikasi web modern karena ukurannya yang lebih kecil dan kemampuannya untuk diurai dengan mudah oleh JavaScript.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

karena JSON lebih ringan dan lebih mudah untuk diakses

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

hal pertama yang saya lakukan saat mengerjakan tugas ini adalah membuat file forms.py agar bisa membuat form, kemudian saya mengedit file html agar ada create product dan membuat fungsi create_product di views.py, kemudian saya membuat semua fungsi yang dibutuhkan yaitu view berdasarkan html, xml, json, xml by id, json by id. untuk html saya membuat sebuah file html baru bernama items.html yang isinya hanya daftar dari item yang ada, untuk xml dan json saya memakai serialize dan untuk by id saya memfilter item by id. setelah itu saya menambahkan semua urls ke dalam urls main. setelah itu saya mengerjakn html main untuk dapat mendisplay semua barang dengan forloop. setelah itu saya mengerjakn bagian bonus dengan memakai kondisi di html yang jika item ada maka akan di render banyak barang adalah item|legths dan jika item tidak ada akan di render tidak ada item di aplikasi

![Screenshot 2023-09-17 204610](https://github.com/angganion/Tugas2_PBP/assets/120027733/6db4ee12-971d-4727-9f41-4b5a31ab9e7a)
![Screenshot 2023-09-17 203953](https://github.com/angganion/Tugas2_PBP/assets/120027733/4ed0c94b-588f-4ba9-99de-b57ed1110eb1)
![Screenshot 2023-09-17 204009](https://github.com/angganion/Tugas2_PBP/assets/120027733/d899c57b-3853-466e-ad85-4b38b4b6177f)
![Screenshot 2023-09-17 204026](https://github.com/angganion/Tugas2_PBP/assets/120027733/0d634ca9-c350-49f6-aad1-5f9e21ae6510)
![Screenshot 2023-09-17 204039](https://github.com/angganion/Tugas2_PBP/assets/120027733/4eafddf0-02de-4231-b9cd-1fa14e2edc69)


# tugas4_PBP

 ----------Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Django UserCreationForm adalah sebuah bentuk (form) yang disediakan oleh Django untuk mempermudah proses pembuatan pengguna (user) dalam aplikasi web yang menggunakan Django. Form ini biasanya digunakan dalam proses registrasi pengguna baru. Beberapa kelebihan dan kekurangan dari UserCreationForm adalah:

Kelebihan:

---Mudah Digunakan: UserCreationForm sudah siap pakai dan mengikuti konvensi Django, sehingga tidak perlu membuat form registrasi dari awal.

---Validasi Otomatis: Form ini mencakup validasi otomatis untuk memastikan data yang dimasukkan sesuai dengan kebutuhan seperti panjang password, format email, dsb.

---Integrasi dengan Model User: UserCreationForm secara otomatis terhubung dengan model User Django, yang membuat proses penyimpanan data pengguna ke database menjadi mudah.

Kekurangan:

---Terbatas pada Fitur Bawaan: UserCreationForm memiliki fitur bawaan yang mungkin tidak sesuai dengan kebutuhan kita. Jika kita memerlukan atribut tambahan atau validasi kustom, perlu penyesuaian

---Tampilan Terbatas: Form ini tidak mengurus tampilan (UI) secara penuh. masih perlu mendesain tampilan registrasi yang sesuai dengan kebutuhan aplikasi yang di inginkan

----------Perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

---Autentikasi (Authentication): Autentikasi adalah proses verifikasi identitas pengguna. Dalam konteks Django, ini mencakup memeriksa apakah pengguna yang mencoba mengakses aplikasi adalah pengguna yang telah terdaftar dan memiliki kredensial yang valid (misalnya, username dan password). Django menyediakan berbagai metode autentikasi, termasuk otentikasi berbasis sesi, token, dan OAuth, untuk memverifikasi identitas pengguna.

---Otorisasi (Authorization): Otorisasi adalah proses menentukan akses apa yang diberikan kepada pengguna setelah mereka berhasil terautentikasi. Ini mengatur hak akses pengguna terhadap berbagai bagian aplikasi, misalnya, apa yang dapat mereka baca, tulis, atau hapus. Django menggunakan sistem izin (permission) untuk mengatur otorisasi, yang memungkinkan Anda untuk menentukan aturan-aturan terkait akses.

---Keduanya penting karena:

Autentikasi memastikan bahwa hanya pengguna yang sah yang memiliki akses ke aplikasi, melindungi data dan sumber daya dari akses yang tidak sah.
Otorisasi memungkinkan untuk mengontrol tingkat akses pengguna, memastikan bahwa pengguna hanya dapat melakukan tindakan sesuai dengan peran atau izin yang mereka miliki. Ini membantu melindungi data sensitif dan menjaga keamanan aplikasi.

----------Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah file teks kecil yang disimpan di sisi klien (browser) saat pengguna berinteraksi dengan sebuah situs web. Cookies digunakan untuk menyimpan informasi di sisi klien yang dapat digunakan oleh situs web tersebut untuk mengidentifikasi dan mengingat informasi tentang pengguna, seperti preferensi, data sesi, atau detail otentikasi.

Django menggunakan cookies untuk mengelola data sesi pengguna. Data sesi adalah cara untuk menyimpan informasi tentang pengguna di server web, tetapi mengidentifikasinya dengan unik melalui cookie di sisi klien. Django akan mengatur cookie pada sisi klien yang berisi ID sesi unik, dan data sesi yang sesungguhnya akan disimpan di server. Setiap kali pengguna mengirimkan permintaan ke server, ID sesi akan digunakan untuk mengambil data sesi yang sesungguhnya.

----------Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan cookies dalam pengembangan web memiliki risiko potensial yang perlu diwaspadai. Beberapa risiko dan pertimbangan meliputi:

Keamanan Data: Data yang disimpan dalam cookies dapat dibaca oleh siapa saja jika tidak dienkripsi. Ini bisa menjadi masalah jika cookies mengandung informasi sensitif seperti token otentikasi atau data pengguna pribadi.

Cross-Site Scripting (XSS): Serangan XSS dapat dimanfaatkan untuk mencuri cookies pengguna dan mengakses sesi mereka jika tidak ada tindakan perlindungan yang kuat.

Cross-Site Request Forgery (CSRF): Cookies juga dapat digunakan dalam serangan CSRF jika tidak diatur dengan benar.

Pemantauan Jejak (Tracking): Cookies juga digunakan untuk melacak aktivitas pengguna secara online, yang dapat menjadi masalah privasi.

-----------Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

pertama saya membuat fungsi registrasi dengan mengambil form dari bawaan django dan menaruhnya di views.py dan memberikan perintah ketika post form nya akan di masukkan dan disimpan. karena fungsi sudah selesai, kemudian saya membuat html untuk tampilan form yang akan diisi oleh pengguna. kemudian memasukkan urls nya ke urls.py, karena fungsi registrasi sudah selelesai saya kemudian membuat fungsi untuk login dari data registrasi yang telah disimpan, saya akan get username dan password user kemudian akan saya cek di data user jika ada akan saya balikan main page dan akan set cookie sehingga nanti bisa menampilkan cookie dan saya juga menambahkan cookie di context. jika tidak maka tidak akan masuk, setelah fungsi selesai saya membuat html login page pada templates untuk menampilkan halaman login user yang berisi tempat untuk username dan password. setelah itu saya menaruh urls login ke urls.py. kemudian saya menambahkan @login_required(login_url='/login') diatas show main agar saat kita membuka web tidak akan langsung masuk ke main page kecuali kita login terlebih dahulu. kemudian saya membuat fungsi logout dari bawaan django serta menambahkan perinth untuk hapus cookie jika melakukan logout

setelah itu saya membuat fungsi untuk menyimpan user dengan barangnya masing masing, dengan memodifikasi models.py pada kelas item dengan menambahkan atribut user. sehingga setipa item akan unik ke user user tertentu saja. kemudian di fungsi create product di user saya menambahkan variable user ke dalam product tersebut. kemudian pada showmain saya akan menampilkan username dari login user kemudian di productnya saya akan fill berdasarkan usernya siapa sehingga product yang ditampilkan nanti hanya miliki si user ini


---------2 user dengna 3 dummy data

![Screenshot (295)](https://github.com/angganion/Tugas2_PBP/assets/120027733/bc99d360-a143-4b6e-b9cb-2337a030cd46)
![Screenshot (296)](https://github.com/angganion/Tugas2_PBP/assets/120027733/deec4f9b-2b5f-451a-aa0b-23c3666c900a)


# tugas5_PBP


1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya

---universa Selector:  

Manfaat: Universal selector memilih semua elemen dalam dokumen HTML.

Kapan digunakan: Biasanya digunakan untuk memberikan gaya default atau reset pada semua elemen, tetapi harus digunakan dengan hati-hati karena dapat mempengaruhi semua elemen di halaman.

---Type Selector (Element Selector):

Manfaat: Memilih semua elemen dengan tipe tertentu (misalnya, <p>, <h1>, <a>).

Kapan digunakan: Digunakan ketika Anda ingin memberikan gaya khusus pada tipe elemen tertentu.

---Class Selector (.classname):

Manfaat: Memilih semua elemen yang memiliki atribut class tertentu.

Kapan digunakan: Berguna ketika Anda ingin menggabungkan beberapa elemen yang memiliki karakteristik atau fungsi yang sama.

---ID Selector (#idname):

Manfaat: Memilih elemen dengan ID tertentu.

Kapan digunakan: Digunakan ketika Anda ingin memberikan gaya unik pada satu elemen tertentu. Sebaiknya hindari penggunaan ID selector untuk menggaya banyak elemen dengan gaya yang sama karena ID harus unik dalam satu halaman.

---Attribute Selector ([attribute=value]):

Manfaat: Memilih elemen yang memiliki atribut tertentu dengan nilai tertentu.

Kapan digunakan: Berguna ketika Anda ingin menggaya elemen berdasarkan atribut mereka, seperti memilih semua tautan dengan atribut target="_blank".

---Pseudo-class Selector (:pseudo-class):

Manfaat: Memilih elemen berdasarkan kondisi atau interaksi pengguna, seperti :hover untuk menggaya saat kursor berada di atas elemen atau :focus untuk menggaya elemen yang sedang difokuskan.

Kapan digunakan: Digunakan untuk menggaya elemen dalam respons terhadap tindakan pengguna tertentu.

---Pseudo-element Selector (::pseudo-element):

Manfaat: Memilih bagian-bagian tertentu dari elemen, seperti ::before untuk menambahkan konten sebelum elemen atau ::first-letter untuk menggaya huruf pertama dalam elemen.

Kapan digunakan: Digunakan untuk menggaya bagian-bagian tertentu dari elemen.


2. Jelaskan HTML5 Tag yang kamu ketahui?

<header>: Digunakan untuk mengelompokkan elemen-elemen header di dalamnya, seperti judul, logo, dan navigasi.

<nav>: Digunakan untuk mengelompokkan elemen-elemen navigasi, seperti menu utama, menu samping, atau tautan navigasi lainnya.

<main>: Menandakan bagian utama dari halaman web yang berisi konten utama. Ini membantu dalam aksesibilitas dan SEO.

<article>: Digunakan untuk mengelompokkan konten independen yang dapat berdiri sendiri, seperti postingan blog, artikel berita, atau komentar.

<section>: Digunakan untuk mengelompokkan konten terkait dalam sebuah bagian dari halaman web. Ini membantu dalam strukturisasi dan semantik halaman.

<aside>: Digunakan untuk mengelompokkan konten yang tidak terkait secara langsung dengan konten utama, seperti iklan, sidebar, atau elemen-elemen terkait lainnya.

<time>: Digunakan untuk mengelompokkan informasi waktu, seperti tanggal atau jam. Ini dapat membantu dalam penguraian dan tampilan waktu dengan benar.

<mark>: Digunakan untuk menyorot atau menandai teks dalam sebuah konten untuk menarik perhatian pengguna.

<details> dan <summary>: <details> digunakan untuk mengelompokkan konten yang dapat diperluas atau dikurangi, sementara <summary> digunakan untuk memberikan judul atau label untuk konten yang dapat dikembangkan atau dilipat.

<section>: Menandakan sebagian besar konten yang berdiri sendiri atau bagian terpisah dalam halaman web.

<footer>: Digunakan untuk mengelompokkan elemen-elemen penutup di dalamnya, seperti informasi kontak, tautan ke halaman lain, atau hak cipta.

<canvas>: Digunakan untuk menggambar grafis atau animasi menggunakan JavaScript. Ini sering digunakan untuk pembuatan permainan dan visualisasi data interaktif.

<video> dan <audio>: Digunakan untuk menanamkan video atau audio di halaman web. Ini memungkinkan konten multimedia yang lebih kaya.

<input type="email">, <input type="url">, <input type="date">, dan lain-lain: Input types ini memberikan validasi dan kontrol khusus untuk jenis data tertentu dalam formulir.

<datalist>: Digunakan dengan input fields untuk menyediakan daftar pilihan yang dapat dipilih oleh pengguna.

<progress>: Digunakan untuk menampilkan kemajuan suatu tugas, seperti mengunggah berkas atau proses pemrosesan.

3. Jelaskan perbedaan antara margin dan padding.

Margin adalah jarak di luar elemen dari semua sisi dan mempengaruhi jarak antara elemen ini dengan elemen-elemen lain di sekitarnya, seperti seberapa jauh elemen ini dari elemen-elemen lain.

Padding, di sisi lain, adalah jarak di dalam elemen antara konten elemen dan batas elemen itu sendiri, seperti seberapa jauh teks atau gambar dari tepi elemen itu.

Dengan kata lain, margin mengontrol seberapa jauh elemen dari elemen-elemen lain, sementara padding mengatur seberapa jauh kontennya dari tepi elemen itu sendiri.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya? 

Bootstrap adalah sebuah framework CSS yang sudah memiliki desain dan komponen siap pakai, sehingga Anda cukup menggunakan kelas-kelas yang telah ditentukan untuk mengatur tampilan halaman web Anda dengan cepat. Bootstrap lebih cocok digunakan jika Anda ingin membuat halaman dengan tampilan yang konsisten dan cepat, tetapi mungkin memerlukan penyesuaian lebih lanjut untuk tampilan yang sangat spesifik.

Tailwind CSS adalah sebuah framework CSS yang memberikan banyak kelas kecil yang dapat Anda tambahkan ke elemen HTML Anda untuk mengatur tampilan dan tata letak. Ini memberi Anda lebih banyak kendali, tetapi juga memerlukan lebih banyak penulisan kode. Tailwind cocok jika Anda ingin lebih banyak kreativitas dalam mendesain tampilan halaman web Anda atau jika Anda ingin menghindari desain yang terlalu seragam.

Kapan sebaiknya menggunakan Bootstrap atau Tailwind:

Bootstrap: Gunakan Bootstrap jika ingin membuat halaman web dengan cepat, tanpa banyak pekerjaan desain tambahan, dan jika ingin tampilan yang konsisten. Ini juga baik untuk proyek besar dengan banyak pengembang, karena aturan yang jelas dapat membantu menghindari kebingungan.

Tailwind CSS: Gunakan Tailwind jika ingin lebih banyak kendali dalam desain tampilan, atau jika Anda bekerja pada proyek dengan desain yang sangat spesifik. Ini cocok jika ingin berkreasi dalam desain 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


hal pertama yang saya lakukan yaitu mengambil bootstrap dengan menambahkan link css bootsrap beserta js nya di base.html, setelah melakukan itu saya mulai mengedit html pada login, register dan add product, di 3 html itu saya melakukan hal yang hampir sama persis, yaitu menambahkan container, menambahkan card mt5 menambahkan button dan mengubah warna menjadi biru di sebagian tombol. setelah itu saya baru mulai mengedit html pada bagian main dengan mengubah warna tombol dan letaknya, kemudian melakukan style pada tabelnya 


