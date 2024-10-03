## <summary><strong>Tugas 2 </strong></summary></br>
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). </br>
a. Pertama-tama saya membuat lokal repositori yang bernama "koalove" </br>
b. Kemudian saya install djanggo dan beberapa keperluan lainnya </br>
c. Setelah menginstall django, saya mulai menginstall dan mengaktifkan virtual environment  </br>
d. Langkah selanjutnya saya menyiapkan dependencies dan menyiapkan port server </br>
e. setelah semuanya selesai menambahkan berkas .gitignore dan diupload ke repository github. </br>
f. Pada step ini, saya mulai membuat aplikasi main di proyek "koalove" saya dan membuat template dasar yang berisi nama aplikasi, nama dan kelas saya di file html </br>
g. setelah membuat template, saya membuat model dari django dan mengingtegrasikan MVT dan memodifikasi template </br>
h. langkah selanjutnya mengkonfigurasi routing url proyek kemudian membuat unit test agar menghindari error minor </br>
i. setelah menjalankan unit test saya mulai mengpush ke pws </br>
j. langkah terakhir yang sedang saya lakukan saat ini adalah mengerjakan task README.md </br>

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.</br>
Link : https://www.canva.com/design/DAGPzPr0RrA/BBssep0tMzI8kTqEQIWeqQ/watch?utm_content=DAGPzPr0RrA&utm_campaign=designshare&utm_medium=link&utm_source=editor </br>

<details>
  <summary><strong>View More</strong></summary>

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!</br>
a. git membantu memudahkan programmer dalam berkolaborasi dengan programmer lainnya dalam membuat perubahan kode</br>
b. pada git terdapat riwayat perubahan yang dapat di cek kembali dan memudahkan pengembang dalam melacak apa saja yang telah dimodifikasi</br>
c. git memudahkan pengembang dalam membuat cabang sebelum dijadikan kode utama dan dapat dijadikan sebagai backup apabila repositori lokal mengalami kesalahan atau hilang.</br>

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?</br>
Django merupakan framework berbasis bahasa Python yang pernah dipelajari juga pada mata kuliah DDP 1. Framework ini juga sudah memiliki berbagai template yang dapat mempermudah pemula seperti kami dalam membuat perangkat lunak. Selain itu, django dipilih karena django sangat cocok digunakan sebagai media penerapan server side yang akan sangat berguna bagi kami nantinya ketika mengaplikasikan flutter di perangkat android yang akan kami pelajari kedepannya.</br>

5. Mengapa model pada Django disebut sebagai ORM?</br>
Perlu kita ketahui bahwa ORM atau sering disebut dengan Object-Relational Mapping merupakan kerangka kerja yang digunakan oleh Django dalam struktur nya. Model pada django ini diberi nama ORM karena teknik ini bekerja dengan cara berinteraksi dengan database menggunakan bahasa pemrograman dan objek, bukan dengan perintah SQL (database) langsung.

</details>
</br>

## <summary><strong>Tugas 3</strong></summary></br>
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?</br>
Karena data delivery digunakan sebagai fasilitator dalam menstransfer data dari satu tempat ke tempat lainnya. Data delivery juga digunakan untuk memastikan data yang dikirimkan aman dan tidak terjadi kebocoran data.</br>

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?</br>
Menurut saya JSON lebih baik dibandingkan XML karena JSON lebih mudah dibaca dan lebih ringan. JSON juga lebih populer dibandingkan XML karena JSON lebih mudah diakses dan diolah oleh manusia dan mesin.</br>
<details>
  <summary><strong>View More</strong></summary>

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?</br>
Method is_valid() pada form Django digunakan untuk memvalidasi data yang diinputkan oleh pengguna. Kita membutuhkan method tersebut untuk memastikan data yang diinputkan oleh pengguna valid dan sesuai dengan aturan yang telah ditentukan.</br>

