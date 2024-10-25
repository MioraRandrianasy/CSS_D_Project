#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:16:29 2024

@author: astrostudent1
"""

import pandas as pd
import numpy as np

csv_file=pd.read_csv("movie_dataset.csv")
print(csv_file.describe())
print(csv_file.columns)

#Rename of the column 
csv_file=csv_file.rename(columns={'Revenue (Millions)':'Revenue_(Millions)'})
csv_file=csv_file.rename(columns={'Runtime (Millions)':'Runtime_(Millions)'})

print(csv_file)

#filling the nan with the average
metascore_mean=csv_file['Metascore'].mean()
revenue_mean=csv_file['Revenue_(Millions)'].mean()

csv_file['Metascore']=csv_file['Metascore'].fillna(metascore_mean)
csv_file['Revenue_(Millions)']=csv_file['Revenue_(Millions)'].fillna(revenue_mean)

print(csv_file)

#1- What is the highest rated movie in the dataset? 
best_title=csv_file.loc[csv_file['Rating'].idxmax(), 'Title']
print('The highest rated movie in the dataset is', best_title)

#2- What is the average revenue of all movies in the dataset? 
print('The average revenue of all movies in the dataset', revenue_mean)

#3- What is the average revenue of movies from 2015 to 2017 in the dataset?
filtered=csv_file[(csv_file['Year'] >= 2015) & (csv_file['Year'] <= 2017)]
average_revenue= filtered['Revenue_(Millions)'].mean()
print('The average revenue of movies from 2015 to 2017 in the dataset is', average_revenue)

#4- How many movies were released in the year 2016? 
movies_2016=csv_file[csv_file['Year'] == 2016]
num_movies_2016=len(movies_2016)
print('the mumber of movies were released in the year 2016 is', num_movies_2016)

#5- How many movies were directed by Christopher Nolan? 
nolan_films=csv_file[csv_file['Director'] == 'Christopher Nolan']
num_nolan_films=len(nolan_films)
print('The number of movies were directed by Christopher Nolan is ', num_nolan_films)

#6- How many movies in the dataset have a rating of at least 8.0?
num_high_rated_movies = np.sum(np.where(csv_file['Rating'] >= 8.0, 1, 0))
'''1 is for true that means at least 8.0 and 0 is for the other'''
print('The number of movies in the dataset have a rating of at least 8.0 is', num_high_rated_movies)

#7- What is the median rating of movies directed by Christopher Nolan? 
median_rating=nolan_films['Rating'].median()
print('The median rating of movies directed by Christopher Nolan is ', median_rating)

#8- Find the year with the highest average rating?
year_avg_ratings=csv_file.groupby('Year')['Rating'].mean()
best_year = year_avg_ratings.idxmax()
print('The year with the highest average rating is',best_year)

#9- What is the percentage increase in number of movies made between 2006 and 2016? 
year_counts=csv_file['Year'].value_counts().sort_index()
total_2006=year_counts.get(2006, 0)
total_2016=year_counts.get(2016, 0)
percent_increase=((total_2016 - total_2006) / total_2006) * 100
print('The percentage increase in number of movies made between 2006 and 2016 is ',percent_increase )

#10- Find the most common actor in all the movies?
all_actors=csv_file['Actors'].str.split(', ').explode().tolist()
actor_counts={}
for actor in all_actors:
    actor_counts[actor]=actor_counts.get(actor, 0) + 1
max_appearances=max(actor_counts.values())
most_common_actor=next(actor for actor, count in actor_counts.items() if count == max_appearances)
print('The most common actor in all the movies is', most_common_actor )

#11- How many unique genres are there in the dataset?
all_genres=csv_file['Genre'].str.split(',').explode().tolist()
unique_genres=len(set(all_genres))
print('The number of unique genres are there in the dataset is', unique_genres)