import streamlit as st
import pandas as pd
import csv
import random
ph = "Type your Question here!"
with open(r'C:/Users/Ajeet/Downloads/JokeGeneratorSeq2Seq-master/JokeGeneratorSeq2Seq-master/data/jokes.csv', newline='') as f:
    reader = csv.reader(f)
    jok = list(reader)

def getJokeID():
    return random.randrange(1, 525, 1)
def getJokeAnchor(jokeId):
    return jok[jokeId][0]

def getJokeAnswer(jokeId):
    return jok[jokeId][1]

def tellJoke():
    jokeId = getJokeID()
    st.text_input("💬 Sample Statement", value=str(getJokeAnchor(jokeId)), max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None,placeholder=ph, disabled=False)
    st.success(getJokeAnswer(jokeId), icon="😂")

def getJokeAnchor(jokeId):
    return jok[jokeId][0]

def getJokeAnswer(jokeId):
    return jok[jokeId][1]

def tellJoke():
    jokeId = getJokeID()
    st.text_input("💬 Sample Statement", value=str(getJokeAnchor(jokeId)), max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None,placeholder=ph, disabled=False)
    st.success(getJokeAnswer(jokeId), icon="😂")


def getAnswerById(id):
    return jok[id+1][1]

def findJoke(text):
    text = text.lower().strip()
    index = -1
    for row in jok:
        if text == row[0].strip():
            return index
        index=index+1
    print(index)
    return -1     

def update(str):
    if str=="":
        return
    index = findJoke(str)
    if index!=-1:
        st.success("".join(getAnswerById(index)), icon="😂")
    else:
        st.warning('Sorry, that was indeed a blind spot!', icon="⚠️")

text = st.text_input("🎮 Your Turn", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None,args=None, on_change=update(""), kwargs=None,placeholder=ph, disabled=False)
update(text)

st.title('Corporate Joker 🃏')
st.subheader('Team Catalyst ⚡')
#st.button("Question-Answer ❓", key=None, help="", args=None, kwargs=None, disabled=False)
st.button("I'm feeling Lucky 🍀", key=None, help="", on_click=tellJoke, args=None, kwargs=None, disabled=False)

