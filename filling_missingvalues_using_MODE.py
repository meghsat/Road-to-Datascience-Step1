import pandas as pd
import numpy as np
import random

df = pd.read_csv(r'./DATA/diabetes.csv')
c=df.mode()
print(c)
print((df[['Pregnancies', 'Glucose', 'BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']] == 0).sum())

df['Pregnancies']=df['Pregnancies'].replace([0],np.NaN)
k=df.loc[:,"Pregnancies"].mode(dropna=True)
df['Pregnancies']=df['Pregnancies'].replace(np.NaN,k[0])

df['Glucose']=df['Glucose'].replace([0],np.NaN)
l=df.loc[:,"Glucose"].mode(dropna=True)
df['Glucose']=df['Glucose'].replace(np.NaN,l[0])

df['BloodPressure']=df['BloodPressure'].replace([0],np.NaN)
m=df.loc[:,"BloodPressure"].mode(dropna=True)
df['BloodPressure']=df['BloodPressure'].replace(np.NaN,m[0])

df['SkinThickness']=df['SkinThickness'].replace([0],np.NaN)
n=df.loc[:,"SkinThickness"].mode(dropna=True)
df['SkinThickness']=df['SkinThickness'].replace(np.NaN,n[0])
print(n[0])

df['Insulin']=df['Insulin'].replace([0],np.NaN)
o=df.loc[:,"Insulin"].mode(dropna=True)
df['Insulin']=df['Insulin'].replace(np.NaN,o[0])
print(o[0])

df['BMI']=df['BMI'].replace([0],np.NaN)
p=df.loc[:,"BMI"].mode(dropna=True)
df['BMI']=df['BMI'].replace(np.NaN,p[0])



df.to_csv(r'NaNdiabetes_mode(0-1)_Noheading.csv')
print((df[['Pregnancies', 'Glucose', 'BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']] == 0).sum())
