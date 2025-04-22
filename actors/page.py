import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write("Lista de atores/atrizes")

        AgGrid(
            data=pd.json_normalize(actors),
            key="actors_grid",
        )
    else:
        st.warning("Nenhum ator/atriz cadastrado!")

    st.title("Cadastrar novo")
    name = st.text_input("Nome")
    nationality_choices = [
        "BRA",
        "EUA",
        "ENG",
        "GER",
        "AUS",
        "AUT",
        "MEX",
        "CHN",
        "COL",
        "NZL",
        "ESP",
        "CAN",
        "ZAF",
        "GBR",
        "IRL",
        "ITA",
        "PRT",
    ]
    nationality = st.selectbox(label="Nacionalidade", options=nationality_choices)
    if st.button("Cadastrar"):
        new_actor = actor_service.create_actor(name=name, nationality=nationality)
        if new_actor:
            st.rerun()
        else:
            st.error(f'Erro ao cadastrar o ator/atriz "{name}"!')
