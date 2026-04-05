import pandas as pd
import numpy as np
from parallel_processor import parallel_similarity

def load_data():
    movies=pd.read_csv("movies.csv")
    ratings=pd.read_csv("ratings.csv")
    return movies,ratings

def create_matrix(ratings):
    return ratings.pivot_table(index='userId',columns='movieId',values='rating').fillna(0)

def sequential_similarity(matrix):
    norm=np.linalg.norm(matrix,axis=1)
    return np.dot(matrix,matrix.T)/(norm[:,None]*norm[None,:]+1e-9)

def get_recommendations(movie_name,use_parallel=True):
    movies,ratings=load_data()
    matrix=create_matrix(ratings)

    match=movies[movies['title'].str.contains(movie_name,case=False,na=False)]
    if match.empty:
        return [],0

    movie_id=match.iloc[0]['movieId']
    movie_matrix=matrix.T.values

    import time
    start=time.time()

    if use_parallel:
        similarity=parallel_similarity(movie_matrix)
    else:
        similarity=sequential_similarity(movie_matrix)

    exec_time=time.time()-start

    movie_index=list(matrix.columns).index(movie_id)
    scores=list(enumerate(similarity[movie_index]))
    scores=sorted(scores,key=lambda x:x[1],reverse=True)[1:6]

    rec_ids=[matrix.columns[i[0]] for i in scores]
    rec_movies=movies[movies['movieId'].isin(rec_ids)]['title'].tolist()

    return rec_movies,exec_time
