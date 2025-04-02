from langchain_groq import ChatGroq
import getpass
import os
os.environ["LANGCHAIN_API_KEY"] = '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'
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="CourseLanggraph"
os.environ["GROQ_API_KEY"] = "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"

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg)