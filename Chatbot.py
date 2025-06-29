print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
while True:
user_input = input("You: ").lower()
if user_input == "hello":  
    print("Bot: Hi there!")  
elif user_input == "hi":  
    print("Bot: Hello!")  
elif user_input == "how are you":  
    print("Bot: I'm doing great, thank you!")  
elif user_input == "what is your name":  
    print("Bot: I am CodeAlphaBot.")  
elif user_input == "what can you do":  
    print("Bot: I can chat with you and respond to simple questions.")  
elif user_input == "bye":  
    print("Bot: Goodbye! Have a great day! 👋")  
    break  
else:  
    print("Bot: Sorry, I didn't understand that.")
