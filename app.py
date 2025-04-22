import streamlit as st
from home.page import show_home
from actors.page import show_actors
from genres.page import show_genres
from login.page import show_login
from movies.page import show_movies
from reviews.page import show_reviews


def main():
    if "token" not in st.session_state:
        show_login()
    else:
        st.title("Flix App")

        menu_options = st.sidebar.selectbox(
            "Selecione uma opção",
            ["Início", "Gêneros", "Atores", "Filmes", "Avaliações"],
        )

        if menu_options == "Início":
            show_home()

        if menu_options == "Gêneros":
            show_genres()

        if menu_options == "Atores":
            show_actors()

        if menu_options == "Filmes":
            show_movies()

        if menu_options == "Avaliações":
            show_reviews()


if __name__ == "__main__":
    main()
