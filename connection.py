import requests 
import xml.etree.ElementTree as ET 

class Network:
    def __init__(self, rssURL):
        self.__rssURL = rssURL


    def rssResponse(self):
        response = requests.get(self.__rssURL)
        response = response.content
        return response


    def xmlParser(self, content):
        #function to parse the xml content
        
        base = ET.fromstring(content) 

        updatesitems = [] 
   
        for item in base.findall('./channel/item'): 
            updates = {} 
    
            for branch in item: 
    
                if branch.tag == '{https://news.google.com/search/}content': 
                    updates['media'] = branch.attrib['url'] 
                else: 
                    updates[branch.tag] = branch.text

            updatesitems.append(updates) 

        return updatesitems 

    def headlines(self):
        content_rss = self.rssResponse()
        headline_items = self.xmlParser(content_rss)
        
        return headline_items


 