4.Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? </br>
Kita membutuhkan csrf_token saat membuat form di Django untuk mencegah serangan CSRF. Jika kita tidak menambahkan csrf_token pada form Django, maka penyerang dapat melakukan serangan CSRF dengan mengirimkan request palsu ke server. Hal tersebut dapat dimanfaatkan oleh penyerang untuk mencuri data pengguna. </br>

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). </br>
- yang pertama saya membuat input form </br>
- selanjutnya saya mengkoordinasikan dengan mengimplementasikan skeleton dan uuid </br>
- kemudian saya mengembalikan data dalam bentuk XML dan JSON </br>
- langkah selanjutnya saya cek menggunakan data viewer dengan postman </br>
- lalu platform harusnya sudah bisa dijalankan dengan baik dan tinggal di push ke github dan pws </br>

Link ss : https://drive.google.com/drive/folders/1s3J3Cyxsyq_zVZvryOtuh3a-1Xq8leTC?usp=sharing
</details>
</br>

## <summary><strong>Tugas 4 </strong></summary></br>

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()? </br>
Dalam Django, HttpResponseRedirect() digunakan untuk mengarahkan pengguna ke URL yang ditentukan secara manual, sementara redirect() adalah fungsi yang lebih fleksibel karena dapat mengarahkan ke URL absolut, nama view, atau objek model yang memiliki metode get.</br>

2. Jelaskan cara kerja penghubungan model Product dengan User! </br>
Penghubungan model Product dengan User dalam Django biasanya dilakukan dengan menggunakan ForeignKey untuk menunjukkan bahwa setiap produk dimiliki oleh satu pengguna tetapi satu pengguna dapat memiliki banyak produk, atau menggunakan ManyToManyField jika produk dapat dimiliki oleh banyak pengguna dan sebaliknya, serta OneToOneField jika setiap produk hanya dapat dimiliki oleh satu pengguna dan setiap pengguna hanya dapat memiliki satu produk. </br>

<details>
  <summary><strong>View More</strong></summary>

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut. </br>
Autentikasi adalah proses verifikasi identitas pengguna dengan melakukan login yang menggunakan kredential. Otorisasi adalah proses yang menentukan apakah pengguna terautentikasi untuk melakukan suatu tindakan tertentu. Kedua tindakan ini penting dilakukan untuk menghindari adanya penyalagunaan akses pada suatu akun.  </br>

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan? </br>
Django mengingat pengguna yang telah login dengan menyimpan id dari session yang pernah mereka lakukan saat pertama kali login. Kegunaan lain cookies diantaranya menyimpan session,menyimpan preferensi pengguna, pelacakan pengunjung dan analisis penggunaan situs web dan dalam e-commerce dapat membantu menyimpan barang di keranjang belanja.
Tidak semua cookies aman digunakan karena rentan terhadap XSS dan CSRF, contoh nya data sensitif seperti jumlah saldo, pin dll. </br>

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). </br>
a. Pertama-tama saya membuat form registrasi dengan membuat file html kemudian mengatur di urls.py dan views.py nya begitu pula dengan form login dan logout. </br>
b. setelah semuanya selesai,  saya mencoba keberhasilan membuat 3 akun user yang berisi data dummy sebagai akun uji coba. </br>
c. menhubungkan product yang telah saya buat sebelumnya dengan setiap usernya dengan konfigurasi pada models dan view kemudian melakukan migrations. </br>
d. menkonfigurasi cookies last login pada web saya. </br> 

</details>
</br>


## <summary><strong>Tugas 5 </strong></summary></br>
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut! </br>
</br>
low to high priority</br>
a. Element</br>
Ini memiliki prioritas paling rendah. Misalnya, selector div, p, h1, dll. berlaku untuk semua elemen dari jenis tersebut.</br>

b. Class selectors</br>
Class selectors berlaku untuk elemen yang memiliki atribut class tertentu. Dapat digunakan untuk elemen yang berbeda.</br>

c. ID Selectors</br>
Selector ini memiliki prioritas yang lebih tinggi dari class. ID harus unik untuk setiap halaman, sehingga penggunaannya lebih spesifik.</br>

