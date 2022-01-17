#!/usr/bin/env python
# coding: utf-8

# https://blog.qlik.com/third-pillar-of-mapping-data-to-visualizations-usage

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import *


# In[2]:


df = pd.read_csv('../data/ch2_scores_em.csv', index_col='student number')
df.head()


# In[3]:


# 50명의 영어 점수 array
eng = df['english']

# Series로 변환하여 describe를 표시
eng.describe()


# In[6]:


freq, _ = np.histogram(eng, bins = 10, # 막대의 갯수
            range=(0,100))
freq


# In[22]:


#0~10,10~20 .... 이라는 문자열 리스트를 작성
freq_class = [f'{i}~{i+10}' for i in range(0,100,10)]

#freq_class를 인덱스로 DataFrame을 작성
freq_dist_df = pd.DataFrame({'frequency': freq},
                            index=pd.Index(freq_class, name='class'))
freq_dist_df


# In[23]:


#계급값

class_value = [(i+(i+10))//2 for i in range(0,100,10)]
class_value


# In[24]:


#상대도수
rel_freq = freq/freq.sum()
rel_freq


# In[28]:


#누적 상대도수
cum_rel_freq = np.cumsum(rel_freq)
cum_rel_freq


# In[29]:


#도수 분포표 확장
freq_dist_df['class_value']=class_value
freq_dist_df['relative freq']=rel_freq
freq_dist_df['cum, relative freq'] = cum_rel_freq
freq_dist_df


# In[30]:


##############################################################################


# In[31]:


import pandas as pd

dataframe=pd.DataFrame({'Attendance': {0: 60, 1: 100, 2: 80,3: 78,4: 95},
                        'Obtained Marks': {0: 90, 1: 75, 2: 82, 3: 64, 4: 45}})
dataframe


# In[32]:


series = dataframe.idxmax()
series


# In[33]:


series = dataframe.idxmin()
series


# ## 도수 분포표 최빈값
#  - 빈도가 높은 계급이 계급값 반환

# In[34]:


freq_dist_df.loc[freq_dist_df['frequency'].idxmax(), 'class_value']  #65


# ### 백분위수 및 사분위수 계산

# In[35]:


x = np.arange(1,12,1)
x


# In[36]:


print(np.percentile(x, 10))  # 백분위수
print(np.quantile(x, 0.1))   # 0~1 사이의 값으로 입력


# In[37]:


print(np.percentile(x, 25))  # 25%
print(np.quantile(x, 0.25))   # 하사분위수


# In[38]:


## 히스토그램


# In[39]:


import matplotlib.pyplot as plt


# In[40]:


plt.hist(eng, bins=25, range=(0,100))
plt.show


# In[41]:


plt.hist(eng, bins=15, range=(0,100))
plt.show


# In[42]:


plt.hist(eng, bins=20, range=(0,100))
plt.show


# In[43]:


plt.boxplot(eng, labels = ['Englsih'])
plt.show()


# 1. 분포의 모양 : 왜도 - 대칭/비대칭
# 2. 이상치

# In[ ]:




