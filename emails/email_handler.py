from . import *
from imap_tools import MailBox, AND

class EmailHandler:
    def __init__(self):
        self.imap = MailBox("imap.gmail.com")

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
            return f"Você tem {len(messages)} email novo."
        
        if len(messages) > 1:
            return f"Você tem {len(messages)} emails novos."
        
        return "Nenhum Email novo."


if __name__ == "__main__":
    email_handler = EmailHandler()
    if email_handler.login():
        print("Erro ao fazer login. Verifique suas credenciais.")

    print(email_handler.verifyNewEmails())
