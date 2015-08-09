#!/usr/bin/python
import email, getpass, imaplib, os

user = raw_input("Enter your GMail username:")
pwd = getpass.getpass("Enter your password: ")

directory = './myemails/'
i = 1000

# connecting to the gmail imap server
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select("INBOX")

resp, items = m.search(None, "ALL") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
items = items[0].split()

for mail in items:
    resp, data = m.fetch(mail, '(BODY.PEEK[TEXT])')
    for response_part in data:
        if isinstance(response_part, tuple):
            filename = str(i)
            save_path = os.path.join(directory, filename)

            if not os.path.isfile(save_path):
            	fp = open(save_path, 'wb')
            	fp.write(response_part[1])
            	fp.close()
            	print str(i) + ' done'
            	i = i+1	

m.close()
m.logout()