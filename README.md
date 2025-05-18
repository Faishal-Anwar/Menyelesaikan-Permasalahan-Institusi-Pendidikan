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

## Ringkasan Mahasiswa & Analisis Dropout
Dashboard ini menyajikan ringkasan komprehensif mengenai demografi mahasiswa, latar belakang akademik, serta analisis penyebab mahasiswa dropout berdasarkan data dari **4.424 mahasiswa**. Informasi mencakup distribusi jenis kelamin, status beasiswa, kewarganegaraan, status pernikahan, program studi, dan indikator utama terkait dropout.


### Demografi Mahasiswa

### Rata-rata Nilai Masuk (Average of Admission Grade)
- Rata-rata nilai masuk seluruh mahasiswa adalah **126,7**.

### Rata-rata Usia Saat Diterima (Average Age at Enrollment)
- Rata-rata usia mahasiswa saat diterima adalah sekitar **23,27 tahun**.

### Distribusi Jenis Kelamin (Gender) dari Total: 4.424 mahasiswa
- **Perempuan:** 64,83% → sekitar **2.868 mahasiswa**
- **Laki-laki:** 35,17% → sekitar **1.556 mahasiswa**

### Penerima Beasiswa (Scholarship Holder)
- **Ya (Penerima Beasiswa):** 24,84% → sekitar **1.099 mahasiswa**
- **Tidak:** 75,16% → sekitar **3.325 mahasiswa**

### Status Internasional (International)
- **Mahasiswa Internasional:** 2,49% → sekitar **110 mahasiswa**
- **Mahasiswa Domestik:** 97,51% → sekitar **4.314 mahasiswa**

### Status Pernikahan (Marital Status)
- **Lajang (Single):** 3.919 mahasiswa (Mayoritas)
- **Menikah:** 379 mahasiswa
- **Cerai:** 91 mahasiswa
- **Pasangan Hidup Tidak Resmi:** 25 mahasiswa
- **Pisah Resmi:** 6 mahasiswa
- **Duda/Janda:** 4 mahasiswa

### Distribusi Program Studi (Course)
- **Keperawatan (Nursing):** 766 mahasiswa
- **Manajemen:** 380 mahasiswa
- **Pelayanan Sosial (Social):** 355 mahasiswa
- **Kedokteran Hewan (Veterinary):** 337 mahasiswa
- **Jurnalistik (Journalism):** 331 mahasiswa

## Analisis Dropout

### Status Mahasiswa (Status)
- **Tidak Dropout:** 3.003 mahasiswa → **67,88%**
- **Dropout:** 1.421 mahasiswa → **32,12%**

### Distribusi Status Mahasiswa Berdasarkan Program Studi (Distribution of Student Status By Course)
- Program studi dengan **tingkat dropout tinggi** (batang oranye lebih dominan):
  - **Manajemen**
  - **Jurnalistik**
  - **Pelayanan Sosial**
  - **Kedokteran Hewan**
- Program studi dengan **tingkat kelulusan tinggi** (mayoritas bertahan):
  - **Keperawatan (Nursing)**

### Status Pembayaran Uang Kuliah dan Dropout (Count of Student by Tuition Payment Status and Dropout Status)

    | Pembayaran Uang Kuliah | Dropout | Tidak Dropout |
    |------------------------|---------|---------------|
    | Ya (Tepat Waktu)       | Tinggi  | Sangat Tinggi |
    | Tidak (Menunggak)      | Sedang  | Sangat Rendah |

- Mahasiswa **yang menunggak pembayaran** cenderung lebih besar kemungkinannya untuk dropout.
- Mahasiswa **yang membayar tepat waktu** mayoritas **tidak dropout**.

### Distribusi Beasiswa Berdasarkan Status Dropout (Scholarshp Distribution by Dropout Status)

    | Penerima Beasiswa | Dropout | Tidak Dropout |
    |-------------------|---------|---------------|
    | Ya                | Rendah  | Sedang        |
    | Tidak             | Tinggi  | Tinggi        |

- Mahasiswa **tanpa beasiswa** memiliki tingkat dropout yang lebih tinggi.
- Mahasiswa **dengan beasiswa** cenderung bertahan dalam studi.

### Dampak Status Hutang terhadap Dropout (Impact of Debt Status on Student Dropout)

    | Status Hutang | Dropout | Tidak Dropout |
    |---------------|---------|---------------|
    | Ya            | Sedang  | Rendah        |
    | Tidak         | Tinggi  | Sangat Tinggi |

- Mahasiswa **tanpa hutang** cenderung bertahan dan menyelesaikan studi.
- Mahasiswa **dengan hutang** memiliki kecenderungan dropout lebih tinggi.

- 
Komponen Dashboard
- Rata-rata Nilai Masuk (Average of Admission Grade) : Rata-rata nilai masuk seluruh siswa adalah 126,7.
- Rata-rata Usia Saat Diterima (Average Age at Enrollment) : Rata-rata usia siswa saat diterima adalah sekitar 23 tahun.
- Jenis Kelamin (Gender) dari total 4.424 siswa, distribusinya adalah:
  > Laki-laki: 35,17% → sekitar 1.556 siswa
  > Perempuan: 64,83% → sekitar 2.868 siswa
- Penerima Beasiswa (Scholarship Holder) Dari total 4.424 siswa, distribusinya adalah:
  > Penerima (Scholarship Holder(Yes)) : 24,84% → sekitar 1.099 siswa
  > Bukan Penerima (Scholarship Holder(No)) : 75,16% sekitar → 3.325 siswa
- Status Internasional (International), berdasarkan status kewarganegaraan:
  > Siswa Internasional (2,49%) → sekitar 110 siswa
  > Siswa Domestik (97,51%) → sekitar 4.314 siswa
- Status Pernikahan (Marital Status) : Mayoritas siswa berstatus lajang (Single) sebanyak 3.919 siswa.
- Program Studi (Course) : Program studi dengan jumlah siswa terbanyak adalah Keperawatan (Nursing) dengan total 766 siswa.
- Status : Status mahasiswa saat ini
  > Mahasiswa Tidak Dropout: 3.003 → 67,88%
  > Mahasiswa Dropout: 1.421 → 32,12%
- Distribusi Status siswa berdasarkann Program Studi (Distribution of Student Status By Course) : Program studi dengan dropout cukup tinggi (ditunjukkan dengan batang oranye dominan)
  > Manajemen, Jurnalistik, Sosial, Veteriner
  > Keperawatan (Nursing): Mayoritas tidak dropout (jumlah terbesar mahasiswa bertahan)
- Count of Student by Tu

