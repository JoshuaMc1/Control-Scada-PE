import imaplib

# Correo electronico
SERVER_MAIL="imap.gmail.com"
USER_MAIL="pruebaprogramacionembebida"
PASSWORD_MAIL="mdvh ujwj qjzk prnw"
EMAIL="pruebaprogramacionembebida@gmail.com"

server = imaplib.IMAP4_SSL(SERVER_MAIL, 993)

server.login(USER_MAIL, PASSWORD_MAIL)

status, count = server.select('Inbox')
status, data = server.fetch(count[0], '(UID BODY[TEXT])')

print(str(data[0][1]))

server.close()