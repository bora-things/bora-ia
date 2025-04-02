### Router

from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


from pydantic import BaseModel, Field

class RouteQuery(BaseModel):
    """Roteia a pergunta do usuário para o nó mais relevante."""

    datasource: Literal["rag", "fora_de_contexto"] = Field(
        ...,
        description="Dado a pergunta do usuário, escolha rotear para 'rag' ou 'fora_de_contexto.",
    )

llm = ChatGroq(model="llama3-70b-8192", temperature=0)

llm_router = llm.with_structured_output(RouteQuery)

# Prompt
system = """ 
    Você é um especialista em direcionar a pergunta de um usuário para um 'rag' ou para um tratamento de perguntas fora de contexto.
    O 'rag' responderá perguntas relacionadas a Universidade Federal do Rio Grande do Norte (UFRN) ou assuntos academicos.
    Caso não se aplique ao 'rag', roteei para 'fora_de_contexto'.
"""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | llm_router
print('rag',
    question_router.invoke(
        {"question": "Quantos semestres para terminar ciencia da computação?"}
    )
)
print('fora de contexto', question_router.invoke({"question": "Quem escreveu Harry Potter?"}))
