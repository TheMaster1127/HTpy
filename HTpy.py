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
    # Check if the delimiter is empty
    if delimiter == '':
        # Return an empty string since splitting with an empty delimiter is not possible
        return ''
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
            variables['result'] += ((Chr(32) + RepeatSpaces(variables['current_indent'])) + (variables['trimmed_line'] + "\n"))
            variables['current_indent'] = variables['current_indent'] + variables['indent_size']
        elif (variables['trimmed_line'] == Chr(125)):
            variables['current_indent'] = variables['current_indent'] - variables['indent_size']
            variables['result'] += ((Chr(32) + RepeatSpaces(variables['current_indent'])) + (variables['trimmed_line'] + "\n"))
        else:
            variables['result'] += ((Chr(32) + RepeatSpaces(variables['current_indent'])) + (variables['trimmed_line'] + "\n"))
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
                variables['outOftranspileVariables'] += variables['A_LoopField10'] + Chr(32)
            else:
                if (InStr(variables['A_LoopField10'] , "%")):
                    if ((SubStr(Trim(variables['A_LoopField10']), 1 , 1)== "%")and(SubStr(Trim(variables['A_LoopField10']), 0)== "%")):
                        variables['var1'] = StringTrimRight(variables['A_LoopField10'], 1)
                        variables['var1'] = StringTrimLeft(variables['var1'], 1)
                        variables['out1'] = "variables['" + variables['var1'] + "']"
                        variables['outOftranspileVariables'] += variables['out1'] + Chr(32)
                    else:
                        variables['var1'] = StrSplit(variables['A_LoopField10'] , "%" , 1)
                        variables['var2'] = StrSplit(variables['A_LoopField10'] , "%" , 2)
                        variables['out1'] = "variables[f" + Chr(39) + variables['var1'] + "{variables[" + Chr(34) + variables['var2'] + Chr(34) + "]}" + Chr(39) + "]"
                        variables['outOftranspileVariables'] += variables['out1'] + Chr(32)
                else:
                    variables['out1'] = "variables[" + Chr(39) + variables['A_LoopField10'] + Chr(39) + "]"
                    variables['outOftranspileVariables'] += variables['out1'] + Chr(32)
        else:
            variables['outOftranspileVariables'] += variables['A_LoopField10'] + Chr(32)
        variables['wasHereVarTryUhBug'] = 0
    if (variables['wasHereVarTryUhBug'] == 1):
        variables['outOftranspileVariables'] = variables['outOftranspileVariablesOut']
    #OutputDebug, |%outOftranspileVariables%|
    items = LoopParseFunc(variables['functionNames'], "|")
    for A_Index15, A_LoopField15 in enumerate(items, start=1):
        variables['A_Index15'] = A_Index15
        variables['A_LoopField15'] = A_LoopField15
        variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "variables['" + variables['A_LoopField15'] + "']" , variables['A_LoopField15'])
    for A_Index16 in range(1, variables['numOfStrings'] + 1):
        variables['A_Index16'] = A_Index16
        variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "freeeeepaestine-sav-etehmtyeah-freee-n" + variables['A_Index16'] , Chr(34) + variables[f'theString{variables["A_Index16"]}'] + Chr(34))
    variables['weEverUseVars'] = "# Define a dictionary to store dynamic variables\nvariables = {}\n\n"
    #OutputDebug, |%outOftranspileVariables%|
    variables['outOftranspileVariables'] = Trim(variables['outOftranspileVariables'])
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , Chr(96), Chr(92))
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , Chr(92) + Chr(92), Chr(96))
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "cyiasasasasstAYtheummonlyemlpystringya-a-" + Chr(100), Chr(34) + Chr(34))
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
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " (" , "(")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , ") " , ")")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , ")." , ") .")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , ".(" , ". (")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "  >= " , " >= ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "  <= " , " <= ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " . " , " + ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " ,  " , ", ")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " [ " , "[")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " ] " , "]")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "!=" , " !=")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , " )" , ")")
    variables['outOftranspileVariables'] = StrReplace(variables['outOftranspileVariables'] , "( " , "(")
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
                variables['outOftranspileVariablesOut'] += Chr(34) + " + variables['" + variables['A_LoopField17'] + Chr(39) + Chr(93) + " + " + Chr(34)
    else:
        variables['sstr'] = Chr(34) + variables['sstr'] + Chr(34)
        return variables['sstr']
    variables['outOftranspileVariablesOut'] = variables['outOftranspileVariablesOut'] + Chr(34)
    return variables['outOftranspileVariablesOut']
