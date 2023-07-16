import Task
import random
import json
import torch
from Model import NeuralNet
from NeuralNetwork import bag_of_words,tokenize
from Listen import take_command
from Speech import speak
from Task import NonInputFunctions
import mailing as ma
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents=json.load(json_data)

FILE="TrainData.pth"
data=torch.load(FILE)
# print(data)
input_size=data["input_size"]
hidden_size=data["hidden_size"]
output_size=data["output_size"]
all_words=data["allwords"]
tags=data["tags"]
model_state=data["model_state"]
# print(model_state)
model=NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

name="jack"
speak(f"Hello ! I am {name}.")
Task.wishme()
def Main():
    sentence=take_command()
    if "bye" in sentence:
        speak("Bye.. Have a nice day...")
        exit()
    sentence = tokenize(sentence)
    print(f'sentence {sentence}')
    x=bag_of_words(sentence,all_words)
    print(f'bag of words {x}')
    x=x.reshape(1,x.shape[0])
    x=torch.from_numpy(x).to(device)
    output=model(x)
    # print(output)
    _,predicted=torch.max(output,dim=1)
    tag=tags[predicted.item()]
    probs=torch.softmax(output,dim=1)
    prob=probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag==intent["tag"]:
                reply=random.choices(intent["responses"])
                if "samay" in reply:
                    NonInputFunctions(reply)
                elif "list of commands" in reply:
                   pass
                elif "date" in reply:
                    NonInputFunctions(reply)
                    
                elif "day" in reply:
                    NonInputFunctions(reply)
                    
                elif "timesheet" in reply or "attendance" in reply:
                    NonInputFunctions(reply)
                    
                elif "shutdown" in reply:
                    NonInputFunctions(reply)
                    
                elif "restart" in reply or "reboot" in reply:
                    NonInputFunctions(reply)
                    
                elif "music" in reply:
                    NonInputFunctions(reply)
                
                elif "mail" in reply:
                    NonInputFunctions(reply)
                    
                elif "note" in reply or "notes" in reply:
                    NonInputFunctions(reply)
                    
                elif "temperature" in reply:
                    NonInputFunctions(reply)

                elif "youtube" in reply:
                    NonInputFunctions(reply)

                elif "chrome" in reply:
                    NonInputFunctions(reply)

                elif "sketch" in reply:
                    NonInputFunctions(reply)

                elif "speedtest" in reply:
                    NonInputFunctions(reply)

                else:
                    speak(reply)

while True:
    Main()