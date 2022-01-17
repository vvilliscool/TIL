#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import math
from scipy.stats import *
import scipy as sp

# Jupyter Notebook의 출력을 소수점 이하 3자리로 제한
get_ipython().run_line_magic('precision', '3')
# Dataframe의 출력을 소수점 이하 3자리로 제한
pd.set_option('precision', 3)


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# 참고사이트
# https://docs.scipy.org/doc/scipy/reference/stats.html
# https://numpy.org/doc/stable/reference/routines.statistics.html
# https://docs.python.org/ko/3/library/math.html#number-theoretic-and-representation-functions

# # 산술평균

# In[3]:


x=[1,2,3,4,5]

np.array(x).mean()
pd.Series(x).mean()


# In[4]:


df = pd.read_csv('../data/ch2_scores_em.csv', index_col='student number')


# In[5]:


df.head()


# In[6]:


df.shape        #df의 크기


# In[7]:


#영어 과목의 평균 계산
sum(df['english']) / len(df['english'])


# In[8]:


np.mean(df['english'])


# In[9]:


df['english'].mean()


# In[10]:


sp.mean(df['english'])


# # 기하평균

# - n개의 양수값을 모두 곱한것의 n 제곱근
# - 성장률의 평균

# In[11]:


data = [2,8,3]
math.prod(data)**(1/len(data))


# In[12]:


#scipy.stats,gmean 이용해 기하평균 계산
gmean(data)


# # 조화평균
# 비율 및 변화율의 평균

# In[14]:


data = np.array([80,120])
len(data)/np.sum(1/data)


# In[15]:


# scipy.stat.hmean 이용해 조화평균 계산
hmean(data)


# In[16]:


# 가중평균 np.average( , axis, weights) 이용
np.average(np.arange(1,5))
np.average(np.arange(1,11),weights = np.arange(10,0,-1))


# In[17]:


scores = np.array(df['english'])
scores


# In[18]:


# 순서통계량
sorted_scores = np.sort(scores)
sorted_scores


# In[22]:


# median 계산식
n = len(sorted_scores)
if n %2 == 0:
    x1=sorted_scores[n//2-1]
    x2=sorted_scores[n//2]
    median = (x1+x2)/2
else:
    meidan = sorted_scores[(n+1)//2-1]
    
median


# In[23]:


sorted_scores[24], sorted_scores[25]


# In[25]:


np.median(scores)


# In[26]:


df['english'].median()


# # 절사평균
# 최고점과 최저점을 제외한 나머지 점수의 평균

# In[31]:


np.random.seed(3)
income = np.random.normal(2000000,500000,100)
income[:10]


# In[32]:


np.mean(income)


# In[33]:


income = np.append(income, 10**9)
np.mean(income)


# In[35]:


# 절사평균
#scipy.stats.trim_mean
trim_mean(income, 0.2)


# # 최빈값(mode)

# 범주형 데이터일때

# In[37]:


np.random.seed(3)
data = np.random.choice(['A','B','C'], 1000)
# A,B,C 요소로 이루어진 데이터

data[:10]
len(data)


# In[38]:


# scipy.stats.mode 최빈값
mode(data)


# In[39]:


# 최빈값
mode(data).mode


# In[40]:


#최빈값의 빈도
mode(data).count


# In[41]:


pd.Series(data).value_counts()


# In[43]:


pd.Series(data).value_counts().index[0]
pd.Series(data).value_counts()[0]


# In[44]:


np.random.seed(1123)
data = np.random.normal(100, 20, size = 1000)
data[:10]


# In[45]:


sorted(data)[0], sorted(data)[-1]


# In[46]:


np.min(data), np.max(data)


# ## np.quantile 4분위수, 백분위수 계산

# In[48]:


# 제1사분위 수(하사분위수, Q1)
np.percentile(data, 25)


# In[49]:


# 제3사분위 수(상사분위수, Q3)
np.percentile(data, 75)


# In[50]:


# 제2사분위 수(하사분위수, Q2)
np.percentile(data, 50)


# # boxplot

# In[51]:


import matplotlib.pyplot as plt
plt.boxplot(data)


# In[52]:


describe(data)
describe(df['english'])  # 표본집단 데이터에 대한 기술통계


# In[53]:


(df['english']).describe()


# In[54]:


describe(df['english'], ddof=0) # 모집단 데이터에 대한 기술통계


# In[ ]:




