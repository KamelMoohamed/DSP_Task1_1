import streamlit as st
from stateManagement.stateManagement import stateManagement


class signalsListWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        signalsList = []
        for signal in st.session_state.signalsList:
            signalsList.append(signal['name'])

        # st.radio("Signalls", signalsList)

        # if st.session_state.selectedSignal:
        #     state.on_change()