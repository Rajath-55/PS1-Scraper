#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# In[20]:


df = pd.read_csv('stationlist.csv')
file = open('list.txt', 'r+')
stuff = {}
visited = {}
count = 0
for line in file.readlines():
    count+=1
    stuff[line.strip('\n')] = count
    visited[line.strip('\n')] = False
df.columns
df = df.drop(columns = ['Stipend (UG)', 'Stipend (PG)', 'Have Accommodation?'])

for index, row in df.iterrows():
    row['Facilities (Raw)'] = ''.join(row['Facilities (Raw)'].strip('\n').split(' '))
df


# In[21]:


for index, row in df.iterrows():
    print(row['Preferred Branches'].split(','))
    
        
    
stuff


# In[22]:


matching_ones = []


for index, row in df.iterrows():
    station_name = row['Company Name']
#     print(station_name)
    station_pref = row['Preferred Branches'].split(",")
    for line, rank in stuff.items():
        temp = []
        if fuzz.partial_ratio(line, station_name) > 90 and visited[line] == False:
            temp.append(stuff[line])
            visited[line] = True
            for col in row:
                temp.append(col)    
            matching_ones.append(temp)
                
            
        
    
            
            
matching_ones 


# In[23]:


df_1 = pd.DataFrame(matching_ones)
df_1.columns = ['Rank','Station ID', 'Company Name', 'Location', 'Domain', 'Branch Preferences', 'Facilities', 'Projects']


# In[24]:


df_1


# In[25]:


df_1 = df_1.sort_values('Rank')
df_1


# In[26]:


df_1.to_csv('govind_list.csv')


# In[27]:


df_1


# In[ ]:




