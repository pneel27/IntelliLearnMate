from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import FAISS

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

vector_store = FAISS.from_documents(text_chunks, embedding=embeddings)
vector_store.save_local("faiss_index")