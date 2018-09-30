# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:24:33 2018

@author: ADMIN
"""

import os
import pandas as pd
import numpy as np

#Setting the path
os.getcwd()
os.chdir('C:/Users/ADMIN/Desktop/github')

df=pd.read_csv('airbnb.csv',encoding='ISO-8859-1')

#Load the csv and create a copy
dc_listings = pd.read_csv('airbnb.csv',encoding='ISO-8859-1')
list(dc_listings)
dc_listings1= dc_listings.copy()


#Finding the distance of my house with 3 rooms compared to other houses
dc_listings1["distance"]=abs(dc_listings["accommodates"]-3)
list(dc_listings1["distance"].value_counts())

#Cleaning the price column
dc_listings["price"] = dc_listings["price"].str.replace(",","")
dc_listings["price"] = dc_listings["price"].str.replace("$","").astype("float")
dc_listings1["price"] = dc_listings1["price"].str.replace(",","")
dc_listings1["price"] = dc_listings1["price"].str.replace("$","").astype("float")

dc_listings["price"].describe()

#Finding the mean prices of all the houses with 3 rooms
mean = dc_listings[dc_listings1["distance"]==0]["price"].mean()
mean

#Function that finds the absolute distance for accomodates and finds the predicted price
def get_mean(number_of_rooms,k,dc_listings1):
    np.random.seed(6)
    dc_listings1["distance"]=abs(dc_listings["bathrooms"]-number_of_rooms)
    dc_listings1 = dc_listings1.loc[np.random.permutation(len(dc_listings1))]
    mean =  dc_listings1[dc_listings1["distance"]==0]["price"][:k].mean()
    error = (dc_listings1[dc_listings1["distance"]==0]["price"]-mean)**2
    return mean,(error.sum()/len(error))**0.5
#centeral limit theory
    
#prints mean and error with repect to changes  in mean 
print(get_mean(3,5,dc_listings1))

#finding missing data of security_deposit
print (dc_listings["security_deposit"].isnull().sum()/len(dc_listings["security_deposit"]))

#nonrmalizing the maximum nights
print (dc_listings["maximum_nights"].max())

#nonrmalizing the maximum nights
dc_listings["maximum_nights"]=(dc_listings["maximum_nights"].mean()/dc_listings["maximum_nights"]-dc_listings["maximum_nights"].mean())/dc_listings["maximum_nights"].std()
print (dc_listings["maximum_nights"])

































