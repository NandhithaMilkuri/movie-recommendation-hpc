import time
from recommender import get_recommendations

def compare_performance(movie_name):
    # Sequential
    start=time.time()
    _,seq_time=get_recommendations(movie_name,use_parallel=False)
    total_seq=time.time()-start

    # Parallel
    start=time.time()
    _,par_time=get_recommendations(movie_name,use_parallel=True)
    total_par=time.time()-start

    print("🎬 Movie:",movie_name)
    print("Sequential Execution Time:",round(total_seq,4),"seconds")
    print("Parallel Execution Time:",round(total_par,4),"seconds")

if __name__=="__main__":
    movie=input("Enter movie name: ")
    compare_performance(movie)
