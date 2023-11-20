import os
import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fonction pour initialiser ou récupérer l'historique des messages de la session
def get_message_history():
    if 'message_history' not in st.session_state:
        st.session_state.message_history = [{'role': 'system', 'content': "En tant qu'assistant expert en opportunités d'investissement en Afrique, fournis des informations détaillées et des conseils sur des projets d'investissement dans tous les secteurs, en utilisant des sources fiables comme le Forum pour l'investissement en Afrique de la Banque Africaine de Développement et d'autres références crédibles. Présente des exemples de projets réussis pour illustrer les opportunités. Oriente vers des ressources pertinentes et offre des conseils sur les stratégies de projets privés et de partenariats public-privé. Adapte la présentation des informations selon le niveau d'expertise de l'utilisateur. En cas de requête hors sujet, indique poliment que l'assistance se limite aux investissements en Afrique et suggère de reformuler la question ou de chercher une source appropriée pour le sujet demandé. Réponds toujours dans la langue de l'utilisateur."}]
    return st.session_state.message_history

def main():
    st.markdown("<h2 style='text-align: center; color: navy;'>Chatbot intelligent dédié aux opportunités d'investissement en Afrique</h2>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: green;'>Auteur : Hamaya AG-ABDOULAYE</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: blue;'>Ce chatbot est réglé sur des sources fiables, les prédictions peuvent souvent produire des informations inexactes sur des personnes, des lieux ou des faits. Son assistant a été programmé sur les opportunités d'investissement en Afrique, plus souvent promut par le Forum pour l'investissement en Afrique. N'hésitez pas à rebondir sur les reponses prédites, le relancé pour recadrer et ainsi tiré profit du meilleur de cet assistant intelligent</h6>", unsafe_allow_html=True)

    st.sidebar.header("PARAMETRES")
    slider1 = st.sidebar.slider("Max tokens", min_value=80, max_value=2000, value=1000, step=10)
    slider2 = st.sidebar.slider("Reglage de la temperature", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    
    

    input_user = st.text_input("Posez une question en rapport avec les investissements en Afrique:")

    if st.button("Exécuter"):
        if input_user:
            message_history = get_message_history()
            message_history.append({'role': 'user', 'content': input_user})
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=message_history,
                max_tokens=slider1,
                temperature=slider2
            ).choices[0].message
            message_history.append(response)

            st.write(response['content'])

if __name__ == '__main__':
    main()
