# Instruções de como usar os elementos do Streamlit
# https://docs.streamlit.io/develop/api-reference

import streamlit as st

def pagina_auxiliar():
    st.title('Page 2')

def p3():
    st.title('Página 3.')

def pagina_referencia01():
    st.title('Primeira página de referência')

def home_page():
    st.title('Página Inicial')

def pagina_teste():
    st.title('Teste')
    st.write('*E aí,* **CE Valadão**!')
    st.button('OK', on_click=lambda: st.write('Clicou no botão!'))
    st.write('E aí, **Adan**!')
    txt = st.text_area('Escreva seu texto aqui')

    # Chat individual
    # prompt = st.chat_input('Diga alguma coisa')
    # if prompt:
    #     st.write(f'Você disse: {prompt}')

    st.page_link(page='https://smartsampa.sentinelx.com.br', label='Acesse o SmartSampa')



if __name__ == '__main__':
    # Definindo um menu lateral esquerdo
    paginas = {
        '': [
            st.Page(home_page, title='Início', icon=':material/home:'),
        ],
        'Dados': [
            st.Page('hw.py', title='Olá mundo'),
            st.Page(p3, title='Olá mundo reduzido'),
        ],
        'Referências': [
            st.Page(pagina_referencia01, title='referência 01'),
        ],
        'Teste': [
            st.Page(pagina_teste, title='1º Teste')
        ],
    }

    inicio = st.Page(
        p3,
        title='Início',
        icon=':material/home:'
    )

    #menu_lateral_esquerdo = st.navigation(['hw.py', pagina_auxiliar, p3])
    #menu_lateral_esquerdo = st.navigation({'Dados':[pagina_auxiliar, p3]})
    menu_lateral_esquerdo = st.navigation(paginas)
    menu_lateral_esquerdo.run()