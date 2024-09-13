Tugas 1
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

Tugas 2
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena data delivery digunakan sebagai fasilitator dalam menstransfer data dari satu tempat ke tempat lainnya. Data delivery juga digunakan untuk memastikan data yang dikirimkan aman dan tidak terjadi kebocoran data.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik dibandingkan XML karena JSON lebih mudah dibaca dan lebih ringan. JSON juga lebih populer dibandingkan XML karena JSON lebih mudah diakses dan diolah oleh manusia dan mesin.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django digunakan untuk memvalidasi data yang diinputkan oleh pengguna. Kita membutuhkan method tersebut untuk memastikan data yang diinputkan oleh pengguna valid dan sesuai dengan aturan yang telah ditentukan.

4.Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan csrf_token saat membuat form di Django untuk mencegah serangan CSRF. Jika kita tidak menambahkan csrf_token pada form Django, maka penyerang dapat melakukan serangan CSRF dengan mengirimkan request palsu ke server. Hal tersebut dapat dimanfaatkan oleh penyerang untuk mencuri data pengguna. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- yang pertama saya membuat input form\
- selanjutnya saya mengkoordinasikan dengan mengimplementasikan skeleton dan uuid 
- kemudian saya mengembalikan data dalam bentuk XML dan JSON 
- langkah selanjutnya saya cek menggunakan data viewer dengan postman
- lalu platform harusnya sudah bisa dijalankan dengan baik dan tinggal di push ke github dan pws
