import streamlit as st
import main


data = []
st.title('Statistika')

with st.form(key='data_form'):
    intRate = st.number_input("Suku Bunga", min_value=0.0, max_value=1.0,value= 0.0 , step = .1,)
    instalment = st.number_input("Cicilan", min_value=100, max_value=100000,value= 100 , step = 50,)
    dti = st.number_input("Rasio Pendapatan", min_value=0.0, max_value=1.0,value= 0.0 , step = .1,)
    fico = st.number_input("Skor Kredit", min_value=100, max_value=1000,value= 100 , step = 10,)
    daysWithCrLine = st.number_input("Tenggat Hutang", min_value=120, max_value=1826,value= 120 , step = 30,)
    revolBal = st.number_input("Tunggakan", min_value=100, max_value=100000,value= 100 , step = 50,)
    revolUtil = st.number_input("Penggunaan Kredit", min_value=1, max_value=100,value= 1 , step = 1,)
    delinq2yrs = st.number_input("Keterlambatan 2 Tahun", min_value=0, max_value=1,value= 0 , step = 1,)
    inqLast6mths = st.number_input("Pertanyaan 6 Bulan Terakhir", min_value=0, max_value=1,value= 0 , step = 1,)

    submit_button = st.form_submit_button(label='Submit')

if submit_button:

   input_data = {
        'int.rate': intRate,
        'installment': instalment,
        'dti': dti,
        'fico': fico,
        'days.with.cr.line': daysWithCrLine,
        'revol.bal': revolBal,
        'revol.util': revolUtil,
        'delinq.2yrs': delinq2yrs,
        'inq.last.6mths': inqLast6mths
    }
   st.write(main.main(input_data))



