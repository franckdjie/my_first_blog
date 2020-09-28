from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    text ="""<header style="font-size:100px">willy djie</header>
<form methode="post" action="traitement.php">

<p>
<label for="commentaire">entrer votre commentaire ici</label>
<textarea name="commentaire" style="height:40px"> </textarea>
</p>
<p>
<label for="commentaire">entrer votre second commentaire ici</label>
<textarea name="commentaire"style="height:40px"></textarea>
</p>
<p>
<label for="telephone">telephone</label>
<input type="tel" name="telephone" placeholder="655071888"/>
</p>
faisons des cases à cocher(pré-cocher)
<p>
entrer votre sexe<br>
<input type="checkbox" name="homme" checked="checked"/>
<label for="homme">homme</label>
<input type="checkbox" name="femme"/>
<label for="femme">femme</label>
</p>
creons maintenant une zone d'option<br>
quel est votre age
<p><input type="radio" name="age" value="mineur">
<label for="mineur">-18ans</label></p>
<p><input type="radio" name="age" value="majeur">
<label for="majeur">+18ans</label></p>
<input type="submit" value="envoyer">
</form>"""
    return HttpResponse(text)
