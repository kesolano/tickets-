# 📊 Clasificador de Tickets con IA

Una aplicación web desarrollada con **Streamlit** que utiliza la API de **Perplexity** para clasificar automáticamente tickets de soporte técnico y detectar casos urgentes.

## 🚀 Características

- **Clasificación automática**: Categoriza tickets en logística, pagos, producto defectuoso u otros
- **Detección de urgencia**: Identifica tickets que requieren atención inmediata
- **Interfaz web intuitiva**: Sube archivos CSV y visualiza resultados al instante
- **Procesamiento con IA**: Utiliza modelos avanzados de Perplexity para análisis de texto
- **Despliegue en la nube**: Aplicación accesible desde cualquier dispositivo

## 🎯 Cómo funciona

1. **Sube tu archivo CSV** con una columna llamada `ticket` que contenga los textos de los tickets
2. **La IA procesa cada ticket** y lo clasifica en una de las categorías predefinidas
3. **Detecta casos urgentes** basándose en palabras clave críticas
4. **Visualiza los resultados** en una tabla interactiva en tiempo real

## 📋 Categorías de clasificación

- **Logística**: Problemas de envío, entrega, ubicación
- **Pagos**: Inconvenientes con facturación, cobros, métodos de pago
- **Producto defectuoso**: Artículos dañados, defectuosos o con fallas
- **Otros**: Consultas técnicas, generales o que no encajan en categorías anteriores

## 🔧 Instalación local

### Prerrequisitos
- Python 3.8+
- Cuenta y API Key de Perplexity

### Pasos
1. **Clona el repositorio**
   ```bash
   git clone https://github.com/kesolano/tickets-.git
   cd tickets-
   ```

2. **Crea un entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura tu API Key**
   - Crea un archivo `.env` en la raíz del proyecto
   - Agrega tu clave de API:
   ```
   PERPLEXITY_API_KEY=tu_api_key_aqui
   ```

5. **Ejecuta la aplicación**
   ```bash
   streamlit run ticket.py
   ```

6. **Accede a la app**
   - Abre tu navegador en `http://localhost:8501`

## 📁 Estructura del proyecto

```
tickets-/
├── ticket.py           # Aplicación principal de Streamlit
├── requirements.txt    # Dependencias de Python
├── .gitignore         # Archivos a ignorar por Git
├── .env               # Variables de entorno (no incluido en repo)
└── README.md          # Este archivo
```

## 📊 Formato del archivo CSV

Tu archivo CSV debe tener **al menos una columna llamada `ticket`** con el texto de cada ticket:

```csv
ticket
"Mi pedido no ha llegado después de una semana"
"No puedo pagar con mi tarjeta de crédito"
"El producto llegó dañado"
"URGENTE: El sistema no responde"
```

## 🌐 Aplicación en línea

**¡Prueba la aplicación directamente en la nube!**
- **URL**: [Próximamente - una vez desplegada]
- No requiere instalación
- Sube tu CSV y obtén resultados inmediatos

## ⚡ Detección de urgencia

La aplicación identifica automáticamente tickets urgentes buscando palabras clave como:
- "urgente"
- "ayuda ya"
- "inmediatamente"
- "no funciona"
- "crítico"
- "emergencia"

## 🛠️ Tecnologías utilizadas

- **Streamlit**: Framework para aplicaciones web en Python
- **Pandas**: Manipulación y análisis de datos
- **Requests**: Cliente HTTP para comunicación con APIs
- **Perplexity API**: Modelos de IA para procesamiento de lenguaje natural
- **Python-dotenv**: Gestión de variables de entorno

## 📝 Ejemplo de uso

1. Prepara un archivo CSV con tus tickets
2. Sube el archivo usando el botón "Browse files"
3. Espera a que la IA procese todos los tickets
4. Visualiza los resultados con las nuevas columnas:
   - `categoría`: Clasificación automática
   - `urgente`: True/False según el nivel de prioridad

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📧 Contacto

**Desarrollador**: [Tu nombre]  
**GitHub**: [@kesolano](https://github.com/kesolano)  
**Proyecto**: [https://github.com/kesolano/tickets-](https://github.com/kesolano/tickets-)

---

⭐ **¡Dale una estrella al repo si te resultó útil!** ⭐