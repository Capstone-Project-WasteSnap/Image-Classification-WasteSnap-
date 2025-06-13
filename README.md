# Machine Learning Capstone Project 
WasteSnap : Sistem Klasifikasi Gambar dan Sistem Prediksi Komposisi Sampah

## **Project Team Members** : <br>
Arthur Setiawan Waruwu (MC319D5Y2042) - Machine Learning Engineer - Universitas Sumatera Utara <br>		
Sakifa Indira Putri (MC319D5X2380) - Machine Learning Engineer - Universitas Sumatera Utara <br>
Diva Anggreini Harahap (MC319D5X2329) - Machine Learning Engineer - Universitas Sumatera Utara <br>		
Ahmad Wildan Naufi Raharjo (FC525D5Y0132) - Front End Back End Engineer - Politeknik Negeri Bamyuwangi <br>		
Achmad Naufal Falendra (FC525D5Y0162) - Front End Back End Engineer - Politeknik Negeri Banyuwangi <br>		
Achmad Yogi Firdani (FC525D5Y0124) - Front End Back End Engineer - Politeknik Negeri Banyuwangi <br>

## Project Overview
Manajemen sampah rumah tangga di Indonesia menjadi isu lingkungan yang mendesak, dengan 40% sampah nasional berasal dari rumah tangga. Faktor penyebab utama termasuk pertumbuhan jumlah penduduk, perubahan pola konsumsi, rendahnya partisipasi masyarakat dalam memilah sampah, dan keterbatasan infrastruktur pengelolaan sampah. Sekitar 32% sampah belum terkelola dengan baik, yang berisiko menimbulkan pencemaran air, tanah, penyebaran penyakit, dan emisi gas rumah kaca.

Untuk mengatasi tantangan ini, kami mengembangkan WasteSnap, sebuah solusi berbasis AI interaktif yang mengintegrasikan sistem klasifikasi gambar dan sistem prediksi komposisi sampah menggunakan machine learning. Sistem ini memungkinkan pengguna untuk mengidentifikasi jenis sampah melalui gambar, serta memprediksi komposisi sampah (organik dan anorganik). Selain itu, WasteSnap juga memberikan informasi tentang TPS3R (Tempat Pengolahan Sampah Sementara Terdekat) dan cara pengelolaan sampah organik dan anorganik secara praktis.

Proyek ini memanfaatkan algoritma machine learning untuk menghasilkan klasifikasi dan prediksi yang akurat, menjadikannya sebagai alat yang berguna untuk meningkatkan praktik pemilahan sampah dan mendorong partisipasi masyarakat dalam pengelolaan sampah yang berkelanjutan.

## Business Understanding
### Problem Statements
- Masyarakat kesulitan dalam memilah sampah secara manual karena tidak adanya alat bantu yang efisien dan otomatis. Hal ini memperlambat proses pemilahan dan menyebabkan tumpukan sampah yang tidak tekelola dengan baik.
- Banyak daerah kesulitan memprediksi jenis dan volume sampah yang akan dihasilkan di masa depan. Tanpa data yang memadai, perencaan infrastruktur pengelolaan sampah menjadi tidak optimal, menyebabkan pemborosan sumber daya dan kurangnya fasilitas yang sesuai dengan kebutuhan.

### Goals
- Mengembangkan alat bantu berbasis teknologi AI yang dapat secara otomatis mengklasifikasikan dan memilah sampah, sehingga mempercepat proses pemilihan dan mengurangi ketergantungan pada upaya manual, serta meminimalisir tumpukan sampah yang tidak terkelola dengan baik.
- Mengembangkan sistem prediksi berbasis machine learning yang dapat memprediksi jenis dan volume sampah yang akan dihasilkan di masa depan, sehingga dapat memabntu dalam perencanaan infrastruktur pengelolaan sampah yang lebih efektif dan efisien.

### Solution Approach
- Model Klasifikasi Gambar dengan Convolutional Neural Networks (CNN) <br>
Untuk memudahkan pemilahan sampah secara otomatis, kami menggunakan Convolutional Neural Networks (CNN) untuk membangun dua model klasifikasi gambar, Model Klasifikasi Organik dan Anorganik dan Model Klasifikasi Ada Sampah dan Tidak Ada Sampah. CNN efektif dalam memproses data visual dan mampu mengenali pola-pola yang ada pada gambar sampah, seperti bentuk, tekstur, dan warna.
- Model Prediksi Komposisi Sampah dengan Random Forest <br>
Untuk memprediksi komposisi sampah yang akan dihasilkan di masa depan, kami menggunakan Random Forest. Random Forest adalah algoritma ensemble learning yang dapat memproses data kompleks dan memiliki performa yang baik dalam prediksi dengan data yang memiliki banyak fitur.

