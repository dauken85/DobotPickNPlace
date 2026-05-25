# Elevhandledning — Session 5: Kalibrering av arbetsobjekt

## Vad du kommer att göra i den här sessionen
1. Kalibrera arbetsobjektet för roboten
2. Rita segmenteringsmasker runt varje föremål
3. Träna en AI-modell att känna igen dina föremål
4. Utvärdera hur bra modellen fungerar

## Varför man använder ett arbetsobjektkoordinatsystem
Arbetsobjektet (koordinatsystemet) används så att roboten vet hur den ska översätta det kameran ser (ArUco-markörens pose) till sitt eget rörelsesystem. Genom att skapa arbetsobjektet på samma plats som koordinatsystemet för ArUco-markören kan relationen mellan kameraramens och TCP-ramens koordinatsystem kopplas samman.

## Dina uppgifter

### Uppgift 1: Identifiera ArUco-markörens koordinatsystem
1. Ta en bild och detektera ArUco-markörens hörn
2. Använd följande inställningar för ledinställningarna
	J1  90
	J2   0
	J3 -50
	J4 -40
	J5  90
	J6 -90
2. Flytta pappret så att ArUco-markörens koordinatsystem hamnar i det nedre vänstra hörnet. Se till att du ser hela markören.


### Uppgift 2: Skapa ett arbetsobjekt
1. Fäst den spetsiga nålen på robotens sugkopp, antingen i Dobot Studio eller med knapparna på roboten
2. I DOBOT STUDIO Pro, ställ in roboten i kontinuerligt läge
3. I DOBOT Studio, välj **Parameter settings** -> **User coordinate systems**
4. Välj **CameraFr** och tryck på uppdatera med inställningen för tre punkter
5. Jogga eller dra roboten manuellt till exakt hörnet/origo för ArUco-markörens koordinatsystem och uppdatera den första positionen
6. Jogga roboten rakt ut längs den positiva **x**-riktningen till ArUco-markörens koordinatsystems origo och uppdatera den andra positionen
7. Jogga roboten in i den positiva Y-axelns riktning för ArUco-markörens koordinatsystems origo och uppdatera den tredje positionen. Starta från den andra **x**-positionen (till skillnad från ABB)
8. Klicka på Beräkna och sedan Spara eller OK. Roboten beräknar de nya axlarna och tillämpar förskjutningen.
9. Ställ in roboten i TCP-läge


### Uppgift x: Packa ner roboten
1. Använd följande inställningar för ledinställningarna
	J1    0 
	J2  125
	J3 - 92
	J4 - 90
	J5  135
	J6 -  4
