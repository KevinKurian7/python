#! python3
#phoneAndEmail.py - finds all phone numbers and email addresses on the clipboard
import pyperclip,re
phoneRegex=re.compile(r''' 
(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?


)
''',re.VERBOSE)

#create the email regex 
emailRegex=re.compile(r'''([a-zA-Z0-9._%+-]+ #username
@                                            #@ symbol
[a-zA-Z0-9.-]+                               #domain name

(\.[a-zA-Z]{2,4})                            #dot with something following

)''',re.VERBOSE)



#find matches in the clipboard text
text=str(pyperclip.paste())

matches=[]

for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phoneNum+=' x'+groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])



#copy results to clipboard
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('COPIED TO CLIPBOARD: ')
    print('\n'.join(matches))
else:
    print('NO PHONE NUMBERS OR EMAIL ADDRESSES FOUND. ')               
