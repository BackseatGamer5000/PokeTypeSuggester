import numpy as np
import pandas as pd

typeChart = pd.DataFrame()

listOfTypes = ['Normal','Fire','Water','Grass','Electric','Ice','Fighting','Poison','Ground','Flying','Psychic','Bug','Rock','Ghost','Dragon','Dark','Steel','Fairy']
listOfTypesLowercase = list(map(lambda x: x.lower(), listOfTypes))

typeChart.index = listOfTypes
typeChart['Normal'] = [1.0,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1,]
typeChart['Fire'] = [1,0.5,2,0.5,1,0.5,1,1,2,1,1,0.5,2,1,1,1,0.5,0.5]
typeChart['Water'] = [1,0.5,0.5,2,2,0.5,2,1,2,0.5,2,1,2,1,1,1,1,1]
typeChart['Grass'] = [1,2,0.5,0.5,0.5,2,1,2,0.5,2,1,2,1,1,1,1,1,1]
typeChart['Electric'] = [1,1,1,1,0.5,1,1,1,2,0.5,1,1,1,1,1,1,0.5,1]
typeChart['Ice'] = [1,2,1,1,1,0.5,2,1,1,1,1,1,2,1,1,1,2,1]
typeChart['Fighting'] = [1,1,1,1,1,1,1,1,1,2,2,0.5,0.5,1,1,0.5,1,2]
typeChart['Poison'] = [1,1,1,0.5,1,1,0.5,0.5,2,1,2,0.5,1,1,1,1,1,0.5]
typeChart['Ground'] = [1,1,2,2,0,2,1,0.5,1,1,1,1,0.5,1,1,1,1,1]
typeChart['Flying'] = [1,1,1,0.5,2,2,0.5,1,0,1,1,0.5,2,1,1,1,1,1]
typeChart['Psychic'] = [1,1,1,1,1,1,0.5,1,1,1,0.5,2,1,2,1,2,1,1]
typeChart['Bug'] = [1,2,1,0.5,1,1,0.5,1,0.5,2,1,1,2,1,1,1,1,1]
typeChart['Rock'] = [0.5,0.5,2,2,1,1,2,0.5,2,0.5,1,1,1,1,1,1,2,1]
typeChart['Ghost'] = [0,1,1,1,1,1,0,0.5,1,1,1,0.5,1,2,1,2,1,1]
typeChart['Dragon'] = [1,0.5,0.5,0.5,0.5,2,1,1,1,1,1,1,1,1,2,1,1,2]
typeChart['Dark'] = [1,1,1,1,1,1,2,1,1,1,0,2,1,0.5,1,0.5,1,2]
typeChart['Steel'] = [0.5,2,1,0.5,1,0.5,2,0,2,0.5,0.5,0.5,0.5,1,0.5,1,0.5,0.5]
typeChart['Fairy'] = [1,1,1,1,1,1,0.5,2,1,1,1,0.5,1,1,0,0.5,2,1]

def getInput(acceptedAnswers):
    answer = input("type here")
    while answer not in acceptedAnswers:
        print("I'm sorry, could you repeat that?")
        print(acceptedAnswers)
        answer = input("type here")
    return answer

doneEnteringInput = False
userTypes = []
numberOfTries = 0
print("What are all the types on your team right now?")
print("Press Enter between each one.")
print("When you're done, type 'done' and press Enter.")
while doneEnteringInput == False and numberOfTries < 100:
  userInput = getInput(listOfTypes + listOfTypesLowercase + ['done', 'Done'])

  # Need to check that there aren't duplicates

  if userInput in listOfTypes + listOfTypesLowercase:
      print(userInput.title())
      userTypes.insert(1, userInput.title())

  elif userInput in ['done', 'Done']:
      print("Is this correct?")
      print(userTypes)

      print("Type yes or no.")
      inputWasRight = getInput(['yes','y','no','n'])
      if inputWasRight in ['yes', 'y']:
          doneEnteringInput = True
          print("Awesome! Entering calculation phase.")
      else:
          print("Okay, let's start over.\n")
          
          print("What are all the types on your team right now?")
          print("Press Enter between each one.")
          print("When you're done, type 'done' and press Enter.")

  numberOfTries += 1
