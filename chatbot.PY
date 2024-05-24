import tkinter as tk
from tkinter import messagebox
import random

print("Hey there, this is soft electrical. Am here to answer frequently asked questions ?")

greetings = ["Hello. i'm here to help based on frequently asked question."  ]
responses = ["I'm good thanks", "I'm doing well", "I'm great", "hey there" ]
questions1 = ["where is the company located"]
answer1 = ["The company is located at FFF junction, oka ondo", "The company is located at FFF junction, oka ondo.we sell electrical appliances and also based on tech support."]
question2 =["what are the services provided by your comapany"]
answer2 = [" The services provided by our company include: tech support, sales of electrical appliances, tech trainings and many more... Please message the admin!"]
question3 = ["how can i contact the admin", "how can i contact the ceo", "how can i reach the ceo"]
answer3 = ["you can contact the admin through this number 09031771526"]
question4 = ["what type of training", "what type of training are offered by softelectrical"]
answer4 = ["the trainings offered by softelectrical include electrical and computer trainings"]
question5 = ["what type of electrical training", "what are the available electrical training", "which type of electrical training"]
answer5 = ["we train our students on electrical trainings such as half and full conduit house wiring and solar installations"]
question5 = [""]

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
        return "I don't understand you, please chat the admin on 07038123535"

def create_gui():
	root = tk.Tk()
	root.title("SoftElectrical")
	root.configure(background='#f0f0f0')

	frame = tk.Frame(root, bg='red')
	frame.pack(padx=14, pady=14)

	input_field = tk.Entry(frame, width=30, font=('Arial', 12))
	input_field.pack(side=tk.LEFT, padx=5, pady=5)

	def send_message():
		user_input = input_field.get()
		input_field.delete(0, tk.END) 
		response = chatbot(user_input)
		output_text.insert(tk.END, "User: " + user_input + "\n")
		output_text.insert(tk.END, "SoftElectrical: " + response + "\n")

	send_button = tk.Button(frame, text="Send", command=send_message, font=('monseratbold', 12), bg='yellow', fg='black', padx=5, pady=5)
	send_button.pack(side=tk.LEFT, padx=5, pady=5)

	global output_text
	output_text = tk.Text(root, height=10, width=40, font=('Arial', 12), bg='black', fg="white")
	output_text.pack(side=tk.LEFT, padx=10, pady=10,)


	root.mainloop()

if __name__ == "__main__":
	create_gui()