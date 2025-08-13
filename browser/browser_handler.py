from configparser import ConfigParser


class BrowserHandler:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('browser/urls.ini')

    def email(self, emailName):
        emailName = emailName.lower()
        if emailName == 'jogos':
            return self.config.get('url', 'gmailvalente')
        
        elif emailName == 'formal':
            return self.config.get('url', 'gmailmarques')
        
    def youtube(self):
        return self.config.get('url', 'youtube')
    
    def google(self):
        return self.config.get('url', 'google')
    
    def github(self):
        return self.config.get('url', 'github')
    
    def mangalivre(self):
        return self.config.get('url', 'mangalivre')
    
    def search(self, searchTerm, searchSite):
        searchSite = self.verifySiteSearch(searchSite)
        searchTerm = searchTerm.replace(' ', '+')
        return f"{searchSite}{searchTerm}"
    
    def verifySiteSearch(self, searchSite):
        if 'youtube' in searchSite.lower():
            return 'https://www.youtube.com/results?search_query='
        
        return 'https://www.google.com/search?q='
    
if __name__ == "__main__":
    browser_handler = BrowserHandler()
    print(browser_handler.google())
    print(browser_handler.mangalivre())
