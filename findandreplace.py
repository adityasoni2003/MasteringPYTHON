from typing import Text


def findAndReplace(text, oldText, newText):

    replacedText = ''

    i = 0

    while i < len(text):

        if text[i:i + len(oldText)] == oldText:

            replacedText += newText
            i += len(oldText)
            return replacedText
        else:

            replacedText += text[i]

            i += 1
x=input("Enter the total text :")
y=input("Enter text to be replaced :")
z=input("Enter text to be replaced with :")
print(findAndReplace(x,y,z))