## Data Understanding
### Model Klasifikasi Gambar :
- Dataset ini berisi gambar-gambar sampah rumah tangga yang sudah kami kelompokkan dalam folder yang sesuai dengan jenisnya. Dataset ini memiliki 13.8k gambar, yang masing-masing kami kumpulkan secara mandiri dari berbagai sumber, seperti Kaggle, Google Images, Pinterest, dan sumber-sumber lainnya

- Isi Dataset :
Penjelasan Dataset
Berikut adalah kategori-kategori yang terdapat dalam dataset ini:

**Model Klasifikasi Gambar Organik dan Anorganik** <br>
Organik
- Buah
- Cangkang Telur
- Kotoran Hewan
- Sayuran
- Sisa Teh dan Kopi
- Sisa Makanan <br>

Anorganik
- Elektronik
- Kaca
- Kain
- Kardus
- Karet
- Kayu
- Kertas
- Logam
- Plastik
- Sepatu
- Styrofoam

**Model Klasifikasi Ada Sampah dan Tidak Ada Sampah** <br>
- Ada Sampah
- Tidak Ada Sampah <br>

- Link Kaggle :
https://www.kaggle.com/datasets/arthurwaruwu/datasetcapstonefixx
https://www.kaggle.com/datasets/sakifaindiraputri/dataset-model-2

## Model Prediksi Komposisi Gambar :
Data komposisi sampah yang digunakan berasal dari tahun 2018 hingga 2024 yang diperoleh dari website SIPSN dengan memanfaatkan library BeautifulSoup untuk web scraping
- Link JSON :
https://drive.google.com/file/d/1U07Ld1GOruukNU1F3vjnskVlyTvp9W7h/view?usp=sharing
- Isi Dataset :
- `tahun` : merujuk tahun tertentu 2018 hingga 2024.
- `nama_provinsi` : berisi nama provinsi yang merupakan data kategorikal
- `jenis_sampah` : kategori jenis sampah dan data kategorikal.
- `persentase` : angka desimal menunjukkan jenis sampah dan tipe datanya float.

### Univariate EDA Model Prediksi Komposisi Gambar :
- Cek missing values <br>
![missing values](image-4.png) <br>
Dengan kesimpulan bahwa tidak ada missing values yang terdeteksi. <br>
- Cek data duplikat <br>
![Data duplikat](image-5.png) <br>
Dengan kesimpulan bahwa ada 4 data yang duplikat yang terdeteksi. <br>
- Melakukan `describe()` di kolom `persentase`<br>
![describe() di kolom numerik](image.png)<br>
- Melakukan `describe()` di kolom object<br>
![describe() di kolom object](image-1.png)<br>
- Mendeteksi Outliers<br>
![Outliers](image-2.png) <br>
Secara keseluruhan, boxplot ini menunjukkan distribusi yang cenderung skewed ke kanan, dengan sebagian besar sampah memiliki persentase rendah, namun ada beberapa kategori sampah dengan persentase yang sangat tinggi.<br>
- Unique values dalam kolom tahun<br>
![Unique Values](image-3.png)<br>
- Distribusi `persentase`<br>
![Distribusi Persentase](image-6.png) <br>
Dengan kesimpulan, sebagian besar data menunjukkan frekuensi yang sangat tinggi di kisaran persentase rendah, terutama pada rentang 0 hingga 10%. Hal ini menunjukkan bahwa sebagian besar sampah yang tercatat memiliki persentase yang sangat kecil. Ini bisa berarti bahwa sebagian besar kategori sampah memiliki kontribusi kecil terhadap total volume sampah yang tercatat. <br>
- Distribusi `jenis_sampah`<br>
![jenis sampah](image-7.png) <br>
Dengan kesimpulan, sampah terbagi cukup merata antara berbagai jenis, dengan kategori seperti Sisa Makanan, Plastik, Logam, Kertas/Karton, dan Kain masing-masing berkontribusi sekitar 11% dari total sampah. Beberapa kategori seperti Karet/Kulit dan Lainnya memiliki kontribusi sedikit lebih rendah (sekitar 10-11%). Sisa Makanan menempati persentase tertinggi, yang mengindikasikan bahwa sampah organik menjadi salah satu kategori utama di banyak daerah, sehingga memerlukan perhatian khusus dalam pengelolaannya.<br>
- Top 5 Provinsi dengan Sampah Terbanyak<br>
![5 Provinsi dengan Sampah Terbanyak](image-8.png)<br>

