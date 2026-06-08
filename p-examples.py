#pandas all methods to manipulate data ... firstly we have to validate data.

#series ( one dimensional .. stores data in series )
#dataframe ( two dimensional .. stores data in table format in rows and columns)

import numpy as np
import pandas as pd


#SERIES

marks = pd.Series([90,89,78,67], index=["Arsh","Akash","Sukhan","Navjot"])
print(marks)

student = pd.Series(["Arsh","akash","sukhan"])
print(student)


#common Series methods 

print("Mean:", marks.mean())        #sum of all values / no. of values ( used when some values are missing and data is normal )
print("Median:",marks.median())     #middle value after sorting in ascending order ( if len is even then mean ( average ) of two middle values )
print("Sorted:",marks.sort_values(ascending=False))     #sorting in ascending order

"""
Example:

salary = [20k,25k,30k,35k,500k]

mean = 20k + 25k + 30k + 35k + 500k / 5 = 122k
median = 30k

if one salary is missing : 

salary = [20k,25k,?,35k,500k]

we cant fill mean because it seems unrealistic ( 122k )

so we fill median (30k)

"""

print("Marks head : ")
print(marks.head(2)) #by default head() returns first 5 values from the top
print("Marks tail :")
print(marks.tail())  #it return last 5 values
print("Max")
print(marks.max())      #returns maximum value from series
print("min")
print(marks.min())      #returns minimum value from series
print("sort by values")
print(marks.sort_values())  #sort by values
print("sort by index")
print(marks.sort_index())   #sort by index
print("Unique")
print(marks.unique())       #unique values
print("nunique")
print(marks.nunique())      #number of unique values
print("check missing values")
print(marks.isna())         #checks the missing values
print("fill missing values")
print(marks.fillna(marks.mean()))       #fill missing values ( need parameter )
print("change data type")
print(marks.astype(float))      #changes the datatype

#DATAFRAME

#Dataframe stores data in table format like in rows and columns just similar toh sql and Excel tables.

data = {
    'Name' : ['Aman', 'Riya', 'Kabir', 'Neha', 'Arjun', 'Sara'],
    'Age': [21, 22, 20, 23, np.nan, 22],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Mumbai', None],
    'Marks': [85, 90, 78, 92, 88, np.nan],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT']
}

#inspecting methods 