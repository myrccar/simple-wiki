import requests
import json

class wikipedia:
    def __init__(self):
        pass

    def search(self,keyword):
        """
        input: a string with the keyword
        output: a list with tuples containing title & page id or None
        summary: return the results for a wikipedia search
        """
        self.keyword = keyword
        self.url = f"https://en.wikipedia.org/w/api.php?action=query&origin=*&format=json&generator=search&gsrnamespace=0&gsrlimit=5&gsrsearch='{self.keyword}'"
        self.json = requests.get(self.url).json()
        try:
            self.json['query']['pages']
        except Exception as e:
            print("error: no results")
            return None
        
        self.outlist = [(self.json['query']['pages'][key]['title'],key) for key in self.json['query']['pages']]

        return self.outlist

    def summary(self,page_id):
        """
        input: a int with the page id
        output: a string with the page summary or None
        """

        self.page_id = page_id
        self.url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&pageids={int(page_id)}"
        self.json = requests.get(self.url).json()
        self.json['query']['pages']
        try:
            self.json['query']['pages']
        except Exception as e:
            print("error: no results")
            return None
        
        return (self.json['query']['pages'][str(self.page_id)]['title'],self.json['query']['pages'][str(self.page_id)]['extract'])

    def images(self,page_id):
        """
        input: a page id
        output: a list with the urls
        summary: gets all the related images for the page
        """

        self.page_id = page_id
        self.url = f"https://en.wikipedia.org/w/api.php?action=query&pageids={int(self.page_id)}&generator=images&gimlimit=10&prop=imageinfo&iiprop=url|dimensions|mime&format=json"
        self.json = requests.get(self.url).json()
        try:
            self.json['query']['pages']
        except Exception as e:
            print("error: no results")
            return None
        
        return self.json['query']['pages'][str(self.page_id)]['original']['source']
        


if __name__ == "__main__":
    wiki = wikipedia()    