## Data Preparation
### Model Klasifikasi Gambar
- Menghapus file yang berekstensi tidak valid.
- Membagi dataset dengan rasio Train 80%, Test 10% dan Validation 10%.
- Semua gambar dinormalisasi dengan cara melakukan rescaling, yaitu membagi nilai pixel dengan 255. Hal ini memastikan bahwa nilai pixel berada dalam rentang [0, 1], yang penting untuk mempercepat konvergensi selama pelatihan model.
- Augmentasi Data:
Berbagai teknik augmentasi diterapkan untuk memperkaya variasi data, antara lain:
- Rotasi hingga 30 derajat untuk memperkenalkan variasi dalam orientasi gambar.
- Translasi horizontal dan vertikal (shift) untuk menambah ketahanan model terhadap pergeseran objek dalam gambar.
- Shearing (distorsi) dan zoom untuk membuat model lebih robust terhadap perubahan skala dan perspektif.
- Flip horizontal untuk memperkenalkan lebih banyak variasi dalam posisi objek.
- Channel shift untuk mengubah warna dan memberikan variasi dalam pencahayaan.<br>
- Semua gambar sudah di resize menjadi 224x224 piksel agar sesuai dengan ukuran input yang diperlukan oleh model.
- Data diproses dalam batch size 32 dan setiap gambar diberi label berdasarkan kategori melalui one-hot encoding. Penggunaan class_mode `categorical` memastikan bahwa output dari model adalah dalam format kategori, yang sesuai dengan kebutuhan untuk klasifikasi gambar.
- Data diacak `(shuffle=True)` untuk meningkatkan keberagaman dalam tiap epoch pelatihan dan menghindari bias yang disebabkan oleh urutan data. Pengaturan seed=42 digunakan untuk memastikan replikasi dan konsistensi dalam eksperimen, sehingga hasil pelatihan dapat direproduksi dengan cara yang sama pada eksperimen berikutnya.

### Model Prediksi Komposisi Gambar
- Menghapus baris yang memiliki nilai 'ALL' di kolom `tahun`.
- Mengkonversi tipe data `tahun` menjadi int.
- Menghapus data yang duplikat.
- Encoding kolom kategorikal menggunakan One-Hot Encoding.
- Handling outliers menggunakan metode capping.
- Normalisasi menggunakan StandardScaler. StandardScaler adalah metode normalisasi yang digunakan untuk mengubah data sehingga memiliki distribusi dengan rata-rata 0 dan deviasi standar 1. Tujuannya membuat data lebih seragam sehingga dapat membantu dalam analisis.
- Membagi dataset menjadi 80% data pelatihan dan 20% data uji yang nantinya akan membantu evaluasi model dengan data yang tidak pernah dilihat selama training.

## Modelling
### Model Klasifikasi Gambar
1. Input Layer:
Membuat input layer dengan ukuran gambar 224x224 piksel dan 3 channel (RGB), menggunakan Input dari Keras.

2. Base Model:
- Menggunakan MobileNetV2 sebagai base model, yang telah dilatih sebelumnya dengan dataset ImageNet. Model ini diimpor dari tensorflow.keras.applications.MobileNetV2.
- Pada model ini, parameter include_top=False digunakan untuk menghilangkan layer klasifikasi pada bagian atas model (fully connected layers), sehingga hanya bagian feature extractor yang digunakan.
- Semua layer dalam model base ini diatur untuk dapat dilatih (base_model.trainable = True).

3. Fine-Tuning:
- Agar proses pelatihan lebih efisien, hanya 50 layer terakhir dari MobileNetV2 yang dilatih. Layer lainnya dibekukan untuk mengurangi beban komputasi dan mempercepat pelatihan.
- Ini dilakukan dengan menggunakan loop for layer in base_model.layers[:-50], di mana setiap layer sebelum 50 layer terakhir dibekukan.

4. Custom Layers: <br>

