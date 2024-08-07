import os
import pyttsx3 as p
import subprocess

# Define a function to open PowerPoint
def open_application(theApp):
    try:
        # Attempt to open PowerPoint using the typical executable name
        subprocess.run(["start", theApp], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to open {theApp}: {e}")

#loops until user specify to quit
while True:
  p.speak("what can I do for you ?  ")
  print("> ", end="")
  userinput = input()
  
  if (userinput[:4] in ["exit", "quit"]):
    p.speak("bye for now.")
    break

  if (userinput[:3] == "run"): UserCmd = userinput[4:]
  elif (userinput[:7] == "execute"): UserCmd = userinput[8:]    
  else: UserCmd = userinput
     
  try:
    open_application(UserCmd)
  except:
    print("An error occurred while trying to open {userinput}: {e}")














my_api_key = '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'
