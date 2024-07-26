import streamlit as st
import requests
import time
from sendmail import send_email

def search_jobs(requirements):
    url = 'http://127.0.0.1/research_candidates'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    
    data = {
        'job_requirements': f'{requirements}'
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    # Interface Streamlit
    st.title('Pesquisa de Jobs')
    requirements = st.text_input("Digite os requisitos do job:")
    if 'button1_clicked' not in st.session_state:
        st.session_state.button1_clicked = False
    if 'button2_clicked' not in st.session_state:
        st.session_state.button2_clicked = False

    if st.button('Buscar'):
        st.session_state.button1_clicked = True
        st.session_state.button2_clicked = False

    if st.session_state.button1_clicked:
        start_time = time.time()
        with st.spinner('Buscando os melhores candidatos...'):
            # Mostrar animação enquanto carrega
            gif_path = "loading.gif"
            gif_placeholder = st.empty()
            gif_placeholder.image(gif_path)

            results = search_jobs(requirements)
            end_time = time.time()  # Finaliza o cronômetro
            elapsed_time = end_time - start_time  # Calcula o tempo decorrido
            if results:
                gif_placeholder.empty()
                st.markdown("<h3 style='color:green;'>Busca Finalizada!</h1>", unsafe_allow_html=True)
                st.write('Top 5 Candidatos:')
                st.write(f"{results['result']['raw']}")
                st.write(f"Tokens Usados: {results['result']['token_usage']['total_tokens']}")
                st.write(f"Total de requisições: {results['result']['token_usage']['successful_requests']}")
                st.write(f"Tempo de execução: {elapsed_time:.2f} segundos")
            else:
                st.error("Não foi possível obter resultados.")
    
    email_input = st.text_input("Digite o e-mail do destinatário:", key="email")
    if st.button('Enviar E-mail'):
        st.session_state.button2_clicked = True
        st.session_state.button1_clicked = False

    if st.session_state.button2_clicked:
        if email_input:
            send_email(email_input, results['result']['raw'])
            st.markdown("<h3 style='color:green;'>E-mail enviado!</h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()