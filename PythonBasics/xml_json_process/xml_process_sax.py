# XML processing with - SAX API
"""
Steps:
    Subclass xml.sax.ContentHandler to create our own handler
    Override xml.sax.ContentHandler methods - startDocument,endDocument,characters
    Create SAX Parser and Parse XML
"""

import xml.sax

# XML processing with - SAX API
class LanguageHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ""
        self.type = ""
        self.vm = ""
        self.framework = ""

    # Called when an element starts
    def startElement(self, tag, attribute):
        self.currentData = tag
        if tag == "language":
            print("***** Language *****")
            title = attribute["title"]
            print("Title:", title)

    # Called when a character is read
    def characters(self, content):
        if self.currentData == "type":
            self.type = content
        elif self.currentData == "vm":
            self.vm = content
        elif self.currentData == "framework":
            self.framework = content

    # Called when an element ends
    def endElement(self, tag):
        if self.currentData == "type":
            print("Type:", self.type)
        elif self.currentData == "vm":
            print("vm:", self.vm)
        elif self.currentData == "framework":
             print("framework:", self.framework)

if (__name__ == "__main__"):
    # We create a XMLReader with SAX
    languageParser = xml.sax.make_parser()
    # We turn off namepsace
    languageParser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # We override the default ContentHandler with our custom LanguageHandler class
    languageHandler = LanguageHandler()
    languageParser.setContentHandler(languageHandler)

    languageParser.parse("languages_xml.xml")