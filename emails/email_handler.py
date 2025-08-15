from . import *
from imap_tools import MailBox, AND

class EmailHandler:
    def __init__(self):
        self.imap = MailBox("imap.gmail.com")
        self.loggedIn = self.login()

    def login(self):
        try:
            self.imap.login(emailAddress, emailPassword)
            return False
        except:
            return True
        
    def selectInbox(self):
        self.imap.folder.set("INBOX")
        messages = self.imap.fetch(AND(seen=False), mark_seen=False)
        return list(messages)
    
    def verifyNewEmails(self):
        messages = self.selectInbox()
        if len(messages) == 1:
            return f"Você tem 1 e-mail novo."
        
        if len(messages) > 1:
            return f"Você tem {len(messages)} e-mails novos."
        
        return "Nenhum Email novo."
    
    def getEmails(self):
        messages = self.selectInbox()
        texto = ''
        for msg in messages:
            texto += f"De: {msg.from_}\nAssunto: {msg.subject}\nData: {msg.date}\nCorpo: {msg.text.replace('\n', ' ')}\n\n"
            if len(msg.attachments) > 0:
                for attachment in msg.attachments:
                    texto += f"Anexos: {attachment.filename}\n"

        return texto
        