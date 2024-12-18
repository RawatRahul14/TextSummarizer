import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline

pipeline = PredictionPipeline()

st.title("Text Summarization App")

st.header("Enter the Text You Want to Summarize")
input_text = st.text_area("Input your text here:", height=200)

if st.button("Summarize"):

    if input_text.strip():
        st.subheader("Summarized Text")

        with st.spinner("Summarizing... Please wait."):

            summarized_text = pipeline.predict(input_text)
            summarized_text = summarized_text.replace("<n>", " ")

        st.success("Text summarized successfully!")
        st.write(summarized_text)

    else:
        
        st.warning("Please enter some text to summarize.")