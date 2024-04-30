### HTpy: Early Development Preview

**HTpy** is a custom scripting language designed to transpile AHK-like syntax files into Python scripts. It allows users to write scripts using HTpy syntax and convert them into executable Python code.

**Note:** This project is still in its early stages of development.

#### Try It Out

You can experiment with HTpy syntax using the [HTpy online editor](https://themaster1127.github.io/HTpy/). Note that this editor provides only a subset of HTpy functionality.
The transpiler processes the code in real time. If you encounter any glitches or the transpiled code doesn't work correctly, simply click on 'Transpile' or press Ctrl+Enter, and it should resolve the issue. Otherwise, it could be an error in your code or possibly an issue with the transpiler itself.

#### Usage Example

HTpy currently supports a subset of commands similar to AutoHotkey:

- `msgbox`: Display a message box.
- `sleep`: Pause script execution for a specified duration.
- Variables: Declare and manipulate variables.
- `Random`: Generate random numbers within specified ranges.
- `if`, `else if`, `else`
- `Loop, `
- Functions

Here's an example of HTpy syntax:

```ahk
gameLogic(randomNumber, userNumber, numOfGuesses)
{
    g := str(numOfGuesses)
    if (randomNumber = userNumber)
    {
        MsgBox, You win in %g% guesses
        Sleep, 500
        return "end"
    }
    else if (randomNumber < userNumber)
    {
        msgbox, Lower
    }
    else
    {
        msgbox, Higher
    }
    return "not over"
}


Game()
{
    msgbox, Welcome to Guess the Number
    Sleep, 700
    Random, ran, 1, 100
    guesses := 0
    Loop, 999999999999999999999
    {
        userNum := int(input("enter a number form 1 to 100: "))
        guesses := guesses + 1
        out := gameLogic(ran, userNum, guesses)
        if (out = "end")
        {
            msgbox, Thanks for playing
            msgbox, exiting in 4
            Sleep, 1000
            msgbox, exiting in 3
            Sleep, 1000
            MsgBox, exiting in 2
            Sleep, 1000
            msgbox, exiting in 1
            Sleep, 1000
            Msgbox, bye
            Sleep, 250
            break
        }
    }
}


msgbox, hello
Sleep, 1000
msgbox, wanna play a game
answerToWannaPlay := input("y/n`n")


if (answerToWannaPlay = "y")
{
    Game()
}
else 
{
    msgbox, oh ok bye
    Sleep, 1000
}
```

-----> in python


HTpy will automatically import the python library we need. 

```py
import time
import random
# Define a dictionary to store dynamic variables
variables = {}

def gameLogic(randomNumber, userNumber, numOfGuesses):
    variables['randomNumber'] = randomNumber
    variables['userNumber'] = userNumber
    variables['numOfGuesses'] = numOfGuesses
    
    variables['g'] = str(variables['numOfGuesses'])
    if (variables['randomNumber'] == variables['userNumber']):
        print("You win in " + variables['g'] + " guesses")
        time.sleep(500 / 1000)
        return "end"
    elif (variables['randomNumber'] < variables['userNumber']):
        print("Lower")
    else:
        print("Higher")
    return "not over"

def Game():
    print("Welcome to Guess the Number")
    time.sleep(700 / 1000)
    variables['ran'] = random.randint(1, 100)
    variables['guesses'] = 0
    for variables['A_Index'] in range(1, 999999999999999999999 + 1):
        variables['userNum'] = int(input("enter a number form 1 to 100: "))
        variables['guesses'] = variables['guesses'] + 1
        variables['out'] = gameLogic(variables['ran'], variables['userNum'], variables['guesses'])
        if (variables['out'] == "end"):
            print("Thanks for playing")
            print("exiting in 4")
            time.sleep(1000 / 1000)
            print("exiting in 3")
            time.sleep(1000 / 1000)
            print("exiting in 2")
            time.sleep(1000 / 1000)
            print("exiting in 1")
            time.sleep(1000 / 1000)
            print("bye")
            time.sleep(250 / 1000)
            break

print("hello")
time.sleep(1000 / 1000)
print("wanna play a game")
variables['answerToWannaPlay'] = input("y/n\n")

if (variables['answerToWannaPlay'] == "y"):
    Game()
else:
    print("oh ok bye")
    time.sleep(1000 / 1000)
```
