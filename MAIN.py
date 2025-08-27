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