from os import stat
import streamlit as st
from stateManagement.stateManagement import stateManagement


class samplingWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        sampling_val = st.slider(
            "Sampling", key="sampling_slider", min_value=1, max_value=20, value=5)

        state.set_sampled_signal(sampleRate=sampling_val)
        state.set_reconstructed_signal()