| **Layer**                  | **Deskripsi**                                                                                                                           |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Convolutional Layer**    | Menambahkan layer konvolusi 2D dengan 8 filter dan ukuran kernel (3, 3), diikuti dengan aktivasi ReLU.                                  |
| **BatchNormalization**     | Menstabilkan dan mempercepat pelatihan dengan normalisasi setiap batch untuk menjaga distribusi data tetap stabil.                      |
| **Global Average Pooling** | Mengurangi dimensi output dari layer konvolusi dengan mengambil rata-rata dari setiap feature map.                                      |
| **Dropout**                | Ditambahkan dengan rate 0.5 untuk mengurangi overfitting dengan menghilangkan sebagian neuron selama pelatihan.                         |
| **Dense Layer**            | Layer dense dengan 128 neuron dan fungsi aktivasi ReLU untuk memberikan transformasi non-linear.                                        |
| **Output Layer**           | Menggunakan fungsi aktivasi softmax untuk klasifikasi multi-kelas, dengan jumlah unit sama dengan jumlah kelas dalam dataset pelatihan. |


5. Model Final:
- Model final dibuat dengan menghubungkan input layer dan output layer yang telah didefinisikan.
- Struktur model dapat dilihat dengan memanggil model.summary().

6. Callbacks:
- ReduceLROnPlateau: Digunakan untuk mengurangi learning rate jika validasi loss tidak membaik setelah beberapa epoch (patience=3), untuk membantu model keluar dari local minima.
- EarlyStopping: Menghentikan pelatihan jika validasi loss tidak membaik setelah beberapa epoch (patience=7) dan mengembalikan bobot model ke yang terbaik.

7. Model Compilation:
- Model dikompilasi dengan optimizer Adam dengan learning rate awal 1e-5.
- Fungsi loss yang digunakan adalah categorical_crossentropy, yang umum digunakan untuk klasifikasi multi-kelas.
- Accuracy digunakan sebagai metrik untuk memantau kinerja model.

8. Model Training:
- Model dilatih menggunakan model.fit() dengan data pelatihan (train_generator) dan data validasi (val_generator).
- Proses pelatihan berlangsung selama 50 epoch, dengan menggunakan callbacks ReduceLROnPlateau dan EarlyStopping.
- Jika ada class_weights_dict, bobot kelas akan diterapkan untuk menangani ketidakseimbangan kelas dalam dataset.

| **Kelebihan**                                                                                                                                        | **Kekurangan**                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - Menggunakan **MobileNetV2**, yang merupakan model ringan dan efisien, cocok untuk perangkat dengan keterbatasan komputasi.                         | - Memerlukan pengaturan yang hati-hati pada parameter fine-tuning untuk mendapatkan hasil terbaik.                                                                   |
| - **Fine-tuning** memungkinkan untuk memanfaatkan pengetahuan yang sudah ada dalam pre-trained model untuk mempercepat pelatihan.                    | - Memerlukan waktu komputasi yang cukup besar jika dataset besar dan pelatihan dilakukan dalam banyak epoch.                                                         |
| - **Dropout** dan **BatchNormalization** membantu mencegah overfitting dan mempercepat konvergensi.                                                  | - Penggunaan **MobileNetV2** yang dioptimalkan untuk efisiensi mungkin sedikit mengurangi akurasi dibandingkan model yang lebih besar seperti ResNet atau Inception. |
| - **Callbacks** seperti **EarlyStopping** dan **ReduceLROnPlateau** membantu dalam menghindari overfitting dan memperbaiki model dengan lebih cepat. | - Penggunaan model transfer learning dapat menyebabkan ketergantungan pada kualitas pre-trained model yang digunakan.                                                |


### Model Prediksi Komposisi Gambar
Langkah-langkah modelling menggunakan Random Forest Regressor :
1. Menentukan Parameter Grid untuk GridSearchCV
mendefinisikan parameter grid yang akan digunakan dalam GridSearchCV untuk melakukan pencarian parameter terbaik. Parameter yang dicari antara lain:
- n_estimators: Jumlah pohon yang akan digunakan pada model (50, 100, 150).
- max_depth: Kedalaman maksimum pohon (8, 10, 12, None).
- min_samples_leaf: Jumlah minimum sampel yang diperlukan di setiap daun (3, 5, 7).
- min_samples_split: Jumlah minimum sampel yang diperlukan untuk membelah node (5, 10).

2. Inisialisasi Model
Model dasar Random Forest Regressor diinisialisasi dengan parameter default dan random_state=42 untuk memastikan hasil yang konsisten pada setiap percakapan.

