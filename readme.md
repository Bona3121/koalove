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
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah form bawaan django yang menghandle sejenis pengisian data form oleh user baru seperti username dan password. 
Kelebihan:
a. Terdapat fitur validasi password otomatis
b. Django telah mengimplementasikan enkripsi password secara otomatis menggunakan hashing, sehingga data sensitif (seperti password) tidak disimpan dalam bentuk teks biasa.
c. Integrasi dengan Sistem django sangat mudah dilakukan dengan sistem login dan logoutnya 

Kekurangan:
a. Kustomisasi tampilan yang terbatas bahkan form defaultnya pun terbayas pada tiga field (username, password1, password2), jadi jika ingin menambahkan informasi lain seperti alamat email atau profil lebih mendalam, developer harus melakukan penyesuaian tambahan.
b. Tidak ada email konfirmasi yang dikirimkan apabila berhasil maupun gagal login 

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses verifikasi identitas pengguna dengan melakukan login yang menggunakan kredential. Otorisasi adalah proses yang menentukan apakah pengguna terautentikasi untuk melakukan suatu tindakan tertentu. Kedua tindakan ini penting dilakukan untuk menghindari adanya penyalagunaan akses pada suatu akun. 

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk 
mengelola data sesi pengguna?
Cookies adalah suatu file yang disimpan sementara di perangkat pengguna atau lebih tepatnya pada browser yang dapat diakses oleh server saat pengguna mengunjungi kembali situs web. Cookies memungkinkan server untuk "mengingat" pengguna antara satu kunjungan dengan kunjungan lainnya. Cara kerjanya, django akan membuat sesi pada saat login dan menyimpan sesi login tersebut, jika di lain waktu pengguna ingin mengkases kembali maka django akan mengambil data informasi sesi yang lalu. Namun ketika pengguna melakukan logout pada server maka data yang ada pada cookies juga kan terhapus.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies ini tidak sepenuhnya aman karena tetap masih ada beberapa resiko seperti pencurian data cookies, serangan scripting, dan manipulasi cookies yang rentan akan kebocoran data yang ada pada cookies ini. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Pertama-tama saya membuat form registrasi dengan membuat file html kemudian mengatur di urls.py dan views.py nya begitu pula dengan form login dan logout,
b. setelah semuanya selesai,  saya mencoba keberhasilan membuat 3 akun user yang berisi data dummy sebagai akun uji coba 
c. menhubungkan product yang telah saya buat sebelumnya dengan setiap usernya dengan konfigurasi pada models dan view kemudian melakukan migrations 
d. menkonfigurasi cookies last login pada web saya 
