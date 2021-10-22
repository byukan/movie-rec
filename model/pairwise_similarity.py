#!/usr/bin/env python
# coding: utf-8

# # Calculating Similarity
# 
# create some transformer embedded vectors, then use a cosine similarity

# In[2]:


import h
import pandas as pd
# pd.set_option('display.max_colwidth', None)
# use movies dataset
df = pd.read_csv('../data/imdb_top_1000.csv')#.head(10)
# df[['Series_Title', 'Overview']].head(10)


# In[ ]:





# In[ ]:


# sentences = df['Overview']
# h.compute_similarity(0, sentences)


# In[ ]:


df['similar_movies'] = pd.Series(df.index).apply(lambda x: h.compute_similarity(x, df['Overview']))
# df['similar_movies']


# In[ ]:





# In[ ]:





# In[ ]:


import pickle
with open('similar_movies_df.p', 'wb') as fh:
    pickle.dump(df, fh)
# pickle.load(open('similar_movies_df.p', 'rb'))