d. Inline styles</br>
Gaya yang diterapkan langsung pada elemen menggunakan atribut style. Ini memiliki prioritas yang lebih tinggi dari selektor CSS biasa.</br>

e. !important</br>
Menggunakan !important akan mengesampingkan semua aturan lain, termasuk inline styles. Namun, jika ada beberapa aturan yang sama-sama menggunakan !important, maka specificty akan digunakan untuk menentukan aturan mana yang diterapkan.</br>

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!</br>
Responsive design adalah pendekatan dalam pengembangan aplikasi web yang memungkinkan tampilan web beradaptasi secara otomatis dengan berbagai ukuran layar dan perangkat. Contoh aplikasi yang belum menerapkan responsive design yaitu https://www.bola.net/ dan aplikasi yang sudah menerapkan responsove design contohnya google.com maupun aplikasi lainnya.</br>

<details>
  <summary><strong>View More</strong></summary>


3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!</br>
Margin adalah spasi yang ada di sekitar batas luar suatu elemen, border merupakan garis batas yang bisa digunakan di setiap elemen dan padding adalah ruang kosong atau space antar konten pada website. Cara mengimplementasikannya adalah buat suatu style boelh di dalam html maupun di luar, pada contoh ini di dalam html yang kemudian pada class box saya set margin , padding serta border dengan satuan ukuran pixel. </br>
<p>
<style>
    .box {
        margin: 20px;  /* Jarak luar elemen */
        padding: 15px; /* Jarak dalam elemen */
        border: 2px solid black; /* Garis tepi elemen */
    }
</style>
</p>
</br>
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!</br>
Flexible Box Layout merupakan tata letak css yang digunakan untuk mengatur tata letak komponen dalam satu arah (horizontal atau vertikal) secara dinamis sedangan grid layout merupakan sistem tata letak komponen yang mengatur 2 dimensi dalam baris dan kolom. </br>

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)! </br>
a. Pertama tama saya mempelajari lebih dahulu tentang html dan css dari berbagai sumber salah satunya tutorial</br>
b. Saya mulai buat fitur login dan register serta fitur tambah produknya. </br>
c. setelah itu setiap produk saya jadikan card agar lebih bagus dan menarik. </br>
d. kemudian saya perindah dengan menambahkan navigation bar yang responsif. </br>
</br>
Link Video Demo Program : https://youtu.be/Dgh3OW8nzCY

</details>
</br>


## <summary><strong>Tugas 6 :</strong></summary></br>
1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web! </br>
Javascript membantu membuat website hidup dengan berbagai implementasi mulai dari button hingga animasi yang unik. </br>

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await? </br>
Await membuat kita menunggu hasil dari promise yang dikembalikan sebelum melanjutkan eksekusi kode berikutnya, sehingga memastikan bahwa data yang diperlukan telah tersedia. Tanpa await, kode akan terus berjalan tanpa menunggu respons dari permintaan, yang dapat menyebabkan kesalahan ketika mencoba mengakses data yang belum ada. </br>

<details>
  <summary><strong>View More</strong></summary>

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST? </br>
Hal ini perlu dilakukan untuk mencegah terjadinya serangan CSRF (Cross-Site Request Forgery) yang dapat terjadi pada website. </br>

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja? </br>
Pembersihan data input pengguna sebaiknya dilakukan di backend meskipun sudah ada validasi di frontend karena frontend dapat dengan mudah dimanipulasi oleh pengguna. Pengguna dapat menonaktifkan JavaScript, mengubah kode, atau mengirim permintaan langsung ke server tanpa melalui antarmuka pengguna yang disediakan. </br>

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)! </br>
1. Yang saya lakukan adalah import routing yang diperlukan </br>
2. Mengubah dan mengapus beberapa bagian yang tidak diperlukan lagi di views.py </br>
3. Menambah script untuk get mood </br>

</details>
</br>
