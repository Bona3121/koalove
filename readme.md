Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Pertama-tama saya membuat lokal repositori yang bernama "koalove"
b. Kemudian saya install djanggo dan beberapa keperluan lainnya
c. Setelah menginstall django, saya mulai menginstall dan mengaktifkan virtual environment 
d. Langkah selanjutnya saya menyiapkan dependencies dan menyiapkan port server
e. setelah semuanya selesai menambahkan berkas .gitignore dan diupload ke repository github.
f. Pada step ini, saya mulai membuat aplikasi main di proyek "koalove" saya dan membuat template dasar yang berisi nama aplikasi, nama dan kelas saya di file html
g. setelah membuat template, saya membuat model dari django dan mengingtegrasikan MVT dan memodifikasi template
h. langkah selanjutnya mengkonfigurasi routing url proyek kemudian membuat unit test agar menghindari error minor
i. setelah menjalankan unit test saya mulai mengpush ke pws 
j. langkah terakhir yang sedang saya lakukan saat ini adalah mengerjakan task README.md

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Link : https://www.canva.com/design/DAGPzPr0RrA/BBssep0tMzI8kTqEQIWeqQ/watch?utm_content=DAGPzPr0RrA&utm_campaign=designshare&utm_medium=link&utm_source=editor

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
a. git membantu memudahkan programmer dalam berkolaborasi dengan programmer lainnya dalam membuat perubahan kode
b. pada git terdapat riwayat perubahan yang dapat di cek kembali dan memudahkan pengembang dalam melacak apa saja yang telah dimodifikasi
c. git memudahkan pengembang dalam membuat cabang sebelum dijadikan kode utama dan dapat dijadikan sebagai backup apabila repositori lokal mengalami kesalahan atau hilang.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django merupakan framework berbasis bahasa Python yang pernah dipelajari juga pada mata kuliah DDP 1. Framework ini juga sudah memiliki berbagai template yang dapat mempermudah pemula seperti kami dalam membuat perangkat lunak. Selain itu, django dipilih karena django sangat cocok digunakan sebagai media penerapan server side yang akan sangat berguna bagi kami nantinya ketika mengaplikasikan flutter di perangkat android yang akan kami pelajari kedepannya.

5. Mengapa model pada Django disebut sebagai ORM?
Perlu kita ketahui bahwa ORM atau sering disebut dengan Object-Relational Mapping merupakan kerangka kerja yang digunakan oleh Django dalam struktur nya. Model pada django ini diberi nama ORM karena teknik ini bekerja dengan cara berinteraksi dengan database menggunakan bahasa pemrograman dan objek, bukan dengan perintah SQL (database) langsung.

Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena data delivery digunakan sebagai fasilitator dalam menstransfer data dari satu tempat ke tempat lainnya. Data delivery juga digunakan untuk memastikan data yang dikirimkan aman dan tidak terjadi kebocoran data.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik dibandingkan XML karena JSON lebih mudah dibaca dan lebih ringan. JSON juga lebih populer dibandingkan XML karena JSON lebih mudah diakses dan diolah oleh manusia dan mesin.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django digunakan untuk memvalidasi data yang diinputkan oleh pengguna. Kita membutuhkan method tersebut untuk memastikan data yang diinputkan oleh pengguna valid dan sesuai dengan aturan yang telah ditentukan.

4.Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan csrf_token saat membuat form di Django untuk mencegah serangan CSRF. Jika kita tidak menambahkan csrf_token pada form Django, maka penyerang dapat melakukan serangan CSRF dengan mengirimkan request palsu ke server. Hal tersebut dapat dimanfaatkan oleh penyerang untuk mencuri data pengguna. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- yang pertama saya membuat input form
- selanjutnya saya mengkoordinasikan dengan mengimplementasikan skeleton dan uuid 
- kemudian saya mengembalikan data dalam bentuk XML dan JSON 
- langkah selanjutnya saya cek menggunakan data viewer dengan postman
- lalu platform harusnya sudah bisa dijalankan dengan baik dan tinggal di push ke github dan pws

Link ss : https://drive.google.com/drive/folders/1s3J3Cyxsyq_zVZvryOtuh3a-1Xq8leTC?usp=sharing

Tugas 4 

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
Dalam Django, HttpResponseRedirect() digunakan untuk mengarahkan pengguna ke URL yang ditentukan secara manual, sementara redirect() adalah fungsi yang lebih fleksibel karena dapat mengarahkan ke URL absolut, nama view, atau objek model yang memiliki metode get.

