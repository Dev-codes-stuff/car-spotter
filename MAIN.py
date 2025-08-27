import streamlit as st
from PIL import Image
import random

# Title
st.title("🚗 Car Spotter - MVP Prototype")

# File uploader
uploaded_file = st.file_uploader("Upload a car photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and show the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Car", use_column_width=True)
    
    # Dummy rarity system (placeholder)
    rarity_levels = ["Common", "Uncommon", "Rare", "Luxury", "Super", "Legendary"]
    rarity = random.choice(rarity_levels)  # For now, random
    
    st.subheader(f"🔎 Rarity: {rarity}")


# Page Config
st.set_page_config(page_title="Car Spotter", page_icon="🚗", layout="wide")

# Sidebar Navigation
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Leaderboard", "Events", "Play Now", "About"])

# Home Page
if page == "Home":
    st.title("🚗 Car Spotter")
    st.subheader("Gotta Spot ’Em All!")
    st.write("Car Spotter is a fun AI-powered web app where you can upload car photos, "
             "earn points, join challenges, and climb the leaderboard.")

    st.markdown("### 🔥 Features")
    st.markdown("- Upload car photos and get them recognized instantly")
    st.markdown("- Earn points for every unique car spotted")
    st.markdown("- Compete in weekly & monthly events")
    st.markdown("- Climb the leaderboard and show off your spotting skills")

    st.success("👉 Use the sidebar to explore features!")

# Leaderboard Page
elif page == "Leaderboard":
    st.title("🏆 Leaderboard")
    st.info("Leaderboard feature coming soon...")
    # Later: Display top users, scores from database

# Events Page
elif page == "Events":
    st.title("📅 Events")
    st.write("Join upcoming car spotting challenges!")
    st.info("Events system coming soon... Stay tuned!")

# Play Page
elif page == "Play Now":
    st.title("🎮 Play Now - Upload Your Car Photo")
    uploaded_file = st.file_uploader("Upload a car photo", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Car", use_column_width=True)
        st.success("✅ Car recognition feature coming soon!")

# About Page
elif page == "About":
    st.title("ℹ️ About Car Spotter")
    st.write("""
    Car Spotter is a fun-first project built by a CS student 🚀.  
    The idea: turn real-life car spotting into a game where you can **scan, score, and compete**.  
    Built using **Python, Streamlit, and AI (OpenCV/Torch)**.  
    """)

    st.markdown("Made with ❤️ in India 🇮🇳")

