import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title("Estatísticas de filmes")

    if len(movie_stats["total_by_genre"]) > 0:
        fig = px.pie(
            movie_stats["total_by_genre"],
            values="count",
            names="genre__name",
            title="Filmes por gênero",
        )
        st.plotly_chart(fig)

    st.subheader("Filmes cadastrados")
    st.write(movie_stats["total_movies"])

    st.subheader("Total de filmes por gênero")
    for genre in movie_stats["total_by_genre"]:
        st.write(f"{genre["genre__name"]}: {genre["count"]}")

    st.subheader("Avaliações cadastradas")
    st.write(movie_stats["total_reviews"])

    st.subheader("Média das avaliações cadastradas")
    st.write(movie_stats["average_stars"])
