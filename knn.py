# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 10:34:36 2018

@author: ADMIN
"""
import  numpy as np
import  pandas as pd
import os
os.chdir('C:/Users/ADMIN/Desktop/github')

df=pd.read_csv('airbnb.csv',encoding='ISO-8859-1')
df.info()
df.head(10)

new_df =df.copy()
our_acco =3
new_df["distance"]=abs(new_df["accommodates"]-our_acco)
print (new_df["distance"].value_counts())

new_df["price"].describe()
new_df["price"]=new_df["price"].str.replace(",","")
new_df["price"]=new_df["price"].str.replace("$","").astype("float")
new_df["price"].describe()
print (new_df["distance"].value_counts())


# finding the mean price who have 3 rooms and distance is zero
print(new_df [(new_df["distance"]==0)]["price"].mean())

#    
def get_mean(number_of_rooms,k):
    new_df["distance"]= abs(new_df["accommodates"]-number_of_rooms)         
    new_df=np.new_df.loc[np.random.permutation(len(new_df ))]
    mean=new_df [(new_df["distance"]==0)]["price"][:k].mean()
 
    return mean

int(get_mean(40,5))

new_df.head()





#
#def price_predict(n,k):
#    temp_df["price"]=temp_df["price"].str.replace(",","")
#    new_df["price"]=new_df["price"].str.replace("$","").astype("float")
#    new_df["distance"]= abs(new_df["accommodates"]-number_of_rooms) 
#    temp_df["distance"]=abs (temp_df[features]-n)        
#    new_df=np.new_df.loc[np.random.permutation(len(new_df ))]
#    new_df=new_df [(new_df["distance"]==0)]["price"][:,k].mean()
#    
#price_predict(8,len(new_df))














