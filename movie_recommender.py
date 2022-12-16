import pickle
import streamlit as st
import streamlit.components.v1 as components
from script.recommender import contend_based_recommendations, weighted_average_based_recommendations, contend_based_recommendations_extra
from config import score_based_cfg, content_based_cfg, content_extra_based_cfg
from UI.widgets import initialize_movie_widget, show_recommended_movie_info, show_score_base_info,description_table
import constants as const
st.set_page_config(page_title="Recommender system", layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with open('data/movie_df.pickle', 'rb') as handle:
    movie = pickle.load(handle)

st.markdown('# Movie Recommender system')
st.text("")
st.text("")
st.text("")
st.text("")

main_layout,search_layout = st.columns([10,1])
options = main_layout.multiselect('Which movies do you like?', movie["title"].unique())
recommendation_type = main_layout.radio("",["Score Based","Content Based","Content Based (more Features)"], horizontal=True)
show_recommended_movies = search_layout.button("search")

# recommended_movie_num = st.sidebar.slider("Recommended movie number", min_value=5, max_value=10)
# if recommended_movie_num:
#     const.MOVIE_NUMBER = recommended_movie_num
show_score = True

if recommendation_type == "Score Based":
    description_table(score_based_cfg)
    score_based_recommended_movies = weighted_average_based_recommendations()
    c1 = initialize_movie_widget()
    c2 = initialize_movie_widget()
    col_for_score_based = c1,c2
    show_recommended_movie_info(score_based_recommended_movies, col_for_score_based, show_score)

if recommendation_type == "Content Based":
    contend_based_recommended_movies = contend_based_recommendations(movie, options)
    description_table(content_based_cfg)
    if(not contend_based_recommended_movies.empty):
        c1 = initialize_movie_widget()
        c2 = initialize_movie_widget()
        # c3 = initialize_movie_widget()
        col_for_content_based = c1,c2
        show_recommended_movie_info(contend_based_recommended_movies, col_for_content_based, show_score)
if recommendation_type == "Content Based (more Features)":
    contend_extra_based_recommended_movies = contend_based_recommendations_extra(movie, options)
    description_table(content_extra_based_cfg)
    if(not contend_extra_based_recommended_movies.empty): 
        c1 = initialize_movie_widget()
        c2 = initialize_movie_widget()
        # c3 = initialize_movie_widget()
        col_for_content_based_extra = c1,c2
        show_recommended_movie_info(contend_extra_based_recommended_movies, col_for_content_based_extra, show_score)
