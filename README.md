¿Qué es?
ARMONI IA es el núcleo de inteligencia del ecosistema. Un asistente conversacional construido con Streamlit , con motor RMON y conectado al modelo Gemini de Google, diseñado para procesamiento de lenguaje natural, automatización y toma de decisiones.
Tecnologías

Python — Lenguaje principal
Streamlit — Interfaz de usuario conversacional
Google Gemini API — Motor de inteligencia artificial
n8n — Automatización de flujos de trabajo
Motor RMON - REASONING • MODELING • OPTIMIZATION • NEURAL

Características

Interfaz estilo terminal con estética dark/light (tema camaleón)
Conexión directa con Gemini para generación de respuestas
Sistema de manejo de errores con mensajes estilizados
Integración con n8n para automatización de acciones
Diseño responsive (desktop y mobile)

Instalación
bash# 1. Clonar el repositorio
git clone https://github.com/joansebastianromanatavera-pixel/armoni-ia.git
cd armoni-ia

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar API keys
#Si desea probar la Ia entre a armoni.chat
GOOGLE_API_KEY= # por seguridad y privacidad las API'S estan ocultas 
URL_N8N= # por seguridad y privacidad las API'S estan ocultas 

# 4. Ejecutar
streamlit run armoni_core.py
Configuración
Este proyecto requiere API keys propias para funcionar. Las keys no están incluidas por seguridad. Necesitas:

Una API key de Google Gemini → Obtener aquí
Una URL de webhook de n8n (opcional, para automatización)

Estructura
armoni-ia/
├── armoni_core.py      # Núcleo principal de la IA
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Archivos ignorados por Git
└── README.md           # Este archivo
Ecosistema Romagna
ARMONI IA es parte del Ecosistema Romagna, que incluye:

ARMONI.chat — Plataforma de gestión inteligente
ARMONI Team — Comunidad deportiva digital
ARMONI IA — Este proyecto


Desarrollado por Joan Sebastian Romaña Tavera 
