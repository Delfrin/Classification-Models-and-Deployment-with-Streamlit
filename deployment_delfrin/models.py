import streamlit as st
import pandas as pd
import pickle
import sklearn

def run():
# Load All Files
    st.title('Prediksi Default Payment') 
    with open('model_knn_tuned.pkl', 'rb') as file1:
        model_knn = pickle.load(file1)
    with open('model_logreg_tuned.pkl', 'rb') as file2:
        model_logreg = pickle.load(file2)
    with open('model_svm_tuned.pkl', 'rb') as file3:
        model_svm = pickle.load(file3)


    limit_balance = st.number_input(label='Input your limit balance', min_value=0.0,max_value=1000000000.0)
    sex = st.selectbox(label='Choose your gender', options=[1, 2])
    education_level = st.selectbox(label='Choose your education level',options=[1, 2, 3, 4, 5, 6, 7])
    age = st.number_input(label='Input your age', min_value=0,max_value=150)
    marital_status = st.selectbox(label='Choose your marital status',options=[1, 2, 3])
    pay_0 = st.selectbox(label='Choose your repayment status in september',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pay_2 = st.selectbox(label='Choose your repayment status in august',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pay_3 = st.selectbox(label='Choose your repayment status in july',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pay_4 = st.selectbox(label='Choose your repayment status in june',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pay_5 = st.selectbox(label='Choose your repayment status in may',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pay_6 = st.selectbox(label='Choose your repayment status in april',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    bill_amt_1 = st.number_input(label='Input the amount of your bill statement in september', min_value=-100000000,max_value=100000000)
    bill_amt_2 = st.number_input(label='Input the amount of your bill statement in august', min_value=-100000000,max_value=100000000)
    bill_amt_3 = st.number_input(label='Input the amount of your bill statement in july', min_value=-100000000,max_value=100000000)
    bill_amt_4 = st.number_input(label='Input the amount of your bill statement in june', min_value=-100000000,max_value=100000000)
    bill_amt_5 = st.number_input(label='Input the amount of your bill statement in may', min_value=-100000000,max_value=100000000)
    bill_amt_6 = st.number_input(label='Input the amount of your bill statement in april', min_value=-100000000,max_value=100000000)
    pay_amt_1 = st.number_input(label='Input the amount of your previous payment in september', min_value=-100000000,max_value=100000000)
    pay_amt_2 = st.number_input(label='Input the amount of your previous payment in august', min_value=-100000000,max_value=100000000)
    pay_amt_3 = st.number_input(label='Input the amount of your previous payment in july', min_value=-100000000,max_value=100000000)
    pay_amt_4 = st.number_input(label='Input the amount of your previous payment in june', min_value=-100000000,max_value=100000000)
    pay_amt_5 = st.number_input(label='Input the amount of your previous payment in may', min_value=-100000000,max_value=100000000)
    pay_amt_6 = st.number_input(label='Input the amount of your previous payment in april', min_value=-100000000,max_value=100000000)
    
    st.write('In the following is the result of the data you have input : ')
    
    data_inf = pd.DataFrame({
        'limit_balance' : limit_balance,
        'sex' : sex,
        'education_level' : education_level,
        'age' : age,
        'marital_status' : marital_status,
        'pay_0' : pay_0,
        'pay_2' : pay_2,
        'pay_3' : pay_3,
        'pay_4' : pay_4,
        'pay_5' : pay_5,
        'pay_6' : pay_6,
        'bill_amt_1' : bill_amt_1,
        'bill_amt_2' : bill_amt_2,
        'bill_amt_3' : bill_amt_3,
        'bill_amt_4' : bill_amt_4,
        'bill_amt_5' : bill_amt_5,
        'bill_amt_6' : bill_amt_6,
        'pay_amt_1' : pay_amt_1,
        'pay_amt_2' : pay_amt_2,
        'pay_amt_3' : pay_amt_3,
        'pay_amt_4' : pay_amt_4,
        'pay_amt_5' : pay_amt_5,
        'pay_amt_6' : pay_amt_6
        }, index=[0])

    st.table(data_inf)


    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        y_pred_logreg = model_logreg.predict(data_inf)
        y_pred_svm = model_svm.predict(data_inf)
        y_pred_knn = model_knn.predict(data_inf)


    # Menampilkan hasil prediksi
    if y_pred_logreg[0] == 0:
        st.write('`Your default payment for next month is 0` (Predicted by Logistic Regression)')
    else:
        st.write('`Your default payment for next month is 1` (Predicted by Logistic Regression)')

    if y_pred_svm[0] == 0:
        st.write('`Your default payment for next month is 0` (Predicted by SVM)')
    else:
        st.write('`Your default payment for next month is 1` (Predicted by SVM)')

    if y_pred_knn[0] == 0:
        st.write('`Your default payment for next month is 0` (Predicted by k-Nearest Neighbors)')
    else:
        st.write('`Your default payment for next month is 1` (Predicted by k-Nearest Neighbors)')