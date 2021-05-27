states = ['q1', 'q2', 'q3', 'q4', 'q5', 'qaccept', 'qreject']
inputAlphabet = ["0"]
tapeAlphabet = ["0", "x", "u"]
startState = 'q1'
acceptState = 'qaccept'
rejectState = 'qreject'

# Transiiton function
def transitionFunction(currentState, tapeHead):
    printMessage(inputString, currentState, tapeHead)
    
    while((currentState != acceptState) and (currentState != rejectState)):
        #reject any string not in the alphabet of the Tape
        if inputString[tapeHead] not in tapeAlphabet:
            currentState = rejectState
        # State q1
        elif(currentState == startState):
            if(inputString[tapeHead] == "0"):
                inputString[tapeHead] = "u"
                currentState = "q2"
                tapeHead += 1
            elif(inputString[tapeHead] == "u"):
                currentState = rejectState
            elif(inputString[tapeHead] == "x"):
                currentState = rejectState
            
        # State q2
        elif(currentState == "q2"):
            if(inputString[tapeHead] == "0"):
                inputString[tapeHead] = "x"
                currentState = "q3"
                tapeHead += 1
            elif(inputString[tapeHead] == "u"):
                currentState = acceptState
            elif(inputString[tapeHead] == "x"):
                tapeHead += 1
            
        # State q3
        elif(currentState == "q3"):
            if(inputString[tapeHead] == "0"):
                currentState = "q4"
                tapeHead += 1
            elif(inputString[tapeHead] == "u"):
                currentState = "q5"
                tapeHead -= 1
            elif(inputString[tapeHead] == "x"):
                tapeHead += 1
            
        # State q4
        elif(currentState == "q4"):
            if(inputString[tapeHead] == "0"):
                inputString[tapeHead] = "x"
                currentState = "q3"
                tapeHead += 1
            elif(inputString[tapeHead] == "u"):
                currentState = rejectState
            elif(inputString[tapeHead] == "x"):
                tapeHead += 1
            
        # State q5
        elif(currentState == "q5"):
            if(inputString[tapeHead] == "0"):
                tapeHead -= 1
            elif(inputString[tapeHead] == "u"):
                currentState = "q2"
                tapeHead += 1
            elif(inputString[tapeHead] == "x"):
                tapeHead -= 1
            
        printMessage(inputString, currentState, tapeHead)

# function to print messages
def printMessage(string, state, tapePosition):
    print("Current Tape:", string, "Tape Head Position:", (tapePosition+1), "Current State:", state)

# Begining of execution
inputString = list(input('Enter string: '))
inputString.append("u")
currentState = startState
tapeHead = 0

print("Turing Machine to accept the language consisting of all strings of 0’s whose length is a power of 2.\nInput string: ", inputString)

transitionFunction(currentState, tapeHead)
