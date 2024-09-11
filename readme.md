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