3. Melakukan Grid Search untuk Mencari Parameter Terbaik
- GridSearchCV digunakan untuk menemukan parameter terbaik dengan melakukan pencarian melalui grid parameter yang telah ditentukan.
- Pada proses ini, dilakukan evaluasi menggunakan cross-validation (cv=5) untuk menghindari overfitting dan mendapatkan model yang lebih general.
- Waktu pencarian dicatat untuk mengetahui berapa lama waktu yang dibutuhkan untuk mencari parameter terbaik.

4. Evaluasi Model dengan Parameter Terbaik
- Setelah parameter terbaik ditemukan, model yang terbaik akan disimpan dan diterapkan pada data uji.

- Hasil R2 score dari model terbaik pada data uji akan dievaluasi untuk memastikan performa model dalam memprediksi data yang tidak terlihat sebelumnya.

5. Latih Model Terbaik pada Seluruh Data
- Setelah parameter terbaik ditemukan, model akhirnya dilatih menggunakan seluruh data (X, y) untuk memanfaatkan semua informasi yang tersedia.

- Model yang telah dilatih ini diharapkan memiliki performa yang lebih baik karena telah menggunakan parameter yang dioptimalkan.

| **Kelebihan**                                                                                                                | **Kekurangan**                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **GridSearchCV** memungkinkan pencarian sistematis untuk menemukan parameter terbaik, mengoptimalkan kinerja model.          | **Waktu komputasi** dapat menjadi cukup lama, terutama jika parameter grid besar dan data sangat besar.                   |
| **Random Forest Regressor** adalah model ensemble yang mengurangi risiko overfitting, menghasilkan model yang lebih general. | **GridSearchCV** memerlukan sumber daya yang lebih besar, terutama ketika jumlah parameter yang diuji sangat banyak.      |
| **Cross-validation** membantu menilai model secara lebih akurat, menghindari overfitting pada data pelatihan.                | **Random Forest** terkadang bisa lebih sulit untuk diinterpretasikan karena merupakan model berbasis pohon yang kompleks. |


## Evaluasi
### Model Klasifikasi Gambar Organik dan Anorganik
- Hasil Visualisasi <br>
![alt text](image-12.png) <br>
Grafik pertama menunjukkan bahwa Training Accuracy (garis biru) meningkat secara signifikan, sementara Validation Accuracy (garis oranye) juga menunjukkan peningkatan meskipun ada beberapa fluktuasi. Ini menunjukkan model belajar dengan baik, tetapi fluktuasi pada validasi dapat mengindikasikan overfitting. Grafik kedua menunjukkan Training Loss menurun stabil, yang berarti model semakin baik dalam memprediksi data pelatihan, tetapi Validation Loss sedikit berfluktuasi pada beberapa titik, yang menunjukkan adanya potensi ketidakstabilan atau overfitting dalam model.
- Classification Report <br>
![alt text](image-13.png) <br>
Laporan klasifikasi ini menunjukkan kinerja model dalam mengklasifikasikan dua kelas: Anorganik dan Organik. Precision untuk kelas Anorganik adalah 1.00, yang berarti model sangat tepat dalam mengidentifikasi sampah anorganik, sementara recall 0.96 menunjukkan bahwa model dapat mendeteksi 96% sampah anorganik dengan benar. Untuk kelas Organik, precision adalah 0.95, dan recall 1.00, yang berarti model dapat mendeteksi semua sampah organik dengan sangat baik. F1-score yang tinggi untuk kedua kelas (0.98 untuk Anorganik dan 0.97 untuk Organik) menunjukkan keseimbangan yang baik antara precision dan recall, dengan accuracy keseluruhan 0.97.
- Confusion Matrix <br>
![alt text](image-14.png) <br>
Confusion matrix ini menunjukkan hasil klasifikasi antara dua kelas: Anorganik dan Organik. Model berhasil mengklasifikasikan 543 sampel "Anorganik" dengan benar, sementara hanya 24 sampel yang salah diklasifikasikan sebagai "Organik". Di sisi lain, 460 sampel "Organik" berhasil diklasifikasikan dengan benar, dan hanya 2 sampel yang salah diklasifikasikan sebagai "Anorganik". Hasil ini mengonfirmasi bahwa model memiliki performa yang sangat baik dalam membedakan kedua kelas.

### Model Klasifikasi Gambar Ada Sampah dan Tidak Ada Sampah
- Hasil Visualisasi <br>
![alt text](image-9.png) <br>
1. Training vs Validation Accuracy: Grafik ini menunjukkan perkembangan akurasi selama proses pelatihan. Training Accuracy (garis biru) meningkat secara signifikan, yang menandakan model belajar dengan baik dari data pelatihan. Validation Accuracy (garis oranye) juga meningkat, namun ada beberapa fluktuasi yang menunjukkan sedikit ketidakkonsistenan, yang bisa menjadi indikasi adanya overfitting jika akurasi validasi tidak stabil.

