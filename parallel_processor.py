import numpy as np
from multiprocessing import Pool,cpu_count

def cosine_similarity_chunk(args):
    chunk,full_matrix=args
    norm_full=np.linalg.norm(full_matrix,axis=1)
    norm_chunk=np.linalg.norm(chunk,axis=1)
    sim=np.dot(chunk,full_matrix.T)/(norm_chunk[:,None]*norm_full[None,:]+1e-9)
    return sim

def parallel_similarity(matrix):
    processes=cpu_count()
    chunks=np.array_split(matrix,processes)
    with Pool(processes) as pool:
        results=pool.map(cosine_similarity_chunk,[(c,matrix)for c in chunks])
    return np.vstack(results)
