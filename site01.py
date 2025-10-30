# Instruções de como usar os elementos do Streamlit
# https://docs.streamlit.io/develop/api-reference


import streamlit as st

if __name__ == '__main__':
    st.write('*E aí,* **CE Valadão**!')
    st.button('OK', on_click=lambda: st.write('Clicou no botão!'))
    st.write('E aí, **Adan**!')
    txt = st.text_area('Escreva seu texto aqui')

    # Chat individual
    # prompt = st.chat_input('Diga alguma coisa')
    # if prompt:
    #     st.write(f'Você disse: {prompt}')

    st.page_link(page='smartsampa.sentinelx.com.br', label='Acesse o SmartSampa')
    