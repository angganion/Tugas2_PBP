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
Apa perbedaan antara form POST dan form GET dalam Django?Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

hal pertama yang saya lakukan saat mengerjakan tugas ini adalah membuat semua fungsi yang dibutuhkan yaitu view berdasarkan html, xml, json, xml by id, json by id. untuk html saya membuat sebuah file html baru bernama items.html yang isinya hanya daftar dari item yang ada, untuk xml dan json saya memakai serialize dan untuk by id saya memfilter item by id. setelah itu saya menambahkan semua urls ke dalam urls main. setelah itu saya mengerjakn html main untuk dapat mendisplay semua barang dengan forloop. setelah itu saya mengerjakn bagian bonus dengan memakai kondisi di html yang jika item ada maka akan di render banyak barang adalah item|legths dan jika item tidak ada akan di render tidak ada item di aplikasi

![Screenshot 2023-09-17 204610](https://github.com/angganion/Tugas2_PBP/assets/120027733/6db4ee12-971d-4727-9f41-4b5a31ab9e7a)
![Screenshot 2023-09-17 203953](https://github.com/angganion/Tugas2_PBP/assets/120027733/4ed0c94b-588f-4ba9-99de-b57ed1110eb1)
![Screenshot 2023-09-17 204009](https://github.com/angganion/Tugas2_PBP/assets/120027733/d899c57b-3853-466e-ad85-4b38b4b6177f)
![Screenshot 2023-09-17 204026](https://github.com/angganion/Tugas2_PBP/assets/120027733/0d634ca9-c350-49f6-aad1-5f9e21ae6510)
![Screenshot 2023-09-17 204039](https://github.com/angganion/Tugas2_PBP/assets/120027733/4eafddf0-02de-4231-b9cd-1fa14e2edc69)




