
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def load_model():
    books = pd.read_csv("dataset/Books.csv", sep=";", encoding="latin-1")
    ratings = pd.read_csv("dataset/Ratings.csv", sep=";", encoding="latin-1")
    users = pd.read_csv("dataset/Users.csv", sep=";", encoding="latin-1")

    books.rename(columns={
        "Book-Title": "title",
        "Book-Author": "author"
    }, inplace=True)

    ratings_books = ratings.merge(books, on="ISBN")

    x = ratings_books.groupby('User-ID').count()['Book-Rating'] > 200
    active_users = x[x].index

    filtered = ratings_books[ratings_books['User-ID'].isin(active_users)]

    y = filtered.groupby('title').count()['Book-Rating'] >= 50
    famous_books = y[y].index

    final = filtered[filtered['title'].isin(famous_books)]

    pt = final.pivot_table(index='title', columns='User-ID', values='Book-Rating')
    pt.fillna(0, inplace=True)

    similarity = cosine_similarity(pt)

    return pt, similarity, books

def recommend(book_name, pt, similarity, books):
    index = np.where(pt.index == book_name)[0][0]
    similar = sorted(list(enumerate(similarity[index])),
                     key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar:
        temp = books[books['title'] == pt.index[i[0]]]
        data.append(temp['title'].values[0])

    return data
