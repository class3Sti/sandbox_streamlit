# Site com instruções de como usar o Streamlit
# https://docs.streamlit.io/develop/concepts


import streamlit as st

if __name__ == '__main__':
    st.write('*E aí,* **CE Valadão**!')
    st.button('OK', on_click='')
    st.page_link('Ir para a página de teste', page_name='teste')