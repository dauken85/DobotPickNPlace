# Elevhandledning — Session 6: Beräkning av plockpunkter

## Vad du kommer att göra i den här sessionen
1. Kombinera inferens och kalibrering för att beräkna plockpunkter i robotkoordinater.


## Säkerhetspåminnelse
- Kontrollera nödstoppets placering.
- Meddela gruppen innan du trycker på "Run"

## Dina uppgifter

### Uppgift 1: Verifiera plockpunkten
1. I det första avsnittet, ange höjden för plockpunkten över arbetsytan.
2. Ett Z-värde på 0 ska motsvara arbetsytans nivå.
3. Om de plockade föremålen är 2 mm höga, sätt PICK_Z till 2.0.
4. Kör det andra avsnittet och verifiera avståndet från ArUco-markörens nedre vänstra hörn till plockplatsen i x y z.

    Class         Conf        Pixel (x,y)          Work obj (x,y,z) mm
    --------------------------------------------------------------------
    circle        0.92      ( 855.8,  707.3)   (   48.8,    75.9,   5.0)
