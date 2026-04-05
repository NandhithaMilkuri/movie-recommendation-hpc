import streamlit as st
from recommender import get_recommendations
import matplotlib.pyplot as plt

st.set_page_config(page_title="HPC Movie Recommender",layout="centered")

st.title("🎬 HPC Movie Recommendation System")

movie=st.text_input("Enter Movie Name")

if st.button("Recommend"):
    if movie:
        rec_p,par_time=get_recommendations(movie,True)
        rec_s,seq_time=get_recommendations(movie,False)

        st.subheader("🎥 Recommended Movies")
        for m in rec_p:
            st.write("👉",m)

        st.subheader("⚡ Performance Comparison")
        st.write(f"Parallel Time: {par_time:.4f} sec")
        st.write(f"Sequential Time: {seq_time:.4f} sec")

        fig,ax=plt.subplots()
        ax.bar(["Sequential","Parallel"],[seq_time,par_time])
        ax.set_ylabel("Time (seconds)")
        st.pyplot(fig)
    else:
        st.warning("Please enter a movie name")
