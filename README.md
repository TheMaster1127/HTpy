### HTpy: Still in Development Preview

**HTpy** is a custom scripting language designed to transpile AHK-like syntax files into Python scripts. It allows users to write scripts using HTpy syntax and convert them into executable Python code.

**Note:** This project is still in development.

#### Try It Out

You can experiment with HTpy syntax using the [HTpy online editor](https://themaster1127.github.io/HTpy/). Note that this editor provides only a subset of HTpy functionality.
The transpiler processes the code in real time. If you encounter any glitches or the transpiled code doesn't work correctly, simply click on 'Transpile' or press Ctrl+Enter, and it should resolve the issue. Otherwise, it could be an error in your code or possibly an issue with the transpiler itself.

#### Install localy

1. Clone this repository
2. The tarnspiler is HTpy.py
3. You can make a .htpy file then use the HTpy.py to transpile it to python for example:
```
python HTpy.py file_name.htpy
```
or (optional) add run to run it immediately after
```
python HTpy.py file_name.htpy run
```
you should get a .py file whit the same name as the .htpy
When you transpile the .htpy script it will replace the .py whit the same name if it exists.

I recommend using SciTE4HTH where i added HTpy support.

Why use SciTE4HTH for HTpy?
- It provides syntax highlighting and code completion for the HTpy language, making it easier to write and read HTpy scripts.

How to use SciTE4HTH for HTpy:
1. Download and install the SciTE4HTH editor from https://github.com/TheMaster1127/SciTE4HTH
2. Go to the htpy.properties and put the full path of your HTpy.py then restart the SciTE editor by re-opening it.
3. Open SciTE and create a new file with the .htpy extension (or open an existing .htpy file).
4. Write your HTpy code in the editor. You'll get syntax highlighting and code completion as you type.
5. To transpile your HTpy code to Python, simply press F5 or click the "Run" button. This will execute the transpiled Python code.
6. If you just want to transpile without running, press Ctrl+F7 or go to Tools > Compile.

That's it! SciTE4HTH gives you a user-friendly environment to write HTpy scripts, with helpful features like syntax highlighting and code completion, while allowing you to easily transpile to Python code with just a few clicks or keystrokes.

#### Usage Example

HTpy currently supports a subset of commands similar to AutoHotkey:

- `msgbox`: Display a message box.
- `sleep`: Pause script execution for a specified duration.
- Variables: Declare and manipulate variables.
- `Random`: Generate random numbers within specified ranges.
- `if`, `else if`, `else`
- `Loop, `
- Functions
- return
- Loop, Parse

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
    Loop
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
    for A_Index1, value in enumerate(iter(int, 1), start=1):
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

Here is another exmaple whit a Loop, Parse

```ahk
var1 := "item1|item2|item3|item4"
Loop, Parse, var1, "|"
{
msgbox, % A_Index
msgbox, % A_LoopField 
}


var2 := "item1`nitem2`ritem3`nitem4"
Loop, Parse, var2, `n, `r
{
msgbox, % A_Index
msgbox, % A_LoopField 
}



Loop, 4
{
msgbox, % A_Index
Loop, 4
{
msgbox, % A_Index
}

msgbox, % A_Index
}
```

---> in python

```py
# Define a dictionary to store dynamic variables
variables = {}


def LoopParseFunc(var, delimiter1="", delimiter2=""):
    import re
    if not delimiter1 and not delimiter2:
        # If no delimiters are provided, return a list of characters
        items = list(var)
    else:
        # Construct the regular expression pattern for splitting the string
        pattern = r'[' + re.escape(delimiter1) + re.escape(delimiter2) + r']+'
        # Split the string using the constructed pattern
        items = re.split(pattern, var)
    return items

variables['var1'] = "item1|item2|item3|item4"
items = LoopParseFunc(variables['var1'], "|", "")
for variables['A_Index1'], variables['A_LoopField1'] in enumerate(items, start=1):
    print(variables['A_Index1'])
    print(variables['A_LoopField1'])

variables['var2'] = "item1\nitem2\ritem3\nitem4"
items = LoopParseFunc(variables['var2'], "\n", "\r")
for variables['A_Index2'], variables['A_LoopField2'] in enumerate(items, start=1):
    print(variables['A_Index2'])
    print(variables['A_LoopField2'])

for variables['A_Index3'] in range(1, 4 + 1):
    print(variables['A_Index3'])
    for variables['A_Index4'] in range(1, 4 + 1):
        print(variables['A_Index4'])
    
    print(variables['A_Index3'])
```
