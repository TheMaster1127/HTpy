### HTpy: Early Development Preview

**HTpy** is a custom scripting language designed to transpile AHK-like syntax files into Python scripts. It allows users to write scripts using HTpy syntax and convert them into executable Python code.

**Note:** This project is still in its early stages of development.

#### Try It Out

You can experiment with HTpy syntax using the [HTpy online editor](https://themaster1127.github.io/HTpy/). Note that this editor provides only a subset of HTpy functionality.

#### Usage Example

HTpy currently supports a subset of commands similar to AutoHotkey:

- `msgbox`: Display a message box.
- `sleep`: Pause script execution for a specified duration.
- Variables: Declare and manipulate variables.
- `Random`: Generate random numbers within specified ranges.

HTpy will automatically import the python library we need. 

Here's an example of HTpy syntax:

```ahk
var1 := "Python is not so bad!"
MsgBox, %var1%
num := 42
var%num% := num
MsgBox, %var42%

var23 := (55 + 3) - 1 . var%num%
MsgBox, %var23%
Sleep, 600
var1 := true
var2 := false
MsgBox, %var1%
MsgBox, %var2%

somNumber := 55
somNumber += somNumber
somNumber += somNumber
somNumber += somNumber
somNumber += somNumber
MsgBox, %somNumber%

Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
```

-----> in python

```py
import time
import random

# Define a dictionary to store dynamic variables
variables = {}

variables['var1'] = "Python is not so bad!"
print(variables['var1'])
variables['num'] = 42
variables[f'var{variables["num"]}'] = variables['num']
print(variables['var42'])

variables['var23'] =  ( 55 + 3 )  - 1 + variables[f'var{variables["num"]}']
print(variables['var23'])
time.sleep(600 / 1000)
variables['var1'] = True
variables['var2'] = False
print(variables['var1'])
print(variables['var2'])

variables['somNumber'] = 55
variables['somNumber'] += variables['somNumber']
variables['somNumber'] += variables['somNumber']
variables['somNumber'] += variables['somNumber']
variables['somNumber'] += variables['somNumber']
print(variables['somNumber'])

variables['someRandomNums'] = random.randint(1, 20)
print(variables['someRandomNums'])
variables['someRandomNums'] = random.randint(1, 20)
print(variables['someRandomNums'])
variables['someRandomNums'] = random.randint(1, 20)
print(variables['someRandomNums'])
variables['someRandomNums'] = random.randint(1, 20)
print(variables['someRandomNums'])
variables['someRandomNums'] = random.randint(1, 20)
print(variables['someRandomNums'])
variables['someRandomNums'] = random.randint(1, 20)
print(variables['someRandomNums'])
variables['someRandomNums'] = random.randint(1, 20)
print(variables['someRandomNums'])
```
