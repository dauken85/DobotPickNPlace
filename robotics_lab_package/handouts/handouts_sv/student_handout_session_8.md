# Elevhandledning — Session 8: Fullständig pipeline

## Vad du kommer att göra i den här sessionen
1. Köra den fullständiga pipelinen

## Den fullständiga pipelinen

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
- Händerna **helt borta** från arbetsytan under robotens rörelse.
- Berätta för din partner innan du trycker på "Run".

## Dina uppgifter

### Uppgift 1: Kör den fullständiga pipelinen
1. Placera **ett** föremål på arbetsytan
2. Kör avsnittet för den fullständiga pipelinen

### Uppgift 2: Automatiserad pipeline
1. Gå till nästa avsnitt, **Automated pipeline**
2. Placera **flera** föremål på arbetsytan
3. Hitta raden **for i in range(1):** och ersätt **1** med antalet föremål.
4. Kör avsnittet för den automatiserade pipelinen

### Uppgift 3: Slutlig demonstration
1. Ställ in ditt bästa arrangemang
2. Demonstrera ditt system för lärarna
3. Var beredd att förklara:
   - Hur din pipeline fungerar
   - Vad din framgångsfrekvens är
   - Vad den största felkällan var
