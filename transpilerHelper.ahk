;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Name:
; transpilerHelper.ahk
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#singleinstance force
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
;;;;;;;;;;;;;;;;;;;;;

!^+F5::
FileRead, indexFile, index.html
FileRead, upCode, upCode.txt
strToFind := "//here;here;here;here;here;here;here;here;here;here;here;here;here;here;here;here"
begin := 0

out := ""
Loop, Parse, indexFile, `n, `r
{

if (InStr(A_LoopField, strToFind))
{
begin := 1
}
if (begin = 1)
{
out .= A_LoopField . "`n"
}

}
StringTrimRight, out, out, 1


out := upCode . "`n" . out

FileDelete, index.html
FileAppend, %out%, index.html
MsgBox, 262208, , Done
return










