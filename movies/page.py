import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
from movies.service import MovieService
from actors.service import ActorService
from genres.service import GenreService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write("Lista de filmes")
        AgGrid(
            data=pd.json_normalize(movies).drop(columns=["actors", "genre.id"]),
            key="movies_grid",
        )
    else:
        st.warning("Nenhum filme cadastrado!")

    st.title("Cadastrar novo")
    title = st.text_input("Título")
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre["name"]: genre["id"] for genre in genres}
    genre = st.selectbox(label="Gênero", options=list(genre_names.keys()))
    release_date = st.date_input(
        label="Data de lançamento",
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format="DD/MM/YYYY",
    )
    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor["name"]: actor["id"] for actor in actors}
    actors_selected = st.multiselect(label="Elenco", options=list(actor_names.keys()))
    actors = [actor_names[name] for name in actors_selected]
    resume = st.text_area("Resumo")

    if st.button("Cadastrar"):
        new_movie = movie_service.create_movie(
            title=title,
            genre=genre_names[genre],
            release_date=release_date,
            actors=actors,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error(f'Erro ao cadastrar o filme "{title}"!')
