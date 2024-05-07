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


def InStr(Haystack, Needle, CaseSensitive=True, StartingPos=1, Occurrence=1):
    if Haystack is None or Needle is None:
        return False
    StartingPos = max(StartingPos, 1)
    if not CaseSensitive:
        Haystack = Haystack.lower()
        Needle = Needle.lower()
    count = 0
    for i in range(StartingPos - 1, len(Haystack)):
        if Haystack[i:i + len(Needle)] == Needle:
            count += 1
            if count == Occurrence:
                return True
    return False  

def SubStr(str, startPos, length=None):
    if str is None or str == "":
        return ""

    if length is None or length == "":
        length = len(str) - startPos + 1

    if startPos < 1:
        startPos = len(str) + startPos

    return str[startPos - 1:startPos - 1 + length]

def Trim(inputString):
    if inputString is None:
        return ""

    return inputString.strip()
  
def StrReplace(originalString, find, replaceWith):
    # Use the replace method to replace occurrences of 'find' with 'replaceWith'
    return originalString.replace(find, replaceWith)

def StringTrimLeft(input, numChars):
    # Convert input to a string if it's not already a string
    if not isinstance(input, str):
        input = str(input)  # Convert input to string

    # Check if the input is long enough to perform trimming
    if len(input) >= numChars:
        return input[numChars:]  # Trim the string from the left
    else:
        return input  # Return input unchanged if numChars is larger than string length

def StringTrimRight(input, numChars):
    # Convert input to a string if it's not already a string
    if not isinstance(input, str):
        input = str(input)  # Convert input to string

    # Check if the input is long enough to perform trimming
    if len(input) >= numChars:
        return input[:-numChars]  # Trim the string from the right
    else:
        return input  # Return input unchanged if numChars is larger than string length

def StrLower(string):
    return string.lower()

def RegExReplace(inputStr, regexPattern, replacement):
    # Create a regular expression object using the provided pattern
    import re
    regex = re.compile(regexPattern, re.MULTILINE)  # re.MULTILINE for multi-line matching

    # Use the sub() method to perform the regex replacement
    resultStr = regex.sub(replacement, inputStr)

    # Return the modified string
    return resultStr

def StrSplit(inputStr, delimiter, num):
    # Split the input string based on the delimiter
    parts = inputStr.split(delimiter)

    # Return the part specified by the num parameter (1-based index)
    if 0 < num <= len(parts):
        return parts[num - 1]  # Return the specified part (0-based index)
    else:
        return ''  # Return an empty string if num is out of range

def Chr(number):
    # Check if the number is None
    if number is None:
        # Return an empty string
        return ""

    # Check if the number is within the valid Unicode range
    if 0 <= number <= 0x10FFFF:
        # Convert the number to a character using chr()
        return chr(number)
    else:
        # Return an empty string for invalid numbers
        return ""


# Custom Mod function in Python
def Mod(dividend, divisor):
    return dividend % divisor

def HTpy():
    import sys
    import os
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python app.py <input_file.htpy> [run]")
        sys.exit(1)

    input_file = sys.argv[1]

    # Ensure the input_file ends with '.htpy'
    if not input_file.endswith('.htpy'):
        print("Error: Input file must have a .htpy extension.")
        sys.exit(1)

    # Check if the input_file exists
    if not os.path.isfile(input_file):
        print(f"Error: '{input_file}' is not a valid file path.")
        sys.exit(1)

    # Determine the output .py file name based on input file name
    output_file = os.path.splitext(input_file)[0] + '.py'

    # Compile the .htpy content using the compiler function
    with open(input_file, 'r') as file:
        htpy_content = file.read()

    compiled_result = compiler(htpy_content)

    # Save the compiled result to the determined .py output file
    with open(output_file, 'w') as file:
        file.write(compiled_result)

    print(f"Compiled result saved to '{output_file}'.")

    # Check if 'run' parameter is provided and execute the compiled Python script
    if len(sys.argv) == 3 and sys.argv[2] == 'run':
        print(f"Running '{output_file}'...")
        try:
            exec(compile(open(output_file).read(), output_file, 'exec'), globals())
        except Exception as e:
            print(f"Error occurred while running the compiled file: {e}")


def indent_nested_curly_braces(input_string):
    variables['input_string'] = input_string
    variables['indent_size'] = 4
    variables['current_indent'] = 0
    variables['result'] = ""
    #MsgBox, % input_string
    variables['input_string'] = variables['input_string']
    items = LoopParseFunc(variables['input_string'], "\n", "\r")
    for A_Index1, A_LoopField1 in enumerate(items, start=1):
        variables['A_Index1'] = A_Index1
        variables['A_LoopField1'] = A_LoopField1
        variables['trimmed_line'] = Trim(variables['A_LoopField1'])
        if (variables['trimmed_line'] == Chr(123)):
            variables['result'] += ((Chr(32) +  RepeatSpaces(variables['current_indent']))  + (variables['trimmed_line']  +  "\n"))
            variables['current_indent'] = variables['current_indent'] + variables['indent_size']
        elif (variables['trimmed_line'] == Chr(125)):
            variables['current_indent'] = variables['current_indent'] - variables['indent_size']
            variables['result'] += ((Chr(32) +  RepeatSpaces(variables['current_indent']))  + (variables['trimmed_line']  +  "\n"))
        else:
            variables['result'] += ((Chr(32) +  RepeatSpaces(variables['current_indent']))  + (variables['trimmed_line']  +  "\n"))
    # Return the result
    return variables['result']
def RepeatSpaces(count):
    variables['count'] = count
    variables['spaces'] = ""
    for A_Index2 in range(1, variables['count'] + 1):
        variables['A_Index2'] = A_Index2
        variables['spaces'] += Chr(32)
    return variables['spaces']
def ifTheLineIsAFuncDec(strgjvkh, theFuncWeFound):
    variables['strgjvkh'] = strgjvkh
    variables['theFuncWeFound'] = theFuncWeFound
    items = LoopParseFunc(variables['theFuncWeFound'], "\n", "\r")
    for A_Index3, A_LoopField3 in enumerate(items, start=1):
        variables['A_Index3'] = A_Index3
        variables['A_LoopField3'] = A_LoopField3
        variables['numOfChars'] = 0
        items = LoopParseFunc(variables['A_LoopField3'])
        for A_Index4, A_LoopField4 in enumerate(items, start=1):
            variables['A_Index4'] = A_Index4
            variables['A_LoopField4'] = A_LoopField4
            variables['numOfChars'] += 1
        variables['ALoopFieldd'] = StrSplit(variables['A_LoopField3'] , Chr(40), 1)
        variables['ALoopFieldd2'] = StrSplit(variables['strgjvkh'] , Chr(40), 1)
        if (SubStr(variables['ALoopFieldd'] , 1 , variables['numOfChars'])== variables['ALoopFieldd2'])and(InStr(variables['strgjvkh'] , Chr(40))):
            return True
    return False
def isVarAnumKindaVar(strrrrr):
    variables['strrrrr'] = strrrrr
    variables['strLettersStart'] = 48
    for A_Index5 in range(1, 10 + 1):
        variables['A_Index5'] = A_Index5
        if (InStr(variables['strrrrr'] , Chr(variables['strLettersStart']))):
            return True
        variables['strLettersStart'] += 1
    if (InStr(variables['strrrrr'] , Chr(95))):
        return True
    return False
def varDetect(strrrrr):
    variables['strrrrr'] = strrrrr
    variables['strLettersStart'] = 97
    for A_Index6 in range(1, 26 + 1):
        variables['A_Index6'] = A_Index6
        if (InStr(variables['strrrrr'] , Chr(variables['strLettersStart']))):
            return True
        variables['strLettersStart'] += 1
    variables['strLettersStart'] = 65
    for A_Index7 in range(1, 26 + 1):
        variables['A_Index7'] = A_Index7
        if (InStr(variables['strrrrr'] , Chr(variables['strLettersStart']))):
            return True
        variables['strLettersStart'] += 1
    variables['strLettersStart'] = 48
    for A_Index8 in range(1, 10 + 1):
        variables['A_Index8'] = A_Index8
        if (InStr(variables['strrrrr'] , Chr(variables['strLettersStart']))):
            return True
        variables['strLettersStart'] += 1
    if (InStr(variables['strrrrr'] , Chr(95))):
        return True
    if (InStr(variables['strrrrr'] , Chr(37))):
        return True
    return False
def funcToChecIfVaidNameForFunc(strrrrr):
    variables['strrrrr'] = strrrrr
    # Check if the string is empty
    if ( not (variables['strrrrr'])):
        #MsgBox, Invalid function name: %strrrrr% (empty string)
        return False
    # Check if the first character is a digit (invalid for function name)
    variables['firstChar'] = SubStr(variables['strrrrr'] , 1 , 1)
    if (variables['firstChar'] >= "0" and variables['firstChar'] <= "9"):
        #   MsgBox, Invalid function name: %strrrrr% (starts with a digit)
        return False
    # Initialize a flag for validation
    variables['isValid'] = True
    # Loop through each character in the string using Loop, Parse
    items = LoopParseFunc(variables['strrrrr'])
    for A_Index9, A_LoopField9 in enumerate(items, start=1):
        variables['A_Index9'] = A_Index9
        variables['A_LoopField9'] = A_LoopField9
        # Check the current parsed item (character)
        variables['char'] = variables['A_LoopField9']
        # Check if the character is a valid letter, digit, or underscore
        if ( not (variables['char'] >= "A" and variables['char'] <= "Z" or variables['char'] >= "a" and variables['char'] <= "z" or variables['char'] >= "0" and variables['char'] <= "9" or variables['char'] == "_")):
            # MsgBox, Invalid character %char% in function name: %strrrrr%
            variables['isValid'] = False
            break
    # If passed all checks, return true (valid function name)
    return variables['isValid']
