import requests
import json

class wikipedia:
    def __init__(self):
        self.image_file_types = [".jpg",".jpeg",".png",".svg",".JPG",".JPEG",]

    def search(self,keyword:int,limit:int):
        """
        input: a string with the keyword and the number of results
        output: a list with tuples containing title & page id or None
        summary: return the results for a wikipedia search
        """

        self.keyword = keyword
        self.limit = limit
        self.url = f"https://en.wikipedia.org/w/api.php?action=query&origin=*&format=json&generator=search&gsrnamespace=0&gsrlimit={self.limit}&gsrsearch='{self.keyword}'"
        self.json = requests.get(self.url).json()
        try:
            self.json['query']['pages']
        except Exception as e:
            print("error: no results")
            return None
        
        self.outlist = [(self.json['query']['pages'][key]['title'],key) for key in self.json['query']['pages']]

        return self.outlist

    def summary(self,page_id:int):
        """
        input: a int with the page id
        output: a string with the page summary or None
        """

        self.page_id = page_id
        self.url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&pageids={int(self.page_id)}"
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
        
    def html(self,page_id:int):
        """
        input: a wikipedia page id
        output: a html string for the page
        summary: returns the raw html for a page
        """
        self.page_id = page_id
        
        return self.response.text
    
    def get_url(self,page_id:int):
        """
        input: a page id
        output: a string with the url
        summary: get the url for a page by id
        """

        self.page_id = page_id
        self.url = f"https://en.wikipedia.org/w/index.php?curid={int(page_id)}"

        return self.url

if __name__ == "__main__":
    wiki = wikipedia()
    print(wiki.search("cats",5))
    print(wiki.summary(6678))   
    print(wiki.get_url(6678))
