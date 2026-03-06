#Librerias 

import streamlit as st
import requests
import time
from google import genai
from google.genai import types

ICON_TRANSPARENT = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
ICON_IA = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCAyNCAyNCc+PHRleHQgeD0nNTAlJyB5PSc1MCUnIGRvbWluYW50LWJhc2VsaW5lPSdjZW50cmFsJyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPSd3aGl0ZScgZm9udC1mYW1pbHk9J0hlbHZldGljYSwgQXJpYWwsIHNhbnMtc2VyaWYnIGZvbnQtc2l6ZT0nMTInIGZvbnQtd2VpZ2h0PSdub3JtYWwnIGxldHRlci1zcGFjaW5nPScxJz5JQTwvdGV4dD48L3N2Zz4="
ICON_USER = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIGQ9Ik0yMCAyMXYtMmE0IDQgMCAwIDAtNC00SDhhNCA0IDAgMCAwLTQgNHYyIj48L3BhdGg+PGNpcmNsZSBjeD0iMTIiIGN5PSI3IiByPSI0Ij48L2NpcmNsZT48L3N2Zz4="

#Estetica de la pagina para que sea similar a armoni.chat 

st.set_page_config(page_title="ARMONI | Neural Core", page_icon=ICON_TRANSPARENT, layout="centered")

st.markdown("""
    <style>
    @font-face { font-family: 'Hadley'; src: local('Hadley'), url('https://fonts.cdnfonts.com/s/17045/Hadley.woff') format('woff'); }

    :root {
        --bg-color: #000000; --text-color: #aaaaaa; --grid-color: rgba(255, 255, 255, 0.04);
        --box-bg: rgba(15, 15, 15, 0.5); --box-border: rgba(255, 255, 255, 0.1);
        --hover-bg: #ffffff; --hover-text: #000000; --input-bg: rgba(15, 15, 15, 0.6);
        --title-color: #ffffff; --tagline-color: #555555;
        --icon-filter: none; --hover-icon-filter: invert(1); --thinking-color: #aaaaaa;
    }

    @media (prefers-color-scheme: light) {
        :root {
            --bg-color: #f4f4f4; --text-color: #333333; --grid-color: rgba(0, 0, 0, 0.05);
            --box-bg: rgba(255, 255, 255, 0.6); --box-border: rgba(0, 0, 0, 0.15);
            --hover-bg: #000000; --hover-text: #ffffff; --input-bg: rgba(255, 255, 255, 0.8);
            --title-color: #000000; --tagline-color: #888888;
            --icon-filter: invert(1); --hover-icon-filter: none; --thinking-color: #444444;
        }
    }

    html, body, [class*="css"], p, div, input, textarea, span, button {
        font-family: 'Hadley', 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
        font-size: 14px !important; letter-spacing: 2px !important; font-weight: 300 !important;
        color: var(--text-color) !important; text-transform: uppercase !important;
    }

    .block-container { padding-top: 3rem !important; padding-bottom: 2rem !important; }

    .stApp {
        background-color: var(--bg-color) !important;
        background-image: linear-gradient(var(--grid-color) 1px, transparent 1px), linear-gradient(90deg, var(--grid-color) 1px, transparent 1px) !important;
        background-size: 50px 50px !important; transition: background-color 0.5s ease;
    }

    header { display: none !important; } #MainMenu, footer { visibility: hidden; }

    .stChatMessage {
        background-color: var(--box-bg) !important; backdrop-filter: blur(15px) !important; -webkit-backdrop-filter: blur(15px) !important;
        border: 1px solid var(--box-border) !important; border-radius: 0px !important; padding: 40px !important; margin-bottom: 20px !important; transition: all 0.4s ease !important;
    }
    .stChatMessage:hover {
        background-color: var(--hover-bg) !important; backdrop-filter: none !important; -webkit-backdrop-filter: none !important;
        transform: translateY(-5px) !important; box-shadow: 0 0 50px rgba(0, 0, 0, 0.1) !important;
    }
    .stChatMessage:hover p, .stChatMessage:hover div, .stChatMessage:hover span { color: var(--hover-text) !important; }

    .stChatMessage img { filter: var(--icon-filter); transition: filter 0.4s ease; }
    .stChatMessage:hover img { filter: var(--hover-icon-filter) !important; }

    [data-testid="stChatInput"] { background-color: transparent !important; padding-bottom: 40px !important; }
    [data-testid="stChatInput"] > div {
        background-color: var(--input-bg) !important; backdrop-filter: blur(15px) !important; -webkit-backdrop-filter: blur(15px) !important;
        border: 1px solid var(--box-border) !important; border-radius: 0px !important;
    }
    [data-testid="stChatInput"] > div:focus-within { border-color: var(--title-color) !important; box-shadow: 0 0 15px var(--box-border) !important; }
    [data-testid="stChatInput"] textarea { color: var(--title-color) !important; }
    [data-testid="stChatInput"] textarea::placeholder { color: var(--tagline-color) !important; }

    [data-testid="stChatInput"] button { border: 1px solid var(--box-border) !important; background-color: transparent !important; color: var(--title-color) !important; border-radius: 0px !important; transition: all 0.3s ease !important; }
    [data-testid="stChatInput"] button:hover { background-color: var(--title-color) !important; color: var(--bg-color) !important; }
    [data-testid="stChatInput"] button svg { fill: var(--title-color) !important; }
    [data-testid="stChatInput"] button:hover svg { fill: var(--bg-color) !important; }

    [data-testid="stChatInput"]::after {
        content: "ARMONI BY ROMAGNA"; position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%);
        font-size: 9px !important; letter-spacing: 4px !important; color: var(--tagline-color) !important; white-space: nowrap;
    }

    .armoni-h1 {
        font-size: 5rem !important; font-weight: 100 !important; letter-spacing: 20px !important; color: var(--title-color) !important; 
        text-align: center; margin-top: 10px !important; margin-bottom: 10px; line-height: 0.9; transition: color 0.5s ease;
    }
    .armoni-tagline { font-size: 10px !important; letter-spacing: 4px !important; text-align: center; color: var(--tagline-color) !important; margin-bottom: 5px; white-space: nowrap !important; }
    .powered-by { font-size: 9px !important; letter-spacing: 3px !important; text-align: center; color: var(--tagline-color) !important; margin-bottom: 60px; }

    [data-testid="stNotification"] { background: var(--bg-color) !important; border: 1px solid var(--box-border) !important; }

    .thinking-text { font-size: 14px !important; letter-spacing: 2px !important; color: var(--thinking-color) !important; animation: pulse-text 1.5s infinite ease-in-out; }
    @keyframes pulse-text { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }

    /* ESTILO PARA MENSAJES DE SISTEMA (Como el Enfriamiento) */
    .sys-msg { color: var(--tagline-color) !important; font-style: italic; letter-spacing: 2px !important; font-size: 12px !important; }

    @media (max-width: 768px) {
        .block-container { padding-left: 1rem !important; padding-right: 1rem !important; padding-top: 2rem !important; }
        .armoni-h1 { font-size: 3rem !important; letter-spacing: 12px !important; margin-top: 10px !important; }
        .armoni-tagline { font-size: 6px !important; letter-spacing: 1px !important; }
        .powered-by { font-size: 7px !important; letter-spacing: 2px !important; margin-bottom: 30px !important; }
        .stChatMessage { padding: 20px !important; }
        [data-testid="stChatInput"] { padding-bottom: 30px !important; }
        [data-testid="stChatInput"]::after { bottom: 5px !important; font-size: 7px !important; letter-spacing: 2px !important; }
        [data-testid="stChatInput"] textarea { font-size: 16px !important; }
    }
    @media (max-width: 400px) { .armoni-h1 { font-size: 2.5rem !important; letter-spacing: 8px !important; } .armoni-tagline { font-size: 5px !important; letter-spacing: 0.5px !important; } }
    </style>
    
    <div class="armoni-h1">ARMONI</div>
    <div class="armoni-tagline">AGENT [ REASONING • MODELING • OPTIMIZATION • NEURAL ] INTELLIGENCE</div>
    <div class="powered-by">POWERED BY GEMINI</div>
    """, unsafe_allow_html=True)

