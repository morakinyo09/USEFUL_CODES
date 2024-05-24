import random

print("Hey there, this is soft electrical. Am here to answer frequently asked questions ?")
print("frequently asked questions:")
print("where is the company located, \nwhat are the services provided by your company, \n ")
print("")

greetings = ["hello", "hi there", "hi there; how are you","hey"]
responses = ["I'm good thanks", "I'm doing well", "I'm great", "hey there \n" ]
questions1 = ["where is the company located"]
answer1 = ["The company is located at FFF junction, along ondo ore road, Ondo", "\nThe company is located at FFF junction, oka ondo.we sell electrical appliances and also based on tech support."]
question2 =["what are the services provided by your comapany"]
answer2 = [" The services provided by our company include: tech support, sales of electrical appliances, tech trainings and many more... Please message the admin!"]
question3 = ["how can i contact the admin", "how can i contact the ceo", "how can i reach the ceo"]
answer3 = ["you can contact the admin through this number 09031771526"]
question4 = ["what type of training", "what type of training are offered by softelectrical"]
answer4 = ["the trainings offered by softelectrical include electrical and computer trainings"]
question5 = ["what type of electrical training", "what are the available electrical training", "which type of electrical training"]
answer5 = ["we train our students on electrical trainings such as half and full conduit house wiring and solar installations"]

def chatbot(input):
    if "hello" in input.lower():
        return random.choice(greetings)
    elif "hi" in input.lower():
        return random.choice(greetings)
    elif "how are you" in input.lower():
        return random.choice(responses)
    elif "hey" in input.lower():
        return random.choice(responses)
    elif "where is the company located" in input.lower():
        return random.choice(answer1)
    elif "what are the services provided by your company" in input.lower():
        return random.choice(answer2)
    elif "how can i contact the ceo" in input.lower():
        return random.choice(answer3)
    elif random.choice(question4) in input.lower():
        return random.choice(answer4)
    elif random.choice(question5) in input.lower():
        return random.choice(answer5)
    else:
        return "please chat the admin on 09031771526"

while True:
    #if():
        user_input = input("you: ")
        print("chatbot:", chatbot(user_input))
    #elif user_input == "":
       # print("how can i help you ")
    #else:
        #print("thank you for today")






