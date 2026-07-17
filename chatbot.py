print("Rule-Based AI Chatbot")
while True:
    user=input("You: ").strip().lower()
    if user in ["hi","hello","hey"]:
        print("Bot: Hello! How can I help you?")
    elif user in ["how are you","how are you?"]:
        print("Bot: I'm doing great!")
    elif user in ["your name","what is your name","name"]:
        print("Bot: I am a Rule-Based AI Chatbot.")
    elif user in ["bye","exit","quit"]:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand that yet.")
