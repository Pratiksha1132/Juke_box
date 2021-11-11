import streamlit as st
import data_store
import data_read
side_box = st.sidebar.selectbox("Please select your choice", ("upload", "available songs", "listen", "delete", "update"))
if side_box == "upload":
    with st.form("audio_store"):
        name = st.text_input("Please enter the name of the song")
        uploaded_audio = st.file_uploader("Please put the mp3 file here", type="mp3")
        audio_submit = st.form_submit_button("submit")

        if audio_submit:
            bytes_data = uploaded_audio.getvalue()

            st.write(type(bytes_data))
            data_store.store_audio(name, bytes_data)

elif side_box == "available songs":
    with st.form("playlist"):
        name = st.text_input("Please enter the song name")

        playlist_submit = st.form_submit_button("Submit")

        if playlist_submit:
            data = data_read.display_data(name)
            st.write(data)
elif side_box == "listen":
    with st.form("form_id"):
        id = st.number_input("Enter the id of the song")

        submit_id = st.form_submit_button("submit")

        if submit_id:
            audio = data_read.play_song(id)
            st.audio(audio[0], format="audio/mp3")

