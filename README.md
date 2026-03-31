# Student Dropout Prediction System

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi tersebut telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat juga persentase mahasiswa yang tidak menyelesaikan pendidikannya alias *dropout*.

Jumlah *dropout* yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin mahasiswa yang berpotensi melakukan *dropout* sehingga mereka dapat diberi bimbingan khusus sedini mungkin.

## Permasalahan Bisnis
Pada institusi pendidikan ini terdapat 4000 lebih mahasiswa. Namun, terdapat fenomena yang merugikan institusi yaitu tingkat *dropout* yang cukup tinggi (sekitar 32.1%). Untuk mengatasi hal tersebut, diperlukan analisa mengenai faktor mengapa mahasiswa cenderung melakukan *dropout* dan bagaimana penanganan preventifnya agar *dropout rate* pada institusi dapat menurun.

## Cakupan Proyek
Cakupan atau *scope* dari proyek *Data Science* ini meliputi:
1. **Data Understanding & Exploratory Data Analysis (EDA):** Mengeksplorasi dataset *dropout* mahasiswa untuk menemukan anomali, tren, dan distribusi nilai target.
2. **Data Preprocessing:** Melakukan pembersihan data, penanganan *missing value* (jika ada), *encoding* variabel kategorikal, dan *feature scaling*.
3. **Modelling:** Melatih model *Machine Learning* bertipe klasifikasi (*Logistic Regression* dan *Random Forest Classifier*) untuk mempelajari pola *dropout* mahasiswa.
4. **Evaluation:** Mengukur performa model dengan metrik *Accuracy*, *Precision*, *Recall*, *F1-Score*, dan menganalisis visualisasi *Confusion Matrix* serta *Feature Importance*.

## Persiapan
**Sumber Data:**
Data yang digunakan adalah `data.csv` yang berisi rincian demografis, berbagai macam metrik akademik/pekerjaan, dan target variabel *Dropout*.
Link dataset: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

**Setup Environment:**
Untuk menjalankan proyek ini, Anda membutuhkan instalasi Python (>= 3.8). Berikut adalah langkah-langkah untuk menyiapkan *environment* dan menjalankan skrip prediksi:

1. **Membuat dan Mengaktifkan Virtual Environment (venv):**
   ```bash
   # Masuk ke direktori proyek
   cd "Menyelesaikan masalah institusi pendidikan"
   
   # Membuat virtual environment bernama 'env'
   python -m venv env
   
   # Mengaktifkan virtual environment (Windows)
   .\env\Scripts\activate
   
   # Mengaktifkan virtual environment (Linux/Mac)
   source env/bin/activate
   ```

