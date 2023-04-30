import pickle
import streamlit as sl

model = pickle.load(open('Estimasi_Wendys.sav', 'rb'))

sl.title('Estimasi Jumlah Kalori Makanan Di Menu Wendys')
sl.write('---')


Fat = sl.number_input('Input Total Fat')
SatFat = sl.number_input('Input Total SatFat')
TransFat = sl.number_input('Input Total TransFat')
Cholesterol = sl.number_input('Input Total Cholesterol')
Sodium = sl.number_input('Input Total Sodium')
TotalCarb = sl.number_input('Input Total TotalCarb')
DietaryFiber = sl.number_input('Input Total DietaryFiber')
Sugars = sl.number_input('Input Total Sugars')
Protein = sl.number_input('Input Total Protein')
WeightWatchers = sl.number_input('Input Total WeightWatchers')


predict = ''

if sl.button('Calories'):
    predict = model.predict(
        [[Fat,SatFat,TransFat,Cholesterol,Sodium,TotalCarb,DietaryFiber,Sugars,Protein,WeightWatchers]]
    )
    sl.write ('Estimasi jumlah kalori makanan  di Wendys (kCal) : ', predict)