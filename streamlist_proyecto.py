import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Teacher IA", 
                   page_icon="📘",
                   layout="wide",  
                   initial_sidebar_state="auto" )

# Página principal
def main_page():
    st.title("Teacher IA - Página Principal")
    
    # Interfaz de usuario para ingresar una frase
    frase_usuario = st.text_input("Ingresa una frase en español:",max_chars=100)
    
    if st.button("Traducir"):
        # Procesamiento de la frase
        frase_procesada = procesar_frase(frase_usuario)
        
        # Mostrar la frase procesada
        st.success(f"Frase ingresada: {frase_procesada}")

# Página "Acerca de"
def about_page():
    st.title("Teacher IA - Acerca de")
    st.write("Web del proyecto final de 'Inteligencia artificial: Prompt Engineering para programadores' diseñada por Pablo Montovani.")
    st.write("Teacher IA es una aplicación que dado una frase escrita en español, gracias al poder de la inteligencia artificial la misma es traducida en inglés y se genera una explicación de su gramática. ")
    st.write("Su funcionamiento es simple, en la página principal introduce la frase en español en el lugar indicado y luego presione 'Traducir'. Luego de unos momentos la información procesada se mostrara por debajo. ")

# Función de procesamiento de frase
def procesar_frase(frase):
    # Aquí puedes implementar la lógica de procesamiento de la frase
    fraseProcesada = obtenerAnalisisFrase(frase)
    return fraseProcesada

# Función para inicializar OpenAI API
def obtenerAnalisisFrase(frase):
   client = OpenAI(api_key=st.secrets["OPENAI_API"])
   prompt = f"Traducir al ingles la siguiente frase y explicar brevemente su gramatica: '{frase}'?"
   
   response = client.chat.completions.create(
     model= "gpt-3.5-turbo",
     messages=[{"role": "user", "content": prompt}],
     max_tokens=1024,
   )
       
   return response.choices[0].message.content

# Enrutador para las páginas
def main():
    pages = {"Página Principal": main_page, "Acerca de": about_page}
    
    st.sidebar.title("Menú")
    selection = st.sidebar.radio("Selecciona una página", list(pages.keys()))
    
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
