# -*- coding: utf-8 -*-
"""Linear regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16zpLoKfkYr3sx_FVJc7-N2evoH0taF6c

Linear Equation prediction
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

from google.colab import files
uploded=files.upload()

df=pd.read_csv("Linear Regression - Single variable.csv")
df.head()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel('area(sqr ft)')
plt.ylabel('price(US$)')
plt.scatter(df.area,df.price,color="red",marker="+")
plt.plot(df.area,reg.predict(df[['area']]),color='blue')

reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)

reg.predict([[3300]])

reg.coef_

reg.intercept_

from google.colab import files
uploded=files.upload()

ar = pd.read_csv("area.csv")
ar

p=reg.predict(ar)

ar['prices'] = p
ar

"""Linear Regression - Multiple Variable"""

pip install word2number

import word2number

url="https://raw.githubusercontent.com/codebasics/py/master/ML/2_linear_reg_multivariate/Exercise/hiring.csv"
ex2=pd.read_csv(url)
ex2

ex=ex2.rename(columns={ 'test_score(out of 10)':'test_score', 'interview_score(out of 10)':'interview_score', 'salary($)':'salary'}, inplace= False)

ex['experience'] = ex['experience'].fillna('zero')
ex.experience = ex.experience.apply(w2n.word_to_num)
ex

m=ex.test_score.median()
ex['test_score'] = ex['test_score'].fillna(m)
ex

reg1 = linear_model.LinearRegression()
reg1.fit(ex[['experience','test_score','interview_score']],ex.salary)

plt.scatter(ex.experience,ex.test_score,ex.interview_score,ex.salary)

reg1.predict([[2,9,6]])

reg1.predict([[12,10,10]])