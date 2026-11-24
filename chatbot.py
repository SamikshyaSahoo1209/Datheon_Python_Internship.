
import json
import re

# Load FAQ dataset
try:
    with open("faq_dataset.json", "r", encoding="utf-8") as file:
        faq_data = json.load(file)
except FileNotFoundError:
    faq_data = {}

# Chatbot responses
def chatbot_response(user_input):

    text = user_input.lower().strip()

    # Exit commands
    if re.search(r"\b(bye|exit|quit)\b", text):
        return "Thank you for chatting with us. Goodbye!"

    # Greetings
    if re.search(r"\b(hello|hi|hey|good morning|good evening)\b", text):
        return "Hello! Welcome to Customer Support. How can I help you?"

    # Business hours
    if re.search(r"\b(hours|timing|open|closing|working time)\b", text):
        return "Our business hours are 9 AM to 6 PM, Monday to Saturday."

    # Return policy
    if re.search(r"\b(return|refund|exchange)\b", text):
        return "You can request a return within 7 days of receiving your product."

    # Product questions
    if re.search(r"\b(product|price|cost|available)\b", text):
        return "Please tell me which product you want to know about."

    # Search FAQ dataset
    if isinstance(faq_data, dict):
        for key, answer in faq_data.items():
            if key.lower() in text:
                return str(answer)

    # Fallback response
    return "Sorry, I didn't understand your question. Please try asking differently."


# Main chatbot program
print("=" * 45)
print("       CUSTOMER SUPPORT CHATBOT")
print("=" * 45)
print("Type 'bye', 'exit', or 'quit' to stop.")

while True:
    user_input = input("\nYou: ")

    if not user_input.strip():
        print("Bot: Please enter a question.")
        continue

    response = chatbot_response(user_input)
    print("Bot:", response)

    if re.search(r"\b(bye|exit|quit)\b", user_input.lower()):
        break
