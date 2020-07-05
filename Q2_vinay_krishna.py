
# coding: utf-8

# In[2]:


import pandas as pd
dataf = pd.read_csv("C:/Users/vinay krishna/Downloads/stats - stats.csv")


# In[3]:


dataf


# In[21]:


dataf = dataf.groupby(['Player']).agg('sum')
dataf


# In[22]:



#Top 10 Players by FT%, PTS, AST, 2P%, 3P%.(All time)

df = dataf
df.sort_values(["FT%", "PTS","AST","2P%","3P%"],ascending=False)[:10]


# In[55]:


dataf = pd.read_csv("C:/Users/vinay krishna/Downloads/stats - stats.csv")
apd = dataf.groupby(['Tm']).agg('sum')

#Q Team with the highest 3PT%
apd
apd.sort_values(["3P%"],ascending=False)
# ANS: Team = "TOT"




# In[56]:


dataf = pd.read_csv("C:/Users/vinay krishna/Downloads/stats - stats.csv")
apd = dataf.groupby(['Tm']).agg('sum')

#Q Team with the highest 3PT%
apd
apd.sort_values(["2P%"],ascending=False)
# ANS: Team = "TOT"



