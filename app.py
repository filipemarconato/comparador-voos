import streamlit as st

st.set_page_config(page_title="Comparador de Voos", page_icon="✈️")

st.title("✈️ Comparador de Voos")

voo_esperado = st.text_area(
    "Cole aqui o voo da lâmina",
    height=200
)

voo_encontrado = st.text_area(
    "Cole aqui o voo encontrado",
    height=200
)

if st.button("Comparar"):

    esperado = voo_esperado.upper().strip()
    encontrado = voo_encontrado.upper().strip()

    if esperado == encontrado:
        st.success("✅ MATCH PERFEITO")
    else:
        st.error("❌ DIVERGÊNCIA ENCONTRADA")

        st.write("### Esperado")
        st.code(esperado)

        st.write("### Encontrado")
        st.code(encontrado)
