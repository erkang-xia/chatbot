#TODO what if info collected is not enough for the reservation?
#pull customer info 
preload_reservation_questions = [{"question":"When is the desired date and time for your reservation?"},{"question":"Total of guests?"},{"action":"end_conversation"}]
interrupted = "Let's resume the reservation" # merge to the next stack.top(), respose to the customer question + interrupted + intent ask questions

#if stack is empty use open ai for intention looking, after find out what customer want, fill the stack and repeast the process 
