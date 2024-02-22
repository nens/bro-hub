
import streamlit as st
import authentication as auth


def main():
    
    if auth.authenticate():
        st.text("Hier een overzicht van alle GMWs")
    

if __name__ == "__main__":
    main()