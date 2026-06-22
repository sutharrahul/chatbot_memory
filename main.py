from langchain_ollama import ChatOllama
from memory import get_chat_history
from langchain_core.messages import AIMessage, HumanMessage




llm = ChatOllama(model="gemma3:4b")

chat_history = get_chat_history("rahul-session-1")

SYSTEAM_PROMPT = """
You are a smart AI assistent. You name is leo, you will answer of user query and question. You will not answer any mathametic question and progremming related question. 

if user ask about programming and mathametic related question you will say "Sorry, I can not answer about the maths and programming relatred problem, But you can answer the programming syntext but syntext should contain more then 20 world.

Example:
Q1 : What is output of 2 + 2 * 67/2 - 5?
Ans : Sorry, I can not answer about maths question

Q2 : Write program which accept argument connect the database make a API request return the response and pass value in component?
And : Sorry, I can't do it but I can give the systext.

Q3 : Give me a systext of Javascript funcation which make API connection request and return the value?
Ans : async function getData() {
  try {
    const response = await fetch('https://example.com');
    return response
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}
"""

USER_MESSAGE = input("🦁 Ask somthing > ")

# last chat_history.messages[-20] messages only
history = chat_history.messages[-20]


messages = [("system", SYSTEAM_PROMPT)] + history + [("human", USER_MESSAGE)]

response = llm.invoke(messages)

LLM_Message = response.content

chat_history.add_messages(
    [
        HumanMessage(content=USER_MESSAGE),
        AIMessage(content=LLM_Message)
    ]
)
print(f"🚀 > {LLM_Message}")
