# Dieses Modul wurde erstellt, um Projekte im Bereich Research auf eine Basis zu vereinheitlichen.

Eine Dokumentation für die aktuellen Funktionen findet ihr auf http://datalib.bandy.at/bandyDataserGen.html


folgende Module sind für dieses Paket notwendig:

tweepy: https://docs.tweepy.org/en/stable/install.html

Google API Client: https://pypi.org/project/google-api-python-client/

youtube_dl : https://pypi.org/project/youtube_dl/



Whats Next:
- Logging wird genutzt um das verhalten einzelner Funktionen Sinngemäß auszugeben
- Standartwerte für Settings werden defeniert
- Template für die Erstellung weiterer Module
- Eine .Runtine Ordnerstruktur wird erstellt, um jeden Durchlauf mit minimalen Speicheranforderungen zu archivieren.
- weitere Module nach Anforderungen des Counterspeech Projekts


Release Notes:

v.0.01:
Release der ersten Version mit allen Grundfunktionen
- Datasets können geladen, aufbereitet und in ein standardisiertes Format gebracht werden um diese an zukünftige Module übergeben werden.
- Datasets werden um Daten von Youtube und Twitter erweitert. Anhand der ID können Daten gecrawlt werden
- Logging wurde implementiert, so kann bei einem späteren Zeitpunkt das verhalten sowie Fehler der einzelnen Sub-Module gelistet werden.
- Create Dataset wurde implementiert. Es erstellt einen Ordnerstrang und speichert alle Dokumente und Daten in eine standardisierte Struktur
- Settings werden in einem Json zum jeweiligen Dataset gespeichert. Dieses beinhaltet alle Einstellungen für das spätere starten der Pipeline