#API'S  y conexion con la AI (gemini)

GOOGLE_API_KEY = "" # por seguridad y privacidad las API'S estan ocultas 
URL_N8N = "" # por seguridad y privacidad las API'S estan ocultas 
 
try:
    client = genai.Client(api_key=GOOGLE_API_KEY)
except Exception as e:

    #Exception de falla de ia 

    st.error(f"Error iniciando el cliente de Google.")

    #construccion del cerebro bajo el motor RMON

def consultar_cerebro(mensaje_usuario):

    # PERSONALIDAD / IDENTIDAD 

    identidad = """
    INSTRUCCIONES DEL SISTEMA:
    Tu nombre es ArmonI. Eres el sistema operativo central de la empresa "Romagna".
    TU USUARIO (CEO): Joan Sebastian Romaña Tavera.
    TU TONO: Profesional, directo, técnico y leal.
    """
    try:

        # PRONTS 

        prompt_completo = identidad + "\n\nUsuario dice: " + mensaje_usuario
        response = client.models.generate_content(
            model="gemini-flash-latest", #modelo de ia gemini flash 
            contents=prompt_completo
        )
        return response.text
    except Exception as e:
        error_str = str(e)

        #Exception para que se vea mas profesional el error y no se vea muchas letras de error [SYS] SISTEMA EN ENFRIAMIENTO TÉRMICO. LÍMITE DE PROCESAMIENTO ALCANZADO. en lugar de muchos caracteres 

        if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str or "quota" in error_str.lower():
            return '<span class="sys-msg">[SYS] SISTEMA EN ENFRIAMIENTO TÉRMICO. LÍMITE DE PROCESAMIENTO ALCANZADO.</span>'
        else:
            return f'<span class="sys-msg">[SYS] ANOMALÍA DETECTADA: {error_str}</span>'

def activar_manos(mensaje, usuario):
    try: requests.post(URL_N8N, json={"mensaje": mensaje, "usuario": usuario, "origen": "ArmonI Core"}, timeout=1)
    except: pass

#Interfaz grafica del core dentro de (streamlit as st)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    avatar_val = ICON_USER if message["role"] == "user" else ICON_IA
    with st.chat_message(message["role"], avatar=avatar_val):
        st.markdown(message["content"], unsafe_allow_html=True)

prompt = st.chat_input("Escribe una orden para ArmonI...")

if prompt:
    with st.chat_message("user", avatar=ICON_USER):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant", avatar=ICON_IA): 
        contenedor_mensaje = st.empty()
        
        contenedor_mensaje.markdown(
            '<span class="thinking-text">CREANDO LA MEJOR RESPUESTA...</span>', 
            unsafe_allow_html=True
        )
        
        respuesta_ia = consultar_cerebro(prompt)
        contenedor_mensaje.markdown(respuesta_ia, unsafe_allow_html=True)
        activar_manos(prompt, "Joan Romaña")

    st.session_state.messages.append({"role": "assistant", "content": respuesta_ia})