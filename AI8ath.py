Assignment No 8
     Name :- Atharv Yadav                                                  Div:- B
     Batch:-T3                                                                      Roll No :- CO3B4
Title – Develop a simple chatbot using predefined rules and pattern matching.

Program:-
def chatbot_response(message):
    text = message.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! How can I help you?"

    if "bfs" in text:
        return "BFS explores states level by level."

    if "dfs" in text:
        return "DFS explores deeply before backtracking."

    if "a*" in text or "astar" in text:
        return "A* uses f(n) = g(n) + h(n) to guide the search."

    if "viva" in text:
        return "Prepare definitions, algorithms, complexity and code logic."

    if "lab" in text or "experiment" in text:
        return "Please study the aim, theory, algorithm, code and output."

    return "Sorry, I do not understand that question."


print("Simple Rule-Based Chatbot")
print("Type 'bye' to exit.")

while True:
    message = input("You: ")

    if message.lower().strip() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    print("Bot:", chatbot_response(message))




Output:-
Simple Rule-Based Chatbot
Type 'bye' to exit.
You: hello
Bot: Hello! How can I help you?
You: bfs
Bot: BFS explores states level by level.
You: a*
Bot: A* uses f(n) = g(n) + h(n) to guide the search.
You: viva
Bot: Prepare definitions, algorithms, complexity and code logic.
You: lab
Bot: Please study the aim, theory, algorithm, code and output.
You: xyz
Bot: Sorry, I do not understand that question.
You: bye
Bot: Goodbye! Have a nice day.

Process finished with exit code 0