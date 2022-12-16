import streamlit as st
import constants as const
from script.utils import movie_link, fetch_poster


def description_table (cfg): 
    with st.expander(cfg["title"]):
        st.markdown(cfg["description"])

def initialize_movie_widget():
    movie_cols = st.columns(const.MOVIE_NUMBER)
    for c in movie_cols:
        with c:
            st.empty() 

    return movie_cols


def show_recommended_movie_info(recommended_movies, movie_cols, show_score):
    movie_ids = recommended_movies["movieId"]
    movie_titles = recommended_movies["title"]
    movie_scores = recommended_movies["score"]
    posters = [fetch_poster(i) for i in movie_ids]
    links = [movie_link(i) for i in movie_ids]
    be1 = const.MOVIE_NUMBER
    be2 = const.MOVIE_NUMBER*2
    be3 = const.MOVIE_NUMBER*3
    for c, t, s, p, l in zip(movie_cols[0], movie_titles[0:be1], movie_scores[0:be1], posters[0:be1], links[0:be1]):
        with c:
            st.image(p)
            st.markdown(f"<a style='display: block; text-align: center;' href='{l}'>{t}</a>", unsafe_allow_html=True)
            if show_score:
                st.write(round(s, 3))
    for c, t, s, p, l in zip(movie_cols[1], movie_titles[be1:be2], movie_scores[be1:be2], posters[be1:be2], links[be1:be2]):
        with c:
            st.image(p)
            st.markdown(f"<a style='display: block; text-align: center;' href='{l}'>{t}</a>", unsafe_allow_html=True)
            if show_score:
                st.write(round(s, 3))
    # for c, t, s, p, l in zip(movie_cols[2], movie_titles[be2:be3], movie_scores[be2:be3], posters[be2:be3], links[be2:be3]):
    #     with c:
    #         st.image(p)
    #         st.markdown(f"<a style='display: block; text-align: center;' href='{l}'>{t}</a>", unsafe_allow_html=True)
    #         if show_score:
    #             st.write(round(s, 3))
                
def show_score_base_info(recommended_movies, movie_cols, show_score):
    movie_ids = recommended_movies["movieId"]
    movie_titles = recommended_movies["title"]
    movie_scores = recommended_movies["score"]
    posters = [fetch_poster(i) for i in movie_ids]
    links = [movie_link(i) for i in movie_ids]
    for c, t, s, p, l in zip(movie_cols, movie_titles, movie_scores, posters, links):
        with c:
            st.image(p)
            st.markdown(f"<a style='display: block; text-align: center;' href='{l}'>{t}</a>", unsafe_allow_html=True)
            if show_score:
                st.write(round(s, 3))
                