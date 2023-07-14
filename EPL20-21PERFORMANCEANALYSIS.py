#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')



# In[3]:


# Load Dataset
    
epl_df= pd.read_csv('EPL_20_21.csv')
epl_df.head 


# In[4]:


epl.df(info)


# In[5]:


epl_df.info()


# In[6]:


epl_df.describe()


# In[7]:


9 epl_df.isna().sum()


# In[13]:


epl_df['MinsPerMatch']= (epl_df['Mins']/ epl_df['Matches']).astype(int)
epl_df['GoalsPerMatch'] = (epl_df['Goals'] / epl_df['Matches']).astype(float)
epl_df.head()


# In[14]:


Total_Goals=epl_df['Goals'].sum()
print(Total_Goals)


# In[16]:


Total_PenaltyGoals= epl_df['Penalty_Goals'].sum()
print(Total_PenaltyGoals)


# In[17]:


Total_Penaltyattempts= epl_df['Penalty_Attempted'].sum()
print(Total_Penaltyattempts)


# In[32]:


#Pie chart for penalty conversion rate
plt.figure(figsize=(13, 6))
Pl_not_scored = epl_df['Penalty_Attempted'].sum() - Total_PenaltyGoals
data= [Pl_not_scored, Total_PenaltyGoals]
Labels=['Penalties missed','Penalites Scored']
color = sns.color_palette('Set2')
plt.pie(data, labels = Labels, colors = color, autopct = '%.0f%%')
plt.show()


# In[33]:


#Unique Positions
epl_df['Position'].unique()


# In[34]:


# Total FW players
epl_df[epl_df['Position'] == 'FW']


# In[35]:


#Players according to Nation
 


# In[55]:


# Most players from what country
nationality = epl_df.groupby('Nationality').size().sort_values(ascending=False)
nationality.head(10).plot(kind = 'barh' , figsize=(12,6), color = sns.color_palette("magma"))
 


# In[48]:


# Most players from what country
nationality = epl_df.groupby('Nationality').size().sort_values(ascending=False)
nationality.head(15).plot(kind='barh', figsize=(12, 6), color='#000080')



# In[54]:


# Most players from what country
nationality = epl_df.groupby('Nationality').size().sort_values(ascending=False)
nationality.head(10).plot(kind='barh', figsize=(12, 6), color='#4078ff')


# In[64]:


#clubs with maximum players in squad
epl_df['Club'].value_counts().nlargest(5).plot(kind= 'bar',color=sns.color_palette("viridis"))


# In[60]:


# Clubs with maximum players in squad
epl_df['Club'].value_counts().nlargest(5).plot(kind='bar', color=sns.color_palette("viridis"))

# Set the y-axis labels to show above each bar
for i in range(len(epl_df['Club'].value_counts().nlargest(5))):
  plt.text(i, epl_df['Club'].value_counts().nlargest(5).values[i], epl_df['Club'].value_counts().nlargest(5).index[i])

# Add a title and labels to the axes
plt.title('Clubs with Maximum Players in Squad')
plt.ylabel('Number of Players')
plt.xlabel('Club')

# Show the plot
plt.show()


# In[61]:


# Clubs with maximum players in squad
epl_df['Club'].value_counts().nlargest(5).plot(kind='bar', color=sns.color_palette("viridis"))

# Set the y-axis labels to show below each bar
for i in range(len(epl_df['Club'].value_counts().nlargest(5))):
  plt.text(i, 0, epl_df['Club'].value_counts().nlargest(5).values[i], va='top')

# Add a title and labels to the axes
plt.title('Clubs with Maximum Players in Squad')
plt.ylabel('Number of Players')
plt.xlabel('Club')

# Show the plot
plt.show()



# In[ ]:





# In[62]:


# Clubs with maximum players in squad
epl_df['Club'].value_counts().nlargest(5).plot(kind='bar', color=sns.color_palette("viridis"))

# Set the y-axis labels to show above each bar
for i in range(len(epl_df['Club'].value_counts().nlargest(5))):
  plt.text(i, epl_df['Club'].value_counts().nlargest(5).values[i], epl_df['Club'].value_counts().nlargest(5).index[i], va='bottom')

# Add a title and labels to the axes
plt.title('Clubs with Maximum Players in Squad')
plt.ylabel('Number of Players')
plt.xlabel('Club')

# Show the plot
plt.show()


# In[67]:


#clubs with maximum players in squad
epl_df['Club'].value_counts().nsmallest(5)


# In[68]:


#clubs with maximum players in squad
epl_df['Club'].value_counts().nsmallest(5).plot(kind= 'bar',color=sns.color_palette("viridis"))


# In[70]:


#Average age of players in each club

plt.figure(figsize=(12,6))
sns.boxplot(x='Club', y ='Age', data =epl_df)
plt.xticks(rotation = 90)


# In[ ]:





# In[72]:


# Average age of players in each club
plt.figure(figsize=(12,6))
sns.boxplot(x='Club', y ='Age', data =epl_df)
sns.stripplot(x='Club', y ='Age', data =epl_df, color='gray', alpha=0.3)
plt.xticks(rotation = 90)

# Add a title and labels to the axes
plt.title('Average Age of Players in Each Club')
plt.ylabel('Age')
plt.xlabel('Club')

# Show the plot
plt.show()


# In[75]:


num_player =epl_df.groupby('Club').size()
data= (epl_df.groupby('Club')['Age'].sum())/num_player
data.sort_values(ascending= False)


# In[83]:


# Total Assists from each club

Assists_by_clubs= pd.DataFrame(epl_df.groupby('Club', as_index=False)['Assists'].sum())
sns.set_theme(style="whitegrid",color_codes=True)
ax= sns.barplot(x='Club',y='Assists', data=Assists_by_clubs.sort_values(by="Assists"),palette='Set2')
ax.set_xlabel("Club",fontsize=30)
ax.set_ylabel("Assists",fontsize=20)
plt.xticks(rotation=75)
plt.rcParams["figure.figsize"]=(20,8)
plt.title('Plot of Clubs vs Total assists',  fontsize=20)


# In[84]:


#TOP 10 ASSISTS
top_10_assists=epl_df[['Name', 'Club','Assists', 'Matches']].nlargest(n=10, columns = 'Assists')
top_10_assists


# In[87]:


# Total Assists from each club

Goals_by_Clubs= pd.DataFrame(epl_df.groupby('Club', as_index=False)['Goals'].sum())
sns.set_theme(style="whitegrid",color_codes=True)
ax= sns.barplot(x='Club',y='Goals', data=Goals_by_Clubs.sort_values(by="Goals"),palette='rocket')
ax.set_xlabel("Club",fontsize=30)
ax.set_ylabel("Goals",fontsize=20)
plt.xticks(rotation=75)
plt.rcParams["figure.figsize"]=(20,8)
plt.title('Plot of Clubs vs Total Goals',  fontsize=20)


# In[ ]:




