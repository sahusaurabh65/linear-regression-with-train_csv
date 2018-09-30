
# coding: utf-8

# In[75]:


#30 sept,2018 
#linear regression




import os

os.chdir('C:/Users/ADMIN/Desktop/greyatom/data sets')


# In[76]:


import pandas as pd
import numpy as np


# In[77]:


df=pd.read_csv("train.csv")


# In[78]:


df


# In[79]:



#finding correlation 
correlation_values=df.select_dtypes(include=[np.number]).corr()
type(correlation_values)

#df["OverallQual"]


# In[80]:


#correlation_values[["Id","SalePrice"]]
#len(correlation_values[["SalePrice"]])
correlation_values[["SalePrice"]]

selected_features=correlation_values[["SalePrice"]][(correlation_values["SalePrice"]>=-0.6)|(correlation_values["SalePrice"]<=0.6)]

# for correlation_values in range(-0.6, 0.6):
#     append[correlation_values]


# In[81]:


selected_features


# In[82]:


X=df[["OverallQual","TotalBsmtSF","GrLivArea","GarageArea"]]


# In[83]:


y=df["SalePrice"]


# In[84]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts


# In[85]:


X_train,X_test,y_train,y_test=tts(X,y, test_size=0.3,random_state=42)


# In[86]:


reg=LinearRegression()


# In[87]:


reg.fit(X_train,y_train)


# In[88]:


y_pred=reg.predict(X_test)


# In[89]:


import numpy as np


# In[90]:


reg.score(X_test,y_test)


# In[91]:


from sklearn.metrics import mean_squared_error
rmse=np.sqrt(mean_squared_error(y_test,y_pred))
rmse


# In[93]:


#from sklearn.metrics import r2_score
#r2_score(X_test,y_test)

