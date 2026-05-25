# Elevhandledning — Session 4: ArUco-kalibrering

## Vad du kommer att göra i den här sessionen
1. Lära dig varför roboten behöver kalibrering för att förstå kamerabilder
2. Utföra en enkel kalibrering med en ArUco-markör
3. Konvertera objektpositioner från pixlar till millimeter

## Kärnproblemet
Kameran ser **pixlar** (t.ex. "cirkelns centrum är vid pixel 800, 450").
Roboten arbetar i **millimeter** (t.ex. "flytta till 250 mm, 150 mm").

I den här sessionen ska du ta reda på omvandlingen mellan dessa två världar.

## Dina uppgifter

### Uppgift 1: Förstå kalibreringskonceptet
Titta på kamerabilden. Svara på dessa frågor:
- Bilden är _______ pixlar bred och _______ pixlar hög
- Arbetsytan är ungefär _______ mm bred (mät med linjal)
- Alltså är ungefär 1 pixel ≈ _______ mm (dela arbetsytans bredd med bildens bredd)

Detta grova estimat visar idén. Nu ska vi göra det exakt.

### Uppgift 2: ArUco-kalibrering
1. Placera ArUco-markören plant på arbetsytan
2. **Mät markören**: _______ mm
4. Hitta raden märkt `# TODO: enter your measured marker size` i avsnitt 2.
5. Ange din mätning
6. Kör avsnittet, det visar storleken du angav.
7. Placera nu ArUco-markören plant på arbetsytan i nedre vänstra hörnet av kameravyn.
8. Kör inspelningsavsnittet så visas en bild med ArUco-markören.
9. Anteckna resultaten:
   - Markörbredd i pixlar: _______
   - Markörsstorlek i mm: _______
   - **mm per pixel**: _______

### Uppgift 3: Verifiering av din kalibrering
1. Placera ett föremål på arbetsytan inom kamerans synfält.
2. Ta en linjal och mät avståndet från ArUco-markörens nedre vänstra hörn till markörens centrum.
3. Längst upp i avsnittet hittar du **MANUAL_MEASUREMENT_MM = 130 # <-- CHANGE THIS**, ange rätt mätning i mm.
4. Kör verifieringsavsnittet för att ta en bild och hitta föremålets pixelposition
5. Programmet visar en bild där det markerat markören och det beräknade avståndet.
6. Är felet mellan det uppmätta och det beräknade acceptabelt för en sugkopp? (tips: ±5–10 mm är vanligtvis bra)
