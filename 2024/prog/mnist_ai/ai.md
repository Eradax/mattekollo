# Neurala nätverk

- Klassificering (Convolutional Neural Network)
- Spela spel (deep Q learning)
- Spela logiska spel (schack, go, etc) - black magic
- Generera bilder (Generative Adversarial Networks / Diffusion)
- Generera text (RMMs / GPTs)
- Skapa AGI och erövra världen

## Hur Tobias ser på ett netualt nätverk
1. Numerisk representation av data
2. *Svart låda*
3. Nice output

## Matten
- Fully connected är när alla lager anslutna
- Deep learning är när man har flera dolda lager

## Neuralt nätverk
1. En nod till nästa fås genom att man multiplicerar föregående nod med kantens weight
2. 2 noder sätts samman genom att man adderar föregående noder multiplicerat med vikterna mellan första och andra lagret (forward propagation)
3. Använd kedjeregeln för att beräkna derivatan av förlusten med avseende på föregående nod, och fortsätt bakåt (back propagation)
4. Varje nod utsätts för activation function, till exempel max(nod, 0)
5. 

## Minstakvadratmetoden
- Exempel: ax² utifrån diverse datapunkter
- Tag felet (riktiga minus från funktionen) i kvadrat
- Tag och dra i från ax², till exempel, om det är det man söker
- Sätt in x-värdet man har på punkten, och derivera med avseende på a
- Gå i *motsatt* riktning (Gradient Descent), så om derivatan är positiv, ska man minska på

## Deep learning
- Isolera en vikt, kör minstakvadratmedod på den
- I deep learning anses vikterna vara självständiga - frysta
- Hoppas på att det fungerar
- Använd kedjeregeln för att beräkna derivatan av förlusten med avseende på föregående nod, och fortsätt bakåt (back propagation)
- En iteration är till exempel en forward prop och en backward prop på varje vikt
- Vid flera node på output layers -> nyttja cross entropy
- Om man har sannolikheter tar man den mest sannolika

## Convolutional layer
- Man har ett filter, t.ex 3x3 matris
- Multiplicera FilterIJ med DataIJ, och summera dessa till *ett* nytt värde
- Shifta över filtret ett steg höger, och upprepa
- Då fås mönster givet att matrisen är bra
- Filtermatrisen kan hittas med ett neuralt nätverk

* Overfitting - neuralt nätverk är övertränat på träningsdatan, kan motverkas med valideringsdatauppsättning
* Checkpoints kan användas för backups av vikterna vid olika antal iterationer ifall att modellen skulle bli sämre
