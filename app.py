import streamlit as st
import time
import pandas as pd 
from model import AVML


# Title
st.markdown('<h1>Chat Bot</h1>', unsafe_allow_html=True)
df = pd.read_csv('data.csv')
model = AVML()
model.train(df)


# Stream Data
def stream_data(txt, sleep_time=0.09):
    for word in txt.split(" "):
        yield word + " "
        time.sleep(sleep_time)

if "message" not in st.session_state:
    st.session_state.message = []


def main():
    

    with st.container():
        prompt = st.chat_input("Say something")

        if prompt:
            st.chat_message("human").write(prompt)
            
            # Recommend similar medicines
            trans_input = model.transform_text(prompt)
            recommend , similarity = model.recommend(trans_input , 2)
            response =f'''You can use {recommend['Herb'][0]}. Most common benfits are : {recommend['Benefits'][0]}. Medical use {recommend['Medicinal_Uses'][0]}. Climate conditions are {recommend['Climate'][0]} . Method of Cultivation are {recommend['Method_of_Cultivation'][0]}'''

            st.chat_message("ai").write_stream(stream_data(response))
            
            # Add messages to history
            st.session_state.message.append({"role": "user", "message": prompt})
            st.session_state.message.append({"role": "ai", "message": recommend})

if __name__ == "__main__":
    main()
