import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write("Lista de gêneros")

        AgGrid(
            data=pd.json_normalize(genres),
            key="genres_grid",
        )
    else:
        st.warning("Nenhum gênero cadastrado!")

    st.title("Cadastrar novo")
    name = st.text_input("Nome")
    if st.button("Cadastrar"):
        new_genre = genre_service.create_genre(name=name)
        if new_genre:
            st.rerun()
        else:
            st.error(f'Erro ao cadastrar o gênero "{name}"!')
