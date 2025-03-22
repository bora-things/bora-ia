from langgraph.graph import StateGraph, START, END
from .rag import MessageState, retrieve, generate


workflow = StateGraph(state_schema=MessageState)

# Criando os nós
workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

# Ligando os nós pelas arestas
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

graph = workflow.compile()
