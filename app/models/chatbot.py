from app.services.openai_service import generate_response
class Chatbot():

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.questions = []
        self.reservation_questions = ["When is the desired date and time for your reservation? ", "Total of guests?"]
        self.chat_history = []
        self.state = "ai"
        self.conversation_stack = []
        
    # def check_for_intention_ai(message_body, wa_id, name):
    #     # OpenAI Integration
    #     return generate_response(message_body, wa_id, name)
    
    def handle_intent(self, intent_name, arguments=None):
        """Handle detected intent and update chatbot state accordingly."""
        if intent_name == "reservation_intend":
            self.questions.extend(self.reservation_questions)  # Add reservation questions
            self.state = "collecting_reservation_info"  # Update state to reflect new focus
        return "Ask customer for his contact information for start of the reservation process."
        
    def ask_question(self,phone_number, message,name):
        # Return the next question if there are any left, else indicate the end of conversation
        return self.questions.pop(0) if self.questions else "Thank you for chatting with us!"

    def append_history(self, chat):
        self.chat_history.append(chat)

    # Additional methods as needed for chatbot functionality

class ChatBotManager:
    def __init__(self):
        self.chatbots = {}  # Maps phone numbers to ChatBot instances

    def get_bot_for_number(self, phone_number):
        if phone_number not in self.chatbots:
            self.chatbots[phone_number] = Chatbot(phone_number)
        return self.chatbots[phone_number]

    def handle_incoming_message(self, phone_number, message,name):
        chatbot = self.get_bot_for_number(phone_number)
        chatbot.append_history(message)
        if (chatbot.state == "ai"):
            return generate_response(message,phone_number,name,chatbot)
        return chatbot.ask_question(phone_number, message,name)

# # Example usage
# manager = ChatBotManager()
# phone_number = "+1234567890"

# # Simulate incoming messages
# print(manager.handle_incoming_message(phone_number, "Hello!"))
# print(manager.handle_incoming_message(phone_number, "I need help with my account."))
