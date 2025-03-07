import streamlit as st

st.title("Info") 

with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """     
-   This app performs named entity recognition for medical entities. 
-   myDemo model was developed from dslim/distilbert-NER (a general NER model with 66M parameters) in HuggingFace, and fine-tuned on singh-aditya/MACCROBAT_biomedical_ner (a dataset annotated with medical entity labels in 41 categories). 
-   The model uses the default pretrained tokenizer in dslim/distilbert-NER.
       """
    )
