import pickle
import numpy as np
import streamlit as st
import itertools

#load save model
model = pickle.load(open('pcos_model.sav', 'rb'))

#judul web
st.title('Prediksi Penyakit PCOS')

Age = st.number_input ('Masukan Usia')

Weight = st.number_input ('Masukan Berat Badan (kg)')

Height = st.number_input ('Masukan Tinggi Badan (cm)')

BMI = st.number_input ('Masukan BMI')

Blood_Group = st.number_input('Masukan Blood Group')

RR = st.number_input ('Masukan Nilai Respirasi')

Pregnant = st.selectbox('Apakah Anda Hamil', ['Ya', 'Tidak'])

BP_Systolic = st.number_input ('Masukan Angka Tekanan Darah Sistolik (mmHg)')

BP_Diastolic= st.number_input ('Masukan Angka Tekanan Darah Diastolik (mmHg)')

Endometrium = st.number_input ('Masukan Tebal Dinding Rahim (mm)')

#code untuk prediksi
pp_diagnosis = ''

#mengubah data input pregnant dari string ke numerik
Pregnant = next(itertools.cycle(map(lambda x: 1 if x == 'Ya' else 0, [Pregnant])))

#deklarasikan
pp_prediction = model.predict([[Age, Weight, Height, BMI, Blood_Group, RR, Pregnant, BP_Systolic, BP_Diastolic, Endometrium]])

#mengeksekusi prediksi dengan model
if st.button('Test Prediksi PCOS'):
#mengecek hasil prediksi
    if (pp_prediction[0] == 1):
        pp_diagnosis = 'Pasien Terkena PCOS'
    else:
        pp_diagnosis = 'Pasien Tidak Terkena PCOS'
    
    #menampilkan hasil prediksi
    st.success(pp_diagnosis)
