import streamlit as st

st.title("Example projects")

chess, reddit, reference = st.tabs(['Chess Openings', 'Reddit CI Comparison', 'Quick Reference Guide'])

with chess:
    st.markdown("You can put descriptive text here")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.subheader("Select Options")
        mmlp = st.slider("Minimum Move-Link Percentage",
                         min_value=0,
                         max_value=2,
                         step=1)
        elo = st.slider("ELO Mean",
                        min_value=900,
                        max_value=2700,
                        step=300)
        gl = st.slider("Game Length",
                       min_value=10,
                       max_value=220,
                       step=30)
        delo = st.slider("Difference in ELO",
                         min_value=0,
                         max_value=1000,
                         step=100)
        higherelo = st.radio("Higher ELO",
                             ('White', 'Black', 'Either'))
        type = st.multiselect("Game Type", ["classical", "Bullet", "Blitz"])

    with col2:
        st.write("your plot goes here")

with reddit:
    st.markdown("More descriptive text")

    st.selectbox("Pick a subreddit",
                 options=['a', 'whole', 'list', 'of', 'options'])
    st.write('plot goes here')

with reference:
    st.markdown("You get the idea by now")
