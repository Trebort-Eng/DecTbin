import streamlit as st
import dectobin as db
import bintodec as bd

st.title("Converter")
choice = st.radio("Pick an Option", ("Decimal to Binary Converter", "Binary to Decimal Converter"))

if choice == "Decimal to Binary Converter":
    st.header("Decimal to Binary Converter")
    decimal_num = st.text_input("Decimal:", key= "decimal_num")
    convert = st.button("Convert", key= "convert")
    if convert:
        if decimal_num.strip():
            import time
            import streamlit as st

            with st.spinner('Pleace wait'):
                time.sleep(2)
            binary_num = db.dectobin(int(decimal_num))
            st.text_input("Binary:", value=str(binary_num))
            st.success('Done!')
        else:
            import time
            import streamlit as st

            with st.spinner('Please wait'):
                time.sleep(2)
            st.error("Wrong Input")

elif choice == "Binary to Decimal Converter":
    st.header("Binary to Decimal Converter")
    binary_number = st.text_input("Binary:", key="binary_number")
    convert = st.button("Convert", key= "convert")
    if convert:
        if binary_number.strip():
            import time
            import streamlit as st

            with st.spinner('Please wait'):
                time.sleep(2)
            decimal_number = bd.bintodec(binary_number)
            st.text_input("Decimal:", value=str(decimal_number))
            st.success('Done!')
        else:
            import time
            import streamlit as st

            with st.spinner('Please wait'):
                time.sleep(2)
            st.error("Wrong Input")

