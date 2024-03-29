import streamlit as st

import utils as ut

IMAGE_ADDRESS = "https://res.cloudinary.com/de6ptp3ms/image/upload/emmcxw01kmoe6kyqzpls"

if 'lang' not in st.session_state:
    st.session_state.lang = "en"


with st.sidebar:
    option = st.selectbox("Please select a language",("English", "Spanish"))
    if option == "Spanish":
        st.session_state.lang = "sp"
    elif option == "English":
        st.session_state.lang = "en"

# set the title
st.title(ut.translate("sent1", st.session_state.lang))

# set image
st.image(IMAGE_ADDRESS, caption = "Eczema")