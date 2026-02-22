import re

def chatbot():
    print("🤖 CodSoft AI Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if re.search(r"\b(hello|hi|hey)\b", user_input):
            print("Bot: Hello! How can I assist you today?")
        elif "ai" in user_input:
            print("Bot: Artificial Intelligence enables machines to mimic human intelligence.")
        elif "finance" in user_input:
            print("Bot: Finance involves managing money, investments, and assets.")
        elif "stock" in user_input:
            print("Bot: Stocks represent ownership in a company.")
        elif "bye" in user_input:
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: I’m still learning. Can you rephrase?")

chatbot()
