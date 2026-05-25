# Elevhandledning — Session 2: Annotering och träning

## Vad du kommer att göra i den här sessionen
1. Ladda upp dina bilder till Roboflow
2. Rita segmenteringsmasker runt varje föremål
3. Träna en AI-modell att känna igen dina föremål
4. Utvärdera hur bra modellen fungerar

## Varför annotering är viktigt

AI-modellen lär sig **enbart** från de exempel du ger den. Om du märker upp föremål slarvigt, kommer modellen att segmentera föremål slarvigt. Dina annoteringar är sanningen.

## Dina uppgifter

### Uppgift 1: Ladda upp bilder
1. Logga in på Roboflow på [app.roboflow.com](https://app.roboflow.com)
2. Öppna din grupps projekt
3. Ladda upp alla dina bra bilder från Session 1

### Uppgift 2: Definiera dina klasser
Använd exakt dessa klassnamn:
- `square`
- `rectangle`
- `circle`
- `triangle`
- `hexagon`
- `ellipse`

**Viktigt:** Lägg inte till extra klasser om inte läraren säger det.

### Uppgift 3: Annotera
1. Använd "Find objects with AI" vid annotering för automatisk bilddetektering.
2. Välj klassnamnet från listan eller ange det innan du trycker på "Find Objects".
3. Om den hittar för många eller för få, justera konfidenströskel.
4. Klicka på spara.
5. Upprepa detta för alla bilder.


### Uppgift 4: Träna din modell
1. Gå till **Dataset** → **Train Model** -> **Custom Training**
2. Använd 10% för validering och 10% för testning.
3. Använd standardinställningarna för förbehandling och dataaugmentering
4. Klicka på **Train** och välj segmenteringsmodellen
5. Träningen tar ungefär 15–20 minuter


### Uppgift 6: Anteckna din API-nyckel
1. Klicka på kugghjulsikonen i den vänstra menyn -> API keys
2. Gå till Jupiter och ange den under **2. Model training (session 2)**
3. Gå till Projects i den vänstra menyn
4. Välj ditt projekt.
5. Under modellnamnet står: ID: <model-id>/<model version>
    Exempel: markers-uorw8/2
6. Ange model-id under **2. Model training (session 2)**
7. Ange versionen under **2. Model training (session 2)**

8. Kör avsnittet och granska resultatet:
   - Vilken klass detekterades?
   - Vad är konfidenspoängen?
   - Var i bilden finns masken?
