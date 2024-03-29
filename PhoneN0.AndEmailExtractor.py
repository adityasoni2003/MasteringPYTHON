#PhoneAndEmailFinder
import paperclip , re
phonenumber = re.compile(r'''(
    (\s|+|\.)?
    (\d{2}|\(\d{2}\))?
    (\s|-|\.)?
    (\d{5})
    (\d{5})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)
email = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''',re.VERBOSE)
text = str(paperclip.paste())
matches = []
for groups in phonenumber.findall(text):
    phoneNo = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNo += ' x' + groups[8]
    matches.append(phoneNo)
for groups in email.findall(text):
    matches.append(groups[0])
if len(matches) > 0 :
    pyperclip.copy('\n'.join(matches))
    print("Copied to Clipboard :")
    print('\n'.join(matches))
else :
    print('No phone numbers or email addresses found.')

