import imapclient, pprint, sys

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')
pprint.pprint(imapObj.list_folders())
