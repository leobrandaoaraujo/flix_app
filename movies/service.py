import streamlit as st
from movies.repository import MovieRepository


class MovieService:
    def __init__(self):
        self.__movie_repository = MovieRepository()

    def get_movies(self):
        if "movies" in st.session_state:
            return st.session_state.movies
        movies = self.__movie_repository.get_movies()
        st.session_state.movies = movies
        return movies

    def create_movie(self, title, genre, release_date, actors, resume):
        movie = dict(
            title=title,
            genre=genre,
            release_date=release_date,
            actors=actors,
            resume=resume,
        )
        new_movie = self.__movie_repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        return self.__movie_repository.get_movie_stats()
