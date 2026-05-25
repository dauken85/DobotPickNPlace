# Elevhandledning — Session 3: Inferens och kalibrering

## Vad du kommer att göra i den här sessionen
1. Köra din tränade modell på bilder och granska resultaten

## Kärnproblemet
I den här sessionen testar vi bilddetekteringsförmågan.

## Dina uppgifter

### Uppgift 1: Konfigurera inferens
1. Gå till **3. Inference (session 3)**
2. Kör det första avsnittet, det laddar bara Roboflow-projektet.
3. Kör det andra avsnittet som registrerar de funktioner vi kommer att använda i nästa steg.

### Uppgift 2: Kör inferens på sparade bilder
4. Det tredje avsnittet kör inferens på en försparat bild, kör det.
5. Förhoppningsvis visas en bild med alla delar detekterade och korrekt märkta.
6. I nästa avsnitt kan du ändra inferensnivån. Om du bara kör det testar det med 0,2, 0,4 och 0,8 som konfidenströsklar.
7. **Prova detta:** Ändra konfidenströskeln på raden märkt `# TODO: adjust threshold`
   - Sätt den till `0.3` — vad händer?
   - Sätt den till `0.95` — vad händer?
   - Välj ett bra tröskelvärde: _______
