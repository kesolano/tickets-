import streamlit as st
import pandas as pd
import requests
import os
import re
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("PERPLEXITY_API_KEY")
if not API_KEY:
    st.error("No se encontró PERPLEXITY_API_KEY en .env")
    st.stop()

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def clasificar_con_perplexity(texto):
    prompt = f"""
Clasifica el siguiente ticket de soporte en una de las siguientes categorías exactas:
- logística
- pagos
- producto defectuoso
- otros

Responde ÚNICAMENTE con el nombre exacto de la categoría, sin explicaciones ni texto extra.
Ticket: "{texto}"
"""

    data = {
        "model": "sonar-reasoning-pro",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        r = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        r.raise_for_status()
        res = r.json()

        if "choices" in res and res["choices"]:
            raw_response = res["choices"][0]["message"]["content"].strip().lower()

            # Buscar la última coincidencia válida en todo el texto
            matches = re.findall(r"(logística|pagos|producto defectuoso|otros)", raw_response)
            if matches:
                return matches[-1]  # Devuelve la última encontrada, que suele ser la correcta

        return "error"

    except Exception:
        return "error"

def es_urgente(ticket):
    claves = ["urgente", "ayuda ya", "inmediatamente", "no funciona", "crítico", "emergencia"]
    return any(k in ticket.lower() for k in claves)

# --- INTERFAZ Streamlit ---
st.title("📊 Clasificador de Tickets")

archivo = st.file_uploader("Sube un CSV con columna 'ticket'", type="csv")

if archivo:
    df = pd.read_csv(archivo)
    if "ticket" not in df.columns:
        st.error("El CSV debe contener una columna llamada 'ticket'")
    else:
        st.write("Procesando…")
        df["categoría"] = df["ticket"].apply(clasificar_con_perplexity)
        df["urgente"] = df["ticket"].apply(es_urgente)
        st.success("Clasificación completa ✅")
        st.dataframe(df)
