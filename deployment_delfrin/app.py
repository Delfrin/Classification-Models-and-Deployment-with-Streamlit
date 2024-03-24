import streamlit as st
import eda
import models
import sklearn

page = st.sidebar.selectbox(label='Pilih Halaman:', options=['Home', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home':
    st.title('Perkenalan') 
    st.write('')
    st.write('**Graded Challenge 5**')
    st.write('Nama      : Delfrin Adiyatma Situmeang')
    st.write('Batch     : MSIB')
    st.write('Tujuan    : Program ini dibuat untuk menggunakan feature engineering untuk mengolah data mentah menjadi data siap pakai yang akan dimodelkan menggunakan 3 Model klasifikasi (Logistic Regression, SVM, dan kNN) dimana base modelnya akan di cross-validate serta di-tuning. Semua proses tersebut akan dirangkai dalam pipeline.')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk mengakses hasil analisis')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Pemahaman tentang konsep dasar dan aplikasi dari teknik klasifikasi menjadi kunci dalam analisis data. Classification merupakan salah satu teknik penting dalam machine learning yang memiliki berbagai macam aplikasi, termasuk dalam prediksi, deteksi, dan pengambilan keputusan. Dalam konteks ini, Logistic Regression, Support Vector Machine (SVM), dan k-Nearest Neighbors (KNN) adalah tiga algoritma klasifikasi yang akan digunakan. Memahami konsep dan prinsip kerja dari ketiga algoritma ini menjadi sangat penting bagi *data scientist*')

    with st.expander("Problem Statement"):
            st.caption('Pembelajaran tentang Support Vector Machine (SVM), Logistic Regression, dan k-Nearest Neighbors (KNN) adalah untuk benar-benar memahami konsep dasar dari ketiga model tersebut serta menjadi mahir dalam menerapkannya dalam pemodelan dan prediksi. Proses pembelajaran ini melibatkan **Apa** saja teori di balik masing-masing model, **Siapa** target analisis dari masing - masing model, **Bagaimana** praktik implementasi menggunakan Python dan scikit-learn, serta **Kapan** sebuah model dapat dikatakan memiliki kinerja baik.')

    with st.expander("Kesimpulan"):
        st.caption('`Setelah berhasil menyelesaikan proses membangun dan mengimplementasikan ketiga model, dapat disimpulkan bahwa setiap model memiliki kelebihan uniknya masing-masing. Logistic regression memiliki kelebihan dalam interpretasi yang mudah dan efisiensi komputasi yang tinggi. SVM efektif dalam menangani dataset dengan pemisah yang kompleks dan memiliki kemampuan untuk bekerja dengan baik dalam ruang dimensi tinggi. Sedangkan kNN memiliki kemampuan untuk menangani pola-pola lokal yang kompleks dan fleksibilitas dalam menyesuaikan diri dengan struktur data yang beragam. Oleh karena itu, pemahaman karakteristik dan kelebihan masing-masing model memungkinkan saya untuk memilih dan menyesuaikan model yang paling sesuai dengan kebutuhan dan karakteristik data yang dihadapi.`')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
     models.run()
