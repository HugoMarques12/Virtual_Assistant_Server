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
    
    def search(self, query, site):
        query = query.replace(' ', '+')
        return self._verifySiteSearch(site, query)
    
    def _verifySiteSearch(self, site, query):
        if 'youtube' in site.lower():
            return f'https://www.youtube.com/results?search_query={query}'
        
        elif 'github' in site.lower():
            return f'https://github.com/search?q={query}&type=repositories'
        
        return f'https://www.google.com/search?q={query}'
    
if __name__ == "__main__":
    browser_handler = BrowserHandler()
    print(browser_handler.google())
    print(browser_handler.mangalivre())
