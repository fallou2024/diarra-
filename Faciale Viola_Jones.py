import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Title and Instructions
st.title("Application de détection de visages avec Viola-Jones")
st.write(
    """
    **Instructions :**
    1. Chargez une image en utilisant le bouton ci-dessous.
    2. Ajustez les paramètres si nécessaire pour améliorer la détection des visages.
    3. Les visages détectés seront affichés avec des rectangles autour d'eux.
    4. Vous pouvez enregistrer l'image avec les visages détectés.
    """
)

# Upload image
uploaded_file = st.file_uploader("Chargez une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

    # Load Haar cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Adjustable parameters
    scaleFactor = st.slider("Facteur d'échelle (scaleFactor)", 1.1, 2.0, 1.1, step=0.1)
    minNeighbors = st.slider("Nombre minimum de voisins (minNeighbors)", 1, 10, 5)

    # Face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

    # Allow user to choose rectangle color
    rectangle_color = st.color_picker("Choisissez la couleur du rectangle", "#FF0000")
    rectangle_color_rgb = tuple(int(rectangle_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image_np, (x, y), (x + w, y + h), rectangle_color_rgb, 2)

    # Display image with detected faces
    st.image(image_np, caption="Image avec visages détectés", use_column_width=True, channels="RGB")

    # Save the image functionality
    if st.button("Enregistrer l'image avec les visages détectés"):
        save_path = "detected_faces.jpg"
        cv2.imwrite(save_path, cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))
        st.success(f"Image enregistrée sous le nom : {save_path}")
else:
    st.write("Veuillez charger une image pour commencer.")
