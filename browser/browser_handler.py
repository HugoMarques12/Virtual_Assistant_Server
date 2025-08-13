from configparser import ConfigParser


class BrowserHandler:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('urls.ini')

    def email(self, emailName):
        emailName = emailName.lower()
        if emailName == 'jogos':
            return self.config.get('URL', 'gmailmarques')
        
        elif emailName == 'formal':
            return self.config.get('URL', 'gmailvalentte')
        
    def youtube(self):
        return self.config.get('URL', 'youtube')
    
    def google(self):
        return self.config.get('URL', 'google')
    
    def github(self):
        return self.config.get('URL', 'github')
    
    def mangalivre(self):
        return self.config.get('URL', 'mangalivre')
    
    def search(self, searchTerm, searchSite):
        searchSite = self.verifySiteSearch(searchSite)
        searchTerm = searchTerm.replace(' ', '+')
        return f"{searchSite}{searchTerm}"
    
    def verifySiteSearch(self, searchSite):
        if 'youtube' in searchSite.lower():
            return 'https://www.youtube.com/results?search_query='
        
        return 'https://www.google.com/search?q='
    