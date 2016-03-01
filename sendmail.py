import smtplib


fromaddr = ''#sender's email
toaddr = ['','']#list of all receivers' emailid
msg = 'Hi there'#The message

#gmail credentials
username = ''
password = ''

server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()


server.login(username,password)
server.sendmail(fromaddr,toaddr,msg)

server.quit()