2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model Product dengan User dalam Django biasanya dilakukan dengan menggunakan ForeignKey untuk menunjukkan bahwa setiap produk dimiliki oleh satu pengguna tetapi satu pengguna dapat memiliki banyak produk, atau menggunakan ManyToManyField jika produk dapat dimiliki oleh banyak pengguna dan sebaliknya, serta OneToOneField jika setiap produk hanya dapat dimiliki oleh satu pengguna dan setiap pengguna hanya dapat memiliki satu produk.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Autentikasi adalah proses verifikasi identitas pengguna dengan melakukan login yang menggunakan kredential. Otorisasi adalah proses yang menentukan apakah pengguna terautentikasi untuk melakukan suatu tindakan tertentu. Kedua tindakan ini penting dilakukan untuk menghindari adanya penyalagunaan akses pada suatu akun. 

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menyimpan id dari session yang pernah mereka lakukan saat pertama kali login. Kegunaan lain cookies diantaranya menyimpan session,menyimpan preferensi pengguna, pelacakan pengunjung dan analisis penggunaan situs web dan dalam e-commerce dapat membantu menyimpan barang di keranjang belanja.
Tidak semua cookies aman digunakan karena rentan terhadap XSS dan CSRF, contoh nya data sensitif seperti jumlah saldo, pin dll. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Pertama-tama saya membuat form registrasi dengan membuat file html kemudian mengatur di urls.py dan views.py nya begitu pula dengan form login dan logout,
b. setelah semuanya selesai,  saya mencoba keberhasilan membuat 3 akun user yang berisi data dummy sebagai akun uji coba 
c. menhubungkan product yang telah saya buat sebelumnya dengan setiap usernya dengan konfigurasi pada models dan view kemudian melakukan migrations 
d. menkonfigurasi cookies last login pada web saya 

Tugas 5 
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

low to high priority
a. Element
Ini memiliki prioritas paling rendah. Misalnya, selector div, p, h1, dll. berlaku untuk semua elemen dari jenis tersebut.

b. Class selectors
Class selectors berlaku untuk elemen yang memiliki atribut class tertentu. Dapat digunakan untuk elemen yang berbeda.

c. ID Selectors
Selector ini memiliki prioritas yang lebih tinggi dari class. ID harus unik untuk setiap halaman, sehingga penggunaannya lebih spesifik.

d. Inline styles
Gaya yang diterapkan langsung pada elemen menggunakan atribut style. Ini memiliki prioritas yang lebih tinggi dari selektor CSS biasa.

e. !important
Menggunakan !important akan mengesampingkan semua aturan lain, termasuk inline styles. Namun, jika ada beberapa aturan yang sama-sama menggunakan !important, maka specificty akan digunakan untuk menentukan aturan mana yang diterapkan.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design adalah pendekatan dalam pengembangan aplikasi web yang memungkinkan tampilan web beradaptasi secara otomatis dengan berbagai ukuran layar dan perangkat. Contoh aplikasi yang belum menerapkan responsive design yaitu https://www.bola.net/ dan aplikasi yang sudah menerapkan responsove design contohnya google.com maupun aplikasi lainnya.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah spasi yang ada di sekitar batas luar suatu elemen, border merupakan garis batas yang bisa digunakan di setiap elemen dan padding adalah ruang kosong atau space antar konten pada website. Cara mengimplementasikannya adalah buat suatu style boelh di dalam html maupun di luar, pada contoh ini di dalam html yang kemudian pada class box saya set margin , padding serta border dengan satuan ukuran pixel. 
<style>
    .box {
        margin: 20px;  /* Jarak luar elemen */
        padding: 15px; /* Jarak dalam elemen */
        border: 2px solid black; /* Garis tepi elemen */
    }
</style>

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexible Box Layout merupakan tata letak css yang digunakan untuk mengatur tata letak komponen dalam satu arah (horizontal atau vertikal) secara dinamis sedangan grid layout merupakan sistem tata letak komponen yang mengatur 2 dimensi dalam baris dan kolom. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
a. Pertama tama saya mempelajari lebih dahulu tentang html dan css dari berbagai sumber salah satunya tutorial
b. Saya mulai buat fitur login dan register serta fitur tambah produknya
c. setelah itu setiap produk saya jadikan card agar lebih bagus dan menarik
d. kemudian saya perindah dengan menambahkan navigation bar yang responsif