{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4caed39a-86bb-43d3-9306-de1cec0533cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# movies.csv\n",
    "url = 'https://drive.google.com/file/d/1EknR8ceW4HEkjW-41F4z_IVku0RZERWH/view?usp=sharing' \n",
    "path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]\n",
    "movies = pd.read_csv(path)\n",
    "\n",
    "# 'ratings.csv'\n",
    "url = 'https://drive.google.com/file/d/1IdcUbfqlIIY0djoAtTKEDXhL6TCXyCoG/view?usp=sharing' \n",
    "path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]\n",
    "ratings = pd.read_csv(path) \n",
    "\n",
    "ratings_movies = ratings_df.groupby('movieId')[['movieId', 'rating', 'userId']].agg({\"userId\":\"count\", \"rating\":\"mean\"})\n",
    "ratings_movies = ratings_movies.reset_index()\n",
    "\n",
    "ratings_movies = ratings_movies.merge(movies_df, left_on='movieId', right_on='movieId')\n",
    "ratings_movies.pop('genres')\n",
    "\n",
    "ratings_movies = ratings_movies[['movieId', 'title', 'userId', 'rating']]\n",
    "ratings_movies = ratings_movies.rename(columns={\n",
    "    'userId':'Total Reviews',\n",
    "    'title':'Title',\n",
    "    'rating':'Rating'\n",
    "})\n",
    "\n",
    "ratings_movies_top_20_popular = ratings_movies.nlargest(20, 'Total Reviews').sort_values(by='Rating', ascending=False)\n",
    "char_20_rating = ratings_movies_top_20_popular[['Title', 'Rating']].plot(kind='bar', x='Title');\n",
    "char_20_reviews = ratings_movies_top_20_popular[['Title', 'Total Reviews']].plot(kind='bar', x='Title');\n",
    "\n",
    "st.header('Most Popular Movies')\n",
    "st.dataframe(ratings_movies_top_20_popular[['Title', 'Total Reviews', 'Rating']], use_container_width=True)\n",
    "\n",
    "st.bar_chart(data=ratings_movies_top_20_popular, x='Title', y='Total Reviews')\n",
    "st.bar_chart(data=ratings_movies_top_20_popular, x='Title', y='Rating')\n",
    "st.header('HOLAAAA')\n",
    "\n",
    "ratings_movies['year'] = ratings_movies.title.str[-6:]\n",
    "ratings_movies['year'] = ratings_movies.year.str.strip('()')\n",
    "\n",
    "st.bar_chart(data=ratings_movies, x='year', y='Title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0fea93a7-a912-4d43-af34-e507c0aa14e9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ade296c3-ce94-42b5-b4f5-2fe5b4f20e9e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
