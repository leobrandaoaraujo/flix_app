import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from movies.service import MovieService
from reviews.service import ReviewService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write("Lista de avaliações")
        AgGrid(
            data=pd.json_normalize(reviews).drop(columns=["movie"]),
            key="reviews_grid",
        )
    else:
        st.warning("Nenhuma avalização cadastrada!")

    st.title("Cadastrar nova")
    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie["title"]: movie["id"] for movie in movies}
    movie = st.selectbox(label="Filme", options=list(movie_titles.keys()))
    stars = st.number_input(
        label="Número de estrelas", min_value=0, max_value=5, step=1
    )
    comment = st.text_area("Comentários")
    if st.button("Cadastrar"):
        new_review = review_service.create_review(
            movie=movie_titles[movie],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error(f'Erro ao cadastrar a avaliação do filme "{movie}"!')
