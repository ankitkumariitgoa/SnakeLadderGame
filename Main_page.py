import streamlit as st
from streamlit_option_menu import option_menu
import Home
import snake_ladder_1
import practice
import rules
import resources

import About_us
st.set_page_config(
    page_title="Project",
    layout='wide'
)
class MultiApp:
    def __init__(self) -> None:
        self.apps=[]
    def add_app(self,title,func):
        self.apps.append({
            'title':title,
            'function':func
        })
    def run():
        with st.sidebar:
            app=option_menu(
                menu_title='Project',
                options=['🏠Home','🐍Game','❓About Us❔',"📚Rule Book",'🛜Resources Used/Referred'],
                # icons=['a','b','c','d']
                default_index=0
            )
        if app=='🏠Home':
            Home.run()
        if app=='🐍Game':
            # with st.sidebar:
            apps=option_menu(
                menu_title='Snake And Ladder',
                options=["🐍Player vs Player",'🐍Player vs Computer'],
                # icons=['a','b']
                default_index=0,
                orientation='horizontal'
            )
            if apps=='🐍Player vs Player':
                snake_ladder_1.run()
            if apps=='🐍Player vs Computer':
                practice.run()
                
        

        if app=='❓About Us❔':
            About_us.run()
        if app=='🛜Resources Used/Referred':
            resources.run()
        if app=="📚Rule Book":
            rules.run()
    run()
