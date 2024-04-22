# IntelliLearnMate<br/>
This ChatBot Application utilizes a custom dataset by converting it into vectors. Through similarity search, the system retrieves ranked results. Finally, a Language Model (LLM) selects an appropriate response from these ranked results based on the user's question.<br/><br/>

Implementation Steps:<br/>
Step 1: Extract data from the PDF file <br/>
Step 2: Split the data into chunks.<br/>
Step 3: Convert the chunks to vector using embedding model and store them into FIASS DB.<br/>
Step 4: Creating Prompt Template<br/>
Step 5: Loading Index from FIASS DB<br/>
Step 6: Initializing Language Model and RetrievalQA Chain, which helps to generate the relevant response according to question. <br/>
Step 7: Utilized Flask for User Interface <br/><br/>

Tech Stack<br/>
Programming Language: Python<br/>
Generative AI Framework: Langchain<br/>
LLM : Llama2<br/>
Front-End : Flask<br/>
Vector DB : FIASS<br/><br/>

Output:<br/>
