# Elevhandledning — Session 7: Robotens plock och placering

## Vad du kommer att göra i den här sessionen
1. Koppla din synpipeline till robotarmen
2. Plocka föremål med kameravägledda koordinater

## Den fullständiga pipelinen (körs idag)

```
Kameran tar en bild
       ↓
Modellen segmenterar föremål
       ↓
Plockpunkt beräknas (pixel → mm)
       ↓
Roboten rör sig till plockpunkten
       ↓
Sugning PÅ → Lyft → Flytta till avlämningszon → Sugning AV
```

## Säkerhetspåminnelse
- Nödstoppet finns vid: _________________________________
- **Läraren måste godkänna ditt första automatiserade plock**
- Berätta för din partner innan du trycker på "Run"

## Dina uppgifter

### Uppgift 1: Robotkonfiguration
1. Det första avsnittet innehåller kalibreringsinformation.
2. Det bör vara korrekt så vi behöver bara köra det.

### Uppgift 2: Anslut roboten
1. Kontrollera i Dobot Studio att roboten är aktiverad och läget är inställt på TCP.
2. Kör avsnitt 2.
3. Resultatet ska visa **Robot mode 5** och **Robot ready** i slutet.

### Uppgift 3: Anslut roboten
1. När det är ok, kör avsnitt 3 (steg 3a)
2. I avsnitt 3b, notera VERIFY_Z-värdet, det ska INTE vara negativt. Negativt innebär under arbetsplanet.
3. Kör avsnitt 3b.
4. Kör avsnitt 3c och TCP:n ska peka ut var 0,0-koordinaten är, dvs. ovanför ArUco-markörens nedre vänstra hörn.

### Uppgift 4: Testförflyttning
1. Kör avsnitt 4 och TCP:n ska peka ut var 0,0-koordinaten är, dvs. ovanför ArUco-markörens nedre vänstra hörn.

### Uppgift 5: Fånga, inferera, plocka
1. Innan du kör steg 5, kontrollera att alla förskjutningar är inställda på 0,0.
2. X_OFFSET = 0.0, osv. representerar spetsen på TCP-pekaren.
3. Men vi börjar med 0,0 bara för att verifiera att det fungerar.
4. Kör steg 5.
5. Roboten ska:
    - flytta sig till ovanför markören
    - börja suga
    - flytta sig till avlämningspositionen
    - sluta suga
    - flytta sig till neutralpositionen
6. Justera nu Z_OFFSET så att vi faktiskt plockar upp markören. Z_OFFSET måste sänkas (till negativa tal) för att kompensera för användning av sugverktyget utan TCP-pekaren.
7. Du kan behöva finjustera X- och Y-förskjutningarna för att kompensera för mätfel (linser).
