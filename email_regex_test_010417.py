import re

email = r"[\w.-]+@[\w-]+\.[\w-]+"
#\w matches any word character A-Z,a-z,0-9
#+ means it must occur at least once
#[] provides an or list. | also does an or list
#not used in example, but {min,max} specifies the number of matches

if re.match(email,"mgavin@python.com"):
    print('Valid email!')
else:
    print('Sorry, try again!')

email_list = ['greatstuff@value.com',
              'hey-itsanemail@email.net',
              'gr.ea\'t.stuff@things.org',
              '9910@asdf..org.net',
              'notanemail.net',
              'support@ensignservices.net']
email_list.append('hello@cool.com')

print(email_list)


valid = 0
for item in list(email_list):
    if re.match(email,item):
        #print('{} is a valid email!'.format(item))
        valid += 1
    else:
        print('{} is not a valid email!'.format(item))
print(str(valid), "valid emails found!")
print(round((float(valid)/float(len(email_list)))*100,2),"% success rate")

while True:
    new = str(input('Please enter your email: \n'))
    if re.match(email,new):
        print('That is a valid email!')
        email_list.append(new)
        break
    else:
        print('Try again, buddy!')

        



