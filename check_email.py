import re

email_text = '''

my name is ugwoke levi
After the form is submitted, you should validate the email on the server side to ensure security and handle cases where JavaScript is disabled.

PHP Example
Here is an example of server-side validation using PHP:

soromtolevi1@gmail.com

After the form is submitted, you should validate the email on the server side to ensure security and handle cases where JavaScript is disabled.

PHP Example
Here is an example of server-side validation using PHP:

levisoromto1@gmail.com

After the form is submitted, you should validate the email on the server side to ensure security and handle cases where JavaScript is disabled.

PHP Example
Here is an example of server-side validation using PHP:
Valid: 

user.name@example.com

 user_name@example.co.uk

Invalid: user@@example.com

 user@example
  
  user@.com, user@com.
'''

def Email(email):
    if not re.match(r'[a-zA-Z0-9\._-]+@[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,6}',email):
        print('Invalid Email')

    else:
        print('Valid')


Email('user.name@example.com')