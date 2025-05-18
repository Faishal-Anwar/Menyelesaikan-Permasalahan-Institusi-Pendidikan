# Proyek Akhir: Menyelesaikan-Permasalahan-Institusi-Pendidikan Jaya Jaya Institute
# Id : anwarfaishal86

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik.

## Permasalahan Bisnis
Berikut adalah permasalahan bisnis yang dihadapi oleh Jaya jaya institute

- Jumlah mahasiswa dropout yang tinggi (1.421 dari 4.424 mahasiswa).
- Belum adanya sistem prediksi untuk deteksi dini mahasiswa yang berpotensi dropout.
- Kebutuhan akan dashboard visual untuk membantu monitoring performa dan pengambilan keputusan berbasis data.

## Cakupan Proyek
- Melakukan analisis deskriptif terhadap data mahasiswa berdasarkan status akademik, pembayaran, beasiswa, dan jurusan.
- Membangun model machine learning untuk memprediksi kemungkinan mahasiswa melakukan dropout.
- Mengembangkan dashboard visual interaktif menggunakan Streamlit.
- Memberikan rekomendasi strategis untuk menurunkan angka dropout.

## Persiapan

### Sumber Data
Dataset diambil dari:  
[students' performance - GitHub](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

### Setup Environment (Local Deployment)

Ikuti langkah-langkah berikut untuk menjalankan aplikasi secara lokal:

#### 1. Clone Repository
```bash
https://github.com/Matahari-Masalalu/Menyelesaikan-Permasalahan-Institusi-Pendidikan.git
cd /Menyelesaikan-Permasalahan-Institusi-Pendidikan
```

#### 2. Buat Virtual Environment
```bash
virtualenv venv
```

#### 3. Aktifkan Virtual Environment
Windows:
```bash
venv\Scripts\activate
```
macOS/Linux:
```bash
source venv/bin/activate
```

#### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 5. Jalankan Aplikasi Streamlit
```bash
streamlit run streamlit_app.py
```

## Dashboard Analitik - Tableau Public
untuk link dashboard bisa diakses melalui

link dashboard : [link dashboard](https://public.tableau.com/views/Book3_17472601956340/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

![Cuplikan layar 2025-05-18 124806](https://github.com/user-attachments/assets/0cc381a2-6334-4ac2-82a8-75eb86a015ad)
![Cuplikan layar 2025-05-18 124816](https://github.com/user-attachments/assets/61ce5e0a-7d46-4d1b-a02e-1d9b7371ac61)

### Komponen Dashboard
- Rata-rata Nilai Masuk (Average of Admission Grade) : Seluruh mahasiswa memiliki rata-rata nilai masuk sebesar 126,7.

- Rata-rata Usia Saat Diterima (Average Age at Enrollment) : Mahasiswa diterima pada usia rata-rata sekitar 23,27 tahun.

- Distribusi Jenis Kelamin (Gender) : Dari total 4.424 mahasiswa, sebanyak 64,83% adalah perempuan (sekitar 2.868 orang), dan 35,17% adalah laki-laki (sekitar 1.556 orang).

- Penerima Beasiswa (Scholarship Holder) : Sebanyak 24,84% mahasiswa menerima beasiswa (sekitar 1.099 orang), dan 75,16% tidak menerima beasiswa (sekitar 3.325 orang).

- Status Internasional (International) : Mahasiswa internasional berjumlah sekitar 110 orang (2,49%), sedangkan mahasiswa domestik sebanyak 4.314 orang (97,51%).

- Status Pernikahan (Marital Status) : Mayoritas mahasiswa berstatus lajang (3.919 orang), disusul menikah (379), cerai (91), memiliki pasangan tidak resmi (25), pisah resmi (6), dan duda/janda (4).

- Distribusi Program Studi (Course) : Program studi dengan jumlah mahasiswa terbanyak adalah Keperawatan (766), disusul Manajemen (380), Pelayanan Sosial (355), Kedokteran Hewan (337), dan Jurnalistik (331).

- Status Mahasiswa (Status) : Sebanyak 3.003 mahasiswa (67,88%) tercatat tidak dropout, sementara 1.421 mahasiswa (32,12%) mengalami dropout.

- Distribusi Status Mahasiswa Berdasarkan Program Studi (Distribution of Student Status By Course) : Program studi dengan tingkat dropout tinggi meliputi Manajemen, Jurnalistik, Pelayanan Sosial, dan Kedokteran Hewan. Program studi Keperawatan menunjukkan tingkat retensi tertinggi.

- Pembayaran Uang Kuliah dan Dropout (Count of Student by Tuition Payment Status and Dropout Status) : Mahasiswa yang membayar tepat waktu mayoritas tidak dropout. Sebaliknya, mereka yang menunggak cenderung lebih besar kemungkinannya mengalami dropout.

- Pengaruh Beasiswa terhadap Dropout (Scholarshp Distribution by Dropout Status) : Mahasiswa tanpa beasiswa memiliki tingkat dropout yang lebih tinggi. Penerima beasiswa cenderung menyelesaikan studi.

- Pengaruh Hutang terhadap Dropout (Impact of Debt Status on Student Dropout) : Mahasiswa tanpa hutang memiliki tingkat kelulusan tinggi. Sebaliknya, mahasiswa dengan hutang lebih rentan mengalami dropout.

