import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()
API_KEY = os.getenv("PERPLEXITY_API_KEY")

if not API_KEY:
    raise Exception("❌ No se encontró la API Key en el archivo .env")

# Cargar tickets.csv
try:
    df = pd.read_csv("tickets.csv")
except FileNotFoundError:
    raise FileNotFoundError("❌ El archivo 'tickets.csv' no se encuentra en el directorio actual.")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def clasificar_con_perplexity(texto):
    prompt = f"""Clasifica el siguiente ticket de soporte en una de las siguientes categorías:
- logística
- pagos
- producto defectuoso
- otros

Solo devuelve la categoría. Ticket: \"{texto}\""""

    data = {
        "model": "sonar-reasoning-pro",  # Asegúrate que el modelo es el correcto para tu cuenta
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json=data,
            timeout=30  # Ampliado timeout para evitar errores por demora
        )
        response.raise_for_status()
        response_json = response.json()

        if "choices" in response_json and response_json["choices"]:
            category = response_json["choices"][0]["message"]["content"].strip().lower()
            category = category.strip(' "\'')
            return category
        else:
            return "error"

    except requests.exceptions.RequestException as e:
        print(f"❌ Error al llamar la API: {e}")
        return "error"

def es_urgente(ticket):
    palabras_clave = ["urgente", "ayuda ya", "inmediatamente", "no funciona", "crítico", "emergencia"]
    return any(palabra in ticket.lower() for palabra in palabras_clave)

def reenviar_a_agente(ticket):
    print(f"🚨 Reenviando ticket urgente a agente humano: {ticket}")

print("🔎 Clasificando tickets...")

# Creamos listas para guardar resultados de clasificación y urgencia
categorias = []
urgencias = []

for _, row in df.iterrows():
    categoria = clasificar_con_perplexity(row["ticket"])
    print(categoria)
    categorias.append(categoria)
    urgente = es_urgente(row["ticket"])
    if urgente:
        reenviar_a_agente(row["ticket"])
    urgencias.append(urgente)

# Añadimos columnas nuevas al dataframe y guardamos a CSV
df["categoría"] = categorias
df["urgente"] = urgencias

df.to_csv("tickets_clasificados.csv", index=False)

print("✅ Clasificación finalizada. Revisa el archivo 'tickets_clasificados.csv'.")
