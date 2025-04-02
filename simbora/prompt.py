from langchain_core.prompts import PromptTemplate 

system_prompt = (
    "Você é um assistente para tarefas de perguntas e respostas."
    "Use os seguintes trechos de contexto recuperados para responder à pergunta."
    "Se você não souber a resposta, diga que não sabe."
    "Você deve deixar explícito os nomes e páginas dos PDFs do contexto que foram usados."
    "\n\n"
    "{context}"
)

document_prompt = PromptTemplate(
    input_variables=["page_content", "title"],
    template="[O texto a seguir foi retirado de \"{title}\" na página {page}] {page_content}"
)
