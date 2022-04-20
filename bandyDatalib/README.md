# pythonlib

from bandyDatalib.bandyDatasetGen import *

Functions
DictGenerator generiert die standadisierte Ordnerstruktur, falls noch keine exestiert.


----------- Create New Dataset --------------------------------------------------------------------------

Dictgenerator sorgt dafuer, generiert die standadisierte Ordnerstruktur, falls noch keine exestiert. daf

def getcurrentpath():
    return os.path.dirname(os.path.abspath(__file__))

newproject =DictGenerator(getcurrentpath()) 
newproject.createproject()

newproject-Class hat nun die gesamte Ordnerstruktur um mit weiteren Aufgaben zu beginnen

----------- Enter exist Dataset --------------------------------------------------------------------------

Sollte ein Dataset schon exisitieren, so kann dieses ausgewaehlt werden 

projekt_exist =BandyDictGenerator(getcurrentpath()) # initialize the class with the root directory of the Dataset Pipeline
projekt_exist = projekt_exist.setProject("002_Dataset") # open an existing project

projekt_exist hat nun die gesamte Ordnerstruktur um mit weiteren Aufgaben zu beginnen

------------Class Variables-------------------------------------------------------------------------

ori= class.original_data_path
itermediate= class.itermediate_data_path
cleanDataset= class.clean_dataset_path
project= class.project_path

Alle Vaiablen verweissen auf die jeweiligen Ordner 

------------Dataset Manager-------------------------------------------------------------------------

oridata=BandyDatasetManager(ori,'youTube_Counterspeech_Dataset.json')

#beim initialisieren werden Daten uebergeben. Die Klasse erkennt durch die Endung alle weiteren Convertierungsschritte und wandelt diese in ein #Array von Dictionarys um.

------------Dataset Manager-------------------------------------------------------------------------

oridata.getSample() # Return Dictionary Entry - einen zufaelligen Datensatz 

oridata.show() # Print Info -  Laenge vom Datensatz sowie die Kopfzeile der Liste

oridata.getRows(Spaltenname,Wert) # Return Array - erstellt ein Array mit selben Wert z.B Binary, ID 
#print(len(oridata.getRows("Counterspeech", 1)))
#print(len(oridata.getRows("Counterspeech", 0)))



#-----------------------------------------------------------------------------------------------------------------------
#ywitter crawler
"""


tweets=TweetCrawl(consumer_key,consumer_key_secret,access_token,access_token_secret)

counterspeechs=oridata.getRows("Counterspeech", 0)
ids= oridata.getvalue("TweetID",counterspeechs)

tweetslist=tweets.crawlList(ids)

print(len(tweetslist))
print(tweetslist)

"""
#-----------------------------------------------------------------------------------------------------------------------
#youtube crawler
"""
yb= YoutubeCrawl( 'key')
counterspeechs=oridata.getRows("CounterSpeech", False)
ids= oridata.getvalue("id",counterspeechs)
data= yb.crawlList(ids[0:1])
video=data[0][0]['snippet']['videoId']

download= yb.videodownloader(video,itermediate)
"""
#-----------------------------------------------------------------------------------------------------------------------
#youtube crawler
