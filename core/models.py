from django.db import models
import string
import random
import uuid

lieuretrait = [
    'Korhogo Centre - Place de la Paix','Korhogo - Quartier Sinistré','Korhogo - Soba','Korhogo - DEM','Korhogo - Haoussabougou','Korhogo - Cocody','Ferkessédougou - Centre ville','Boundiali - Centre ville'
]


# Create your models here.

def generer_code():
    chars =  string.ascii_uppercase + string.digits
    # renvoie une chaîne aléatoire de 8 caractères (lettres majuscules + chiffres)
    return ''.join(random.choices(chars, k=8))

class Edition(models.Model):
    annee = models.IntegerField("année", unique=True)
    is_active = models.BooleanField(" Editions actuelle ?", default=True)
    date_event = models.DateField("Date de l'evenement")
    heure_debut = models.TimeField("heure de début", default="08:00")
    heure_fin = models.TimeField("heure de fin", default="22:00")
    #donnée google maps
    map_iframe_url = models.URLField("url de google maps", max_length=500, blank=True)
    def __str__(self):
        return f" Poro Run editions {self.annee}"
    
class HeroImage(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, related_name='hero_images')
    image = models.ImageField(upload_to='hero/')
    alt_text = models.CharField(max_length=200, default="ambiance poro run")


class Partenaire(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, related_name='partenaire')
    logo = models.ImageField(upload_to='media')
    name = models.CharField(max_length= 50)
    level = models.CharField(max_length=20, help_text="EX: Or, Platine, Bronze") # OR, Argent, Bronze

    def __str__(self):
        return self.name


class Activite(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, related_name='activite')
    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=255)



class Kit(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, related_name='kit')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='kits')
    avantage = models.TextField(help_text='Liste des avantages separées par des virgules')

    def avantages(self):
        return [f.strip() for f in self.avantage.split(',')]
    
    def __str__(self):
        return self.name
    

# lieu de retrait avec fonctions qui permet de choisir dans lieuretrait


"""
class Kit5000(models.Model):
    #prix = models.DecimalField(max_digits=10, decimal_places=0),
    maillot = models.ImageField(upload_to=''),
    avantage= models.CharField(max_length=20),

class Kit10000(models.Model):
    #prix = models.DecimalField(max_digits=10, decimal_places=0) #le prix du kit
    maillot = models.ImageField(upload_to=''),
    avantage= models.CharField(max_length=20),
"""

#class Lieu_retrait(models.Model):
 #   nom = models.CharField(max_length =30, choices=lieuretrait )


class Commande(models.Model):
    reference = models.CharField(max_length = 20, unique =True, default=generer_code)
    numero = models.CharField(max_length=20)
    lieuRetrait = models.ForeignKey('LieuRetrait', on_delete=models.SET_NULL, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args, **kwargs ):
        if not self.reference:
            self.reference = f"PR-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"commande {self.reference} - {self.numero}"


class LieuRetrait(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name





