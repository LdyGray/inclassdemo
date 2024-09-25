import streamlit as st
from openai import OpenAI
import os


st.title("🎈 Homework App")
st.write(
    "Please add your prompt here!"
)

title = st.text_input("Prompt", "What is Barcelona?")
st.write("Barcelona is", title)


os.environ["OPENAI_API_KEY"] = st.secrets["MyOpenAIkey"]

### OpenAI stuff
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  temperature = 1.8,
  max_tokens=20
)

### Display
st.write(
    "Creative: " + response.choices[0].message.content
)


### OpenAI stuff
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  temperature = 0.2,
  max_tokens=20
)

### Display
st.write(
    "Predictable: " + response.choices[0].message.content
)
