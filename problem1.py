# question1
print('''twinkle, twinkle, little star,
       how I wonder what you are!''') 
# question2 
import pyttsx3
engine = pyttsx3.init()
engine.say(" twinkle twinkel little star ")
engine.runAndWait()
# question3
import os 
directory_path = 'C:' 
contents = os.listdir(directory_path)
for item in contents:
    print(item) 
    print("hello world")
    print("hello world")
    