# the compiler
def compiler(HTpyCode):
    variables['HTpyCode'] = HTpyCode
    variables['nothing'] = ""
    variables['HTpyCode'] = StrReplace(variables['HTpyCode'] , Chr(13), variables['nothing'])
    variables['pyCode'] = ""
    variables['out'] = ""
    variables['HTpyCodeD1'] = ""
    variables['skipLeftCuleyForFuncPLS'] = 0
    variables['eavbnsalvbaslv'] = 0
    variables['port'] = "8000"
    items = LoopParseFunc(variables['HTpyCode'], "\n", "\r")
    for A_Index18, A_LoopField18 in enumerate(items, start=1):
        variables['A_Index18'] = A_Index18
        variables['A_LoopField18'] = A_LoopField18
        if (variables['A_Index18'] == 1):
            variables['HTpyCodeD1'] += Trim(variables['A_LoopField18']) + "\n"
        else:
            if (Trim(variables['A_LoopField18'])== Chr(123))and(variables['eavbnsalvbaslv'] == 1):
                # nothing
                variables['nothing'] = ""
            else:
                variables['HTpyCodeD1'] += Trim(variables['A_LoopField18']) + "\n"
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
                variables['HTpyCodeOUT754754'] += "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-" + Chr(65) + Chr(65) + str(variables['theIdNumOfThe34']) + Chr(65) + Chr(65)
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
    variables['func_LoopParseFunc_func'] = "\ndef LoopParseFunc(var, delimiter1=" + Chr(34) + "" + Chr(34) + ", delimiter2=" + Chr(34) + "" + Chr(34) + "):\n    import re\n    if not delimiter1 and not delimiter2:\n        # If no delimiters are provided, return a list of characters\n        items = list(var)\n    else:\n        # Construct the regular expression pattern for splitting the string\n        pattern = r'[' + re.escape(delimiter1) + re.escape(delimiter2) + r']+'\n\n        # Split the string using the constructed pattern\n        items = re.split(pattern, var)\n\n    return items\n\n"
    variables['func_InStr_func'] = "\ndef InStr(Haystack, Needle, CaseSensitive=True, StartingPos=1, Occurrence=1):\n    if Haystack is None or Needle is None:\n        return False\n    StartingPos = max(StartingPos, 1)\n    if not CaseSensitive:\n        Haystack = Haystack.lower()\n        Needle = Needle.lower()\n    count = 0\n    for i in range(StartingPos - 1, len(Haystack)):\n        if Haystack[i:i + len(Needle)] == Needle:\n            count += 1\n            if count == Occurrence:\n                return True\n    return False  \n"
    variables['func_SubStr_func'] = "\ndef SubStr(str, startPos, length=None):\n    if str is None or str == " + Chr(34) + "" + Chr(34) + ":\n        return " + Chr(34) + "" + Chr(34) + "\n\n    if length is None or length == " + Chr(34) + "" + Chr(34) + ":\n        length = len(str) - startPos + 1\n\n    if startPos < 1:\n        startPos = len(str) + startPos\n\n    return str[startPos - 1:startPos - 1 + length]\n"
    variables['func_Trim_func'] = "\ndef Trim(inputString):\n    if inputString is None:\n        return " + Chr(34) + "" + Chr(34) + "\n\n    return inputString.strip()\n"
    variables['func_StrReplace_func'] = "  \ndef StrReplace(originalString, find, replaceWith):\n    # Use the replace method to replace occurrences of 'find' with 'replaceWith'\n    return originalString.replace(find, replaceWith)\n"
    variables['func_StringTrimLeft_func'] = "\ndef StringTrimLeft(input, numChars):\n    # Convert input to a string if it's not already a string\n    if not isinstance(input, str):\n        input = str(input)  # Convert input to string\n\n    # Check if the input is long enough to perform trimming\n    if len(input) >= numChars:\n        return input[numChars:]  # Trim the string from the left\n    else:\n        return input  # Return input unchanged if numChars is larger than string length\n"
    variables['func_StringTrimRight_func'] = "\ndef StringTrimRight(input, numChars):\n    # Convert input to a string if it's not already a string\n    if not isinstance(input, str):\n        input = str(input)  # Convert input to string\n\n    # Check if the input is long enough to perform trimming\n    if len(input) >= numChars:\n        return input[:-numChars]  # Trim the string from the right\n    else:\n        return input  # Return input unchanged if numChars is larger than string length\n"
    variables['func_StrLower_func'] = "\ndef StrLower(string):\n    return string.lower()\n"
    variables['func_RegExReplace_func'] = "\ndef RegExReplace(inputStr, regexPattern, replacement):\n    # Create a regular expression object using the provided pattern\n    import re\n    regex = re.compile(regexPattern, re.MULTILINE)  # re.MULTILINE for multi-line matching\n\n    # Use the sub() method to perform the regex replacement\n    resultStr = regex.sub(replacement, inputStr)\n\n    # Return the modified string\n    return resultStr\n"
    variables['func_StrSplit_func'] = "\ndef StrSplit(inputStr, delimiter, num):\n    # Check if the delimiter is empty\n    if delimiter == '':\n        # Return an empty string since splitting with an empty delimiter is not possible\n        return ''\n\n    # Split the input string based on the delimiter\n    parts = inputStr.split(delimiter)\n\n    # Return the part specified by the num parameter (1-based index)\n    if 0 < num <= len(parts):\n        return parts[num - 1]  # Return the specified part (0-based index)\n    else:\n        return ''  # Return an empty string if num is out of range\n"
    variables['func_Chr_func'] = "\ndef Chr(number):\n    # Check if the number is None\n    if number is None:\n        # Return an empty string\n        return " + Chr(34) + "" + Chr(34) + "\n\n    # Check if the number is within the valid Unicode range\n    if 0 <= number <= 0x10FFFF:\n        # Convert the number to a character using chr()\n        return chr(number)\n    else:\n        # Return an empty string for invalid numbers\n        return " + Chr(34) + "" + Chr(34) + "\n\n"
    variables['func_Mod_func'] = "\n# Custom Mod function in Python\ndef Mod(dividend, divisor):\n    return dividend % divisor\n"
    variables['func_HTpy_func'] = "\ndef HTpy():\n    import sys\n    import os\n    if len(sys.argv) < 2 or len(sys.argv) > 3:\n        print(" + Chr(34) + "Usage: python app.py <input_file.htpy> [run]" + Chr(34) + ")\n        sys.exit(1)\n\n    input_file = sys.argv[1]\n\n    # Ensure the input_file ends with '.htpy'\n    if not input_file.endswith('.htpy'):\n        print(" + Chr(34) + "Error: Input file must have a .htpy extension." + Chr(34) + ")\n        sys.exit(1)\n\n    # Check if the input_file exists\n    if not os.path.isfile(input_file):\n        print(f" + Chr(34) + "Error: '{input_file}' is not a valid file path." + Chr(34) + ")\n        sys.exit(1)\n\n    # Determine the output .py file name based on input file name\n    output_file = os.path.splitext(input_file)[0] + '.py'\n\n    # Compile the .htpy content using the compiler function\n    with open(input_file, 'r') as file:\n        htpy_content = file.read()\n\n    compiled_result = compiler(htpy_content)\n\n    # Save the compiled result to the determined .py output file\n    with open(output_file, 'w') as file:\n        file.write(compiled_result)\n\n    print(f" + Chr(34) + "Compiled result saved to '{output_file}'." + Chr(34) + ")\n\n    # Check if 'run' parameter is provided and execute the compiled Python script\n    if len(sys.argv) == 3 and sys.argv[2] == 'run':\n        print(f" + Chr(34) + "Running '{output_file}'..." + Chr(34) + ")\n        try:\n            exec(compile(open(output_file).read(), output_file, 'exec'), globals())\n        except Exception as e:\n            print(f" + Chr(34) + "Error occurred while running the compiled file: {e}" + Chr(34) + ")\n\n"
    variables['func_FileRead_func'] = Chr(10) + Chr(105) + Chr(109) + Chr(112) + Chr(111) + Chr(114) + Chr(116) + Chr(32) + Chr(111) + Chr(115) + Chr(10) + Chr(100) + Chr(101) + Chr(102) + Chr(32) + Chr(70) + Chr(105) + Chr(108) + Chr(101) + Chr(82) + Chr(101) + Chr(97) + Chr(100) + Chr(40) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(35) + Chr(32) + Chr(82) + Chr(101) + Chr(109) + Chr(111) + Chr(118) + Chr(101) + Chr(32) + Chr(97) + Chr(110) + Chr(121) + Chr(32) + Chr(101) + Chr(120) + Chr(116) + Chr(114) + Chr(97) + Chr(32) + Chr(100) + Chr(111) + Chr(117) + Chr(98) + Chr(108) + Chr(101) + Chr(32) + Chr(113) + Chr(117) + Chr(111) + Chr(116) + Chr(101) + Chr(115) + Chr(32) + Chr(97) + Chr(114) + Chr(111) + Chr(117) + Chr(110) + Chr(100) + Chr(32) + Chr(116) + Chr(104) + Chr(101) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(32) + Chr(61) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(46) + Chr(115) + Chr(116) + Chr(114) + Chr(105) + Chr(112) + Chr(40) + Chr(39) + Chr(34) + Chr(39) + Chr(41) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(35) + Chr(32) + Chr(69) + Chr(110) + Chr(115) + Chr(117) + Chr(114) + Chr(101) + Chr(32) + Chr(116) + Chr(104) + Chr(101) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(32) + Chr(105) + Chr(115) + Chr(32) + Chr(97) + Chr(98) + Chr(115) + Chr(111) + Chr(108) + Chr(117) + Chr(116) + Chr(101) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(105) + Chr(102) + Chr(32) + Chr(110) + Chr(111) + Chr(116) + Chr(32) + Chr(111) + Chr(115) + Chr(46) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(46) + Chr(105) + Chr(115) + Chr(97) + Chr(98) + Chr(115) + Chr(40) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(32) + Chr(61) + Chr(32) + Chr(111) + Chr(115) + Chr(46) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(46) + Chr(106) + Chr(111) + Chr(105) + Chr(110) + Chr(40) + Chr(111) + Chr(115) + Chr(46) + Chr(103) + Chr(101) + Chr(116) + Chr(99) + Chr(119) + Chr(100) + Chr(40) + Chr(41) + Chr(44) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(116) + Chr(114) + Chr(121) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(119) + Chr(105) + Chr(116) + Chr(104) + Chr(32) + Chr(111) + Chr(112) + Chr(101) + Chr(110) + Chr(40) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(44) + Chr(32) + Chr(39) + Chr(114) + Chr(39) + Chr(44) + Chr(32) + Chr(101) + Chr(110) + Chr(99) + Chr(111) + Chr(100) + Chr(105) + Chr(110) + Chr(103) + Chr(61) + Chr(39) + Chr(117) + Chr(116) + Chr(102) + Chr(45) + Chr(56) + Chr(39) + Chr(44) + Chr(32) + Chr(101) + Chr(114) + Chr(114) + Chr(111) + Chr(114) + Chr(115) + Chr(61) + Chr(39) + Chr(105) + Chr(103) + Chr(110) + Chr(111) + Chr(114) + Chr(101) + Chr(39) + Chr(41) + Chr(32) + Chr(97) + Chr(115) + Chr(32) + Chr(102) + Chr(105) + Chr(108) + Chr(101) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(99) + Chr(111) + Chr(110) + Chr(116) + Chr(101) + Chr(110) + Chr(116) + Chr(32) + Chr(61) + Chr(32) + Chr(102) + Chr(105) + Chr(108) + Chr(101) + Chr(46) + Chr(114) + Chr(101) + Chr(97) + Chr(100) + Chr(40) + Chr(41) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(114) + Chr(101) + Chr(116) + Chr(117) + Chr(114) + Chr(110) + Chr(32) + Chr(99) + Chr(111) + Chr(110) + Chr(116) + Chr(101) + Chr(110) + Chr(116) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(101) + Chr(120) + Chr(99) + Chr(101) + Chr(112) + Chr(116) + Chr(32) + Chr(70) + Chr(105) + Chr(108) + Chr(101) + Chr(78) + Chr(111) + Chr(116) + Chr(70) + Chr(111) + Chr(117) + Chr(110) + Chr(100) + Chr(69) + Chr(114) + Chr(114) + Chr(111) + Chr(114) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(114) + Chr(101) + Chr(116) + Chr(117) + Chr(114) + Chr(110) + Chr(32) + Chr(39) + Chr(39) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(101) + Chr(120) + Chr(99) + Chr(101) + Chr(112) + Chr(116) + Chr(32) + Chr(69) + Chr(120) + Chr(99) + Chr(101) + Chr(112) + Chr(116) + Chr(105) + Chr(111) + Chr(110) + Chr(32) + Chr(97) + Chr(115) + Chr(32) + Chr(101) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(114) + Chr(101) + Chr(116) + Chr(117) + Chr(114) + Chr(110) + Chr(32) + Chr(78) + Chr(111) + Chr(110) + Chr(101) + Chr(10)
    variables['func_FileAppend_func'] = Chr(10) + Chr(105) + Chr(109) + Chr(112) + Chr(111) + Chr(114) + Chr(116) + Chr(32) + Chr(111) + Chr(115) + Chr(10) + Chr(100) + Chr(101) + Chr(102) + Chr(32) + Chr(70) + Chr(105) + Chr(108) + Chr(101) + Chr(65) + Chr(112) + Chr(112) + Chr(101) + Chr(110) + Chr(100) + Chr(40) + Chr(99) + Chr(111) + Chr(110) + Chr(116) + Chr(101) + Chr(110) + Chr(116) + Chr(44) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(35) + Chr(32) + Chr(82) + Chr(101) + Chr(109) + Chr(111) + Chr(118) + Chr(101) + Chr(32) + Chr(97) + Chr(110) + Chr(121) + Chr(32) + Chr(101) + Chr(120) + Chr(116) + Chr(114) + Chr(97) + Chr(32) + Chr(100) + Chr(111) + Chr(117) + Chr(98) + Chr(108) + Chr(101) + Chr(32) + Chr(113) + Chr(117) + Chr(111) + Chr(116) + Chr(101) + Chr(115) + Chr(32) + Chr(97) + Chr(114) + Chr(111) + Chr(117) + Chr(110) + Chr(100) + Chr(32) + Chr(116) + Chr(104) + Chr(101) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(32) + Chr(61) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(46) + Chr(115) + Chr(116) + Chr(114) + Chr(105) + Chr(112) + Chr(40) + Chr(39) + Chr(34) + Chr(39) + Chr(41) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(35) + Chr(32) + Chr(69) + Chr(110) + Chr(115) + Chr(117) + Chr(114) + Chr(101) + Chr(32) + Chr(116) + Chr(104) + Chr(101) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(32) + Chr(105) + Chr(115) + Chr(32) + Chr(97) + Chr(98) + Chr(115) + Chr(111) + Chr(108) + Chr(117) + Chr(116) + Chr(101) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(105) + Chr(102) + Chr(32) + Chr(110) + Chr(111) + Chr(116) + Chr(32) + Chr(111) + Chr(115) + Chr(46) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(46) + Chr(105) + Chr(115) + Chr(97) + Chr(98) + Chr(115) + Chr(40) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(32) + Chr(61) + Chr(32) + Chr(111) + Chr(115) + Chr(46) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(46) + Chr(106) + Chr(111) + Chr(105) + Chr(110) + Chr(40) + Chr(111) + Chr(115) + Chr(46) + Chr(103) + Chr(101) + Chr(116) + Chr(99) + Chr(119) + Chr(100) + Chr(40) + Chr(41) + Chr(44) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(116) + Chr(114) + Chr(121) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(119) + Chr(105) + Chr(116) + Chr(104) + Chr(32) + Chr(111) + Chr(112) + Chr(101) + Chr(110) + Chr(40) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(44) + Chr(32) + Chr(39) + Chr(97) + Chr(39) + Chr(44) + Chr(32) + Chr(101) + Chr(110) + Chr(99) + Chr(111) + Chr(100) + Chr(105) + Chr(110) + Chr(103) + Chr(61) + Chr(39) + Chr(117) + Chr(116) + Chr(102) + Chr(45) + Chr(56) + Chr(39) + Chr(41) + Chr(32) + Chr(97) + Chr(115) + Chr(32) + Chr(102) + Chr(105) + Chr(108) + Chr(101) + Chr(58) + Chr(32) + Chr(32) + Chr(35) + Chr(32) + Chr(39) + Chr(97) + Chr(39) + Chr(32) + Chr(109) + Chr(111) + Chr(100) + Chr(101) + Chr(32) + Chr(102) + Chr(111) + Chr(114) + Chr(32) + Chr(97) + Chr(112) + Chr(112) + Chr(101) + Chr(110) + Chr(100) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(102) + Chr(105) + Chr(108) + Chr(101) + Chr(46) + Chr(119) + Chr(114) + Chr(105) + Chr(116) + Chr(101) + Chr(40) + Chr(99) + Chr(111) + Chr(110) + Chr(116) + Chr(101) + Chr(110) + Chr(116) + Chr(41) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(114) + Chr(101) + Chr(116) + Chr(117) + Chr(114) + Chr(110) + Chr(32) + Chr(84) + Chr(114) + Chr(117) + Chr(101) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(101) + Chr(120) + Chr(99) + Chr(101) + Chr(112) + Chr(116) + Chr(32) + Chr(69) + Chr(120) + Chr(99) + Chr(101) + Chr(112) + Chr(116) + Chr(105) + Chr(111) + Chr(110) + Chr(32) + Chr(97) + Chr(115) + Chr(32) + Chr(101) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(114) + Chr(101) + Chr(116) + Chr(117) + Chr(114) + Chr(110) + Chr(32) + Chr(70) + Chr(97) + Chr(108) + Chr(115) + Chr(101) + Chr(10)
    variables['func_FileDelete_func'] = Chr(10) + Chr(105) + Chr(109) + Chr(112) + Chr(111) + Chr(114) + Chr(116) + Chr(32) + Chr(111) + Chr(115) + Chr(10) + Chr(100) + Chr(101) + Chr(102) + Chr(32) + Chr(70) + Chr(105) + Chr(108) + Chr(101) + Chr(68) + Chr(101) + Chr(108) + Chr(101) + Chr(116) + Chr(101) + Chr(40) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(35) + Chr(32) + Chr(69) + Chr(110) + Chr(115) + Chr(117) + Chr(114) + Chr(101) + Chr(32) + Chr(116) + Chr(104) + Chr(101) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(32) + Chr(105) + Chr(115) + Chr(32) + Chr(97) + Chr(98) + Chr(115) + Chr(111) + Chr(108) + Chr(117) + Chr(116) + Chr(101) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(105) + Chr(102) + Chr(32) + Chr(110) + Chr(111) + Chr(116) + Chr(32) + Chr(111) + Chr(115) + Chr(46) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(46) + Chr(105) + Chr(115) + Chr(97) + Chr(98) + Chr(115) + Chr(40) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(32) + Chr(61) + Chr(32) + Chr(111) + Chr(115) + Chr(46) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(46) + Chr(106) + Chr(111) + Chr(105) + Chr(110) + Chr(40) + Chr(111) + Chr(115) + Chr(46) + Chr(103) + Chr(101) + Chr(116) + Chr(99) + Chr(119) + Chr(100) + Chr(40) + Chr(41) + Chr(44) + Chr(32) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(116) + Chr(114) + Chr(121) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(105) + Chr(102) + Chr(32) + Chr(111) + Chr(115) + Chr(46) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(46) + Chr(101) + Chr(120) + Chr(105) + Chr(115) + Chr(116) + Chr(115) + Chr(40) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(111) + Chr(115) + Chr(46) + Chr(114) + Chr(101) + Chr(109) + Chr(111) + Chr(118) + Chr(101) + Chr(40) + Chr(112) + Chr(97) + Chr(116) + Chr(104) + Chr(41) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(101) + Chr(120) + Chr(99) + Chr(101) + Chr(112) + Chr(116) + Chr(32) + Chr(69) + Chr(120) + Chr(99) + Chr(101) + Chr(112) + Chr(116) + Chr(105) + Chr(111) + Chr(110) + Chr(58) + Chr(10) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(112) + Chr(97) + Chr(115) + Chr(115) + Chr(32) + Chr(32) + Chr(32) + Chr(32) + Chr(10) + Chr(10)
    variables['func_GetParams_func'] = "\nimport os\nimport sys\n\ndef GetParams():\n    # Check if any command line arguments are provided\n    if len(sys.argv) < 2:\n        return " + Chr(34) + "" + Chr(34) + "\n\n    # Store the provided command line arguments\n    params = []\n    for arg in sys.argv[1:]:\n        if os.path.exists(arg):\n            arg = os.path.abspath(arg)\n        params.append(arg)\n\n    return " + Chr(34) + "" + Chr(92) + "n" + Chr(34) + ".join(params)\n"
    variables['func_Floor_func'] = "\ndef Floor(num):\n    import math\n    if num is None or not isinstance(num, (int, float)):\n        return None\n    return math.floor(num)\n"
    variables['func_A_TickCount_func'] = "\nimport time\n\nstart_timestamp = int(time.time() * 1000)  # Initialize with current timestamp in milliseconds\n\n# Function to calculate tick count in milliseconds\ndef A_TickCount():\n    return int(time.time() * 1000) - start_timestamp\n"
    variables['func_RunCMD_func'] = "\nimport subprocess\ndef RunCMD(command):\n    try:\n        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)\n        return result.stdout\n    except subprocess.CalledProcessError as e:\n        print(f" + Chr(34) + "Error: {e}" + Chr(34) + ")\n        return e.stdout + " + Chr(34) + "" + Chr(92) + "n" + Chr(34) + " + e.stderr\n    except Exception as e:\n        print(f" + Chr(34) + "An unexpected error occurred: {e}" + Chr(34) + ")\n        return " + Chr(34) + "" + Chr(34) + "\n"
    variables['func_SortLikeAHK_func'] = "\nimport random\ndef SortLikeAHK(var_name, options):\n    # Determine delimiter based on options\n    delimiter = '" + Chr(92) + "n'\n    if 'D' in options:\n        delimiter = options[options.index('D') + 1]\n    \n    # Split the input variable by delimiter\n    items = var_name.split(delimiter)\n    \n    # Remove empty items and strip whitespace\n    items = [item.strip() for item in items if item.strip()]\n    \n    # Apply sorting based on options\n    if 'N' in options:\n        # Numeric sort\n        items.sort(key=lambda x: int(x))\n    elif 'Random' in options:\n        # Random sort\n        random.shuffle(items)\n    else:\n        # Default alphabetical sort\n        items.sort(key=lambda x: x.lower() if 'C' not in options else x)\n    \n    # Reverse if 'R' option is present\n    if 'R' in options:\n        items.reverse()\n    \n    # Remove duplicates if 'U' option is present\n    if 'U' in options:\n        seen = set()\n        unique_items = []\n        for item in items:\n            lower_item = item.lower() if 'C' not in options else item\n            if lower_item not in seen:\n                seen.add(lower_item)\n                unique_items.append(item)\n        items = unique_items\n    \n    # Join the sorted items back into a string\n    sorted_var = delimiter.join(items)\n    \n    return sorted_var\n"
    variables['func_BuildInVars_func'] = "\nimport time\nfrom datetime import datetime\n# Initialize with current timestamp\nlast_input_time = time.time() * 1000  # Convert to milliseconds\nstart_timestamp = time.time() * 1000  # Convert to milliseconds\n\n# Function to reset the idle timer\ndef reset_idle_timer():\n    global last_input_time\n    last_input_time = time.time() * 1000  # Update last input time in milliseconds\n\n# Function to calculate tick count in milliseconds\ndef A_TickCount():\n    return int(time.time() * 1000 - start_timestamp)\n\n# Function to build in variables\ndef BuildInVars(varName):\n    now = datetime.now()\n    if varName == " + Chr(34) + "A_TickCount" + Chr(34) + ":\n        # Return tick count in milliseconds\n        return A_TickCount()\n    elif varName == " + Chr(34) + "A_Now" + Chr(34) + ":\n        # Return current local timestamp\n        return now.strftime(" + Chr(34) + "%Y-%m-%d %H:%M:%S" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_YYYY" + Chr(34) + ":\n        # Return current year\n        return now.strftime(" + Chr(34) + "%Y" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_MM" + Chr(34) + ":\n        # Return current month\n        return now.strftime(" + Chr(34) + "%m" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_DD" + Chr(34) + ":\n        # Return current day\n        return now.strftime(" + Chr(34) + "%d" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_MMMM" + Chr(34) + ":\n        # Return full month name\n        return now.strftime(" + Chr(34) + "%B" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_MMM" + Chr(34) + ":\n        # Return short month name\n        return now.strftime(" + Chr(34) + "%b" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_DDDD" + Chr(34) + ":\n        # Return full day name\n        return now.strftime(" + Chr(34) + "%A" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_DDD" + Chr(34) + ":\n        # Return short day name\n        return now.strftime(" + Chr(34) + "%a" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_Hour" + Chr(34) + ":\n        # Return current hour\n        return now.strftime(" + Chr(34) + "%H" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_Min" + Chr(34) + ":\n        # Return current minute\n        return now.strftime(" + Chr(34) + "%M" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_Sec" + Chr(34) + ":\n        # Return current second\n        return now.strftime(" + Chr(34) + "%S" + Chr(34) + ")\n    elif varName == " + Chr(34) + "A_Space" + Chr(34) + ":\n        # Return space character\n        return " + Chr(34) + " " + Chr(34) + "\n    elif varName == " + Chr(34) + "A_Tab" + Chr(34) + ":\n        # Return tab character\n        return " + Chr(34) + Chr(92) + "t" + Chr(34) + "\n    else:\n        # Handle unknown variable names\n        return None\n"
    variables['func_Floor_func'] = "\ndef Floor(number):\n    if number > 0:\n        return int(number)\n    else:\n        return int(number) - (1 if number != int(number) else 0)\n\n"
    variables['func_ExitApp_func'] = "\nimport os\n# Function to handle application termination\ndef ExitApp():\n    os._exit(1)\n\n"
    variables['func_SetTimer_func'] = "\nimport time\nimport threading\n# Dictionary to store active timers\nactive_timers = {}\n\n# Function to start, stop, or adjust a timer\ndef SetTimer(func, timeOrOnOff):\n    def timer_wrapper(name, interval_ms):\n        def run_timer():\n            func()\n            if active_timers[name]['running']:\n                active_timers[name]['timer'] = threading.Timer(interval_ms / 1000.0, run_timer)\n                active_timers[name]['timer'].start()\n                \n        if timeOrOnOff == " + Chr(34) + "On" + Chr(34) + " and not active_timers[name]['running']:\n            active_timers[name]['timer'] = threading.Timer(active_timers[name]['interval_ms'] / 1000.0, run_timer)\n            active_timers[name]['timer'].start()\n            active_timers[name]['running'] = True\n            #print(f" + Chr(34) + "Timer '{name}' started with interval {active_timers[name]['interval_ms']} ms." + Chr(34) + ")\n        elif timeOrOnOff == " + Chr(34) + "Off" + Chr(34) + " and active_timers[name]['running']:\n            active_timers[name]['timer'].cancel()\n            active_timers[name]['running'] = False\n            #print(f" + Chr(34) + "Timer '{name}' stopped." + Chr(34) + ")\n        elif isinstance(timeOrOnOff, int):\n            active_timers[name]['interval_ms'] = timeOrOnOff  # Update the stored interval\n            if active_timers[name]['running']:\n                active_timers[name]['timer'].cancel()\n                active_timers[name]['timer'] = threading.Timer(timeOrOnOff / 1000.0, run_timer)\n                active_timers[name]['timer'].start()\n                #print(f" + Chr(34) + "Timer '{name}' adjusted to interval {timeOrOnOff} ms." + Chr(34) + ")\n            else:\n                active_timers[name]['timer'] = threading.Timer(timeOrOnOff / 1000.0, run_timer)\n                active_timers[name]['timer'].start()\n                active_timers[name]['running'] = True\n                #print(f" + Chr(34) + "Timer '{name}' started with adjusted interval {timeOrOnOff} ms." + Chr(34) + ")\n        else:\n            print(" + Chr(34) + "Invalid arguments. Please provide a valid function and time/On/Off state." + Chr(34) + ")\n\n    # Ensure func is callable\n    if not callable(func):\n        print(" + Chr(34) + "Invalid function provided." + Chr(34) + ")\n        return\n\n    name = func.__name__  # Use function name as timer identifier\n\n    # Initialize timer if not already active\n    if name not in active_timers:\n        active_timers[name] = {\n            'timer': None,\n            'running': False,\n            'interval_ms': 1000  # Default interval\n        }\n\n    # Determine the interval_ms value\n    if isinstance(timeOrOnOff, int):\n        interval_ms = timeOrOnOff\n    else:\n        interval_ms = active_timers[name]['interval_ms']  # Use stored interval\n\n    # Call timer_wrapper to manage timer based on timeOrOnOff\n    timer_wrapper(name, interval_ms)\n"
    variables['func_Abs_func'] = "\ndef Abs(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return abs(num)\n"
    variables['func_ACos_func'] = "\ndef ACos(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.acos(num)\n"
    variables['func_ASin_func'] = "\ndef ASin(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.asin(num)\n"
    variables['func_ATan_func'] = "\ndef ATan(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.atan(num)\n"
    variables['func_Ceil_func'] = "\ndef Ceil(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.ceil(num)\n"
    variables['func_Cos_func'] = "\ndef Cos(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.cos(num)\n"
    variables['func_Exp_func'] = "\ndef Exp(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.exp(num)\n"
    variables['func_Ln_func'] = "\ndef Ln(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.log(num)\n"
    variables['func_Log_func'] = "\ndef Log(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.log10(num)\n"
    variables['func_Round_func'] = "\ndef Round(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return round(num)\n"
    variables['func_Sin_func'] = "\ndef Sin(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.sin(num)\n"
    variables['func_Sqrt_func'] = "\ndef Sqrt(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.sqrt(num)\n"
    variables['func_Tan_func'] = "\ndef Tan(num):\n    import math\n    if num is None or math.isnan(num):\n        return None\n    return math.tan(num)\n"
    variables['func_RegExMatch_func'] = "\ndef RegExMatch(Haystack, NeedleRegEx, OutputVar=None, StartingPos=0):\n    import re\n    if Haystack is None or NeedleRegEx is None:\n        return None\n\n    regex = re.compile(NeedleRegEx)\n    match = regex.search(Haystack)\n\n    if match:\n        if OutputVar is not None:\n            OutputVar.append(match.group(0))\n        return match.start() + 1\n    else:\n        return 0\n"
    variables['func_StrLen_func'] = "\ndef StrLen(string):\n    if string is None:\n        return None\n    return len(string)\n"
    variables['func_Asc_func'] = "\ndef Asc(char):\n    if char is None or len(char) == 0:\n        return None\n    return ord(char[0])\n"
    variables['func_getDataFromAPI_func'] = "\nimport json\nimport urllib.request\nimport urllib.error\ndef getDataFromAPI(url):\n    try:\n        with urllib.request.urlopen(url) as response:\n            if response.getcode() == 200:\n                return response.read()\n            else:\n                return None\n    except urllib.error.URLError as e:\n        print(f" + Chr(34) + "Error accessing URL: {e.reason}" + Chr(34) + ")\n        return None\n"
    variables['func_getDataFromJSON_func'] = "\nimport json\nimport re\ndef getDataFromJSON(json_data, json_path):\n    try:\n        if json_data:\n            json_data = json.loads(json_data)  # Parse JSON data into Python object\n\n        # Check if the path starts with a dot and remove it if present\n        if json_path.startswith(" + Chr(34) + "." + Chr(34) + "):\n            json_path = json_path[1:]\n\n        path_segments = json_path.split(" + Chr(34) + "." + Chr(34) + ")  # Split the path into segments\n        current_data = json_data  # Use json_data directly (already an object)\n\n        for segment in path_segments:\n            if current_data is None:\n                return None\n\n            # Handle array indices e.g., " + Chr(34) + "Children[0]" + Chr(34) + "\n            if " + Chr(34) + "[" + Chr(34) + " in segment and " + Chr(34) + "]" + Chr(34) + " in segment:\n                array_index = re.search(r" + Chr(34) + "" + Chr(92) + "[(" + Chr(92) + "d+)" + Chr(92) + "]" + Chr(34) + ", segment)\n                if array_index:\n                    array_name = segment[:segment.index(" + Chr(34) + "[" + Chr(34) + ")]\n                    index = int(array_index.group(1))\n                    if array_name:\n                        current_data = current_data.get(array_name, [])[index]\n                    else:\n                        current_data = current_data[index]\n                    segment = segment[segment.index(" + Chr(34) + "]" + Chr(34) + ") + 1:]\n\n            # Handle regular dictionary keys\n            if segment:\n                current_data = current_data.get(segment, None)\n\n        return current_data\n\n    except (TypeError, IndexError, KeyError) as error:\n        print(f" + Chr(34) + "Error accessing data: {error}" + Chr(34) + ")\n        return None\n"
    variables['funcs_func'] = "LoopParseFunc|InStr|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|StrLower|RegExReplace|StrSplit|Chr|Mod|FileRead|FileAppend|FileDelete|GetParams|Floor|RunCMD|SortLikeAHK|BuildInVars|Floor|ExitApp|SetTimer|Abs|ACos|ASin|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|RegExMatch|StrLen|Asc|getDataFromAPI|getDataFromJSON"
    variables['functionNames'] = "input|int|chr|str|InStr|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|StrLower|RegExReplace|StrSplit|Chr|Mod|FileRead|FileAppend|FileDelete|GetParams|RunCMD|SortLikeAHK|BuildInVars|Floor|ExitApp|SetTimer|Abs|ACos|ASin|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|RegExMatch|StrLen|Asc|getDataFromAPI|getDataFromJSON|float"
    variables['funcs_func'] += "|HTpy"
    variables['functionNames'] += "|HTpy"
    variables['awesdrtf'] = "|A" + Chr(95) + "LoopField|A" + Chr(95) + "Index"
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
                variables['functionNames'] += "|" + variables['lastFuncName']
                #lastFuncFullName
                variables['theFuncWeFound'] += variables['lastFuncFullName'] + "\n"
                variables['theFuncWeFoundAllNames'] += variables['lastFuncName'] + Chr(40) + "\n"
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
        if (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 10)== StrLower("msgbox, % ")):
            variables['var1'] = StringTrimLeft(variables['A_LoopField23'], 10)
            variables['var2'] = Trim(transpileVariables(variables['var1'] , variables['functionNames']))
            variables['out'] = "print(" + variables['var2'] + ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 8)== StrLower("msgbox, "))and(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 10) != StrLower("msgbox, % ")):
            variables['var1'] = StringTrimLeft(variables['A_LoopField23'], 8)
            variables['OUTvarMsgLow'] = transpileLowVariables(variables['var1'])
            variables['OUTvarMsgLow'] = StrReplace(variables['OUTvarMsgLow'] , Chr(96), Chr(92))
            variables['out'] = "print(" + variables['OUTvarMsgLow'] + ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 6)== "sort, "):
            variables['str1'] = StringTrimLeft(variables['A_LoopField23'], 6)
            variables['str1'] = Trim(variables['str1'])
            variables['weHaveAcommaFixSortCommand'] = 0
            if (SubStr(variables['str1'] , 0)== Chr(44)):
                #MsgBox, comma YES
                variables['str1'] = StringTrimRight(variables['str1'], 1)
                variables['weHaveAcommaFixSortCommand'] = 1
            else:
                #MsgBox, comma NO
                variables['gg'] = 0
            variables['s'] = StrSplit(variables['str1'] , "," , 1)
            variables['out1'] = Trim(variables['s'])
            variables['s'] = StrSplit(variables['str1'] , "," , 2)
            variables['out2'] = Trim(variables['s'])
            if (variables['weHaveAcommaFixSortCommand'] == 1):
                variables['out2'] = variables['out2'] + Chr(44)
            variables['var1'] = "variables['" + variables['out1'] + "'] = SortLikeAHK(variables['" + variables['out1'] + "'], " + Chr(34) + variables['out2'] + Chr(34) + ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['var1'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 6)== StrLower("Port, ")):
            variables['str1'] = StringTrimLeft(variables['A_LoopField23'], 6)
            variables['str1'] = Trim(transpileVariables(variables['str1'] , variables['functionNames']))
            variables['var1'] = "variables['port'] = " + str(variables['str1'])
            variables['port'] = "variables['port']"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['var1'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 8)== StrLower("Random, ")):
            variables['varr1'] = StrSplit(variables['A_LoopField23'] , "," , 2)
            variables['varr2'] = StrSplit(variables['A_LoopField23'] , "," , 3)
            variables['varr3'] = StrSplit(variables['A_LoopField23'] , "," , 4)
            variables['outt1'] = Trim(transpileVariables(variables['varr1'] , variables['functionNames']))
            variables['outt2'] = Trim(transpileVariables(variables['varr2'] , variables['functionNames']))
            variables['outt3'] = Trim(transpileVariables(variables['varr3'] , variables['functionNames']))
            variables['weUseRandomAtLeastOnce'] += 1
            if (variables['weUseRandomAtLeastOnce'] == 1):
                variables['usedLib'] += "import random\n"
            variables['out'] = variables['outt1'] + " = " + "random.randint(" + variables['outt2'] + ", " + variables['outt3'] + ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 17)== StrLower("StringTrimRight, ")):
            variables['varr1'] = StrSplit(variables['A_LoopField23'] , "," , 2)
            variables['varr2'] = StrSplit(variables['A_LoopField23'] , "," , 3)
            variables['varr3'] = StrSplit(variables['A_LoopField23'] , "," , 4)
            variables['outt1'] = Trim(transpileVariables(variables['varr1'] , variables['functionNames']))
            variables['outt2'] = Trim(transpileVariables(variables['varr2'] , variables['functionNames']))
            variables['outt3'] = Trim(transpileVariables(variables['varr3'] , variables['functionNames']))
            variables['out'] = variables['outt1'] + " = " + "StringTrimRight(" + variables['outt2'] + ", " + variables['outt3'] + ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 16)== StrLower("StringTrimLeft, ")):
            variables['varr1'] = StrSplit(variables['A_LoopField23'] , "," , 2)
            variables['varr2'] = StrSplit(variables['A_LoopField23'] , "," , 3)
            variables['varr3'] = StrSplit(variables['A_LoopField23'] , "," , 4)
            variables['outt1'] = Trim(transpileVariables(variables['varr1'] , variables['functionNames']))
            variables['outt2'] = Trim(transpileVariables(variables['varr2'] , variables['functionNames']))
            variables['outt3'] = Trim(transpileVariables(variables['varr3'] , variables['functionNames']))
            variables['out'] = variables['outt1'] + " = " + "StringTrimLeft(" + variables['outt2'] + ", " + variables['outt3'] + ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 7)== StrLower("sleep, ")):
            variables['var1'] = StringTrimLeft(variables['A_LoopField23'], 7)
            variables['var1'] = Trim(transpileVariables(variables['var1'] , variables['functionNames']))
            variables['out'] = "time.sleep(" + variables['var1'] + " / 1000" + ")"
            variables['lineDone'] = 1
            variables['onceImportTime'] += 1
            if (variables['onceImportTime'] == 1):
                variables['usedLib'] += "import time\n"
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 10)== "settimer, "):
            variables['str1'] = StringTrimLeft(variables['A_LoopField23'], 10)
            variables['str2'] = Trim(StrSplit(variables['str1'] , "," , 1))
            variables['str3'] = Trim(StrSplit(variables['str1'] , "," , 2))
            if (StrLower(variables['str3'])== "on"):
                variables['str3'] = Chr(34) + "On" + Chr(34)
            if (StrLower(variables['str3'])== "off"):
                variables['str3'] = Chr(34) + "Off" + Chr(34)
            variables['out1'] = "SetTimer(" + variables['str2'] + ", " + variables['str3'] + ")"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out1'] + "\n"
        elif (Trim(StrLower(variables['A_LoopField23']))== "exitapp"):
            variables['lineDone'] = 1
            variables['pyCode'] += "ExitApp()" + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 10)== "fileread, "):
            variables['filereadCommand'] = StringTrimLeft(variables['A_LoopField23'], 10)
            variables['filereadCommand1varname'] = StrSplit(variables['filereadCommand'] , ", " , 1)
            variables['filereadCommand2path'] = StrSplit(variables['filereadCommand'] , ", " , 2)
            variables['filereadCommand2path'] = StrReplace(variables['filereadCommand2path'] , "\\" , "\\\\")
            variables['filereadCommand2path'] = Trim(transpileLowVariables(variables['filereadCommand2path']))
            variables['filereadCommand1varname'] = Trim(transpileVariables(variables['filereadCommand1varname'] , variables['functionNames']))
            variables['pyCode'] += variables['filereadCommand1varname'] + " = FileRead(" + variables['filereadCommand2path'] + ")\n"
            variables['lineDone'] = 1
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 12)== "fileappend, "):
            variables['fileAppendCommand'] = StringTrimLeft(variables['A_LoopField23'], 12)
            variables['fileAppendCommand1varname'] = StrSplit(variables['fileAppendCommand'] , ", " , 1)
            variables['fileAppendCommand2path'] = StrSplit(variables['fileAppendCommand'] , ", " , 2)
            variables['fileAppendCommand2path'] = StrReplace(variables['fileAppendCommand2path'] , "\\" , "\\\\")
            variables['fileAppendCommand1varname'] = Trim(transpileLowVariables(variables['fileAppendCommand1varname']))
            variables['fileAppendCommand2path'] = Trim(transpileLowVariables(variables['fileAppendCommand2path']))
            variables['pyCode'] += "FileAppend(" + variables['fileAppendCommand1varname'] + ", " + variables['fileAppendCommand2path'] + ")\n"
            variables['lineDone'] = 1
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 12)== "filedelete, "):
            variables['fileDeleteCommand'] = StringTrimLeft(variables['A_LoopField23'], 12)
            variables['fileDeleteCommand2path'] = StrSplit(variables['fileDeleteCommand'] , ", " , 1)
            variables['fileDeleteCommand2path'] = StrReplace(variables['fileDeleteCommand2path'] , "\\" , "\\\\")
            variables['fileDeleteCommand2path'] = Trim(transpileLowVariables(variables['fileDeleteCommand2path']))
            variables['pyCode'] += "FileDelete(" + variables['fileDeleteCommand2path'] + ")\n"
            variables['lineDone'] = 1
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
                    variables['theVarsPArmFormTheFunc'] += "variables['" + variables['var1'] + "'] = " + variables['var1'] + "\n"
            variables['skipLeftCuleyForFuncPLS'] = 0
            if (variables['str23IfFuncInALL']  != ""):
                variables['str234567'] = "def " + variables['str23IfFuncInNAME'] + Chr(40) + variables['str23IfFuncInALL'] + Chr(41) + ":\n{\n" + variables['theVarsPArmFormTheFunc']
                variables['skipLeftCuleyForFuncPLS'] = 1
            else:
                variables['str234567'] = "def " + variables['str23IfFuncInNAME'] + Chr(40) + variables['str23IfFuncInALL'] + Chr(41) + ":"
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
                            variables['var12312'] += transpileVariables(variables['var1'] , variables['functionNames']) + ", "
                        variables['var12312'] = StringTrimRight(variables['var12312'], 2)
                    if (variables['wasHereInfuncAndgetingVar1'] == 0):
                        variables['str2345678'] = variables['str23IfFuncInNAME'] + Chr(40) + Chr(41)
                    else:
                        variables['str2345678'] = variables['str23IfFuncInNAME'] + Chr(40) + variables['var12312'] + Chr(41)
                    variables['lineDone'] = 1
            variables['str23IfFuncInNAMEnum'] += 1
            variables[f'str23IfFuncInNAME{variables["str23IfFuncInNAMEnum"]}'] = variables['str23IfFuncInNAME']
            if (variables['lineDone'] == 1):
                variables['pyCode'] += variables['str2345678'] + "\n"
            else:
                variables['lineDone'] = 1
                variables['pyCode'] += variables['str234567'] + "\n"
        elif (SubStr(Trim(variables['A_LoopField23']), 1 , 7)== "return "):
            variables['strFormReturn'] = StringTrimLeft(variables['A_LoopField23'], 7)
            variables['var12312'] = transpileVariables(variables['strFormReturn'] , variables['functionNames'])
            variables['out'] = "return " + variables['var12312']
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 10)== "endpoint, "):
            variables['strFormEndpoint'] = StringTrimLeft(variables['A_LoopField23'], 10)
            variables['strFormEndpoint1'] = Trim(StrSplit(variables['strFormEndpoint'] , "," , 1))
            variables['strFormEndpoint2'] = Trim(StrSplit(variables['strFormEndpoint'] , "," , 2))
            variables['putEndPointFlask1Up'] = "from flask import Flask, send_file, request, jsonify\nimport os\nvariables = {}\napp = Flask(__name__)\n\n@app.route('/')\ndef app_route():\n    return send_file(os.path.join(os.path.dirname(__file__), 'index.html')), 200\n"
            variables['putEndPointFlask2Down'] = "\n@app.errorhandler(404)\ndef not_found(e):\n    return " + Chr(34) + "Page not found" + Chr(34) + ", 404\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=" + str(variables['port']) + ", debug=True)"
            variables['firstLineVar1'] = "@app.route('/" + variables['strFormEndpoint2'] + "', methods=['POST'])"
            variables['firstLineVar2'] = "def " + variables['strFormEndpoint2'] + "():"
            variables['firstLineVar3'] = "|variables['" + variables['strFormEndpoint1'] + "'] = request.get_json()"
            variables['out'] = variables['firstLineVar1'] + "\n" + variables['firstLineVar2'] + "\n" + variables['firstLineVar3']
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (StrLower(variables['A_LoopField23'])== "loop"):
            # infinity loops
            variables['haveWeEverUsedAloop'] = 1
            variables['lineDone'] = 1
            variables['var1'] = "for A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " , value in enumerate(iter(int, 1), start=1):"
            variables['nothing'] = ""
            variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
            variables['theFixTextLoopNL'] = "variables['A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "'] = A" + Chr(95) + "Index" + str(variables['AindexcharLength'])
            variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
            variables['lineDone'] = 1
            variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
            variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
            variables['AindexcharLength'] += 1
            variables['pyCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 6)== "loop, ")and(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 8) != "loop, % ")and(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 7) != "loop % ")and(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 11) != StrLower("Loop, Parse")):
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
            variables['var1'] = "for A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " in range(1, " + variables['line'] + " + 1):"
            variables['nothing'] = ""
            variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
            variables['theFixTextLoopNL'] = "variables['A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "'] = A" + Chr(95) + "Index" + str(variables['AindexcharLength'])
            variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
            variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
            variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
            variables['AindexcharLength'] += 1
            variables['lineDone'] = 1
            variables['pyCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 8)== "loop, % "):
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
            variables['var1'] = "for A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " in range(1, " + variables['line'] + " + 1):"
            variables['nothing'] = ""
            variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
            variables['theFixTextLoopNL'] = "variables['A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "'] = A" + Chr(95) + "Index" + str(variables['AindexcharLength'])
            variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
            variables['haveWeEverUsedAloop'] = 1
            variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
            variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
            variables['AindexcharLength'] += 1
            variables['lineDone'] = 1
            variables['pyCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 13)== StrLower("Loop, Parse, ")):
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
            if (InStr(variables['var1'] , Chr(96) + ",")):
                variables['line2'] = Chr(34) + "," + Chr(34)
                variables['itemsOut'] = "items = LoopParseFunc(" + variables['line1'] + ", " + variables['line2'] + ")"
            else:
                if (variables['line2'] == "")and(variables['line3'] == ""):
                    # nothing so only each char
                    variables['itemsOut'] = "items = LoopParseFunc(" + variables['line1'] + ")"
                if (variables['line2']  != "")and(variables['line3'] == ""):
                    if (InStr(variables['line2'] , Chr(96))):
                        variables['line2'] = Chr(34) + variables['line2'] + Chr(34)
                    variables['itemsOut'] = "items = LoopParseFunc(" + variables['line1'] + ", " + variables['line2'] + ")"
                if (variables['line2']  != "")and(variables['line3']  != ""):
                    if (InStr(variables['line2'] , Chr(96))):
                        variables['line2'] = Chr(34) + variables['line2'] + Chr(34)
                    if (InStr(variables['line3'] , Chr(96))):
                        variables['line3'] = Chr(34) + variables['line3'] + Chr(34)
                    variables['itemsOut'] = "items = LoopParseFunc(" + variables['line1'] + ", " + variables['line2'] + ", " + variables['line3'] + ")"
                variables['itemsOut'] = StrReplace(variables['itemsOut'] , Chr(96), Chr(92))
            variables['var1out'] = variables['itemsOut'] + "\n" + "for A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + ", A" + Chr(95) + "LoopField" + str(variables['AindexcharLength']) + " in enumerate(items, start=1):"
            variables['nothing'] = ""
            variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
            variables['theFixTextLoopLP'] = "variables['A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "'] = A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "\n" + "variables['A" + Chr(95) + "LoopField" + str(variables['AindexcharLength']) + "'] = A" + Chr(95) + "LoopField" + str(variables['AindexcharLength'])
            variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 1
            variables['haveWeEverUsedAloop'] = 1
            variables['pycodeLoopfixa'] += "lp|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
            variables['pycodeLoopfixa1'] = "lp|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
            variables['AindexcharLength'] += 1
            variables['pyCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 7)== "gosub, "):
            #MsgBox, % A_LoopField23
            variables['sstr1'] = variables['A_LoopField23']
            variables['s'] = StrSplit(variables['sstr1'] , "," , 2)
            variables['out1'] = variables['s']
            variables['out1'] = Trim(variables['out1'])
            variables['out2'] = variables['out1'] + "()"
            #MsgBox, % out2
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out2'] + "\n"
        elif (variables['A_LoopField23'] == "Return"):
            variables['pyCode'] += "}" + "\n"
            variables['lineDone'] = 1
        elif (RegExReplace(variables['A_LoopField23'] , "^\\w+:$" , "") != variables['A_LoopField23'])and(Trim(SubStr(variables['A_LoopField23'] , 0))== ":")and(variables['lineDone']  != 1):
            #MsgBox, % A_LoopField23
            variables['out1'] = variables['A_LoopField23']
            variables['out1'] = Trim(variables['out1'])
            variables['out1'] = StringTrimRight(variables['out1'], 1)
            variables['pyCode'] += "def " + variables['out1'] + "():\n{\n"
            #MsgBox, % out1
            #~ MsgBox, % see
            variables['lineDone'] = 1
        elif (SubStr(variables['A_LoopField23'] , -1)== "++"):
            variables['str123'] = Trim(variables['A_LoopField23'])
            variables['str123'] = StringTrimRight(variables['str123'], 2)
            variables['str123'] = Trim(transpileVariables(variables['str123'] , variables['functionNames']))
            variables['out'] = variables['str123'] + " += 1"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(variables['A_LoopField23'] , -1)== "--"):
            variables['str123'] = Trim(variables['A_LoopField23'])
            variables['str123'] = StringTrimRight(variables['str123'], 2)
            variables['str123'] = Trim(transpileVariables(variables['str123'] , variables['functionNames']))
            variables['out'] = variables['str123'] + " -= 1"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 4)== StrLower(variables['CheckIFandElsesss1']))or(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 3)== StrLower(variables['CheckIFandElsesss2']))or(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 5)== StrLower(variables['CheckIFandElsesss3']))or(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 4)== StrLower(variables['CheckIFandElsesss4']))or(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 9)== StrLower(variables['CheckIFandElsesss5']))or(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 8)== StrLower(variables['CheckIFandElsesss6']))or(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 10)== StrLower(variables['CheckIFandElsesss7']))or(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 9)== StrLower(variables['CheckIFandElsesss8'])):
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 4)== StrLower(variables['CheckIFandElsesss1'])):
                variables['CheckIFandElsesssNum'] = 4
                variables['CheckIFandElsesssNumNum'] = 1
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 3)== StrLower(variables['CheckIFandElsesss2'])):
                variables['CheckIFandElsesssNum'] = 3
                variables['CheckIFandElsesssNumNum'] = 2
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 5)== StrLower(variables['CheckIFandElsesss3'])):
                variables['CheckIFandElsesssNum'] = 5
                variables['CheckIFandElsesssNumNum'] = 3
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 4)== StrLower(variables['CheckIFandElsesss4'])):
                variables['CheckIFandElsesssNum'] = 4
                variables['CheckIFandElsesssNumNum'] = 4
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 9)== StrLower(variables['CheckIFandElsesss5'])):
                variables['CheckIFandElsesssNum'] = 9
                variables['CheckIFandElsesssNumNum'] = 5
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 8)== StrLower(variables['CheckIFandElsesss6'])):
                variables['CheckIFandElsesssNum'] = 8
                variables['CheckIFandElsesssNumNum'] = 6
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 10)== StrLower(variables['CheckIFandElsesss7'])):
                variables['CheckIFandElsesssNum'] = 10
                variables['CheckIFandElsesssNumNum'] = 7
            if (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 9)== StrLower(variables['CheckIFandElsesss8'])):
                variables['CheckIFandElsesssNum'] = 9
                variables['CheckIFandElsesssNumNum'] = 8
            variables['str123'] = StringTrimLeft(variables['A_LoopField23'], variables['CheckIFandElsesssNum'])
            variables['str123'] = variables[f'CheckIFandElsesss{variables["CheckIFandElsesssNumNum"]}'] + Chr(32) + transpileVariables(variables['str123'] , variables['functionNames'])
            if (SubStr(Trim(StrLower(variables['str123'])), 1 , 7)== StrLower("else if")):
                variables['str123'] = StrReplace(variables['str123'] , "else if" , "elif")
            else:
                variables['str123'] = variables['str123']
                variables['str123'] = StringTrimLeft(variables['str123'], 2)
                variables['str123'] = "if" + variables['str123']
            variables['str123'] = Trim(variables['str123']) + ":"
            variables['str123'] = StrReplace(variables['str123'] , "if " + Chr(40) + Chr(32), "if " + Chr(40))
            variables['str123'] = StrReplace(variables['str123'] , Chr(32) + Chr(41) + ":" , Chr(41) + ":")
            variables['out'] = variables['str123']
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (StrLower(variables['A_LoopField23'])== StrLower("else")):
            variables['out'] = "else:"
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (InStr(variables['A_LoopField23'] , " := "))or(InStr(variables['A_LoopField23'] , " .= "))or(InStr(variables['A_LoopField23'] , " += "))or(InStr(variables['A_LoopField23'] , " -= "))or(InStr(variables['A_LoopField23'] , " *= "))and(variables['lineDone'] == 0):
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
            variables['out'] = variables['varOUT1avavavavva'] + variables['whatVarWeUse'] + variables['varOUT2avavavavva']
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 1)== Chr(59))and(variables['lineDone'] == 0):
            variables['str123'] = StringTrimLeft(variables['A_LoopField23'], 1)
            variables['str123'] = "#" + variables['str123']
            variables['out'] = variables['str123']
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        elif (SubStr(Trim(StrLower(variables['A_LoopField23'])), 0)== Chr(41))and(variables['lineDone'] == 0):
            variables['str123'] = variables['A_LoopField23']
            variables['FuncNameWhatIsIt'] = StrSplit(variables['str123'] , "(" , 1)
            items = LoopParseFunc(variables['FuncNameWhatIsIt'])
            for A_Index27, A_LoopField27 in enumerate(items, start=1):
                variables['A_Index27'] = A_Index27
                variables['A_LoopField27'] = A_LoopField27
                variables['str123'] = StringTrimLeft(variables['str123'], 1)
            variables['outVarTransiled'] = transpileVariables(variables['str123'] , variables['functionNames'])
            variables['out'] = variables['FuncNameWhatIsIt'] + variables['outVarTransiled']
            variables['lineDone'] = 1
            variables['pyCode'] += variables['out'] + "\n"
        else:
            # this is THE else
            if (variables['lineDone']  != 1):
                if (variables['skipLeftCuleyForFuncPLS']  != 1):
                    if (SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 1)== Chr(125)):
                        variables['pyCode'] += Chr(125) + "\n"
                    else:
                        if (variables['pycodeAcurlyBraceAddSomeVrasFixLP'] == 1)and(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 1)== Chr(123)):
                            variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 0
                            variables['pyCode'] += variables['A_LoopField23'] + "\n" + variables['theFixTextLoopLP'] + "\n"
                        else:
                            if (variables['pycodeAcurlyBraceAddSomeVrasFixNL'] == 1)and(SubStr(Trim(StrLower(variables['A_LoopField23'])), 1 , 1)== Chr(123)):
                                variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 0
                                variables['pyCode'] += variables['A_LoopField23'] + "\n" + variables['theFixTextLoopNL'] + "\n"
                            else:
                                variables['pyCode'] += variables['A_LoopField23'] + "\n"
                else:
                    variables['skipLeftCuleyForFuncPLS'] = 0
    if (variables['haveWeEverUsedAloop'] == 1):
        variables['pycodeLoopfixa'] = StringTrimRight(variables['pycodeLoopfixa'], 1)
        #OutputDebug, |%pycodeLoopfixa%|
        variables['AIndexLoopCurlyFix'] = 1
        items = LoopParseFunc(variables['pycodeLoopfixa'], "\n", "\r")
        for A_Index28, A_LoopField28 in enumerate(items, start=1):
            variables['A_Index28'] = A_Index28
            variables['A_LoopField28'] = A_LoopField28
            variables['str123'] = variables['A_LoopField28']
            variables['fixLoopLokingFor'] = variables['A_LoopField28']
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
                for A_Index29, A_LoopField29 in enumerate(items, start=1):
                    variables['A_Index29'] = A_Index29
                    variables['A_LoopField29'] = A_LoopField29
                    #MsgBox, dsfgsdefgesrdg1
                    #MsgBox, |%A_LoopField29%|`n|%fixLoopLokingFor%|
                    if (InStr(variables['A_LoopField29'] , variables['fixLoopLokingFor']))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['fixLoopLokingForNum'] = 1
                        #MsgBox, do we came here 1
                    if (InStr(variables['A_LoopField29'] , "for "))and(variables['weAreDoneHereCurly']  != 1)and(variables['insdeAnestedLoopBAD']  != 1)and(variables['fixLoopLokingForNum'] == 1):
                        variables['s'] = StrSplit(variables['A_LoopField29'] , "A" + Chr(95) + "Index" , 2)
                        variables['out1z'] = variables['s']
                        variables['s'] = StrSplit(variables['out1z'] , " " , 1)
                        variables['out1z'] = Trim(variables['s'])
                        #MsgBox, % out1z
                        #MsgBox, do we came here 2
                        variables['fixLoopLokingForNum'] = 0
                        variables['foundTheTopLoop'] += 1
                        variables['inTarget'] = 1
                        #MsgBox, % A_LoopField29
                        variables['dontSaveStr'] = 1
                        variables['ALoopField'] = variables['A_LoopField29']
                        variables['DeleayOneCuzOfLoopParse'] = 1
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                    if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField29'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['insideBracket'] = 1
                    if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField29'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['netsedCurly'] += 1
                    if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField29'] , Chr(125)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['netsedCurly'] -= 1
                        variables['readyToEnd'] = 1
                    if (InStr(variables['A_LoopField29'] , "for "))and(variables['insdeAnestedLoopBAD']  != 1)and(variables['foundTheTopLoop'] >= 2):
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
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField29'] + "\n"
                    if (variables['inTarget'] == 1)and(variables['dontSaveStr']  != 1)and(variables['fixLoopLokingForNum']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['ALoopField'] = variables['A_LoopField29']
                        # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                        variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A" + Chr(95) + "Index(?:\\d+)?" , "A" + Chr(95) + "Index" + variables['out1z'])
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                    if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField29'] , Chr(125)))and(variables['readyToEnd'] == 1)and(variables['netsedCurly'] == 0)and(variables['weAreDoneHereCurly'] == 0)and(variables['dontSaveStr']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        #MsgBox, % A_LoopField29
                        variables['weAreDoneHereCurly'] = 1
                        variables['inTarget'] = 0
                        variables['endBracketDOntPutThere'] = 1
                    variables['dontSaveStr'] = 0
                    if (variables['inTarget']  != 1)and(variables['endBracketDOntPutThere']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField29'] + "\n"
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
                for A_Index30, A_LoopField30 in enumerate(items, start=1):
                    variables['A_Index30'] = A_Index30
                    variables['A_LoopField30'] = A_LoopField30
                    if (InStr(variables['A_LoopField30'] , variables['fixLoopLokingFor']))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['fixLoopLokingForNum'] = 1
                        #MsgBox, do we came here 3
                    if (InStr(variables['A_LoopField30'] , "for "))and(variables['weAreDoneHereCurly']  != 1)and(variables['insdeAnestedLoopBAD']  != 1)and(variables['fixLoopLokingForNum'] == 1):
                        variables['s'] = StrSplit(variables['A_LoopField30'] , "A" + Chr(95) + "LoopField" , 2)
                        variables['out1z'] = variables['s']
                        variables['s'] = StrSplit(variables['out1z'] , " " , 1)
                        variables['out1z'] = Trim(variables['s'])
                        #MsgBox, % out1z
                        variables['fixLoopLokingForNum'] = 0
                        #MsgBox, do we came here 4
                        variables['foundTheTopLoop'] += 1
                        variables['inTarget'] = 1
                        #MsgBox, % A_LoopField30
                        variables['dontSaveStr'] = 1
                        variables['ALoopField'] = variables['A_LoopField30']
                        variables['DeleayOneCuzOfLoopParse'] = 1
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                    if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField30'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['insideBracket'] = 1
                    if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField30'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['netsedCurly'] += 1
                    if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField30'] , Chr(125)))and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['netsedCurly'] -= 1
                        variables['readyToEnd'] = 1
                    if (InStr(variables['A_LoopField30'] , "for "))and(variables['insdeAnestedLoopBAD']  != 1)and(variables['foundTheTopLoop'] >= 2):
                        variables['insdeAnestedLoopBAD'] = 1
                        variables['insideBracket1'] = 0
                        variables['netsedCurly1'] = 0
                    if (variables['inTarget'] == 1):
                        variables['foundTheTopLoop'] += 1
                    if (variables['insdeAnestedLoopBAD'] == 1):
                        if (InStr(variables['A_LoopField30'] , Chr(123))):
                            variables['insideBracket1'] = 1
                        if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField30'] , Chr(123))):
                            variables['netsedCurly1'] += 1
                        if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField30'] , Chr(125))):
                            variables['netsedCurly1'] -= 1
                            variables['readyToEnd1'] = 1
                        if (InStr(variables['A_LoopField30'] , Chr(125)))and(variables['readyToEnd1'] == 1)and(variables['netsedCurly1'] == 0)and(variables['insideBracket'] == 1):
                            #MsgBox, % A_LoopField30
                            variables['eldLoopNestedBADlol'] = 1
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField30'] + "\n"
                    if (variables['inTarget'] == 1)and(variables['dontSaveStr']  != 1)and(variables['fixLoopLokingForNum']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        variables['ALoopField'] = variables['A_LoopField30']
                        # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                        variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A" + Chr(95) + "Index(?:\\d+)?" , "A" + Chr(95) + "Index" + variables['out1z'])
                        # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                        variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A" + Chr(95) + "LoopField(?:\\d+)?" , "A" + Chr(95) + "LoopField" + variables['out1z'])
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                    if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField30'] , Chr(125)))and(variables['readyToEnd'] == 1)and(variables['netsedCurly'] == 0)and(variables['weAreDoneHereCurly'] == 0)and(variables['dontSaveStr']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        #MsgBox, % A_LoopField30
                        variables['weAreDoneHereCurly'] = 1
                        variables['inTarget'] = 0
                        variables['endBracketDOntPutThere'] = 1
                    variables['dontSaveStr'] = 0
                    if (variables['inTarget']  != 1)and(variables['endBracketDOntPutThere']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                        variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField30'] + "\n"
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
        for A_Index31, A_LoopField31 in enumerate(items, start=1):
            variables['A_Index31'] = A_Index31
            variables['A_LoopField31'] = A_LoopField31
            variables['ignore'] = 0
            if (InStr(variables['A_LoopField31'] , "for ")):
                if (variables['hold'] == 1)and(variables['holdText'] == variables['A_LoopField31']):
                    variables['ignore'] = 1
                else:
                    variables['holdText'] = variables['A_LoopField31']
                    variables['hold'] = 1
            if ( not (variables['ignore'])):
                variables['out4758686d86dgt8r754444444'] += variables['A_LoopField31'] + "\n"
        variables['out4758686d86dgt8r754444444'] = StringTrimRight(variables['out4758686d86dgt8r754444444'], 1)
        variables['pyCode'] = variables['out4758686d86dgt8r754444444']
    variables['pyCode'] = indent_nested_curly_braces(variables['pyCode'])
    variables['pyCodeOut1234565432'] = ""
    items = LoopParseFunc(variables['pyCode'], "\n", "\r")
    for A_Index32, A_LoopField32 in enumerate(items, start=1):
        variables['A_Index32'] = A_Index32
        variables['A_LoopField32'] = A_LoopField32
        if (Trim(variables['A_LoopField32']) != Chr(123))and(Trim(variables['A_LoopField32']) != Chr(125)):
            variables['out'] = variables['A_LoopField32']
            variables['out'] = StringTrimLeft(variables['out'], 1)
            if (InStr(variables['out'] , "variables['A" + Chr(95) + "Index"))or(InStr(variables['out'] , "variables['A" + Chr(95) + "LoopField")):
                variables['out'] = StrReplace(variables['out'] , Chr(39) + Chr(34) + Chr(93) + Chr(125) + Chr(39) + Chr(93), Chr(34) + Chr(93) + Chr(125) + Chr(39) + Chr(93))
                variables['out'] = StrReplace(variables['out'] , Chr(39) + Chr(39) + Chr(93), Chr(39) + Chr(93))
            if ( not (InStr(variables['out'] , "|itsaersdtgtgfergsdgfsegdfsedAA|"))):
                if (SubStr(Trim(StrLower(variables['A_LoopField32'])), 1 , 1) != Chr(59)):
                    if (SubStr(Trim(StrLower(variables['A_LoopField32'])), 1 , 1)== Chr(124)):
                        variables['nothing'] = ""
                        variables['out'] = StrReplace(variables['out'] , "|" , variables['nothing'])
                        variables['pyCodeOut1234565432'] += Chr(32) + Chr(32) + Chr(32) + Chr(32) + variables['out'] + "\n"
                    else:
                        variables['pyCodeOut1234565432'] += variables['out'] + "\n"
    variables['pyCode'] = StringTrimRight(variables['pyCodeOut1234565432'], 1)
    variables['pyCodeOutOneLastFix'] = ""
    items = LoopParseFunc(variables['pyCode'], "\n", "\r")
    for A_Index33, A_LoopField33 in enumerate(items, start=1):
        variables['A_Index33'] = A_Index33
        variables['A_LoopField33'] = A_LoopField33
        variables['sstr1'] = variables['A_LoopField33']
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_TickCount']" , "BuildInVars(" + Chr(34) + "A_TickCount" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_Now']" , "BuildInVars(" + Chr(34) + "A_Now" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_YYYY']" , "BuildInVars(" + Chr(34) + "A_YYYY" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_MMMM']" , "BuildInVars(" + Chr(34) + "A_MMMM" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_MMM']" , "BuildInVars(" + Chr(34) + "A_MMM" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_MM']" , "BuildInVars(" + Chr(34) + "A_MM" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_DDDD']" , "BuildInVars(" + Chr(34) + "A_DDDD" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_DDD']" , "BuildInVars(" + Chr(34) + "A_DDD" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_DD']" , "BuildInVars(" + Chr(34) + "A_DD" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_Hour']" , "BuildInVars(" + Chr(34) + "A_Hour" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_Min']" , "BuildInVars(" + Chr(34) + "A_Min" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_Sec']" , "BuildInVars(" + Chr(34) + "A_Sec" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_Space']" , "BuildInVars(" + Chr(34) + "A_Space" + Chr(34) + ")")
        variables['sstr1'] = StrReplace(variables['sstr1'] , "variables['A_Tab']" , "BuildInVars(" + Chr(34) + "A_Tab" + Chr(34) + ")")
        variables['pyCodeOutOneLastFix'] += variables['sstr1'] + "\n"
    variables['pyCode'] = StringTrimRight(variables['pyCodeOutOneLastFix'], 1)
    variables['pyCodeFinal'] = variables['pyCode']
    variables['allFuncsHere'] = ""
    items = LoopParseFunc(variables['funcs_func'], "|")
    for A_Index34, A_LoopField34 in enumerate(items, start=1):
        variables['A_Index34'] = A_Index34
        variables['A_LoopField34'] = A_LoopField34
        if (InStr(variables['pyCodeFinal'] , variables['A_LoopField34'] + Chr(40))):
            variables['hererererehre'] = variables['A_LoopField34'] + "_func"
            variables['allFuncsHere'] += variables[f'func_{variables["hererererehre"]}']
    variables['pyCodeFinal'] = variables['allFuncsHere'] + "\n" + variables['pyCodeFinal'] + "\n"
    if (variables['usedLib'] == ""):
        variables['pyCode'] = variables['weEverUseVars'] + "\n" + variables['pyCodeFinal']
        if (variables['weEverUseVars'] == ""):
            variables['pyCode'] = variables['pyCodeFinal']
        else:
            variables['pyCode'] = variables['weEverUseVars'] + "\n" + variables['pyCodeFinal']
    else:
        variables['pyCode'] = variables['usedLib'] + "\n" + variables['weEverUseVars'] + "\n" + variables['pyCodeFinal']
    variables['pyCode'] = StrReplace(variables['pyCode'] , "\n\n" , "\n")
    if (variables['putEndPointFlask1Up']  != ""):
        variables['pyCode'] = variables['putEndPointFlask1Up'] + "\n" + variables['pyCode'] + "\n" + variables['putEndPointFlask2Down'] + "\n"
    for A_Index35 in range(1, variables['theIdNumOfThe34'] + 1):
        variables['A_Index35'] = A_Index35
        variables['pyCode'] = StrReplace(variables['pyCode'] , "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-" + Chr(65) + Chr(65) + str(variables['A_Index35']) + Chr(65) + Chr(65), variables[f'theIdNumOfThe34theVar{variables["A_Index35"]}'])
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
