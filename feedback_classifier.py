from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_FEEDBACK_KEY")
ENDPOINT_FEEDBACK_MODEL = os.getenv("ENDPOINT_FEEDBACK_MODEL")

tagging_prompt = ChatPromptTemplate.from_template(
    """
Classifique a mensagem nas propriedades desejadas.

Extraia apenas as propriedades mencionadas na função de 'Classification'. 

Não adicione justificativas.

Mensagem:
{input}
"""
)

class Classification(BaseModel):
    agressivo: int = Field(description= "agressividade do texto numa escala de 1 a 10")
    ofensivo: int = Field(description= "o quão ofensivo é o texto numa escala de 1 a 10")
    pessoal: int = Field(description= "de 0 a 10, o quão pessoal é a crítica, 0 sendo uma crítica ao professor como profisional e 10 sendo crítica à pessoa")

llm = ChatGroq(temperature=0, model=ENDPOINT_FEEDBACK_MODEL).with_structured_output(
    Classification
)

tagging_chain = tagging_prompt | llm
