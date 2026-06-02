# Elevhandledning — Session 1: Bildinhämtning

## Vad du kommer att göra i den här sessionen
1. Se en livdemo av en robot som plockar föremål med kameravägledning
2. Lära dig hur man arbetar säkert runt roboten
3. Ta bilder av föremål som ska användas för att träna en AI-modell

## Helhetsbilden

```
Kamera  →  AI-modell  →  "Föremålet är här"  →  Robot plockar det
(bild)   (segmentering)  (koordinater)            (rörelse)
```

Idag fokuserar vi på **första steget**: att ta bra bilder för att AI:n ska kunna lära sig.

## Säkerhetsregler
- Sätt **ALDRIG** händerna i robotens arbetsområde när den rör sig
- Lär dig var **nödstopp**-knappen sitter
- Berätta alltid för din partner innan du startar robotens rörelse
- Om något verkar fel, **tryck på nödstoppet**

## Dina uppgifter

### Uppgift 1: Testa kameran
1. Öppna Pylon viewer, anslut Basler-kameran
2. Aktivera kameran och ta en bild eller starta ett videoflöde.
3. Du bör se en liveförhandsvisning från kameran
4. Kontrollera att arbetsytan är synlig och välbelyst

### Uppgift 2: Arrangera föremål
1. Placera 3–5 geometriska former på arbetsytan
2. Se till att de är tydligt synliga (smälter inte in i bakgrunden)
3. Kontrollera kameravyn — kan du se alla föremål?

### Uppgift 3: Ta bilder
1. Gå till avsnitt 1. Image Capture i Jupiter-anteckningsboken.
2. Gå igenom och kör avsnitten ett i taget.
3. Vid "Image Harvesting": Ta minst **20 bilder** med olika arrangemang:
   - [ ] Ett föremål, centrerat
   - [ ] Ett föremål, utanför mitten
   - [ ] Två föremål, separerade
   - [ ] Tre föremål, nära varandra
   - [ ] Fem föremål, blandat kaos
   - [ ] Föremål som rör vid varandra
   - [ ] Olika orienteringar (roterade)
4. Fortsätt och kör resten av avsnitten i Session 1.

## Diskussionsfrågor
- Vad gör en "bra" träningsbild?
- Varför behöver vi många olika arrangemang?
- Vad skulle hända om alla bilder såg likadana ut?
