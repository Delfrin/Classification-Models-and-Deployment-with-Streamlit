import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Hasil Explaration Data Analysis')
#Memanggil data csv 
    df= pd.read_csv('P1G5_Set_1_Delfrin_Adiyatma.csv')
    st.write('')

#menampilkan 5 data teratas
    st.header('**Preview Dataset**')
    st.table(df.head(10))
    st.write('-----------------------------')

#menampilkan deskripsi statistik dari data
    st.header('**Informasi Statistik**')
    st.table(df.describe().T)
    st.write('`Dataset ini terdiri dari beberapa kolom yang mencakup informasi tentang pelanggan. Kolom pertama adalah "limit_balance", yang merupakan jumlah kredit yang disetujui untuk setiap pelanggan. Kemudian, terdapat kolom "sex" yang menunjukkan jenis kelamin pelanggan, dengan nilai 1 untuk laki-laki dan 2 untuk perempuan. Selanjutnya, terdapat kolom "education_level" yang memberikan informasi tentang tingkat pendidikan pelanggan, dengan nilai 1 untuk S2/S3, 2 untuk diplom, 3 untuk SMA, dan 4 untuk tingkat pendidikan lainnya. Kolom "marital_status" menunjukkan status perkawinan pelanggan, dengan nilai 1 untuk menikah, 2 untuk tunggal, dan 3 untuk status perkawinan lainnya.`')
    st.write('')
    st.write('`Kolom "age" memberikan informasi tentang usia pelanggan, sedangkan kolom "pay_0", "pay_2", "pay_3", "pay_4", "pay_5", dan "pay_6" memberikan status pembayaran bulan ke-n, di mana nilai-nilai negatif menunjukkan pelunasan tepat waktu, dan nilai positif menunjukkan keterlambatan pembayaran. Selanjutnya, terdapat kolom-kolom "bill_amt_1" hingga "bill_amt_6" yang mencatat jumlah tagihan bulan ke-n, dan kolom-kolom "pay_amt_1" hingga "pay_amt_6" yang mencatat jumlah pembayaran bulan ke-n. `')
    st.write('')
    st.write('`Terakhir, kolom "default_payment_next_month" menunjukkan status pembayaran bulan depan, di mana nilai 1 menunjukkan bahwa pelanggan terlambat membayar, sementara nilai 0 menunjukkan bahwa pelanggan membayar tepat waktu.`')
    st.write('-----------------------------')
#menampilakn line plot
    st.header('**Analisis Repayment Status**')
    image1 = Image.open('gc5line.png')
    st.image(image1)
    
#menampilkan penjelasan 
    with st.expander('Penjelasan'):
        st.caption('`Linechart yang semakin tinggi seiring dengan berjalannya waktu menunjukkan adanya tren meningkatnya keterlambatan pembayaran tagihan kredit di antara nasabah.`')
    st.write('-----------------------------')
#menampilakn bar plot 1
    st.header('**Analisis Bill Statement**')
    image2 = Image.open('gc5bar1.png')
    st.image(image2)

#menampilkan penjelasan 
    with st.expander('Penjelasan'):
        st.caption('`Barchart menunjukkan bahwa terjadi peningkatan tagihan secara konsisten di seiap bulannya`')
    st.write('-----------------------------')
#menampilakn bar plot 2
    st.header('**Analisis Amount of Previous Payment**')
    image3 = Image.open('gc5bar2.png')
    st.image(image3)

#menampilkan penjelasan 
    with st.expander('Penjelasan'):
        st.caption('`Dapat dilihat pada comparison bar plot bahwa meskipun rata - rata dari bill amount meningkat, pay amount cenderung tidak stabil dan berada di rentang yang sama (jauh lebih kecil dibanding bill) di setiap bulannya, ini menunjukkan bahwa nasabah mulai mengalami kesulitan membayar tagihan yang ada`')


