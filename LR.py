import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


print('***** Market Minds *****')
print('Choose the companies Stock you want to predict\n 1.ABMD \n 2.AAXN \n 3.AAWW \n 4.JEQ \n 5.CHU \n Enter an appropriate choice')
ch = int(input())

if(ch == 1) :
   main = pd.read_csv("ABMD.csv")
   print("Company choosen : ABMD")
elif(ch == 2) :
   main = pd.read_csv("AAXN.csv")  
   print("Company choosen : AAXN")  
elif(ch == 3) :
   main = pd.read_csv("AAWW.csv")  
   print("Company choosen : AAWW") 
elif(ch == 4):
   main = pd.read_csv("JEQ.csv") 
   print("Company choosen : JEQ")
elif(ch == 5):
   main = pd.read_csv("CHU.csv")
   print("Comapny chossen : CHU")
else :
   print("Error : Enter valid input ")   
   sys.exit()

Q1=main.Close.quantile(0.25)
Q3=main.Close.quantile(0.75)

IQR=Q3-Q1

lower=Q1-1.5*IQR
upper=Q3+1.5*IQR

k=main[(main.Close>lower)&(main.Close<upper)]

X=np.array(k.Open).reshape(-1,1)
Y=k['Close']
X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.7,random_state=0)

scaler = StandardScaler().fit(X_train)

lm = LinearRegression()
lm.fit(X_train,Y_train)

def predict(Open) :
    s = lm.predict([[Open]])
    print(f'The Close value on prediction is {s}')


print('Enter the value of 0pen')
Open = float(input())

predict(Open)
