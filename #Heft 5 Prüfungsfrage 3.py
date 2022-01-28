'''Erstellen Sie ein Python-Programm, das Dualzahlen in das Dezimalsystem umrechnen
kann.

Zwei Tipps zur Lösung:
Die letzte Ziffer einer beliebigen Zahl erhalten Sie, wenn Sie die Zahl durch 10 dividieren
und den Rest dieser Division ermitteln.
Die letzte Ziffer einer Zahl können Sie löschen, wenn Sie die Zahl durch 10 dividieren
und nur das ganzzahlige Ergebnis berücksichtigen.'''
#Initialisierung 
zwischentab=[]
dualzahl=2

#Funtion zum umrechnen von Dual in Dezimal
def rechner(A):
    index=0
    liste=[]
    while index <= len(A):
        ziffer=(2**index)*A
        ziffer.append(liste)
        index=index+1
    return liste

#Abfrage Dualzahl zum Umrechnen 
while not(dualzahl <=1 and dualzahl >=0):
    dualzahl=int(input("Bitte geben Sie den Dualzahl an, dass umgerechnet werden soll:\n"))
    zwischentab.append()

#Umdrehen der Reihenfolge des Dualzahls zum Umrehnen und Übergabe an die Funktion
dualzahl.reverse()
rechner(dualzahl)