2. Training vs Validation Loss: Grafik ini memperlihatkan loss pada data pelatihan dan validasi. Training Loss (garis biru) terus menurun seiring dengan bertambahnya epoch, yang menunjukkan bahwa model semakin baik dalam memprediksi data pelatihan. Validation Loss (garis oranye) juga menurun, namun ada beberapa titik di mana kurva validasi loss meningkat sedikit, yang mungkin menandakan model mulai overfit pada data pelatihan.

- Classification Report <br>
![alt text](image-10.png) <br>
Confusion matrix ini menunjukkan hasil klasifikasi model dengan dua kelas: Ada Sampah dan Gak Ada Sampah. Model berhasil mengklasifikasikan 68 sampel "Ada Sampah" dengan benar dan hanya 10 sampel yang salah diklasifikasikan. Semua 43 sampel "Gak Ada Sampah" diklasifikasikan dengan benar, menunjukkan bahwa model sangat akurat dalam mengidentifikasi kedua kelas.

- Confusion Matrix <br>
!![alt text](image-11.png) <br>
Laporan klasifikasi menunjukkan precision, recall, dan F1-score untuk kedua kelas. Untuk "Ada Sampah", precision adalah 1.00 dan recall 0.87, memberikan F1-score 0.93. Untuk "Gak Ada Sampah", precision adalah 0.81 dan recall 1.00, dengan F1-score 0.90. Model memiliki accuracy keseluruhan 92%, dengan macro average dan weighted average yang menunjukkan kinerja model yang baik pada kedua kelas.

### Model Prediksi Komposisi Gambar
- Hasil Evaluasi <br>
![alt text](image-15.png) <br>
Grafik ini menunjukkan learning curve untuk model Random Forest, yang membandingkan R2 score antara training dan validation dengan peningkatan ukuran data pelatihan. Dari grafik, terlihat bahwa seiring bertambahnya jumlah data pelatihan, training score (garis merah) dan validation score (garis hijau) keduanya meningkat. Ini menunjukkan bahwa model mulai mempelajari pola dengan lebih baik seiring dengan data yang lebih banyak, dengan kedua skor mendekati nilai yang lebih tinggi.

- Inference <br>
![alt text](image-16.png) <br>
Grafik ini menunjukkan prediksi persentase sampah berdasarkan jenis sampah di Jawa Barat untuk tahun 2025. Hasilnya menunjukkan bahwa plastik memiliki prediksi persentase tertinggi, diikuti oleh sisa makanan, dan logam. Beberapa jenis sampah seperti kaca, kain, dan karton memiliki persentase yang jauh lebih rendah. Grafik ini menggunakan model Random Forest yang dioptimalkan untuk memprediksi distribusi persentase sampah berdasarkan data yang ada.

## Kesimpulan
Proyek WasteSnap telah berhasil mengembangkan sistem berbasis AI untuk mengatasi masalah pengelolaan sampah rumah tangga di Indonesia dengan dua komponen utama: klasifikasi gambar dan prediksi komposisi sampah. Sistem klasifikasi gambar menggunakan Convolutional Neural Networks (CNN) untuk secara otomatis mengidentifikasi dan memilah jenis sampah (organik dan anorganik), serta mendeteksi apakah sampah ada atau tidak. Model prediksi komposisi sampah menggunakan Random Forest untuk memperkirakan volume sampah yang akan dihasilkan di masa depan, membantu dalam perencanaan pengelolaan sampah yang lebih efektif.

Hasil evaluasi menunjukkan bahwa model klasifikasi gambar memberikan akurasi yang tinggi, dengan precision dan recall yang sangat baik untuk kedua dataset. Confusion matrix dan classification report mengonfirmasi bahwa model mampu membedakan kedua kelas dengan akurat. Sementara itu, untuk model prediksi komposisi sampah, prediksi persentase jenis sampah seperti plastik dan sisa makanan menunjukkan hasil yang realistis, berguna untuk perencanaan pengelolaan sampah jangka panjang.

Dengan demikian, WasteSnap dapat menjadi alat yang sangat berguna dalam meningkatkan kesadaran dan praktik pemilahan sampah di masyarakat, sekaligus membantu pihak berwenang dalam merencanakan infrastruktur pengelolaan sampah yang lebih efisien.
