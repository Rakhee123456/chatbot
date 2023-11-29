from chatterbot import ChatBot

# Create a ChatterBot instance
chatbot = ChatBot('MyChatBot')

# Print a welcome message
print("Welcome to MyChatBot! Ask me anything or just say hi.")

# Additional code for interaction can be added here
# For example, you can use the chatbot.get_response() method

# Example interaction:
user_input = input("You: ")
response = chatbot.get_response(user_input)
print("MyChatBot:", response)
