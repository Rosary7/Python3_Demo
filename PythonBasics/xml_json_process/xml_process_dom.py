from xml.dom.minidom import parse
import xml.dom.minidom

# XML processing with - DOM API
# We parse XML document using minidom parser
domTreeLanguage = xml.dom.minidom.parse("languages_xml.xml")
collectionLanguage = domTreeLanguage.documentElement
if collectionLanguage.hasAttribute("description"):
   print ("Languages : %s" % collectionLanguage.getAttribute("description"))
   print()

# We parse all the languages in the collection
languages = collectionLanguage.getElementsByTagName("language")

#  Loop and print the detail of each language.
for language in languages:
   print ("***** Language *****")
   if language.hasAttribute("title"):
      print ("Title: %s" % language.getAttribute("title"))

   type = language.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   format = language.getElementsByTagName('vm')[0]
   print ("VM: %s" % format.childNodes[0].data)
   rating = language.getElementsByTagName('framework')[0]
   print ("Framework: %s" % rating.childNodes[0].data)
   print()
