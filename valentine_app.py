import streamlit as st
import time

# Page setup
st.set_page_config(page_title="Valentine's Surprise 💖", page_icon="🌹", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .glow-button {
            background-color: #ff4b4b;
            color: white;
            font-size: 20px;
            padding: 15px;
            border-radius: 10px;
            border: none;
            box-shadow: 0px 0px 10px rgba(255, 75, 75, 1);
            transition: 0.3s;
        }
        .glow-button:hover {
            box-shadow: 0px 0px 20px rgba(255, 75, 75, 1);
            background-color: #ff7878;
        }
        .fade-in {
            animation: fadeIn 2s;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h2 style='text-align: center;'>❤️🌹 happy valentines day cutie 🌹❤️</h2>", unsafe_allow_html=True)

# Glowing button
if st.button("💖 Click for a Surprise 💖", key="surprise"):
    with st.spinner("Loading your surprise... 🎁"):
        time.sleep(2)  # Fake loading effect

    st.balloons()  # 🎈🎈🎈 Surprise effect!

    # Center the images
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("rose_bouquet.png", width=200)
        st.image("guitar.png", width=200)

    # Play romantic song 🎶
    st.audio("valentine_song.mp3", format="audio/mp3", autoplay=True)

    # Display "I Love You, Princess ❤️👑" text with a fade-in effect
    st.markdown("<h2 class='fade-in' style='text-align: center; color: red;'>i love you princess ❤️</h2>",
                unsafe_allow_html=True)
