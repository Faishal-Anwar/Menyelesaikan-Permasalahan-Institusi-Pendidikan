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

## Sistem Machine Learning

Untuk membangun sistem prediksi mahasiswa dropout di Jaya Jaya Institute, dilakukan eksperimen dengan beberapa algoritma machine learning. Tujuannya adalah memilih model dengan performa terbaik, khususnya dalam hal recall — agar mampu mendeteksi sebanyak mungkin mahasiswa yang berisiko dropout.

### Langkah-Langkah Pemodelan

1. **Pra-pemrosesan Data**
   - Penanganan missing value
   - Encoding fitur kategorikal
   - Standardisasi fitur numerik

2. **Penerapan PCA (Principal Component Analysis)**
   - Digunakan untuk mereduksi dimensi dan meningkatkan efisiensi pemodelan.

3. **Pelatihan Model**
   - Algoritma yang digunakan:
     - `Logistic Regression`
     - `Decision Tree Classifier`
     - `K-Nearest Neighbors (KNN)`

4. **Evaluasi**
   - Metrik utama: **Recall**
   - Penggunaan K-Fold Cross Validation
   - Perbandingan antara performa pada data pelatihan dan data pengujian

### Hasil Eksperimen Model

| Model                  | Train - Recall Mean | Train - Recall Std | Train - Recall All                                | Test - Recall | Difference   |
|------------------------|---------------------|---------------------|---------------------------------------------------|---------------|--------------|
| Logistic Regression     | 0.6641              | 0.0445              | [0.674, 0.6608, 0.6535, 0.5965, 0.7357]            | **0.8220**     | **-0.1579**   |
| Decision Tree Classifier| 0.6553              | 0.0209              | [0.6696, 0.6608, 0.6623, 0.614, 0.6696]            | 0.6644        | -0.0091      |
| K-Nearest Neighbors     | 0.4424              | 0.0294              | [0.4317, 0.4185, 0.4825, 0.4079, 0.4714]           | 0.7112        | -0.2688      |

> **Catatan:** Nilai *difference* dihitung dari selisih antara *mean recall* pada data latih dan recall pada data uji. Semakin kecil selisihnya, semakin stabil model.


### Model Terbaik: Logistic Regression

Model Logistic Regression dipilih sebagai model final karena:
- Memiliki nilai **recall tertinggi di data uji (0.8220)**
- Konsisten selama proses pelatihan
- Lebih sederhana dan mudah diinterpretasikan
- Cocok digunakan dalam sistem deteksi dini dropout

---

### Deployment dengan streamlit
Langkah-langkah menggunakan sistem machine learning berbasis XGBoost adalah sebagai berikut.
- Membuka link: https://m7e6p7ufh6ul4wt8sepkbe.streamlit.app/
- Mengisi data yang dibutuhkan. Perlu diperhatikan bahwa pengguna harus menekan enter agar dapat menyimpan data numerik.
- Hasil prediksi akan tampil di bagian bawah.
![Cuplikan layar 2025-05-18 143048](https://github.com/user-attachments/assets/a133a454-b1b6-4e60-96a1-ef685840e406)



## Kesimpulan
Berdasarkan analisis dan pemodelan yang dilakukan, ditemukan beberapa insight penting:
- Mahasiswa yang tidak membayar tepat waktu, tidak menerima beasiswa, dan memiliki tunggakan cenderung memiliki kemungkinan lebih tinggi untuk dropout.
- Jurusan tertentu seperti Veterinary Nursing dan Social Service memiliki dropout rate yang signifikan.
- Mahasiswa laki-laki menunjukkan angka dropout yang lebih tinggi dari perempuan, yang bisa menjadi perhatian lebih lanjut dari pihak institusi.
  
## Rekomendasi Action Items
Berikut beberapa rekomendasi yang dapat diambil oleh Jaya Jaya Institut:
- Targeted Counseling: Fokuskan pendampingan akademik pada mahasiswa dengan kombinasi faktor risiko (utang, tanpa beasiswa, tidak tepat waktu membayar).
- Pemberian Beasiswa Adaptif: Perluas cakupan beasiswa untuk mahasiswa dari jurusan atau latar belakang rentan.
- Monitoring Berkala via Dashboard: Gunakan dashboard secara rutin untuk melihat tren dropout dan intervensi dini.
- Evaluasi Jurusan Berisiko: Audit internal terhadap jurusan dengan tingkat dropout tinggi untuk mengevaluasi kurikulum, beban studi, atau dukungan dosen.
- Peningkatan Sistem Informasi Akademik: Integrasi sistem prediksi dropout ke dalam sistem akademik yang sudah ada agar dapat langsung memberikan alert.

## Referensi
- 