def transpileVariables(str123455, functionNames):
    variables['str123455'] = str123455
    variables['functionNames'] = functionNames
    variables['str123455'] = Trim(variables['str123455'])
    variables['numOfStrings'] = 0
    variables['outOftranspileVariables'] = ""
    variables['outOftranspileVariablesOut'] = variables['str123455']
    variables['outOftranspileVariablesOut'] = StrReplace(variables['outOftranspileVariablesOut'] , Chr(40), " ( ")
    variables['outOftranspileVariablesOut'] = StrReplace(variables['outOftranspileVariablesOut'] , Chr(41), " ) ")
    variables['outOftranspileVariablesOut'] = StrReplace(variables['outOftranspileVariablesOut'] , Chr(44), " , ")
    variables['outOftranspileVariablesOut'] = StrReplace(variables['outOftranspileVariablesOut'] , Chr(60), " < ")
    variables['outOftranspileVariablesOut'] = StrReplace(variables['outOftranspileVariablesOut'] , Chr(62), " > ")
    variables['outOftranspileVariablesOut'] = StrReplace(variables['outOftranspileVariablesOut'] , Chr(91), " [ ")
    variables['outOftranspileVariablesOut'] = StrReplace(variables['outOftranspileVariablesOut'] , Chr(93), " ] ")
    variables['wasHereVarTryUhBug'] = 1
    items = LoopParseFunc(variables['outOftranspileVariablesOut'], " ")
    for A_Index10, A_LoopField10 in enumerate(items, start=1):
        variables['A_Index10'] = A_Index10
        variables['A_LoopField10'] = A_LoopField10
        variables['howManyCharIfVar'] = 0
        items = LoopParseFunc(variables['A_LoopField10'])
        for A_Index11, A_LoopField11 in enumerate(items, start=1):
            variables['A_Index11'] = A_Index11
            variables['A_LoopField11'] = A_LoopField11
            if (varDetect(variables['A_LoopField11'])):
                variables['howManyCharIfVar'] += 1
        variables['howManyCharIfVar2'] = 0
        items = LoopParseFunc(variables['A_LoopField10'])
        for A_Index12, A_LoopField12 in enumerate(items, start=1):
            variables['A_Index12'] = A_Index12
            variables['A_LoopField12'] = A_LoopField12
            variables['howManyCharIfVar2'] += 1
        variables['istAvar'] = 0
        if (variables['howManyCharIfVar'] == variables['howManyCharIfVar2']):
            variables['istAvar'] = 1
        if (variables['istAvar'] == 1):
            variables['howManyCharIfVar'] = 0
            items = LoopParseFunc(variables['A_LoopField10'])
            for A_Index13, A_LoopField13 in enumerate(items, start=1):
                variables['A_Index13'] = A_Index13
                variables['A_LoopField13'] = A_LoopField13
                if (isVarAnumKindaVar(variables['A_LoopField13'])):
                    variables['howManyCharIfVar'] += 1
            variables['howManyCharIfVar2'] = 0
            items = LoopParseFunc(variables['A_LoopField10'])
            for A_Index14, A_LoopField14 in enumerate(items, start=1):
                variables['A_Index14'] = A_Index14
                variables['A_LoopField14'] = A_LoopField14
                variables['howManyCharIfVar2'] += 1
            variables['isNumKindaVar'] = 0
            if (variables['howManyCharIfVar2'] == variables['howManyCharIfVar']):
                variables['isNumKindaVar'] = 1
            if (variables['isNumKindaVar'] == 1):
                variables['outOftranspileVariables'] += variables['A_LoopField10']  +  Chr(32)
            else:
                if (InStr(variables['A_LoopField10'] , "%")):
                    variables['var1'] = StrSplit(variables['A_LoopField10'] , "%" , 1)
                    variables['var2'] = StrSplit(variables['A_LoopField10'] , "%" , 2)
                    variables['out1'] = "variables[f"  +  Chr(39) +  variables['var1']  +  "{variables["  +  Chr(34) +  variables['var2']  +  Chr(34) +  "]}"  +  Chr(39) +  "]"
                    variables['outOftranspileVariables'] += variables['out1']  +  Chr(32)
                else:
                    variables['out1'] = "variables["  +  Chr(39) +  variables['A_LoopField10']  +  Chr(39) +  "]"
                    variables['outOftranspileVariables'] += variables['out1']  +  Chr(32)
        else:
            variables['outOftranspileVariables'] += variables['A_LoopField10']  +  Chr(32)
        variables['wasHereVarTryUhBug'] = 0
    if (variables['wasHereVarTryUhBug'] == 1):
        variables['outOftranspileVariables'] = variables['outOftranspileVariablesOut']
    #OutputDebug, |%outOftranspileVariables%|
    items = LoopParseFunc(variables['functionNames'], "|")
    for A_Index15, A_LoopField15 in enumerate(items, start=1):
        variables['A_Index15'] = A_Index15
        variables['A_LoopField15'] = A_LoopField15
        variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "variables['"  +  variables['A_LoopField15']  +  "']" , variables['A_LoopField15'])
    for A_Index16 in range(1, variables['numOfStrings'] + 1):
        variables['A_Index16'] = A_Index16
        variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "freeeeepaestine-sav-etehmtyeah-freee-n"  +  variables['A_Index16'] , Chr(34) +  variables[f'theString{variables["A_Index16"]}']  +  Chr(34))
    variables['weEverUseVars'] = "# Define a dictionary to store dynamic variables\nvariables = {}\n\n"
    #OutputDebug, |%outOftranspileVariables%|
    variables['outOftranspileVariables'] = Trim(variables['outOftranspileVariables'])
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , Chr(96), Chr(92))
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , Chr(92) +  Chr(92), Chr(96))
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "cyiasasasasstAYtheummonlyemlpystringya-a-"  +  Chr(100), Chr(34) +  Chr(34))
    #OutputDebug, %outOftranspileVariables%
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "variables['True']" , "True")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "variables['False']" , "False")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "variables['true']" , "True")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "variables['false']" , "False")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "variables['if']" , "if")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "variables['else']" , "else")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "variables['and']" , "and")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "variables['or']" , "or")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "!" , " not ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " && " , " and ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " || " , " or ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " < = " , " <= ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " > = " , " >= ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "not ==" , " != ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "  not == " , " != ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " not == " , " != ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " not ==" , " != ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "not ==" , " != ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "  not = " , " != ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "not =" , " != ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " = " , " == ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " = " , " == ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " ( " , Chr(40))
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " ) " , Chr(41))
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " )" , Chr(41))
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " < " , Chr(60))
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " > " , Chr(62))
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "  >= " , " >= ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "  <= " , " <= ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "." , " + ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " ,  " , ", ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " [ " , "[")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " ] " , "]")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "!=" , " !=")
    #OutputDebug, %outOftranspileVariables%
    return variables['outOftranspileVariables']
def transpileLowVariables(sstr):
    variables['sstr'] = sstr
    variables['sstr'] = Trim(variables['sstr'])
    variables['outOftranspileVariablesOut'] = Chr(34)
    if (InStr(variables['sstr'] , Chr(37))):
        items = LoopParseFunc(variables['sstr'], "%")
        for A_Index17, A_LoopField17 in enumerate(items, start=1):
            variables['A_Index17'] = A_Index17
            variables['A_LoopField17'] = A_LoopField17
            if (Mod(variables['A_Index17'] , 2)):
                variables['outOftranspileVariablesOut'] += variables['A_LoopField17']
            else:
                variables['outOftranspileVariablesOut'] += Chr(34) +  " + variables['"  +  variables['A_LoopField17']  +  Chr(39) +  Chr(93) +  " + "  +  Chr(34)
    else:
        variables['sstr'] = Chr(34) +  variables['sstr']  +  Chr(34)
        return variables['sstr']
    variables['outOftranspileVariablesOut'] = variables['outOftranspileVariablesOut']  +  Chr(34)
    return variables['outOftranspileVariablesOut']
