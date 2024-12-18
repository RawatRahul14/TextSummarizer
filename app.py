import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline

# Initialize the prediction pipeline
pipeline = PredictionPipeline()

# Streamlit App Title
st.title("Text Summarization App")

# Input Text Box
st.header("Enter the Text You Want to Summarize")
input_text = st.text_area("Input your text here:", height=200)

# Summarize Button
if st.button("Summarize"):
    if input_text.strip():
        st.subheader("Summarized Text")
        summarized_text = pipeline.predict(input_text)
        st.write(summarized_text)
    else:
        st.warning("Please enter some text to summarize.")