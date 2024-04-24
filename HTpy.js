const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

rl.on("line", async (input) => {

      // JavaScript equivalent code with variables

      let lastInputTime = Date.now(); // Initialize with current timestamp
      let startTimestamp = Date.now(); // Initialize with current timestamp

      // Event listener to track user activity
      function resetIdleTimer() {
        lastInputTime = Date.now(); // Update last input time
      }

      // Function to calculate time since last input event
      function A_TimeIdle() {
        return Date.now() - lastInputTime; // Calculate time difference
      }

      // Function to calculate tick count in milliseconds
      function A_TickCount() {
        return Date.now() - startTimestamp;
      }

      function BuildInVars(varName) {
        switch (varName) {
          case "A_ScreenWidth":
            // Return screen width
            return window.innerWidth;
          case "A_LastKey":
            // Return screen width
            return getLastKeyPressed();
          case "A_ScreenHeight":
            // Return screen height
            return window.innerHeight;
          case "A_TimeIdle":
            // Return time idle
            return A_TimeIdle();
          case "A_TickCount":
            // Return tick count in milliseconds
            return A_TickCount();
          case "A_Now":
            // Return current local timestamp
            return new Date().toLocaleString();
          case "A_YYYY":
            // Return current year
            return new Date().getFullYear();
          case "A_MM":
            // Return current month
            return (new Date().getMonth() + 1).toString().padStart(2, "0");
          case "A_DD":
            // Return current day
            return new Date().getDate().toString().padStart(2, "0");
          case "A_MMMM":
            // Return full month name
            return new Date().toLocaleDateString(undefined, { month: "long" });
          case "A_MMM":
            // Return short month name
            return new Date().toLocaleDateString(undefined, { month: "short" });
          case "A_DDDD":
            // Return full day name
            return new Date().toLocaleDateString(undefined, { weekday: "long" });
          case "A_DDD":
            // Return short day name
            return new Date().toLocaleDateString(undefined, { weekday: "short" });
          case "A_Hour":
            // Return current hour
            return new Date().getHours().toString().padStart(2, "0");
          case "A_Min":
            // Return current minute
            return new Date().getMinutes().toString().padStart(2, "0");
          case "A_Sec":
            // Return current second
            return new Date().getSeconds().toString().padStart(2, "0");
          case "A_Space":
            // Return space character
            return " ";
          case "A_Tab":
            // Return tab character
            return "\t";

          default:
            // Handle unknown variable names
            return null;
        }
      }

      // Base-10 logarithm
      function Log(num) {
        if (num === null || isNaN(num)) return null;
        return Math.log10(num);
      }

      // InStr
      function InStr(Haystack, Needle, CaseSensitive = true, StartingPos = 1, Occurrence = 1) {
        if (Haystack === null || Needle === null) return false;

        // Adjust starting position if less than 1
        StartingPos = Math.max(StartingPos, 1);

        // Case-sensitive search by default
        if (!CaseSensitive) {
          Haystack = Haystack.toLowerCase();
          Needle = Needle.toLowerCase();
        }

        let pos = -1;
        let count = 0;
        for (let i = StartingPos - 1; i < Haystack.length; i++) {
          if (Haystack.substring(i, i + Needle.length) === Needle) {
            count++;
            if (count === Occurrence) {
              pos = i + 1;
              break;
            }
          }
        }

        return pos > 0; // Return true if the substring is found, false otherwise
      }

      function SubStr(str, startPos, length) {
        // If str is null or undefined, return an empty string
        if (str === null || str === undefined) {
          return "";
        }

        // If length is not provided or is blank, default to "all characters"
        if (length === undefined || length === "") {
          length = str.length - startPos + 1;
        }

        // If startPos is less than 1, adjust it to start from the end of the string
        if (startPos < 1) {
          startPos = str.length + startPos;
        }

        // Extract the substring based on startPos and length
        return str.substr(startPos - 1, length);
      }

      function Trim(inputString) {
        // Check if inputString is null or undefined
        if (inputString == null) {
          return ""; // Return an empty string if inputString is null or undefined
        }
        return inputString.replace(/^\s+|\s+$/g, ""); // Removes leading and trailing whitespace
      }

      // Function to trim specified number of characters from the left side of a string
      function StringTrimLeft(input, numChars) {
        if (input && input.length >= numChars) {
          return input.substring(numChars);
        } else {
          console.error("Invalid input provided.");
          return input; // Return original input if trimming is not possible
        }
      }

      // Function to trim specified number of characters from the right side of a string
      function StringTrimRight(input, numChars) {
        if (input && input.length >= numChars) {
          return input.substring(0, input.length - numChars);
        } else {
          console.error("Invalid input provided.");
          return input; // Return original input if trimming is not possible
        }
      }

      function GuiControl(action, id, param1, param2, param3, param4) {
        const element = document.getElementById(id);

        if (element) {
          // Handle DOM elements
          if (action === "move") {
            // Set position and size
            element.style.left = param1 + "px";
            element.style.top = param2 + "px";
            element.style.width = param3 + "px";
            element.style.height = param4 + "px";
          } else if (action === "focus" && (element instanceof HTMLInputElement || element instanceof HTMLElement)) {
            // Focus on the element
            element.focus();
          } else if (action === "text") {
            // Set new text content
            element.textContent = param1;
          } else if (action === "hide") {
            // Hide the element
            element.style.display = "none";
          } else if (action === "show") {
            // Show the element
            element.style.display = "";
          } else if (action === "enable") {
            // Enable the element
            element.disabled = false;
          } else if (action === "disable") {
            // Disable the element
            element.disabled = true;
          } else if (action === "font") {
            // Set font size
            element.style.fontSize = param1 + "px";
          } else if (action === "color") {
            // Set color
            element.style.color = param1;
          } else if (action === "picture") {
            // Change the image source
            if (element instanceof HTMLImageElement) {
              element.src = param1;
            } else {
              console.error("Element is not an <img> tag, cannot change picture.");
            }
          }
        } else {
          // Handle canvas or non-existing element
          if (action === "move") {
            // Update position and size of the rectangle
            updateRectangle(id, param1, param2, param3, param4);
            redrawCanvas(); // Redraw the canvas with updated rectangles
          } else if (action === "color") {
            // Update color of the rectangle
            updateRectangleColor(id, param1);
            redrawCanvas(); // Redraw the canvas with updated rectangles
          }
        }
      }

      function StrLower(string) {
        return string.toLowerCase();
      }

      // Single async function to structure the entire script
      async function runScript() {
        // Declare and assign a variable
let variables = {
  A_Index: null,
  A_LoopField: null,
  allowPos: null,
  characters: null,
  editBoxX2: null,
  editBoxX: null,
  editBoxY: null,
  HTpyCode: null,
  HTpyCodeD1: null,
  out: null,
  pos: null,
  posNum: null,
  pyCode: null,
  sendButtonX: null,
  sendButtonY: null,
  str: null,
  StrSplit: null,
  var2: null,
  webMode: null,
};

let funcs = {
  StrSplit: StrSplit,
}

// HTpy

variables.webMode =  0;

if ( variables.webMode == 1 )

{

Gui1.style.position = "absolute";
Gui1.style.width = window.innerWidth + "px"; // Set the width
Gui1.style.height = "" + BuildInVars("A_ScreenHeight") + "px"; // Set the height
Gui1.style.background = "linear-gradient(90deg, " + "#121212" + " 0%, " + "#121212" + " 100%)";
Gui1.style.backgroundColor = "linear-gradient(90deg, " + "#121212" + " 0%, " + "#121212" + " 100%)";
Gui1.style.color = "white";
Gui1.style.fontSize = "15px";
Gui1.style.padding = "0px";
Gui1.style.borderRadius = "0px";
Gui1.style.fontFamily = ", sans-serif"; // Specify your desired font here
Gui1.style.zIndex = "100";

document.body.appendChild(Gui1) // Append the GUI window to the body
Gui1.style.display = "block";

document.documentElement.setAttribute("style", "padding: 0; margin: 0;")
document.head.setAttribute("style", "padding: 0; margin: 0;")
document.body.setAttribute("style", "overflow-x: hidden;padding: 0; margin: 0;")

variables.editBoxX =   ( BuildInVars("A_ScreenWidth") - 500 )  / 2;

variables.editBoxY =   ( BuildInVars("A_ScreenHeight") - 500 )  / 2;

variables.editBoxX =  variables.editBoxX - 250;

variables.editBoxX2 =  variables.editBoxX + 550;

Gui1editBox = document.createElement("textarea")
Gui1editBox.id = "Gui1" + "editBox"; // Set ID for referencing
Gui1editBox.placeholder = "put or type your HTpy code here...";
Gui1editBox.style.fontSize = "19px"; // Set font size
Gui1editBox.style.resize = "none"; // Disable resizing
Gui1editBox.style.position = "absolute"; // Set position to absolute
Gui1editBox.style.left = "" + variables.editBoxX + "px"; // Set initial x position
Gui1editBox.style.top = "" + variables.editBoxY + "px"; // Set initial y position
Gui1editBox.style.width = "500px"; // Set width
Gui1editBox.style.height = "500px"; // Set height
Gui1editBox.style.border = ""
Gui1editBox.style.color = "#ffffff"
Gui1editBox.style.background = ""
Gui1editBox.style.backgroundColor = "#303030"
Gui1editBox.style.borderRadius = ""
Gui1editBox.style.fontFamily = ", sans-serif"; // Specify your desired font here
Gui1editBox.addEventListener("input", function () {
A_GuiControl = Gui1editBox.value
CodeTextEditBox(A_GuiControl)
})
Gui1.appendChild(Gui1editBox)

Gui1codeBox = document.createElement("textarea")
Gui1codeBox.id = "Gui1" + "codeBox"; // Set ID for referencing
Gui1codeBox.placeholder = "";
Gui1codeBox.style.fontSize = "19px"; // Set font size
Gui1codeBox.style.resize = "none"; // Disable resizing
Gui1codeBox.style.position = "absolute"; // Set position to absolute
Gui1codeBox.style.left = "" + variables.editBoxX2 + "px"; // Set initial x position
Gui1codeBox.style.top = "" + variables.editBoxY + "px"; // Set initial y position
Gui1codeBox.style.width = "500px"; // Set width
Gui1codeBox.style.height = "500px"; // Set height
Gui1codeBox.style.border = ""
Gui1codeBox.style.color = "#ffffff"
Gui1codeBox.style.background = ""
Gui1codeBox.style.backgroundColor = "#303030"
Gui1codeBox.style.borderRadius = ""
Gui1codeBox.style.fontFamily = ", sans-serif"; // Specify your desired font here
Gui1.appendChild(Gui1codeBox)

variables.sendButtonX =   ( BuildInVars("A_ScreenWidth") - 140 )  / 2;

variables.sendButtonY =   (  ( BuildInVars("A_ScreenHeight") - 40 )  / 2 )  + 280;

Gui1Button1 = document.createElement("button")
Gui1Button1.id = "Gui1" + "Button" + "1"; // Set ID for referencing
Gui1Button1.textContent = "Transpile";
Gui1Button1.style.fontSize = "19px"; // Set font size
Gui1Button1.style.position = "absolute"; // Set position to absolute
Gui1Button1.style.left = "" + variables.sendButtonX + "px"; // Set initial x position
Gui1Button1.style.top = "" + variables.sendButtonY + "px"; // Set initial y position
Gui1Button1.style.width = "140px"; // Set width
Gui1Button1.style.height = "40px"; // Set height
Gui1Button1.style.cursor = "pointer"; // Change cursor on hover
Gui1Button1.style.border = "";
Gui1Button1.style.background = "";
Gui1Button1.style.backgroundColor = "";
Gui1Button1.style.borderRadius = "";
Gui1Button1.style.color = "";
Gui1Button1.style.fontFamily = ", sans-serif"; // Specify your desired font here
Gui1Button1.onclick = function (event) {
A_GuiControl = event.target.textContent
Button(A_GuiControl)
};
Gui1.appendChild(Gui1Button1)

GuiControl("focus", "Gui1editBox")

return

async function CodeTextEditBox(A_GuiControl)
{

variables.HTpyCode =  A_GuiControl;

}

}

else

{

await Button()

}

return

async function Button(A_GuiControl)
{

if ( variables.webMode == 0 )

{

eval("variables.HTpyCode = input;")

}

variables.pyCode =  ""

variables.HTpyCodeD1 =  ""

variables.characters1 = variables.HTpyCode.split(/[\n\r]/)
variables.charLength1 = variables.characters1.length

for (/* Loop parse */ variables.A_Index1 = 1; variables.A_Index1 <= variables.charLength1; variables.A_Index1++) {
variables.A_LoopField1 = variables.characters1[variables.A_Index1 - 1]; // Using array notation to access characters

variables.HTpyCodeD1 +=  Trim( variables.A_LoopField1 )  + "\n";

}

variables.HTpyCode = StringTrimRight(variables.HTpyCodeD1, 1)

variables.characters2 = variables.HTpyCode.split(/[\n\r]/)
variables.charLength2 = variables.characters2.length

for (/* Loop parse */ variables.A_Index2 = 1; variables.A_Index2 <= variables.charLength2; variables.A_Index2++) {
variables.A_LoopField2 = variables.characters2[variables.A_Index2 - 1]; // Using array notation to access characters

if ( SubStr( Trim( await StrLower ( variables.A_LoopField2 ) ) , 1, 8 ) == await StrLower ( "msgbox, " ) )

{

variables.var1 = StringTrimLeft(variables.A_LoopField2, 8)

if ( await InStr ( variables.var1, "%" ) )

{

variables.var2 =  await StrSplit ( variables.var1, "%", 2 )

variables.out =  "print(" + variables.var2 + ")";

}

else

{

variables.out =  "print(" + String.fromCharCode( 34 )  + variables.var1 + String.fromCharCode( 34 )  + ")";

}

variables.pyCode +=  variables.out + "\n";

}

}

if ( variables.webMode == 1 )

{

GuiControl("text", "Gui1codeBox", variables.pyCode)

}

else

{

console.log("" + variables.pyCode + " ")

}

}

async function StrSplit(str, delimiter, num)
{

variables.str = str

variables.delimiter = delimiter

variables.num = num

if ( variables.num == 1 )

{

variables.out =  ""

variables.characters3 = variables.str.split("")
variables.charLength3 = variables.characters3.length

for (/* Loop parse */ variables.A_Index3 = 1; variables.A_Index3 <= variables.charLength3; variables.A_Index3++) {
variables.A_LoopField3 = variables.characters3[variables.A_Index3 - 1]; // Using array notation to access characters

variables.out +=  variables.A_LoopField3;

if ( variables.A_LoopField3 == variables.delimiter )

{

variables.out = StringTrimRight(variables.out, 1)

break

}

}

return variables.out

}

else

{

variables.str =  variables.delimiter + variables.str;

variables.posNum =  0;

variables.allowPos =  0;

variables.out =  ""

variables.characters4 = variables.str.split("")
variables.charLength4 = variables.characters4.length

for (/* Loop parse */ variables.A_Index4 = 1; variables.A_Index4 <= variables.charLength4; variables.A_Index4++) {
variables.A_LoopField4 = variables.characters4[variables.A_Index4 - 1]; // Using array notation to access characters

if ( variables.allowPos == 1 )

{

variables.out +=  variables.A_LoopField4;

}

if ( variables.A_LoopField4 == variables.delimiter  &&  variables.allowPos == 1 )

{

if ( variables.pos == variables.num )

{

variables.out = StringTrimRight(variables.out, 1)

break

}

else

{

variables.allowPos =  0;

variables.out =  ""

}

}

if ( variables.A_LoopField4 == variables.delimiter  &&  variables.allowPos == 0 )

{

variables.allowPos =  1;

variables.posNum++

variables.pos =  variables.posNum;

}

}  // end of Loop

return variables.out

}

}  // end of func

 }

      // Call the async function to start the script
      runScript();
});
