import streamlit as st
from actors.repository import ActorRepository


class ActorService:
    def __init__(self):
        self.__actor_repository = ActorRepository()

    def get_actors(self):
        if "actors" in st.session_state:
            return st.session_state.actors
        actors = self.__actor_repository.get_actors()
        st.session_state.actors = actors
        return actors

    def create_actor(self, name, nationality):
        actor = dict(name=name, nationality=nationality)
        new_actor = self.__actor_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor
