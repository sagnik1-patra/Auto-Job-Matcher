import spacy
import docx2txt
import PyPDF2

nlp = spacy.load('en_core_web_sm')

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return " ".join(page.extract_text() for page in reader.pages)
    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file type")

def extract_keywords(text):
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ['SKILL', 'ORG', 'WORK_OF_ART']]
    return list(set(skills))  # Remove duplicates

def parse_resume(file_path):
    text = extract_text(file_path)
    return extract_keywords(text)