2. **Menginstal Dependensi:**
   Setelah *virtual environment* aktif, instal seluruh library yang dibutuhkan menggunakan file `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

Selain itu, Anda juga dapat membuka file `notebook.ipynb` melalui *Jupyter Notebook* atau *VS Code* (dengan ekstensi Jupyter) untuk melihat alur proses mulai dari pembacaan data hingga evaluasi model.

## Business Dashboard

Menggunakan Metabase dengan kredensial:
- **Email:** root@mail.com
- **Password:** root123

**Dashboard: Student Dropout Analysis**

**Insight:**
- Terdapat *dropout rate* secara keseluruhan yang cukup tinggi, yaitu sebesar 32.14%.
- Setiap *course* (program studi) memiliki *dropout rate* yang berbeda-beda, namun *course* dengan *dropout rate* tertinggi adalah *Biofuel Production* (67%).
- Umur mahasiswa yang melakukan *dropout* cukup bervariasi.
- Terdapat profil tingkat *dropout* yang berbeda antar negara; mahasiswa yang berasal dari Kanada dan Lithuania memiliki *dropout rate* tertinggi sekitar 16.5%.
- Mahasiswa yang memiliki status *debtor* (hutang) memiliki kecenderungan melakukan *dropout* yang sangat tinggi (62%).
- Status pernikahan memiliki korelasi dengan *dropout*; mahasiswa dengan status bercerai (*divorced*) memiliki *dropout rate* hingga 67%.

## Menjalankan Sistem Machine Learning

**Cara Menjalankan Skrip:**
   Setelah semua dependensi terinstal, Anda dapat menjalankan *dashboard* prediktif yang interaktif melalui aplikasi Streamlit.
   ```bash
   streamlit run app.py
   ```
   Lakukan *input* data yang diperlukan, kemudian klik tombol **Predict Dropout Risk**.
**Atau gunakan link berikut: https://student-dropout-analysis2.streamlit.app**

## Conclusion
Dari analisis eksplorasi data, *dashboard*, dan model di *notebook*, ditarik beberapa kesimpulan utama mengenai faktor penyebab mahasiswa *dropout*:

1. **Performa Akademik Semester 1 sebagai Indikator Utama:**
   Mahasiswa dengan nilai rendah, jumlah mata kuliah lulus sedikit, serta *success rate* rendah pada semester pertama memiliki probabilitas *dropout* yang jauh lebih tinggi. Hal ini menunjukkan bahwa performa akademik awal merupakan prediktor kuat terhadap keberlanjutan studi mahasiswa.

2. **Faktor Finansial sebagai Pemicu Dropout yang Signifikan:**
   Status *debtor* dan keterlambatan pembayaran biaya kuliah (*tuition fees*) memiliki hubungan yang kuat dengan peningkatan risiko *dropout*. Mahasiswa yang mengalami kendala finansial cenderung tidak dapat melanjutkan studi secara konsisten.

3. **Variasi Risiko Berdasarkan Segmentasi Mahasiswa:**
   Tingkat *dropout* tidak merata di seluruh populasi. Terdapat perbedaan signifikan berdasarkan program studi, usia, serta jalur masuk. Mahasiswa kelompok non-tradisional (berusia lebih tua atau dari jalur transfer) menunjukkan kecenderungan risiko *dropout* yang lebih tinggi.

4. **Kombinasi Faktor Akademik dan Finansial:**
   Mahasiswa dengan kombinasi performa akademik rendah dan masalah finansial merupakan kelompok dengan risiko *dropout* tertinggi. Interaksi antar faktor ini memperkuat kemungkinan *dropout* secara eksponensial.

5. **Akurasi Prediksi Model:** Model *Random Forest Classifier* dapat mengidentifikasi mahasiswa yang berisiko *dropout* berdasarkan pola kombinasi dari variabel-variabel kunci dengan performa yang sangat baik, yaitu mencapai akurasi 88%.

## Rekomendasi Action Items
Berdasarkan kesimpulan analisis, berikut adalah rekomendasi tindakan strategis untik meminimalisasi *dropout*:

- **Action Item 1: Implementasi Early Warning System Berbasis Akademik**
  Bangun sistem monitoring yang secara otomatis mengidentifikasi mahasiswa berisiko sejak semester pertama, menggunakan indikator seperti *success rate* dan rata-rata nilai. Mahasiswa yang berisiko harus ditindaklanjuti melalui notifikasi kepada dosen wali.

- **Action Item 2: Program Intervensi Akademik Terfokus**
  Sediakan program pendampingan khusus bagi mahasiswa dengan performa akademik rendah (misal: kelas remedial, *mentoring*, dan konseling akademik) untuk membantu mahasiswa beradaptasi dengan beban studi.

- **Action Item 3: Strategi Dukungan Finansial yang Proaktif**
  Identifikasi mahasiswa berstatus *debtor* atau dengan keterlambatan pembayaran sejak dini. Tawarkan solusi seperti skema cicilan, bantuan keuangan, atau beasiswa darurat untuk mengurangi tekanan finansial.

- **Action Item 4: Pendekatan Intervensi Berbasis Segmentasi Risiko**
  Gunakan pemodelan ini untuk memprioritaskan intervensi pada kelompok dengan profil risiko tertinggi (kombinasi masalah akademik dan finansial). Lakukan juga evaluasi khusus pada program studi dengan tingkat *dropout* tinggi (seperti *Biofuel Production*) terkait kurikulum dan metode pembelajarannya.