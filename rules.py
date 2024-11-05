import streamlit as st 
def run():
    st.markdown(f"## <span style='color:red'>Rule Book 🧾</span>", unsafe_allow_html=True)

    st.write("""
###### 1.) It is a 1V1 Player Game\n
###### 2.) Green lines represent ladders\n
###### 3.) Red lines represent snakes\n
###### 4.) You can choose color of your choice\n
###### 5.) If both the players coincide at the same position, it will be represeted in violet \n
""")