# the compiler
def compiler(HTpyCode):
    variables['HTpyCode'] = HTpyCode
    variables['pyCode'] = ""
    variables['out'] = ""
    variables['HTpyCodeD1'] = ""
    variables['skipLeftCuleyForFuncPLS'] = 0
    variables['eavbnsalvbaslv'] = 0
    items = LoopParseFunc(variables['HTpyCode'], "\n", "\r")
    for A_Index18, A_LoopField18 in enumerate(items, start=1):
        variables['A_Index18'] = A_Index18
        variables['A_LoopField18'] = A_LoopField18
        if (variables['A_Index18'] == 1):
            variables['HTpyCodeD1'] += Trim(variables['A_LoopField18']) +  "\n"
        else:
            if (Trim(variables['A_LoopField18'])== Chr(123)) and(variables['eavbnsalvbaslv'] == 1):
                # nothing
                variables['nothing'] = ""
            else:
                variables['HTpyCodeD1'] += Trim(variables['A_LoopField18']) +  "\n"
            variables['eavbnsalvbaslv'] = 0
            if (Trim(variables['A_LoopField18'])== ""):
                variables['eavbnsalvbaslv'] = 1
    variables['HTpyCode'] = StringTrimRight(variables['HTpyCodeD1'], 1)
    variables['HTpyCodeOUT754754'] = ""
    variables['areWEinSome34sNum'] = 0
    variables['theIdNumOfThe34'] = 0
    items = LoopParseFunc(variables['HTpyCode'])
    for A_Index19, A_LoopField19 in enumerate(items, start=1):
        variables['A_Index19'] = A_Index19
        variables['A_LoopField19'] = A_LoopField19
        variables[f'theIdNumOfThe34theVar{variables["A_Index19"]}'] = Chr(34)
    items = LoopParseFunc(variables['HTpyCode'])
    for A_Index20, A_LoopField20 in enumerate(items, start=1):
        variables['A_Index20'] = A_Index20
        variables['A_LoopField20'] = A_LoopField20
        if (variables['A_LoopField20'] == Chr(34)):
            variables['areWEinSome34sNum'] += 1
        if (variables['areWEinSome34sNum'] == 1):
            if (variables['A_LoopField20']  != Chr(34)):
                if (variables['A_LoopField20'] == Chr(96)):
                    variables[f'theIdNumOfThe34theVar{variables["theIdNumOfThe34"]}'] += Chr(92)
                else:
                    variables[f'theIdNumOfThe34theVar{variables["theIdNumOfThe34"]}'] += variables['A_LoopField20']
            else:
                variables['theIdNumOfThe34'] += 1
                variables['HTpyCodeOUT754754'] += "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-"  +  Chr(65) +  Chr(65) +  str(variables['theIdNumOfThe34']) +  Chr(65) +  Chr(65)
        if (variables['areWEinSome34sNum'] == 2)or(variables['areWEinSome34sNum'] == 0):
            if (variables['A_LoopField20']  != Chr(34)):
                variables['HTpyCodeOUT754754'] += variables['A_LoopField20']
            variables['areWEinSome34sNum'] = 0
    variables['HTpyCode'] = variables['HTpyCodeOUT754754']
    for A_Index21 in range(1, variables['theIdNumOfThe34'] + 1):
        variables['A_Index21'] = A_Index21
        variables[f'theIdNumOfThe34theVar{variables["A_Index21"]}'] += Chr(34)
    variables['str23IfFuncInNAMEnum'] = 0
    variables['CheckIFandElsesss1'] = "if ("
    variables['CheckIFandElsesss2'] = "if("
    variables['CheckIFandElsesss3'] = "if !("
    variables['CheckIFandElsesss4'] = "if!("
    variables['CheckIFandElsesss5'] = "else if ("
    variables['CheckIFandElsesss6'] = "else if("
    variables['CheckIFandElsesss7'] = "else if !("
    variables['CheckIFandElsesss8'] = "else if!("
    variables['CheckIFandElsesssNum'] = 0
    variables['functionNames'] = "input|int|chr|str|InStr|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|StrLower|RegExReplace|StrSplit|Chr|Mod|HTpy"
    variables['awesdrtf'] = "|A"  +  Chr(95) +  "LoopField|A"  +  Chr(95) +  "Index"
    variables['willNextLineBeCurlyBracee'] = 0
    variables['theFuncWeFound'] = ""
    variables['theFuncWeFoundAllNames'] = ""
    variables['haveWeEverUsedAloop'] = 0
    #OutputDebug, %HTpyCode%
    items = LoopParseFunc(variables['HTpyCode'], "\n", "\r")
    for A_Index22, A_LoopField22 in enumerate(items, start=1):
        variables['A_Index22'] = A_Index22
        variables['A_LoopField22'] = A_LoopField22
        if (variables['willNextLineBeCurlyBracee'] == 1):
            # 123 is {
            if (variables['A_LoopField22'] == Chr(123)):
                variables['willNextLineBeCurlyBracee'] = 0
                variables['functionNames'] += "|"  +  variables['lastFuncName']
                #lastFuncFullName
                variables['theFuncWeFound'] += variables['lastFuncFullName']  +  "\n"
                variables['theFuncWeFoundAllNames'] += variables['lastFuncName']  +  Chr(40) +  "\n"
        if (SubStr(StrLower(variables['A_LoopField22']), 1 , 4)== variables['CheckIFandElsesss1'])or(SubStr(StrLower(variables['A_LoopField22']), 1 , 3)== variables['CheckIFandElsesss2'])or(SubStr(StrLower(variables['A_LoopField22']), 1 , 5)== variables['CheckIFandElsesss3'])or(SubStr(StrLower(variables['A_LoopField22']), 1 , 4)== variables['CheckIFandElsesss4'])or(SubStr(StrLower(variables['A_LoopField22']), 1 , 9)== variables['CheckIFandElsesss5'])or(SubStr(StrLower(variables['A_LoopField22']), 1 , 8)== variables['CheckIFandElsesss6'])or(SubStr(StrLower(variables['A_LoopField22']), 1 , 10)== variables['CheckIFandElsesss7'])or(SubStr(StrLower(variables['A_LoopField22']), 1 , 9)== variables['CheckIFandElsesss8'])or(SubStr(StrLower(variables['A_LoopField22']), 1 , 5)== "loop,"):
            # not a func
            variables['willNextLineBeCurlyBracee'] = 0
            #OutputDebug, %A_LoopField22%
        else:
            #OutputDebug, ||%A_LoopField22%||
            variables['strForCheckIfFunc'] = StrSplit(variables['A_LoopField22'] , Chr(40), 1)
            #OutputDebug, |%strForCheckIfFunc%|
            if (funcToChecIfVaidNameForFunc(Trim(variables['strForCheckIfFunc'])))and(variables['strForCheckIfFunc']  != "")and(InStr(variables['A_LoopField22'] , Chr(40))):
                variables['willNextLineBeCurlyBracee'] = 1
                variables['lastFuncName'] = variables['strForCheckIfFunc']
                variables['lastFuncFullName'] = variables['A_LoopField22']
                #OutputDebug, %lastFuncFullName%
            else:
                variables['willNextLineBeCurlyBracee'] = 0
    variables['theFuncWeFound'] = StringTrimRight(variables['theFuncWeFound'], 1)
    variables['theFuncWeFoundAllNames'] = StringTrimRight(variables['theFuncWeFoundAllNames'], 1)
    #OutputDebug, %theFuncWeFound%
    #OutputDebug, %functionNames%
    #OutputDebug, %theFuncWeFoundAllNames%
    variables['onceImportTime'] = 0
    variables['weUseRandomAtLeastOnce'] = 0
    variables['weEverUseVars'] = ""
    variables['usedLib'] = ""
    variables['putEndPointFlask1Up'] = ""
    variables['putEndPointFlask2Down'] = ""
    variables['AindexcharLength'] = 1
    variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 0
    variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 0
    variables['pycodeLoopfixa'] = ""
    items = LoopParseFunc(variables['HTpyCode'], "\n", "\r")
    for A_Index23, A_LoopField23 in enumerate(items, start=1):
        variables['A_Index23'] = A_Index23
        variables['A_LoopField23'] = A_LoopField23
        variables['lineDone'] = 0
        if (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 10)== StrLower("msgbox, % ")):
            variables['var1'] = StringTrimLeft(variables['A_LoopField23'], 10)
            variables['var2'] = Trim(transpileVariables(variables['var1'] , variables['functionNames']))
            variables['out'] = "print("  +  variables['var2']  +  ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 8)== StrLower("msgbox, ")) and(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 10) != StrLower("msgbox, % ")):
            variables['var1'] = StringTrimLeft(variables['A_LoopField23'], 8)
            variables['OUTvarMsgLow'] = transpileLowVariables(variables['var1'])
            variables['out'] = "print("  +  variables['OUTvarMsgLow']  +  ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 8)== StrLower("Random, ")):
            variables['varr1'] = StrSplit(variables['A_LoopField23'] , "," , 2)
            variables['varr2'] = StrSplit(variables['A_LoopField23'] , "," , 3)
            variables['varr3'] = StrSplit(variables['A_LoopField23'] , "," , 4)
            variables['outt1'] = Trim(transpileVariables(variables['varr1'] , variables['functionNames']))
            variables['outt2'] = Trim(transpileVariables(variables['varr2'] , variables['functionNames']))
            variables['outt3'] = Trim(transpileVariables(variables['varr3'] , variables['functionNames']))
            variables['weUseRandomAtLeastOnce'] += 1
            if (variables['weUseRandomAtLeastOnce'] == 1):
                variables['usedLib'] += "import random\n"
            variables['out'] = variables['outt1']  +  " = "  +  "random.randint("  +  variables['outt2']  +  ", "  +  variables['outt3']  +  ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 17)== StrLower("StringTrimRight, ")):
            variables['varr1'] = StrSplit(variables['A_LoopField23'] , "," , 2)
            variables['varr2'] = StrSplit(variables['A_LoopField23'] , "," , 3)
            variables['varr3'] = StrSplit(variables['A_LoopField23'] , "," , 4)
            variables['outt1'] = Trim(transpileVariables(variables['varr1'] , variables['functionNames']))
            variables['outt2'] = Trim(transpileVariables(variables['varr2'] , variables['functionNames']))
            variables['outt3'] = Trim(transpileVariables(variables['varr3'] , variables['functionNames']))
            variables['out'] = variables['outt1']  +  " = "  +  "StringTrimRight("  +  variables['outt2']  +  ", "  +  variables['outt3']  +  ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 16)== StrLower("StringTrimLeft, ")):
            variables['varr1'] = StrSplit(variables['A_LoopField23'] , "," , 2)
            variables['varr2'] = StrSplit(variables['A_LoopField23'] , "," , 3)
            variables['varr3'] = StrSplit(variables['A_LoopField23'] , "," , 4)
            variables['outt1'] = Trim(transpileVariables(variables['varr1'] , variables['functionNames']))
            variables['outt2'] = Trim(transpileVariables(variables['varr2'] , variables['functionNames']))
            variables['outt3'] = Trim(transpileVariables(variables['varr3'] , variables['functionNames']))
            variables['out'] = variables['outt1']  +  " = "  +  "StringTrimLeft("  +  variables['outt2']  +  ", "  +  variables['outt3']  +  ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 7)== StrLower("sleep, ")):
            variables['var1'] = StringTrimLeft(variables['A_LoopField23'], 7)
            variables['var1'] = Trim(transpileVariables(variables['var1'] , variables['functionNames']))
            variables['out'] = "time.sleep("  +  variables['var1']  +  " / 1000"  +  ")"
            variables['lineDone'] = 1
            variables['onceImportTime'] += 1
            if (variables['onceImportTime'] == 1):
                variables['usedLib'] += "import time\n"
            variables['pyCode'] += variables['out']  +  "\n"
        elif (ifTheLineIsAFuncDec(Trim(variables['A_LoopField23']), variables['theFuncWeFound'])):
            #OutputDebug, %A_LoopField23%
            variables['str23IfFuncIn'] = variables['A_LoopField23']
            variables['str23IfFuncInNAME'] = StrSplit(variables['str23IfFuncIn'] , Chr(40), 1)
            variables['str23IfFuncIn'] = StrSplit(variables['str23IfFuncIn'] , Chr(40), 2)
            variables['nothing'] = ""
            variables['str23IfFuncInALL'] = StrReplace(variables['str23IfFuncIn'] , Chr(40), variables['nothing'])
            variables['str23IfFuncInALL'] = StrReplace(variables['str23IfFuncInALL'] , Chr(41), variables['nothing'])
            variables['wasHereInfuncAndgetingVar1'] = 0
            variables['theVarsPArmFormTheFunc'] = ""
            if (variables['str23IfFuncInALL']  != ""):
                items = LoopParseFunc(variables['str23IfFuncInALL'], ",")
                for A_Index24, A_LoopField24 in enumerate(items, start=1):
                    variables['A_Index24'] = A_Index24
                    variables['A_LoopField24'] = A_LoopField24
                    variables['wasHereInfuncAndgetingVar1'] = 1
                    variables['var1'] = Trim(variables['A_LoopField24'])
                    variables['theVarsPArmFormTheFunc'] += "variables['"  +  variables['var1']  +  "'] = "  +  variables['var1']  +  "\n"
            variables['skipLeftCuleyForFuncPLS'] = 0
            if (variables['str23IfFuncInALL']  != ""):
                variables['str234567'] = "def "  +  variables['str23IfFuncInNAME']  +  Chr(40) +  variables['str23IfFuncInALL']  +  Chr(41) +  ":\n{\n"  +  variables['theVarsPArmFormTheFunc']
                variables['skipLeftCuleyForFuncPLS'] = 1
            else:
                variables['str234567'] = "def "  +  variables['str23IfFuncInNAME']  +  Chr(40) +  variables['str23IfFuncInALL']  +  Chr(41) +  ":"
            for A_Index25 in range(1, variables['str23IfFuncInNAMEnum'] + 1):
                variables['A_Index25'] = A_Index25
                if (variables[f'str23IfFuncInNAME{variables["A_Index25"]}'] == variables['str23IfFuncInNAME']):
                    variables['var12312'] = ""
                    if (variables['str23IfFuncInALL']  != ""):
                        items = LoopParseFunc(variables['str23IfFuncInALL'], ",")
                        for A_Index26, A_LoopField26 in enumerate(items, start=1):
                            variables['A_Index26'] = A_Index26
                            variables['A_LoopField26'] = A_LoopField26
                            variables['wasHereInfuncAndgetingVar1'] = 1
                            variables['var1'] = Trim(variables['A_LoopField26'])
                            variables['var12312'] += transpileVariables(variables['var1'] , variables['functionNames']) +  ", "
                        variables['var12312'] = StringTrimRight(variables['var12312'], 2)
                    if (variables['wasHereInfuncAndgetingVar1'] == 0):
                        variables['str2345678'] = variables['str23IfFuncInNAME']  +  Chr(40) +  Chr(41)
                    else:
                        variables['str2345678'] = variables['str23IfFuncInNAME']  +  Chr(40) +  variables['var12312']  +  Chr(41)
                    variables['lineDone'] = 1
            variables['str23IfFuncInNAMEnum'] += 1
            variables[f'str23IfFuncInNAME{variables["str23IfFuncInNAMEnum"]}'] = variables['str23IfFuncInNAME']
            if (variables['lineDone'] == 1):
                variables['pyCode'] += variables['str2345678']  +  "\n"
            else:
                variables['lineDone'] = 1
                variables['pyCode'] += variables['str234567']  +  "\n"
        elif (SubStr(Trim(variables['A_LoopField23']), 1 , 7)== "return "):
            variables['strFormReturn'] = StringTrimLeft(variables['A_LoopField23'], 7)
            variables['var12312'] = transpileVariables(variables['strFormReturn'] , variables['functionNames'])
            variables['out'] = "return "  +  variables['var12312']
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (SubStr(Trim(variables['A_LoopField23']), 1 , 10)== "endpoint, "):
            variables['strFormEndpoint'] = StringTrimLeft(variables['A_LoopField23'], 10)
            variables['putEndPointFlask1Up'] = Chr(102) +  Chr(114) +  Chr(111) +  Chr(109) +  Chr(32) +  Chr(102) +  Chr(108) +  Chr(97) +  Chr(115) +  Chr(107) +  Chr(32) +  Chr(105) +  Chr(109) +  Chr(112) +  Chr(111) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(70) +  Chr(108) +  Chr(97) +  Chr(115) +  Chr(107) +  Chr(44) +  Chr(32) +  Chr(115) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(44) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(113) +  Chr(117) +  Chr(101) +  Chr(115) +  Chr(116) +  Chr(44) +  Chr(32) +  Chr(106) +  Chr(115) +  Chr(111) +  Chr(110) +  Chr(105) +  Chr(102) +  Chr(121) +  Chr(13) +  Chr(10) +  Chr(105) +  Chr(109) +  Chr(112) +  Chr(111) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(111) +  Chr(115) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(97) +  Chr(112) +  Chr(112) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(70) +  Chr(108) +  Chr(97) +  Chr(115) +  Chr(107) +  Chr(40) +  Chr(95) +  Chr(95) +  Chr(110) +  Chr(97) +  Chr(109) +  Chr(101) +  Chr(95) +  Chr(95) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(64) +  Chr(97) +  Chr(112) +  Chr(112) +  Chr(46) +  Chr(114) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(101) +  Chr(40) +  Chr(39) +  Chr(47) +  Chr(39) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(97) +  Chr(112) +  Chr(112) +  Chr(95) +  Chr(114) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(101) +  Chr(40) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(40) +  Chr(111) +  Chr(115) +  Chr(46) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(104) +  Chr(46) +  Chr(106) +  Chr(111) +  Chr(105) +  Chr(110) +  Chr(40) +  Chr(111) +  Chr(115) +  Chr(46) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(104) +  Chr(46) +  Chr(100) +  Chr(105) +  Chr(114) +  Chr(110) +  Chr(97) +  Chr(109) +  Chr(101) +  Chr(40) +  Chr(95) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(95) +  Chr(95) +  Chr(41) +  Chr(44) +  Chr(32) +  Chr(39) +  Chr(105) +  Chr(110) +  Chr(100) +  Chr(101) +  Chr(120) +  Chr(46) +  Chr(104) +  Chr(116) +  Chr(109) +  Chr(108) +  Chr(39) +  Chr(41) +  Chr(41) +  Chr(44) +  Chr(32) +  Chr(50) +  Chr(48) +  Chr(48) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10)
            variables['putEndPointFlask2Down'] = Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(64) +  Chr(97) +  Chr(112) +  Chr(112) +  Chr(46) +  Chr(101) +  Chr(114) +  Chr(114) +  Chr(111) +  Chr(114) +  Chr(104) +  Chr(97) +  Chr(110) +  Chr(100) +  Chr(108) +  Chr(101) +  Chr(114) +  Chr(40) +  Chr(52) +  Chr(48) +  Chr(52) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(111) +  Chr(117) +  Chr(110) +  Chr(100) +  Chr(40) +  Chr(101) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(34) +  Chr(80) +  Chr(97) +  Chr(103) +  Chr(101) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(117) +  Chr(110) +  Chr(100) +  Chr(34) +  Chr(44) +  Chr(32) +  Chr(52) +  Chr(48) +  Chr(52) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(95) +  Chr(95) +  Chr(110) +  Chr(97) +  Chr(109) +  Chr(101) +  Chr(95) +  Chr(95) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(39) +  Chr(95) +  Chr(95) +  Chr(109) +  Chr(97) +  Chr(105) +  Chr(110) +  Chr(95) +  Chr(95) +  Chr(39) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(97) +  Chr(112) +  Chr(112) +  Chr(46) +  Chr(114) +  Chr(117) +  Chr(110) +  Chr(40) +  Chr(104) +  Chr(111) +  Chr(115) +  Chr(116) +  Chr(61) +  Chr(39) +  Chr(48) +  Chr(46) +  Chr(48) +  Chr(46) +  Chr(48) +  Chr(46) +  Chr(48) +  Chr(39) +  Chr(44) +  Chr(32) +  Chr(112) +  Chr(111) +  Chr(114) +  Chr(116) +  Chr(61) +  Chr(56) +  Chr(48) +  Chr(48) +  Chr(48) +  Chr(44) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(98) +  Chr(117) +  Chr(103) +  Chr(61) +  Chr(84) +  Chr(114) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(13) +  Chr(10)
            variables['firstLineVar1'] = "@app.route('/"  +  variables['strFormEndpoint']  +  "', methods=['POST'])"
            variables['firstLineVar2'] = "def "  +  variables['strFormEndpoint']  +  "():"
            variables['firstLineVar3'] = "|request_data = request.get_json()"
            variables['out'] = variables['firstLineVar1']  +  "\n"  +  variables['firstLineVar2']  +  "\n"  +  variables['firstLineVar3']
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (StrLower(variables['A_LoopField23'])== "loop"):
            # infinity loops
            variables['haveWeEverUsedAloop'] = 1
            variables['lineDone'] = 1
            variables['var1'] = "for A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  " , value in enumerate(iter(int, 1), start=1):"
            variables['nothing'] = ""
            variables['AindexcharLengthStr'] = variables['nothing']  +  str(variables['AindexcharLength']) +  variables['nothing']
            variables['theFixTextLoopNL'] = "variables['A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  "'] = A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength'])
            variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
            variables['lineDone'] = 1
            variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength']) +  "\n"
            variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength'])
            variables['AindexcharLength'] += 1
            variables['pyCode'] += variables['pycodeLoopfixa1']  +  "\n"  +  variables['var1']  +  "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 6)== "loop, ")and(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 8) != "loop, % ")and(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 7) != "loop % ")and(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 11) != StrLower("Loop, Parse")):
            variables['str123'] = variables['A_LoopField23']
            #MsgBox, % str123
            variables['out2'] = StringTrimLeft(variables['str123'], 6)
            #MsgBox % out2
            #MsgBox, % out2
            variables['out2'] = Trim(variables['out2'])
            variables['myVar'] = variables['out2']
            variables['lineYGI'] = transpileVariables(variables['myVar'] , variables['functionNames'])
            variables['line'] = variables['lineYGI']
            variables['haveWeEverUsedAloop'] = 1
            #MsgBox, % line
            variables['var1'] = "for A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  " in range(1, "  +  variables['line']  +  " + 1):"
            variables['nothing'] = ""
            variables['AindexcharLengthStr'] = variables['nothing']  +  str(variables['AindexcharLength']) +  variables['nothing']
            variables['theFixTextLoopNL'] = "variables['A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  "'] = A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength'])
            variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
            variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength']) +  "\n"
            variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength'])
            variables['AindexcharLength'] += 1
            variables['lineDone'] = 1
            variables['pyCode'] += variables['pycodeLoopfixa1']  +  "\n"  +  variables['var1']  +  "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 8)== "loop, % "):
            variables['str123'] = variables['A_LoopField23']
            #MsgBox, % str123
            variables['out2'] = StringTrimLeft(variables['str123'], 8)
            #MsgBox % out2
            #MsgBox, % out2
            variables['out2'] = Trim(variables['out2'])
            variables['myVar'] = variables['out2']
            variables['lineYGI'] = transpileVariables(variables['myVar'] , variables['functionNames'])
            variables['line'] = variables['lineYGI']
            #MsgBox, % line
            variables['var1'] = "for A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  " in range(1, "  +  variables['line']  +  " + 1):"
            variables['nothing'] = ""
            variables['AindexcharLengthStr'] = variables['nothing']  +  str(variables['AindexcharLength']) +  variables['nothing']
            variables['theFixTextLoopNL'] = "variables['A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  "'] = A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength'])
            variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
            variables['haveWeEverUsedAloop'] = 1
            variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength']) +  "\n"
            variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength'])
            variables['AindexcharLength'] += 1
            variables['lineDone'] = 1
            variables['pyCode'] += variables['pycodeLoopfixa1']  +  "\n"  +  variables['var1']  +  "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 13)== StrLower("Loop, Parse, ")):
            variables['var1'] = variables['A_LoopField23']
            variables['lineDone'] = 1
            variables['var1'] = Trim(variables['var1'])
            variables['var1'] = StringTrimLeft(variables['var1'], 13)
            variables['line1'] = Trim(StrSplit(variables['var1'] , "," , 1))
            variables['line1'] = transpileVariables(variables['line1'] , variables['functionNames'])
            variables['line2'] = ""
            variables['line3'] = ""
            variables['itemsOut'] = ""
            variables['line2'] = Trim(StrSplit(variables['var1'] , "," , 2))
            variables['line3'] = Trim(StrSplit(variables['var1'] , "," , 3))
            if (InStr(variables['var1'] , Chr(96) +  ",")):
                variables['line2'] = Chr(34) +  ","  +  Chr(34)
                variables['itemsOut'] = "items = LoopParseFunc("  +  variables['line1']  +  ", "  +  variables['line2']  +  ")"
            else:
                if (variables['line2'] == "")and(variables['line3'] == ""):
                    # nothing so only each char
                    variables['itemsOut'] = "items = LoopParseFunc("  +  variables['line1']  +  ")"
                if (variables['line2']  != "")and(variables['line3'] == ""):
                    if (InStr(variables['line2'] , Chr(96))):
                        variables['line2'] = Chr(34) +  variables['line2']  +  Chr(34)
                    variables['itemsOut'] = "items = LoopParseFunc("  +  variables['line1']  +  ", "  +  variables['line2']  +  ")"
                if (variables['line2']  != "")and(variables['line3']  != ""):
                    if (InStr(variables['line2'] , Chr(96))):
                        variables['line2'] = Chr(34) +  variables['line2']  +  Chr(34)
                    if (InStr(variables['line3'] , Chr(96))):
                        variables['line3'] = Chr(34) +  variables['line3']  +  Chr(34)
                    variables['itemsOut'] = "items = LoopParseFunc("  +  variables['line1']  +  ", "  +  variables['line2']  +  ", "  +  variables['line3']  +  ")"
                variables['itemsOut'] = StrReplace(variables['itemsOut'] , Chr(96), Chr(92))
            variables['var1out'] = variables['itemsOut']  +  "\n"  +  "for A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  ", A"  +  Chr(95) +  "LoopField"  +  str(variables['AindexcharLength']) +  " in enumerate(items, start=1):"
            variables['nothing'] = ""
            variables['AindexcharLengthStr'] = variables['nothing']  +  str(variables['AindexcharLength']) +  variables['nothing']
            variables['theFixTextLoopLP'] = "variables['A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  "'] = A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  "\n"  +  "variables['A"  +  Chr(95) +  "LoopField"  +  str(variables['AindexcharLength']) +  "'] = A"  +  Chr(95) +  "LoopField"  +  str(variables['AindexcharLength'])
            variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 1
            variables['haveWeEverUsedAloop'] = 1
            variables['pycodeLoopfixa'] += "lp|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength']) +  "\n"
            variables['pycodeLoopfixa1'] = "lp|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength'])
            variables['AindexcharLength'] += 1
            variables['pyCode'] += variables['pycodeLoopfixa1']  +  "\n"  +  variables['var1out']  +  "\n"
        elif (SubStr(variables['A_LoopField23'] , -1)== "++"):
            variables['str123'] = Trim(variables['A_LoopField23'])
            variables['str123'] = StringTrimRight(variables['str123'], 2)
            variables['str123'] = Trim(transpileVariables(variables['str123'] , variables['functionNames']))
            variables['out'] = variables['str123']  +  " += 1"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (SubStr(variables['A_LoopField23'] , -1)== "--"):
            variables['str123'] = Trim(variables['A_LoopField23'])
            variables['str123'] = StringTrimRight(variables['str123'], 2)
            variables['str123'] = Trim(transpileVariables(variables['str123'] , variables['functionNames']))
            variables['out'] = variables['str123']  +  " -= 1"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 4)== StrLower(variables['CheckIFandElsesss1'])) or(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 3)== StrLower(variables['CheckIFandElsesss2'])) or(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 5)== StrLower(variables['CheckIFandElsesss3'])) or(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 4)== StrLower(variables['CheckIFandElsesss4'])) or(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 9)== StrLower(variables['CheckIFandElsesss5'])) or(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 8)== StrLower(variables['CheckIFandElsesss6'])) or(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 10)== StrLower(variables['CheckIFandElsesss7'])) or(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 9)== StrLower(variables['CheckIFandElsesss8'])):
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 4)== StrLower(variables['CheckIFandElsesss1'])):
                variables['CheckIFandElsesssNum'] = 4
                variables['CheckIFandElsesssNumNum'] = 1
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 3)== StrLower(variables['CheckIFandElsesss2'])):
                variables['CheckIFandElsesssNum'] = 3
                variables['CheckIFandElsesssNumNum'] = 2
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 5)== StrLower(variables['CheckIFandElsesss3'])):
                variables['CheckIFandElsesssNum'] = 5
                variables['CheckIFandElsesssNumNum'] = 3
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 4)== StrLower(variables['CheckIFandElsesss4'])):
                variables['CheckIFandElsesssNum'] = 4
                variables['CheckIFandElsesssNumNum'] = 4
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 9)== StrLower(variables['CheckIFandElsesss5'])):
                variables['CheckIFandElsesssNum'] = 9
                variables['CheckIFandElsesssNumNum'] = 5
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 8)== StrLower(variables['CheckIFandElsesss6'])):
                variables['CheckIFandElsesssNum'] = 8
                variables['CheckIFandElsesssNumNum'] = 6
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 10)== StrLower(variables['CheckIFandElsesss7'])):
                variables['CheckIFandElsesssNum'] = 10
                variables['CheckIFandElsesssNumNum'] = 7
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 9)== StrLower(variables['CheckIFandElsesss8'])):
                variables['CheckIFandElsesssNum'] = 9
                variables['CheckIFandElsesssNumNum'] = 8
            variables['str123'] = StringTrimLeft(variables['A_LoopField23'], variables['CheckIFandElsesssNum'])
            variables['str123'] = variables[f'CheckIFandElsesss{variables["CheckIFandElsesssNumNum"]}']  +  Chr(32) +  transpileVariables(variables['str123'] , variables['functionNames'])
            if (SubStr(Trim(StrLower(variables['str123'])) , 1 , 7)== StrLower("else if")):
                variables['str123'] = StrReplace(variables['str123'] , "else if" , "elif")
            else:
                variables['str123'] = variables['str123']
                variables['str123'] = StringTrimLeft(variables['str123'], 2)
                variables['str123'] = "if"  +  variables['str123']
            variables['str123'] = Trim(variables['str123']) +  ":"
            variables['str123'] = StrReplace(variables['str123'] , "if "  +  Chr(40) +  Chr(32), "if "  +  Chr(40))
            variables['str123'] = StrReplace(variables['str123'] , Chr(32) +  Chr(41) +  ":" , Chr(41) +  ":")
            variables['out'] = variables['str123']
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (StrLower(variables['A_LoopField23'])== StrLower("else")):
            variables['out'] = "else:"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        elif (InStr(variables['A_LoopField23'] , " := ")) or(InStr(variables['A_LoopField23'] , " .= ")) or(InStr(variables['A_LoopField23'] , " += ")) or(InStr(variables['A_LoopField23'] , " -= ")) or(InStr(variables['A_LoopField23'] , " *= ")) and(variables['lineDone'] == 0):
            variables['lineDone'] = 1
            variables['str123'] = variables['A_LoopField23']
            variables['whatVarWeUse'] = ""
            if (InStr(variables['A_LoopField23'] , " := ")):
                variables['whatVarWeUse'] = " = "
            if (InStr(variables['A_LoopField23'] , " .= ")):
                variables['whatVarWeUse'] = " += "
            if (InStr(variables['A_LoopField23'] , " += ")):
                variables['whatVarWeUse'] = " += "
            if (InStr(variables['A_LoopField23'] , " -= ")):
                variables['whatVarWeUse'] = " -= "
            if (InStr(variables['A_LoopField23'] , " *= ")):
                variables['whatVarWeUse'] = " *= "
            variables['str123'] = StrReplace(variables['str123'] , ":=" , "=")
            variables['str123'] = StrReplace(variables['str123'] , ".=" , "=")
            variables['str123'] = StrReplace(variables['str123'] , "+=" , "=")
            variables['str123'] = StrReplace(variables['str123'] , "-=" , "=")
            variables['str123'] = StrReplace(variables['str123'] , "*=" , "=")
            variables['var1avavavavva'] = Trim(StrSplit(variables['str123'] , "=" , 1))
            variables['var2avavavavva'] = Trim(StrSplit(variables['str123'] , "=" , 2))
            #OutputDebug, ||||||||||||%var2%||||||||||||
            variables['varOUT1avavavavva'] = transpileVariables(variables['var1avavavavva'] , variables['functionNames'])
            variables['varOUT2avavavavva'] = transpileVariables(variables['var2avavavavva'] , variables['functionNames'])
            variables['out'] = variables['varOUT1avavavavva']  +  variables['whatVarWeUse']  +  variables['varOUT2avavavavva']
            variables['pyCode'] += variables['out']  +  "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 1)== Chr(59)) and(variables['lineDone'] == 0):
            variables['str123'] = StringTrimLeft(variables['A_LoopField23'], 1)
            variables['str123'] = "#"  +  variables['str123']
            variables['out'] = variables['str123']
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out']  +  "\n"
        else:
            # this is THE else
            if (variables['lineDone']  != 1):
                if (variables['skipLeftCuleyForFuncPLS']  != 1):
                    if (SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 1)== Chr(125)):
                        variables['pyCode'] += Chr(125) +  "\n"
                    else:
                        if (variables['pycodeAcurlyBraceAddSomeVrasFixLP'] == 1)and(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 1)== Chr(123)):
                            variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 0
                            variables['pyCode'] += variables['A_LoopField23']  +  "\n"  +  variables['theFixTextLoopLP']  +  "\n"
                        else:
                            if (variables['pycodeAcurlyBraceAddSomeVrasFixNL'] == 1)and(SubStr(Trim(StrLower(variables['A_LoopField23'])) , 1 , 1)== Chr(123)):
                                variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 0
                                variables['pyCode'] += variables['A_LoopField23']  +  "\n"  +  variables['theFixTextLoopNL']  +  "\n"
                            else:
                                variables['pyCode'] += variables['A_LoopField23']  +  "\n"
                else:
                    variables['skipLeftCuleyForFuncPLS'] = 0
    if (variables['haveWeEverUsedAloop'] == 1):
        variables['pycodeLoopfixa'] = StringTrimRight(variables['pycodeLoopfixa'], 1)
        #OutputDebug, |%pycodeLoopfixa%|
        variables['AIndexLoopCurlyFix'] = 1
        items = LoopParseFunc(variables['pycodeLoopfixa'], "\n", "\r")
        for A_Index27, A_LoopField27 in enumerate(items, start=1):
            variables['A_Index27'] = A_Index27
            variables['A_LoopField27'] = A_LoopField27
            variables['str123'] = variables['A_LoopField27']
            variables['fixLoopLokingFor'] = variables['A_LoopField27']
            variables['fixLoopLokingForfound'] = 1
            variables['out1'] = StrSplit(variables['str123'] , "|" , 1)
            variables['out2'] = StrSplit(variables['str123'] , "|" , 3)
            #OutputDebug, |%out1%|
            #OutputDebug, |%out2%|
            variables['wasAtanyIfsElseAddAIndexLoopCurlyFix'] = 0
            if (variables['out1'] == "nl"):
                variables['inTarget'] = 0
                variables['insideBracket'] = 0
                variables['netsedCurly'] = 0
                variables['eldLoopNestedBADlol'] = 0
                variables['readyToEnd'] = 0
                variables['endBracketDOntPutThere'] = 0
                variables['dontSaveStr'] = 0
                variables['weAreDoneHereCurly'] = 0
                variables['DeleayOneCuzOfLoopParse'] = 0
                variables['fixLoopLokingForNum'] = 0
                variables['insdeAnestedLoopBAD'] = 0
                variables['foundTheTopLoop'] = 0
                variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] = ""
                items = LoopParseFunc(variables['pyCode'], "\n", "\r")
                for A_Index28, A_LoopField28 in enumerate(items, start=1):
                    variables['A_Index28'] = A_Index28
                    variables['A_LoopField28'] = A_LoopField28
                    #MsgBox, dsfgsdefgesrdg1
                    #MsgBox, |%A_LoopField28%|`n|%fixLoopLokingFor%|
                    if (InStr(variables['A_LoopField28'] , variables['fixLoopLokingFor'])) and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['fixLoopLokingForNum'] = 1
                        #MsgBox, do we came here 1
                    if (InStr(variables['A_LoopField28'] , "for ")) and(variables['weAreDoneHereCurly']  != 1)and(variables['insdeAnestedLoopBAD']  != 1)and(variables['fixLoopLokingForNum'] == 1):
                        variables['s'] = StrSplit(variables['A_LoopField28'] , "A"  +  Chr(95) +  "Index" , 2)
                        variables['out1z'] = variables['s']
                        variables['s'] = StrSplit(variables['out1z'] , " " , 1)
                        variables['out1z'] = Trim(variables['s'])
                        #MsgBox, % out1z
                        #MsgBox, do we came here 2
                        variables['fixLoopLokingForNum'] = 0
                        variables['foundTheTopLoop'] += 1
                        variables['inTarget'] = 1
                        #MsgBox, % A_LoopField28
                        variables['dontSaveStr'] = 1
                        variables['ALoopField'] = variables['A_LoopField28']
                        variables['DeleayOneCuzOfLoopParse'] = 1
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField']  +  "\n"
                    if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField28'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['insideBracket'] = 1
                    if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField28'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['netsedCurly'] += 1
                    if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField28'] , Chr(125)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['netsedCurly'] -= 1
                        variables['readyToEnd'] = 1
                    if (InStr(variables['A_LoopField28'] , "for ")) and(variables['insdeAnestedLoopBAD']  != 1)and(variables['foundTheTopLoop'] >= 2):
                        variables['insdeAnestedLoopBAD'] = 1
                        variables['insideBracket1'] = 0
                        variables['netsedCurly1'] = 0
                    if (variables['inTarget'] == 1):
                        variables['foundTheTopLoop'] += 1
                    if (variables['insdeAnestedLoopBAD'] == 1):
                        if (InStr(variables['A_LoopField28'] , Chr(123))):
                            variables['insideBracket1'] = 1
                        if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField28'] , Chr(123))):
                            variables['netsedCurly1'] += 1
                        if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField28'] , Chr(125))):
                            variables['netsedCurly1'] -= 1
                            variables['readyToEnd1'] = 1
                        if (InStr(variables['A_LoopField28'] , Chr(125)))and(variables['readyToEnd1'] == 1)and(variables['netsedCurly1'] == 0)and(variables['insideBracket'] == 1):
                            #MsgBox, % A_LoopField28
                            variables['eldLoopNestedBADlol'] = 1
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField28']  +  "\n"
                    if (variables['inTarget'] == 1)and(variables['dontSaveStr']  != 1)and(variables['fixLoopLokingForNum']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['ALoopField'] = variables['A_LoopField28']
                        # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                        variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A"  +  Chr(95) +  "Index(?:\\d+)?" , "A"  +  Chr(95) +  "Index"  +  variables['out1z'])
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField']  +  "\n"
                    if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField28'] , Chr(125)))and(variables['readyToEnd'] == 1)and(variables['netsedCurly'] == 0)and(variables['weAreDoneHereCurly'] == 0)and(variables['dontSaveStr']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        #MsgBox, % A_LoopField28
                        variables['weAreDoneHereCurly'] = 1
                        variables['inTarget'] = 0
                        variables['endBracketDOntPutThere'] = 1
                    variables['dontSaveStr'] = 0
                    if (variables['inTarget']  != 1)and(variables['endBracketDOntPutThere']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField28']  +  "\n"
                    variables['endBracketDOntPutThere'] = 0
                    if (variables['eldLoopNestedBADlol'] == 1):
                        variables['insdeAnestedLoopBAD'] = 0
                variables['strstysrstsytTRIMHELP'] = variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}']
                variables['strstysrstsytTRIMHELP'] = StringTrimRight(variables['strstysrstsytTRIMHELP'], 1)
                #MsgBox, % out4758686d86d86d86578991a%AIndexLoopCurlyFix%
                variables['pyCode'] = variables['strstysrstsytTRIMHELP']
                #MsgBox, % jsCode
                variables['wasAtanyIfsElseAddAIndexLoopCurlyFix'] = 1
            else:
                variables['inTarget'] = 0
                variables['insideBracket'] = 0
                variables['netsedCurly'] = 0
                variables['eldLoopNestedBADlol'] = 0
                variables['readyToEnd'] = 0
                variables['endBracketDOntPutThere'] = 0
                variables['dontSaveStr'] = 0
                variables['weAreDoneHereCurly'] = 0
                variables['DeleayOneCuzOfLoopParse'] = 0
                variables['fixLoopLokingForNum'] = 0
                variables['insdeAnestedLoopBAD'] = 0
                variables['foundTheTopLoop'] = 0
                variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] = ""
                items = LoopParseFunc(variables['pyCode'], "\n", "\r")
                for A_Index29, A_LoopField29 in enumerate(items, start=1):
                    variables['A_Index29'] = A_Index29
                    variables['A_LoopField29'] = A_LoopField29
                    if (InStr(variables['A_LoopField29'] , variables['fixLoopLokingFor'])) and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['fixLoopLokingForNum'] = 1
                        #MsgBox, do we came here 3
                    if (InStr(variables['A_LoopField29'] , "for ")) and(variables['weAreDoneHereCurly']  != 1)and(variables['insdeAnestedLoopBAD']  != 1)and(variables['fixLoopLokingForNum'] == 1):
                        variables['s'] = StrSplit(variables['A_LoopField29'] , "A"  +  Chr(95) +  "LoopField" , 2)
                        variables['out1z'] = variables['s']
                        variables['s'] = StrSplit(variables['out1z'] , " " , 1)
                        variables['out1z'] = Trim(variables['s'])
                        #MsgBox, % out1z
                        variables['fixLoopLokingForNum'] = 0
                        #MsgBox, do we came here 4
                        variables['foundTheTopLoop'] += 1
                        variables['inTarget'] = 1
                        #MsgBox, % A_LoopField29
                        variables['dontSaveStr'] = 1
                        variables['ALoopField'] = variables['A_LoopField29']
                        variables['DeleayOneCuzOfLoopParse'] = 1
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField']  +  "\n"
                    if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField29'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['insideBracket'] = 1
                    if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField29'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['netsedCurly'] += 1
                    if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField29'] , Chr(125)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['netsedCurly'] -= 1
                        variables['readyToEnd'] = 1
                    if (InStr(variables['A_LoopField29'] , "for ")) and(variables['insdeAnestedLoopBAD']  != 1)and(variables['foundTheTopLoop'] >= 2):
                        variables['insdeAnestedLoopBAD'] = 1
                        variables['insideBracket1'] = 0
                        variables['netsedCurly1'] = 0
                    if (variables['inTarget'] == 1):
                        variables['foundTheTopLoop'] += 1
                    if (variables['insdeAnestedLoopBAD'] == 1):
                        if (InStr(variables['A_LoopField29'] , Chr(123))):
                            variables['insideBracket1'] = 1
                        if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField29'] , Chr(123))):
                            variables['netsedCurly1'] += 1
                        if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField29'] , Chr(125))):
                            variables['netsedCurly1'] -= 1
                            variables['readyToEnd1'] = 1
                        if (InStr(variables['A_LoopField29'] , Chr(125)))and(variables['readyToEnd1'] == 1)and(variables['netsedCurly1'] == 0)and(variables['insideBracket'] == 1):
                            #MsgBox, % A_LoopField29
                            variables['eldLoopNestedBADlol'] = 1
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField29']  +  "\n"
                    if (variables['inTarget'] == 1)and(variables['dontSaveStr']  != 1)and(variables['fixLoopLokingForNum']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['ALoopField'] = variables['A_LoopField29']
                        # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                        variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A"  +  Chr(95) +  "Index(?:\\d+)?" , "A"  +  Chr(95) +  "Index"  +  variables['out1z'])
                        # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                        variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A"  +  Chr(95) +  "LoopField(?:\\d+)?" , "A"  +  Chr(95) +  "LoopField"  +  variables['out1z'])
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField']  +  "\n"
                    if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField29'] , Chr(125)))and(variables['readyToEnd'] == 1)and(variables['netsedCurly'] == 0)and(variables['weAreDoneHereCurly'] == 0)and(variables['dontSaveStr']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        #MsgBox, % A_LoopField29
                        variables['weAreDoneHereCurly'] = 1
                        variables['inTarget'] = 0
                        variables['endBracketDOntPutThere'] = 1
                    variables['dontSaveStr'] = 0
                    if (variables['inTarget']  != 1)and(variables['endBracketDOntPutThere']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField29']  +  "\n"
                    variables['endBracketDOntPutThere'] = 0
                    if (variables['eldLoopNestedBADlol'] == 1):
                        variables['insdeAnestedLoopBAD'] = 0
                variables['strstysrstsytTRIMHELP'] = variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}']
                variables['strstysrstsytTRIMHELP'] = StringTrimRight(variables['strstysrstsytTRIMHELP'], 1)
                #MsgBox, % out4758686d86d86d86578991a%AIndexLoopCurlyFix%
                variables['pyCode'] = variables['strstysrstsytTRIMHELP']
                #MsgBox, % jsCode
                variables['wasAtanyIfsElseAddAIndexLoopCurlyFix'] = 1
            if (variables['wasAtanyIfsElseAddAIndexLoopCurlyFix'] == 1):
                variables['AIndexLoopCurlyFix'] += 1
                variables['wasAtanyIfsElseAddAIndexLoopCurlyFix'] = 0
        variables['out4758686d86dgt8r754444444'] = ""
        variables['hold'] = 0
        items = LoopParseFunc(variables['pyCode'], "\n", "\r")
        for A_Index30, A_LoopField30 in enumerate(items, start=1):
            variables['A_Index30'] = A_Index30
            variables['A_LoopField30'] = A_LoopField30
            variables['ignore'] = 0
            if (InStr(variables['A_LoopField30'] , "for ")):
                if (variables['hold'] == 1)and(variables['holdText'] == variables['A_LoopField30']):
                    variables['ignore'] = 1
                else:
                    variables['holdText'] = variables['A_LoopField30']
                    variables['hold'] = 1
            if ( not (variables['ignore'])):
                variables['out4758686d86dgt8r754444444'] += variables['A_LoopField30']  +  "\n"
        variables['out4758686d86dgt8r754444444'] = StringTrimRight(variables['out4758686d86dgt8r754444444'], 1)
        variables['pyCode'] = variables['out4758686d86dgt8r754444444']
    variables['pyCode'] = indent_nested_curly_braces(variables['pyCode'])
    variables['pyCodeOut1234565432'] = ""
    items = LoopParseFunc(variables['pyCode'], "\n", "\r")
    for A_Index31, A_LoopField31 in enumerate(items, start=1):
        variables['A_Index31'] = A_Index31
        variables['A_LoopField31'] = A_LoopField31
        if (Trim(variables['A_LoopField31']) != Chr(123)) and(Trim(variables['A_LoopField31']) != Chr(125)):
            variables['out'] = variables['A_LoopField31']
            variables['out'] = StringTrimLeft(variables['out'], 1)
            if (InStr(variables['out'] , "variables['A"  +  Chr(95) +  "Index")) or(InStr(variables['out'] , "variables['A"  +  Chr(95) +  "LoopField")):
                variables['out'] = StrReplace(variables['out'] , Chr(39) +  Chr(34) +  Chr(93) +  Chr(125) +  Chr(39) +  Chr(93), Chr(34) +  Chr(93) +  Chr(125) +  Chr(39) +  Chr(93))
                variables['out'] = StrReplace(variables['out'] , Chr(39) +  Chr(39) +  Chr(93), Chr(39) +  Chr(93))
            if ( not (InStr(variables['out'] , "|itsaersdtgtgfergsdgfsegdfsedAA|"))):
                if (SubStr(Trim(StrLower(variables['A_LoopField31'])) , 1 , 1) != Chr(59)):
                    if (SubStr(Trim(StrLower(variables['A_LoopField31'])) , 1 , 1)== Chr(124)):
                        variables['nothing'] = ""
                        variables['out'] = StrReplace(variables['out'] , "|" , variables['nothing'])
                        variables['pyCodeOut1234565432'] += Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  variables['out']  +  "\n"
                    else:
                        variables['pyCodeOut1234565432'] += variables['out']  +  "\n"
    variables['pyCode'] = StringTrimRight(variables['pyCodeOut1234565432'], 1)
    variables['pyCodeFinal'] = variables['pyCode']
    variables['func_LoopParseFunc_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(76) +  Chr(111) +  Chr(111) +  Chr(112) +  Chr(80) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(101) +  Chr(70) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(44) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(49) +  Chr(61) +  Chr(34) +  Chr(34) +  Chr(44) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(50) +  Chr(61) +  Chr(34) +  Chr(34) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(109) +  Chr(112) +  Chr(111) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(49) +  Chr(32) +  Chr(97) +  Chr(110) +  Chr(100) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(50) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(73) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(32) +  Chr(97) +  Chr(114) +  Chr(101) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(111) +  Chr(118) +  Chr(105) +  Chr(100) +  Chr(101) +  Chr(100) +  Chr(44) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(108) +  Chr(105) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(111) +  Chr(102) +  Chr(32) +  Chr(99) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(97) +  Chr(99) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(109) +  Chr(115) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(108) +  Chr(105) +  Chr(115) +  Chr(116) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(117) +  Chr(99) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(117) +  Chr(108) +  Chr(97) +  Chr(114) +  Chr(32) +  Chr(101) +  Chr(120) +  Chr(112) +  Chr(114) +  Chr(101) +  Chr(115) +  Chr(115) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(115) +  Chr(112) +  Chr(108) +  Chr(105) +  Chr(116) +  Chr(116) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(114) +  Chr(39) +  Chr(91) +  Chr(39) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(46) +  Chr(101) +  Chr(115) +  Chr(99) +  Chr(97) +  Chr(112) +  Chr(101) +  Chr(40) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(49) +  Chr(41) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(46) +  Chr(101) +  Chr(115) +  Chr(99) +  Chr(97) +  Chr(112) +  Chr(101) +  Chr(40) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(50) +  Chr(41) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(114) +  Chr(39) +  Chr(93) +  Chr(43) +  Chr(39) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(83) +  Chr(112) +  Chr(108) +  Chr(105) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(117) +  Chr(115) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(117) +  Chr(99) +  Chr(116) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(109) +  Chr(115) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(46) +  Chr(115) +  Chr(112) +  Chr(108) +  Chr(105) +  Chr(116) +  Chr(40) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(44) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(109) +  Chr(115) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10)
    variables['func_InStr_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(73) +  Chr(110) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(40) +  Chr(72) +  Chr(97) +  Chr(121) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(44) +  Chr(32) +  Chr(78) +  Chr(101) +  Chr(101) +  Chr(100) +  Chr(108) +  Chr(101) +  Chr(44) +  Chr(32) +  Chr(67) +  Chr(97) +  Chr(115) +  Chr(101) +  Chr(83) +  Chr(101) +  Chr(110) +  Chr(115) +  Chr(105) +  Chr(116) +  Chr(105) +  Chr(118) +  Chr(101) +  Chr(61) +  Chr(84) +  Chr(114) +  Chr(117) +  Chr(101) +  Chr(44) +  Chr(32) +  Chr(83) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(61) +  Chr(49) +  Chr(44) +  Chr(32) +  Chr(79) +  Chr(99) +  Chr(99) +  Chr(117) +  Chr(114) +  Chr(114) +  Chr(101) +  Chr(110) +  Chr(99) +  Chr(101) +  Chr(61) +  Chr(49) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(72) +  Chr(97) +  Chr(121) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(78) +  Chr(111) +  Chr(110) +  Chr(101) +  Chr(32) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(78) +  Chr(101) +  Chr(101) +  Chr(100) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(78) +  Chr(111) +  Chr(110) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(70) +  Chr(97) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(83) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(109) +  Chr(97) +  Chr(120) +  Chr(40) +  Chr(83) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(44) +  Chr(32) +  Chr(49) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(67) +  Chr(97) +  Chr(115) +  Chr(101) +  Chr(83) +  Chr(101) +  Chr(110) +  Chr(115) +  Chr(105) +  Chr(116) +  Chr(105) +  Chr(118) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(72) +  Chr(97) +  Chr(121) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(72) +  Chr(97) +  Chr(121) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(46) +  Chr(108) +  Chr(111) +  Chr(119) +  Chr(101) +  Chr(114) +  Chr(40) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(78) +  Chr(101) +  Chr(101) +  Chr(100) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(78) +  Chr(101) +  Chr(101) +  Chr(100) +  Chr(108) +  Chr(101) +  Chr(46) +  Chr(108) +  Chr(111) +  Chr(119) +  Chr(101) +  Chr(114) +  Chr(40) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(117) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(48) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(105) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(32) +  Chr(114) +  Chr(97) +  Chr(110) +  Chr(103) +  Chr(101) +  Chr(40) +  Chr(83) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(32) +  Chr(45) +  Chr(32) +  Chr(49) +  Chr(44) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(72) +  Chr(97) +  Chr(121) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(41) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(72) +  Chr(97) +  Chr(121) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(91) +  Chr(105) +  Chr(58) +  Chr(105) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(78) +  Chr(101) +  Chr(101) +  Chr(100) +  Chr(108) +  Chr(101) +  Chr(41) +  Chr(93) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(78) +  Chr(101) +  Chr(101) +  Chr(100) +  Chr(108) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(117) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(43) +  Chr(61) +  Chr(32) +  Chr(49) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(117) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(79) +  Chr(99) +  Chr(99) +  Chr(117) +  Chr(114) +  Chr(114) +  Chr(101) +  Chr(110) +  Chr(99) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(84) +  Chr(114) +  Chr(117) +  Chr(101) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(70) +  Chr(97) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(32) +  Chr(13) +  Chr(10)
    variables['func_SubStr_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(83) +  Chr(117) +  Chr(98) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(44) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(44) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(103) +  Chr(116) +  Chr(104) +  Chr(61) +  Chr(78) +  Chr(111) +  Chr(110) +  Chr(101) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(78) +  Chr(111) +  Chr(110) +  Chr(101) +  Chr(32) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(34) +  Chr(34) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(34) +  Chr(34) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(103) +  Chr(116) +  Chr(104) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(78) +  Chr(111) +  Chr(110) +  Chr(101) +  Chr(32) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(103) +  Chr(116) +  Chr(104) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(34) +  Chr(34) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(103) +  Chr(116) +  Chr(104) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(41) +  Chr(32) +  Chr(45) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(49) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(32) +  Chr(60) +  Chr(32) +  Chr(49) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(41) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(91) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(32) +  Chr(45) +  Chr(32) +  Chr(49) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(80) +  Chr(111) +  Chr(115) +  Chr(32) +  Chr(45) +  Chr(32) +  Chr(49) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(103) +  Chr(116) +  Chr(104) +  Chr(93) +  Chr(13) +  Chr(10)
    variables['func_Trim_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(84) +  Chr(114) +  Chr(105) +  Chr(109) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(78) +  Chr(111) +  Chr(110) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(34) +  Chr(34) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(46) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(112) +  Chr(40) +  Chr(41) +  Chr(13) +  Chr(10)
    variables['func_StrReplace_func'] = Chr(32) +  Chr(32) +  Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(82) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(40) +  Chr(111) +  Chr(114) +  Chr(105) +  Chr(103) +  Chr(105) +  Chr(110) +  Chr(97) +  Chr(108) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(44) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(110) +  Chr(100) +  Chr(44) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(87) +  Chr(105) +  Chr(116) +  Chr(104) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(85) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(32) +  Chr(109) +  Chr(101) +  Chr(116) +  Chr(104) +  Chr(111) +  Chr(100) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(32) +  Chr(111) +  Chr(99) +  Chr(99) +  Chr(117) +  Chr(114) +  Chr(114) +  Chr(101) +  Chr(110) +  Chr(99) +  Chr(101) +  Chr(115) +  Chr(32) +  Chr(111) +  Chr(102) +  Chr(32) +  Chr(39) +  Chr(102) +  Chr(105) +  Chr(110) +  Chr(100) +  Chr(39) +  Chr(32) +  Chr(119) +  Chr(105) +  Chr(116) +  Chr(104) +  Chr(32) +  Chr(39) +  Chr(114) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(87) +  Chr(105) +  Chr(116) +  Chr(104) +  Chr(39) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(111) +  Chr(114) +  Chr(105) +  Chr(103) +  Chr(105) +  Chr(110) +  Chr(97) +  Chr(108) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(46) +  Chr(114) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(40) +  Chr(102) +  Chr(105) +  Chr(110) +  Chr(100) +  Chr(44) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(87) +  Chr(105) +  Chr(116) +  Chr(104) +  Chr(41) +  Chr(13) +  Chr(10)
    variables['func_StringTrimLeft_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(84) +  Chr(114) +  Chr(105) +  Chr(109) +  Chr(76) +  Chr(101) +  Chr(102) +  Chr(116) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(44) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(67) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(111) +  Chr(110) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(105) +  Chr(116) +  Chr(39) +  Chr(115) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(97) +  Chr(108) +  Chr(114) +  Chr(101) +  Chr(97) +  Chr(100) +  Chr(121) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(105) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(110) +  Chr(99) +  Chr(101) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(44) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(41) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(111) +  Chr(110) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(104) +  Chr(101) +  Chr(99) +  Chr(107) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(108) +  Chr(111) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(101) +  Chr(110) +  Chr(111) +  Chr(117) +  Chr(103) +  Chr(104) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(112) +  Chr(101) +  Chr(114) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(109) +  Chr(32) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(109) +  Chr(109) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(41) +  Chr(32) +  Chr(62) +  Chr(61) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(67) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(91) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(67) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(58) +  Chr(93) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(84) +  Chr(114) +  Chr(105) +  Chr(109) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(102) +  Chr(114) +  Chr(111) +  Chr(109) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(102) +  Chr(116) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(104) +  Chr(97) +  Chr(110) +  Chr(103) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(67) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(108) +  Chr(97) +  Chr(114) +  Chr(103) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(97) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(103) +  Chr(116) +  Chr(104) +  Chr(13) +  Chr(10)
    variables['func_StringTrimRight_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(84) +  Chr(114) +  Chr(105) +  Chr(109) +  Chr(82) +  Chr(105) +  Chr(103) +  Chr(104) +  Chr(116) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(44) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(67) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(111) +  Chr(110) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(105) +  Chr(116) +  Chr(39) +  Chr(115) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(97) +  Chr(108) +  Chr(114) +  Chr(101) +  Chr(97) +  Chr(100) +  Chr(121) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(105) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(110) +  Chr(99) +  Chr(101) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(44) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(41) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(111) +  Chr(110) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(104) +  Chr(101) +  Chr(99) +  Chr(107) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(108) +  Chr(111) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(101) +  Chr(110) +  Chr(111) +  Chr(117) +  Chr(103) +  Chr(104) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(112) +  Chr(101) +  Chr(114) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(109) +  Chr(32) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(109) +  Chr(109) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(41) +  Chr(32) +  Chr(62) +  Chr(61) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(67) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(91) +  Chr(58) +  Chr(45) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(67) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(93) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(84) +  Chr(114) +  Chr(105) +  Chr(109) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(102) +  Chr(114) +  Chr(111) +  Chr(109) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(114) +  Chr(105) +  Chr(103) +  Chr(104) +  Chr(116) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(104) +  Chr(97) +  Chr(110) +  Chr(103) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(67) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(108) +  Chr(97) +  Chr(114) +  Chr(103) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(97) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(103) +  Chr(116) +  Chr(104) +  Chr(13) +  Chr(10)
    variables['func_StrLower_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(76) +  Chr(111) +  Chr(119) +  Chr(101) +  Chr(114) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(46) +  Chr(108) +  Chr(111) +  Chr(119) +  Chr(101) +  Chr(114) +  Chr(40) +  Chr(41) +  Chr(13) +  Chr(10)
    variables['func_RegExReplace_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(103) +  Chr(69) +  Chr(120) +  Chr(82) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(44) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(80) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(44) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(109) +  Chr(101) +  Chr(110) +  Chr(116) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(114) +  Chr(101) +  Chr(97) +  Chr(116) +  Chr(101) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(117) +  Chr(108) +  Chr(97) +  Chr(114) +  Chr(32) +  Chr(101) +  Chr(120) +  Chr(112) +  Chr(114) +  Chr(101) +  Chr(115) +  Chr(115) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(111) +  Chr(98) +  Chr(106) +  Chr(101) +  Chr(99) +  Chr(116) +  Chr(32) +  Chr(117) +  Chr(115) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(111) +  Chr(118) +  Chr(105) +  Chr(100) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(109) +  Chr(112) +  Chr(111) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(46) +  Chr(99) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(40) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(80) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(44) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(46) +  Chr(77) +  Chr(85) +  Chr(76) +  Chr(84) +  Chr(73) +  Chr(76) +  Chr(73) +  Chr(78) +  Chr(69) +  Chr(41) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(46) +  Chr(77) +  Chr(85) +  Chr(76) +  Chr(84) +  Chr(73) +  Chr(76) +  Chr(73) +  Chr(78) +  Chr(69) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(109) +  Chr(117) +  Chr(108) +  Chr(116) +  Chr(105) +  Chr(45) +  Chr(108) +  Chr(105) +  Chr(110) +  Chr(101) +  Chr(32) +  Chr(109) +  Chr(97) +  Chr(116) +  Chr(99) +  Chr(104) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(85) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(115) +  Chr(117) +  Chr(98) +  Chr(40) +  Chr(41) +  Chr(32) +  Chr(109) +  Chr(101) +  Chr(116) +  Chr(104) +  Chr(111) +  Chr(100) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(112) +  Chr(101) +  Chr(114) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(109) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(109) +  Chr(101) +  Chr(110) +  Chr(116) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(115) +  Chr(117) +  Chr(108) +  Chr(116) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(46) +  Chr(115) +  Chr(117) +  Chr(98) +  Chr(40) +  Chr(114) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(109) +  Chr(101) +  Chr(110) +  Chr(116) +  Chr(44) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(109) +  Chr(111) +  Chr(100) +  Chr(105) +  Chr(102) +  Chr(105) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(115) +  Chr(117) +  Chr(108) +  Chr(116) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(13) +  Chr(10)
    variables['func_StrSplit_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(83) +  Chr(112) +  Chr(108) +  Chr(105) +  Chr(116) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(44) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(44) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(83) +  Chr(112) +  Chr(108) +  Chr(105) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(98) +  Chr(97) +  Chr(115) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(115) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(46) +  Chr(115) +  Chr(112) +  Chr(108) +  Chr(105) +  Chr(116) +  Chr(40) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(112) +  Chr(101) +  Chr(99) +  Chr(105) +  Chr(102) +  Chr(105) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(98) +  Chr(121) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(114) +  Chr(97) +  Chr(109) +  Chr(101) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(40) +  Chr(49) +  Chr(45) +  Chr(98) +  Chr(97) +  Chr(115) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(100) +  Chr(101) +  Chr(120) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(48) +  Chr(32) +  Chr(60) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(32) +  Chr(60) +  Chr(61) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(112) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(115) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(115) +  Chr(91) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(32) +  Chr(45) +  Chr(32) +  Chr(49) +  Chr(93) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(115) +  Chr(112) +  Chr(101) +  Chr(99) +  Chr(105) +  Chr(102) +  Chr(105) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(40) +  Chr(48) +  Chr(45) +  Chr(98) +  Chr(97) +  Chr(115) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(100) +  Chr(101) +  Chr(120) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(39) +  Chr(39) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(97) +  Chr(110) +  Chr(32) +  Chr(101) +  Chr(109) +  Chr(112) +  Chr(116) +  Chr(121) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(111) +  Chr(102) +  Chr(32) +  Chr(114) +  Chr(97) +  Chr(110) +  Chr(103) +  Chr(101) +  Chr(13) +  Chr(10)
    variables['func_Chr_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(67) +  Chr(104) +  Chr(114) +  Chr(40) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(98) +  Chr(101) +  Chr(114) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(104) +  Chr(101) +  Chr(99) +  Chr(107) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(98) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(78) +  Chr(111) +  Chr(110) +  Chr(101) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(98) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(78) +  Chr(111) +  Chr(110) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(97) +  Chr(110) +  Chr(32) +  Chr(101) +  Chr(109) +  Chr(112) +  Chr(116) +  Chr(121) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(34) +  Chr(34) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(104) +  Chr(101) +  Chr(99) +  Chr(107) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(98) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(119) +  Chr(105) +  Chr(116) +  Chr(104) +  Chr(105) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(105) +  Chr(100) +  Chr(32) +  Chr(85) +  Chr(110) +  Chr(105) +  Chr(99) +  Chr(111) +  Chr(100) +  Chr(101) +  Chr(32) +  Chr(114) +  Chr(97) +  Chr(110) +  Chr(103) +  Chr(101) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(48) +  Chr(32) +  Chr(60) +  Chr(61) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(98) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(60) +  Chr(61) +  Chr(32) +  Chr(48) +  Chr(120) +  Chr(49) +  Chr(48) +  Chr(70) +  Chr(70) +  Chr(70) +  Chr(70) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(111) +  Chr(110) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(98) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(99) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(97) +  Chr(99) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(117) +  Chr(115) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(99) +  Chr(104) +  Chr(114) +  Chr(40) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(99) +  Chr(104) +  Chr(114) +  Chr(40) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(98) +  Chr(101) +  Chr(114) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(97) +  Chr(110) +  Chr(32) +  Chr(101) +  Chr(109) +  Chr(112) +  Chr(116) +  Chr(121) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(105) +  Chr(100) +  Chr(32) +  Chr(110) +  Chr(117) +  Chr(109) +  Chr(98) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(34) +  Chr(34) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10)
    variables['func_Mod_func'] = Chr(13) +  Chr(10) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(117) +  Chr(115) +  Chr(116) +  Chr(111) +  Chr(109) +  Chr(32) +  Chr(77) +  Chr(111) +  Chr(100) +  Chr(32) +  Chr(102) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(116) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(32) +  Chr(80) +  Chr(121) +  Chr(116) +  Chr(104) +  Chr(111) +  Chr(110) +  Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(77) +  Chr(111) +  Chr(100) +  Chr(40) +  Chr(100) +  Chr(105) +  Chr(118) +  Chr(105) +  Chr(100) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(44) +  Chr(32) +  Chr(100) +  Chr(105) +  Chr(118) +  Chr(105) +  Chr(115) +  Chr(111) +  Chr(114) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(100) +  Chr(105) +  Chr(118) +  Chr(105) +  Chr(100) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(100) +  Chr(105) +  Chr(118) +  Chr(105) +  Chr(115) +  Chr(111) +  Chr(114) +  Chr(13) +  Chr(10)
    variables['func_HTpy_func'] = Chr(13) +  Chr(10) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(32) +  Chr(72) +  Chr(84) +  Chr(112) +  Chr(121) +  Chr(40) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(109) +  Chr(112) +  Chr(111) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(121) +  Chr(115) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(109) +  Chr(112) +  Chr(111) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(111) +  Chr(115) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(115) +  Chr(121) +  Chr(115) +  Chr(46) +  Chr(97) +  Chr(114) +  Chr(103) +  Chr(118) +  Chr(41) +  Chr(32) +  Chr(60) +  Chr(32) +  Chr(50) +  Chr(32) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(115) +  Chr(121) +  Chr(115) +  Chr(46) +  Chr(97) +  Chr(114) +  Chr(103) +  Chr(118) +  Chr(41) +  Chr(32) +  Chr(62) +  Chr(32) +  Chr(51) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(40) +  Chr(34) +  Chr(85) +  Chr(115) +  Chr(97) +  Chr(103) +  Chr(101) +  Chr(58) +  Chr(32) +  Chr(112) +  Chr(121) +  Chr(116) +  Chr(104) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(97) +  Chr(112) +  Chr(112) +  Chr(46) +  Chr(112) +  Chr(121) +  Chr(32) +  Chr(60) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(46) +  Chr(104) +  Chr(116) +  Chr(112) +  Chr(121) +  Chr(62) +  Chr(32) +  Chr(91) +  Chr(114) +  Chr(117) +  Chr(110) +  Chr(93) +  Chr(34) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(121) +  Chr(115) +  Chr(46) +  Chr(101) +  Chr(120) +  Chr(105) +  Chr(116) +  Chr(40) +  Chr(49) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(115) +  Chr(121) +  Chr(115) +  Chr(46) +  Chr(97) +  Chr(114) +  Chr(103) +  Chr(118) +  Chr(91) +  Chr(49) +  Chr(93) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(69) +  Chr(110) +  Chr(115) +  Chr(117) +  Chr(114) +  Chr(101) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(115) +  Chr(32) +  Chr(119) +  Chr(105) +  Chr(116) +  Chr(104) +  Chr(32) +  Chr(39) +  Chr(46) +  Chr(104) +  Chr(116) +  Chr(112) +  Chr(121) +  Chr(39) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(46) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(115) +  Chr(119) +  Chr(105) +  Chr(116) +  Chr(104) +  Chr(40) +  Chr(39) +  Chr(46) +  Chr(104) +  Chr(116) +  Chr(112) +  Chr(121) +  Chr(39) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(40) +  Chr(34) +  Chr(69) +  Chr(114) +  Chr(114) +  Chr(111) +  Chr(114) +  Chr(58) +  Chr(32) +  Chr(73) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(109) +  Chr(117) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(104) +  Chr(97) +  Chr(118) +  Chr(101) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(46) +  Chr(104) +  Chr(116) +  Chr(112) +  Chr(121) +  Chr(32) +  Chr(101) +  Chr(120) +  Chr(116) +  Chr(101) +  Chr(110) +  Chr(115) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(46) +  Chr(34) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(121) +  Chr(115) +  Chr(46) +  Chr(101) +  Chr(120) +  Chr(105) +  Chr(116) +  Chr(40) +  Chr(49) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(104) +  Chr(101) +  Chr(99) +  Chr(107) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(101) +  Chr(120) +  Chr(105) +  Chr(115) +  Chr(116) +  Chr(115) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(111) +  Chr(115) +  Chr(46) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(104) +  Chr(46) +  Chr(105) +  Chr(115) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(41) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(40) +  Chr(102) +  Chr(34) +  Chr(69) +  Chr(114) +  Chr(114) +  Chr(111) +  Chr(114) +  Chr(58) +  Chr(32) +  Chr(39) +  Chr(123) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(125) +  Chr(39) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(105) +  Chr(100) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(104) +  Chr(46) +  Chr(34) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(121) +  Chr(115) +  Chr(46) +  Chr(101) +  Chr(120) +  Chr(105) +  Chr(116) +  Chr(40) +  Chr(49) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(68) +  Chr(101) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(109) +  Chr(105) +  Chr(110) +  Chr(101) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(46) +  Chr(112) +  Chr(121) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(110) +  Chr(97) +  Chr(109) +  Chr(101) +  Chr(32) +  Chr(98) +  Chr(97) +  Chr(115) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(110) +  Chr(97) +  Chr(109) +  Chr(101) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(111) +  Chr(115) +  Chr(46) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(104) +  Chr(46) +  Chr(115) +  Chr(112) +  Chr(108) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(120) +  Chr(116) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(41) +  Chr(91) +  Chr(48) +  Chr(93) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(39) +  Chr(46) +  Chr(112) +  Chr(121) +  Chr(39) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(46) +  Chr(104) +  Chr(116) +  Chr(112) +  Chr(121) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(116) +  Chr(101) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(117) +  Chr(115) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(102) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(116) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(119) +  Chr(105) +  Chr(116) +  Chr(104) +  Chr(32) +  Chr(111) +  Chr(112) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(44) +  Chr(32) +  Chr(39) +  Chr(114) +  Chr(39) +  Chr(41) +  Chr(32) +  Chr(97) +  Chr(115) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(104) +  Chr(116) +  Chr(112) +  Chr(121) +  Chr(95) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(116) +  Chr(101) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(46) +  Chr(114) +  Chr(101) +  Chr(97) +  Chr(100) +  Chr(40) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(100) +  Chr(95) +  Chr(114) +  Chr(101) +  Chr(115) +  Chr(117) +  Chr(108) +  Chr(116) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(114) +  Chr(40) +  Chr(104) +  Chr(116) +  Chr(112) +  Chr(121) +  Chr(95) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(116) +  Chr(101) +  Chr(110) +  Chr(116) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(83) +  Chr(97) +  Chr(118) +  Chr(101) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(115) +  Chr(117) +  Chr(108) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(109) +  Chr(105) +  Chr(110) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(46) +  Chr(112) +  Chr(121) +  Chr(32) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(119) +  Chr(105) +  Chr(116) +  Chr(104) +  Chr(32) +  Chr(111) +  Chr(112) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(44) +  Chr(32) +  Chr(39) +  Chr(119) +  Chr(39) +  Chr(41) +  Chr(32) +  Chr(97) +  Chr(115) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(46) +  Chr(119) +  Chr(114) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(40) +  Chr(99) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(100) +  Chr(95) +  Chr(114) +  Chr(101) +  Chr(115) +  Chr(117) +  Chr(108) +  Chr(116) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(40) +  Chr(102) +  Chr(34) +  Chr(67) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(115) +  Chr(117) +  Chr(108) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(97) +  Chr(118) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(39) +  Chr(123) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(125) +  Chr(39) +  Chr(46) +  Chr(34) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(35) +  Chr(32) +  Chr(67) +  Chr(104) +  Chr(101) +  Chr(99) +  Chr(107) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(39) +  Chr(114) +  Chr(117) +  Chr(110) +  Chr(39) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(114) +  Chr(97) +  Chr(109) +  Chr(101) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(111) +  Chr(118) +  Chr(105) +  Chr(100) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(97) +  Chr(110) +  Chr(100) +  Chr(32) +  Chr(101) +  Chr(120) +  Chr(101) +  Chr(99) +  Chr(117) +  Chr(116) +  Chr(101) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(80) +  Chr(121) +  Chr(116) +  Chr(104) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(99) +  Chr(114) +  Chr(105) +  Chr(112) +  Chr(116) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(108) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(115) +  Chr(121) +  Chr(115) +  Chr(46) +  Chr(97) +  Chr(114) +  Chr(103) +  Chr(118) +  Chr(41) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(51) +  Chr(32) +  Chr(97) +  Chr(110) +  Chr(100) +  Chr(32) +  Chr(115) +  Chr(121) +  Chr(115) +  Chr(46) +  Chr(97) +  Chr(114) +  Chr(103) +  Chr(118) +  Chr(91) +  Chr(50) +  Chr(93) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(39) +  Chr(114) +  Chr(117) +  Chr(110) +  Chr(39) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(40) +  Chr(102) +  Chr(34) +  Chr(82) +  Chr(117) +  Chr(110) +  Chr(110) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(39) +  Chr(123) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(125) +  Chr(39) +  Chr(46) +  Chr(46) +  Chr(46) +  Chr(34) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(116) +  Chr(114) +  Chr(121) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(101) +  Chr(120) +  Chr(101) +  Chr(99) +  Chr(40) +  Chr(99) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(40) +  Chr(111) +  Chr(112) +  Chr(101) +  Chr(110) +  Chr(40) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(41) +  Chr(46) +  Chr(114) +  Chr(101) +  Chr(97) +  Chr(100) +  Chr(40) +  Chr(41) +  Chr(44) +  Chr(32) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(112) +  Chr(117) +  Chr(116) +  Chr(95) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(44) +  Chr(32) +  Chr(39) +  Chr(101) +  Chr(120) +  Chr(101) +  Chr(99) +  Chr(39) +  Chr(41) +  Chr(44) +  Chr(32) +  Chr(103) +  Chr(108) +  Chr(111) +  Chr(98) +  Chr(97) +  Chr(108) +  Chr(115) +  Chr(40) +  Chr(41) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(101) +  Chr(120) +  Chr(99) +  Chr(101) +  Chr(112) +  Chr(116) +  Chr(32) +  Chr(69) +  Chr(120) +  Chr(99) +  Chr(101) +  Chr(112) +  Chr(116) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(97) +  Chr(115) +  Chr(32) +  Chr(101) +  Chr(58) +  Chr(13) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(40) +  Chr(102) +  Chr(34) +  Chr(69) +  Chr(114) +  Chr(114) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(111) +  Chr(99) +  Chr(99) +  Chr(117) +  Chr(114) +  Chr(114) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(119) +  Chr(104) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(114) +  Chr(117) +  Chr(110) +  Chr(110) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(109) +  Chr(112) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(102) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(58) +  Chr(32) +  Chr(123) +  Chr(101) +  Chr(125) +  Chr(34) +  Chr(41) +  Chr(13) +  Chr(10) +  Chr(13) +  Chr(10)
    variables['funcs_func'] = "LoopParseFunc|InStr|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|StrLower|RegExReplace|StrSplit|Chr|Mod|HTpy"
    variables['allFuncsHere'] = ""
    items = LoopParseFunc(variables['funcs_func'], "|")
    for A_Index32, A_LoopField32 in enumerate(items, start=1):
        variables['A_Index32'] = A_Index32
        variables['A_LoopField32'] = A_LoopField32
        if (InStr(variables['pyCodeFinal'] , variables['A_LoopField32']  +  Chr(40))):
            variables['hererererehre'] = variables['A_LoopField32']  +  "_func"
            variables['allFuncsHere'] += variables[f'func_{variables["hererererehre"]}']
    variables['pyCodeFinal'] = variables['allFuncsHere']  +  "\n"  +  variables['pyCodeFinal']  +  "\n"
    if (variables['usedLib'] == ""):
        variables['pyCode'] = variables['weEverUseVars']  +  "\n"  +  variables['pyCodeFinal']
        if (variables['weEverUseVars'] == ""):
            variables['pyCode'] = variables['pyCodeFinal']
        else:
            variables['pyCode'] = variables['weEverUseVars']  +  "\n"  +  variables['pyCodeFinal']
    else:
        variables['pyCode'] = variables['usedLib']  +  "\n"  +  variables['weEverUseVars']  +  "\n"  +  variables['pyCodeFinal']
    variables['pyCode'] = StrReplace(variables['pyCode'] , "\n\n" , "\n")
    if (variables['putEndPointFlask1Up']  != ""):
        variables['pyCode'] = variables['putEndPointFlask1Up']  +  "\n"  +  variables['pyCode']  +  "\n"  +  variables['putEndPointFlask2Down']  +  "\n"
    for A_Index33 in range(1, variables['theIdNumOfThe34'] + 1):
        variables['A_Index33'] = A_Index33
        variables['pyCode'] = StrReplace(variables['pyCode'] , "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-"  +  Chr(65) +  Chr(65) +  str(variables['A_Index33']) +  Chr(65) +  Chr(65), variables[f'theIdNumOfThe34theVar{variables["A_Index33"]}'])
    return variables['pyCode']
HTpy()
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;

