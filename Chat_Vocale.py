import nltk
import streamlit as st
import speech_recognition as sr
from nltk.chat.util import Chat, reflections

# Charger les données pour l'algorithme du chatbot
pairs = [
    [r"bonjour", ["Bonjour! Comment puis-je vous aider aujourd'hui?"]],
    [r"(.*) ton nom\?", ["Je suis un chatbot vocale. Et vous?"]],
    [r"au revoir", ["Au revoir! Passez une bonne journée."]],
]

chatbot = Chat(pairs, reflections)

# Fonction pour transcrire la parole en texte
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Parlez maintenant...")
        try:
            audio = recognizer.listen(source, timeout=5)
            transcription = recognizer.recognize_google(audio, language="fr-FR")
            return transcription
        except sr.UnknownValueError:
            return "Je n'ai pas compris. Pouvez-vous répéter?"
        except sr.RequestError:
            return "Erreur de service de reconnaissance vocale."

# Fonction du chatbot avec support vocal et textuel
def chatbot_response(user_input):
    if user_input.strip():
        response = chatbot.respond(user_input)
        return response if response else "Je ne suis pas sûr de comprendre."

# Interface utilisateur avec Streamlit
st.title("Chatbot à commande vocale")

# Choix de l'entrée utilisateur
input_mode = st.radio("Choisissez le mode d'entrée :", ["Texte", "Voix"])

if input_mode == "Texte":
    user_input = st.text_input("Entrez votre message :")
    if st.button("Envoyer") and user_input:
        response = chatbot_response(user_input)
        st.text_area("Chatbot", response, height=100)

elif input_mode == "Voix":
    if st.button("Parlez maintenant"):
        user_input = speech_to_text()
        st.text_area("Votre message", user_input, height=100)
        if user_input:
            response = chatbot_response(user_input)
            st.text_area("Chatbot", response, height=100)

# Instructions pour l'utilisateur
st.info("Assurez-vous que votre microphone est connecté et activé.")
