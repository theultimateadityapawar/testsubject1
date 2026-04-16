# question1
print('''twinkle, twinkle, little star,
       how I wonder what you are!''') 
# question2 
import pyttsx3
engine = pyttsx3.init()
engine.say("you need to exercise daily")
engine.runAndWait()
# question3
import os 
directory_path = 'C:' 
contents = os.listdir(directory_path)
for item in contents:
    print(item) 