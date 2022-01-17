#!/usr/bin/env python
# coding: utf-8

# # 변이통계량    (산포도)

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import *


# In[2]:


import numpy as np
# numpy float 출력옵션 변경
# np.set_printoptions(precision=3)
# np.set_printoptions(precision=20, suppress=True)
# pd.options.display.float_format = '{:.2f}'.format
np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.3f}".format(x)})


# In[3]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# ## 범위

# In[6]:


np.random.seed(123)
data = np.random.normal(100,20,size=1000)
data[:10]


# In[7]:


np.min(data), np.max(data)


# In[8]:


# 범위 = 최댓값 - 최솟값
np.max(data)-np.min(data)


# In[9]:


# np.ptp() 이용
np.ptp(data)


# ## 중간범위

# In[10]:


(np.max(data)+np.min(data))/2


# ## 사분위간 범위

# In[11]:


#np.quantile() 이용해 IQR 계산
np.quantile(data,0.75)-np.quantile(data,0.25)


# In[12]:


# scipy.stats.iqr 이용
iqr(data)


# ## 사분위수 편차

# In[13]:


#numpy.quantile 이용
(np.quantile(data, 0.75)-np.quantile(data, 0.25))/2


# In[14]:


#scipy.stats.iqr이용
iqr(data)/2


# ## 편차
# 자료값과 평균과의 차이

# In[15]:


data-np.mean(data)


# In[16]:


# 편차의 합은 항상 0
(data-np.mean(data)).sum()


# ## 분산
# - 데이터와 평균과의 차이를 제곱하여 합한 값의 평균
#     - 모분산 : n으로 나누어줌
#     - 표본분산 : n-1로 나누어줌

# In[ ]:


# 분산 계산 var(a, ddof=0) 함수
ddof 인수:
    기본값은 0 ==> 모집단 분산
    표본분산의 경우 1


# In[18]:


x = [1,2,3,4,5]
# 표본분산
np.var(x, ddof=1)

# 모분산
np.var(x)

np.array(x).var()

pd.Series(x).var(ddof=0)


# ## 표준편차

# In[19]:


# std 함수 사용

x = [1,2,3,4,5]

# 표본표준편차(S)
np.std(x, ddof=1)

# 모표준편차(sigma)
np.std(x)

np.array(x).std()

pd.Series(x).std(ddof=0)


# ## 변동계수(CV)
# - 상대표준편차
# - 표본표준편차를 표본평균으로 나눈 값(또는 100을 곱한 값)
# - 서로다른 평균과 표준편차를 갖는 여러데이터의 ~~~~

# In[20]:


#변동계수 계산
men=[72,74,77,68,66,75]
women=[45,48,52,53,46,50]

print('평균')
np.mean(men)
np.mean(women)

print('표본표준편차')
np.std(men, ddof=1)
np.std(women, ddof=1)


# In[21]:


print('남자CV : ', np.std(men, ddof=1)/np.mean(men))
print('여자CV : ', np.std(women, ddof=1)/np.mean(women))


# In[22]:


#scipy.stats.variation
print('남자CV : ',variation(men))
print('여자CV : ', variation(women))


# ## 표준화 scaling

# In[23]:


df = pd.read_csv('../data/ch2_scores_em.csv', index_col='student number')
df.head()


# In[24]:


df['english'].describe()


# In[25]:


df['mathematics'].describe()


# In[26]:


df.describe()


# In[27]:


# Z-scaling : 평균이 0, 표준편차가 1
z1 = (df['english']-df['english'].mean())/df['english'].std()
z2 = (df['mathematics']-df['mathematics'].mean())/df['mathematics'].std()

print(z1.min(), z1.max())
print(z2.min(), z2.max())
# -3 ~ 3 사이의 값으로 분포됨


# In[28]:


z1.mean(), z1.std()


# In[30]:


# min-max scaling : 0~1 사이의 값으로 변환

s1 = (df['english']-df['english'].min())/(df['english'].max()-df['english'].min())
s2 = (df['mathematics']-df['mathematics'].min())/(df['mathematics'].max()-df['mathematics'].min())

print('english :',s1.min(), s1.max())
print('mathematics :',s2.min(), s2.max())


# In[35]:


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
S= scaler.fit_transform(df)
pd.DataFrame(S, columns= df.columns, index=df.index).head()


# ## 왜도(skewness)
# 데이터의 비대칭도
# - 대표값을 중심으로 좌우의 모양이 대칭적인가 아닌가를 측정
# - 0에 가까우면 좌우대칭
# - 왜도가 음수로 나타나면 오른쪽으로 치우친 분포(왼쪽 꼬리분포)
# - 평균 < 중앙값 < 최빈값    : 왜도 <0
# - 최빈값 < 중앙값 < 평균    : 왜도 >0
# - 
# - 왜도의 절대값이 1.5이상이면 많이 치우친 것

# In[37]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#오른쪽으로 꼬리가 긴 분포 (right skwed, positive)
x1 = [1]*30+[2]*20+[3]*20+[4]*15+[5]*15

# 좌우대칭 분포
x2 = [1]*15+[2]*20+[3]*30+[4]*20+[5]*15

#왼쪽으로 꼬리가 긴 분포 (left skwed, negative)
x3 = [1]*15+[2]*15+[3]*20+[4]*20+[5]*30


# In[38]:


x1[:10]


# In[40]:


pd.Series(x1).value_counts(sort=False)


# In[41]:


pd.Series(x1).value_counts(sort=False).plot(kind='bar')


# In[42]:


pd.Series(x2).value_counts(sort=False).plot(kind='bar')


# In[43]:


pd.Series(x3).value_counts(sort=False).plot(kind='bar')


# In[44]:


print(' 오른쪽으로 꼬리가 긴 분포의 왜도', skew(x1))
print(' 좌우대칭 분포의 왜도', skew(x2))
print(' 왼쪽으로 꼬리가 긴 분포의 왜도', skew(x3))


# ## 첨도 : 뾰족한 정도
# 기준 : 3

# In[51]:


#좌우대칭 분포(정규분포와 유사)
x1 = [1]*10+[2]*20+[3]*40+[4]*20+[5]*10

# 균일 분포(uniform dist)
x2 = [1]*20+[2]*20+[3]*20+[4]*20+[5]*20

#뾰족한 분포
x3 = [1]*5+[2]*15+[3]*60+[4]*15+[5]*5


# In[52]:


pd.Series(x1).value_counts(sort=False).plot(kind='bar')


# In[53]:


pd.Series(x2).value_counts(sort=False).plot(kind='bar')


# In[54]:


pd.Series(x3).value_counts(sort=False).plot(kind='bar')


# In[55]:


print(' 조금 뽀족할때 첨도', kurtosis(x1))
print(' 전혀 뾰족하지 않을때 (평평할때) 첨도', kurtosis(x2))
print(' 매우 뾰족할때 첨도', kurtosis(x3))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




