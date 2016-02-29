from imbox import Imbox

imbox = Imbox('imap.gmail.com',
              username='',# Gmail Username 
              password='',# Password
              ssl=True)

# Gets all messages 
all_messages = imbox.messages()

# Unread messages 
unread_messages = imbox.messages(unread=True)

for uid,message in unread_messages:
    print message.sent_from
    print message.body.plain
