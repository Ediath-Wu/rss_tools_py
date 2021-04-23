from xml.sax import handler
import requests
import xml.etree.ElementTree as ET

class xml_file():
    def __init__(self) -> None:
        self.url='http://bimiacg.com/rss/index.xml'
        self.hed={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        }
        self.get_xml(self.url)
        
        
    def get_xml(self,url):
        res=requests.get(url=url,headers=self.hed)
        with open('./temp.xml',encoding='utf-8',mode='a') as f:
            f.write(res.text)

# a=xml_file()
import xml.etree.cElementTree as ET
tree = ET.ElementTree(file='./temp.xml')
root = tree.getroot()
print(root.tag, root.attrib)