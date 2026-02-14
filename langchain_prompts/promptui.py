from langchain_google_genai import ChatGoogleGenerativeAI   
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

st.header("Research Tool")

paper_input = st.selectbox("Select a research paper name", [ "Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select an explanation style", [ "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select the length of the summary", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

 
template = load_prompt("template.json")

# fill the placeholders 
# prompt = template.invoke({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input
# })

if st.button("Generate Response"):

    chain = template | model  # Create a chain that connects the prompt template to the model


    # Create an empty placeholder for the output
    output_placeholder = st.empty()  
    # Initialize a variable to accumulate the full response
    full_response = ""  
    
     # Show a spinner while generating the response
    with st.spinner("Generating response..."): 
        for chunk in chain.stream({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    }):
            if chunk.content:
                full_response += chunk.content  # Append the new chunk of content to the full response
                output_placeholder.write(full_response)  # Update the placeholder with each new chunk of content

    # result = model.invoke(prompt)
    # st.text("Generating response...")
    # st.write(result.content)