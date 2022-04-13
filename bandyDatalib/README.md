# CounterSpeech\_Research\_Pipeline

# Einführung in die Pipeline 

## 1. Verhaltensregeln:
- Code ist für uns alle da, sollte ein Datenset weitere Funktionen benötigen, sollte diese in die Pipeline integriert werden und als gecapseltes Modul bereitgestellt und dokumentiert werden.
- In allen erweiterbaren Abschnitten sind Templates bereitgestellt. Nutze diese, denn die Verbindungen sind bereits vorhaben und helfen dir beim integrieren.
- bestehende Projekte habe eine abhängikeit von bestehenden Modulen, behandle diese stehts mit vorsicht und verändere keine bestehnden Funktionen.
- Für die Analyse von Fehlern wird ein Logging Tool bereitgestellt, nutze diese auch
- Die Namensgebung sollte wie in der Übersicht Struktur.pdf verwendet werde. Sollte eine Änderung nötig sein, so muss diese in der Struktur.drawio übernommen werden un als PDF bereitgestellt werden. Nutze dafür https://app.diagrams.net.
- Die Dokumentation von Modulen und Models wird sofern nicht anders bestimmt mit Pdoc umgesetzt. In den Templateordner steht alles dafür bereit.

## 1.  Programmierung und Änderungen.
- Erstelle für neue Module/Modelle eine Kopie des Templates.
- Benutze festgelegte Datenformate ( siehe Datenformate ).
- Die Funktionen und Klassennamen sollen eindeutig und beschreibend sein.
- Kommentare werden entwerder mit **#Kommentar** oder """**Kommentar**""" gekenntzeichnet.
- Mit # Markierte Kommentare werden in durch Pdoc nicht als Beschreibung übernommen.


```python
    def openJsonToArray(file):
        """ open a json File and retrun a list of dictionaries """
        data = importFile(file)
        data = json.loads(data)
		#convert data in dictionary
        dictionary=data
        return dictionary
```

*Ergebnis mit Pdoc:*

####  openJsonToArray: open a json File and retrun a list of dictionaries
	 def openJsonToArray(file):
       





------------

## 3. Datenformate
- Der Input an Daten ist Frei wählbar und kann mittels bestehenden Funktionen in das Arbeitsformat gebracht werden. Als Arbeitsformat wurde List of Dictionary festgelegt.
`dataset= master.setDataset(master.project.original_data_path,'EXIST2021_training.csv')`
die var `dataset` ist nun im passenden Format um mit allen Funktionen der Pipeline genutzt zu werden.



**Einzelner Datensatz:**
```python
{'test_case': 'EXIST2021', 'id': '005696', 'source': 'twitter', 'language': 'es', 'text': '@sofiaxnuez @miiguelrguezz @Brunofdez_ mi polla en una cerda', 'task1': 'sexist', 'task2': 'sexual-violence'}
```

**Liste Datensatz:**
```python
[{'test_case': 'EXIST2021', 'id': '9873495', 'source': 'twitter', 'language': 'es', 'text': '@sofiaxnuez @miiguelrguezz @Brunofdez_ mi polla en una cerda', 'task1': 'sexist', 'task2': 'sexual'}],

[{'test_case': 'EXIST2021', 'id': '000001', 'source': 'twitter', 'language': 'en', 'text': 'She calls herself "anti-feminazi" how about shut the fucking up on your vile commentary on an elderly responsible citizen tu sach muuch ghani baawri-bewdi hai bey https://t.co/ZMxTDwsY5D', 'task1': 'sexist', 'task2': 'ideological-inequality'}],

[{'test_case': 'EXIST2021', 'id': '345345', 'source': 'twitter', 'language': 'es', 'text': '@sofiaxnuez @miiguelrguezz @Brunofdez_ mi polla en una cerda', 'task1': 'sexist', 'task2': 'sexual-violence'}]
```

Nach der Aufbereitung der Daten, werden diese in das TSV Format konvertiert und im CleanDataset-Ordner gespeichert.

------------

# Nutzung:

1. um ein neues Datenset einzuspielen, gehe in den Ordner 0001_P_CounterStrike/_0002_Datasets/ und erstelle eine Kopie von Dataset_000_Template
2. Benne die Kopie nach dem Shema _XXX_Dataset_Name um
3. Öffne die Datei "dataset_start.ipynb" und führe die erste Zelle aus.
4. Durch das ausführen wird die Struktur generiert. Im Ornder erscheinen nun mehrere Dateien und Ordner.
5. Speichere deinen Datensatz im Ordner "001_original_data"
6. Schreibe den namen deiner Datei in die Variable "name_of_the_file" (z.B. 'Hate_Counter_Dataset.csv' )
7. Dein Projekt ist startklar und du kannst deinen Datensatz anhand vorefertigte Funktionen erweitern und bearbeiten.
8. Speichere deine Daten als TSV mit den Headern Text, Class,ID mit den vorgegebenen Funktionen
