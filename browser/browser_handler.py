from configparser import ConfigParser


class BrowserHandler:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('endpoints.ini')

    def email(self, emailType):
        emailType = emailType.lower()
        if emailType == 'jogos':
            return self.config.get('url', 'gmailvalente')
        
        elif emailType == 'formal':
            return self.config.get('url', 'gmailmarques')
        
    def youtube(self):
        return self.config.get('url', 'youtube')
    
    def google(self):
        return self.config.get('url', 'google')
    
    def github(self):
        return self.config.get('url', 'github')
    
    def mangalivre(self):
        return self.config.get('url', 'mangalivre')
    
    def chatgpt(self):
        return self.config.get('url', 'chatgpt')
    
    def search(self, searchTerm, searchSite):
        searchTerm = searchTerm.replace(' ', '+')
        return self.verifySiteSearch(searchSite, searchTerm)
    
    def verifySiteSearch(self, searchSite, searchTerm):
        if 'youtube' in searchSite.lower():
            return 'https://www.youtube.com/results?search_query='
        
        elif 'github' in searchSite.lower():
            return f'https://github.com/search?q={searchTerm}&type=repositories'
        
        return 'https://www.google.com/search?q='
    
if __name__ == "__main__":
    browser_handler = BrowserHandler()
    print(browser_handler.google())
    print(browser_handler.mangalivre())
