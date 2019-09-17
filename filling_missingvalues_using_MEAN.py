import pandas as pd
import numpy as np
import random
df = pd.read_csv(r'./DATA/diabetes.csv')
c=df.mean()   #calculating the mean for each attribute of dataframe
print(c)
df['Pregnancies']=df['Pregnancies'].replace([0],c[0])  #replacing 0’s in the attribute with mean of that particular attribute.
df['Glucose']=df['Glucose'].replace([0],c[1]) #replacing 0’s in the attribute with mean of that particular attribute.
df['BloodPressure']=df['BloodPressure'].replace([0],c[2]) #replacing 0’s in the attribute with mean of that particular attribute.
df['SkinThickness']=df['SkinThickness'].replace([0],c[3]) #replacing 0’s in the attribute with mean of that particular attribute.
df['Insulin']=df['Insulin'].replace([0],c[4]) #replacing 0’s in the attribute with mean of that particular attribute.
df['BMI']=df['BMI'].replace([0],c[5]) #replacing 0’s in the attribute with mean of that particular attribute.
print(df.head())
#df.to_csv(r'NaNdiabetes.csv') #creating a new excel with all the o replaced values with means
print((df[['Pregnancies', 'Glucose', 'BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']] == 0).sum())
