import csv
from enum import EnumMeta 
import pandas as pd
from pandas.core.indexing import maybe_convert_ix
import plotly_express as px

df = pd.read_csv('main.csv')

headl = df.head()
print(headl)

radius = df['planet_radius'].to_list()
mass = df['planet_mass'].to_list()
gravity =[]
 
#df['radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
        
convert_to_si(radius,mass)

def gravity_calculation(radius,mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g= (mass[index]*G)/((radius[index])**2)
        gravity.append(g)
        
gravity_calculation(radius,mass)

df["Gravity"] = gravity
df.to_csv("star_with_gravity.csv")