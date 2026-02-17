PORO - Projet Django
=====================

Aperçu
-------
Ce dépôt contient une application Django simple (app `core`) utilisant SQLite pour le développement. Le but du README est d'aider un débutant à cloner le projet et à le lancer en local.

Prérequis
---------
- Git
- Python 3.8+ (installer Python si nécessaire)
- `pip` (fourni avec Python)

Installation (Windows and *nix)
-------------------------------
1. Cloner le dépôt :

```bash
git clone <URL_DU_DEPOT>
cd PORO
```

2. Créer et activer un environnement virtuel (recommandé)

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows (cmd):

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Installer les dépendances

```bash
pip install -r requirements.txt
```

4. Préparer la base de données

```bash
python manage.py migrate
```

5. (Optionnel) Créer un compte administrateur

```bash
python manage.py createsuperuser
```

6. Lancer le serveur de développement

```bash
python manage.py runserver
```

Fichiers et structure importants
--------------------------------
- `manage.py` : script d'administration Django.
- `RUN/settings.py` : configuration principale (DEBUG=True en développement, base de données SQLite).
- `core/` : application principale du projet (modèles, vues, templates, static).
- `db.sqlite3` : base de données SQLite (déjà présente).
- `media/` : dossier pour fichiers uploadés (vérifier son existence en local).

Remarques pour débutants
------------------------
- Le projet utilise Django 6.0.1 (voir `requirements.txt`).
- En développement `DEBUG` est activé (cf. `RUN/settings.py`). Ne pas exposer ce dépôt en production tel quel.
- La clé secrète est dans `RUN/settings.py` ; pour un déploiement, utilisez des variables d'environnement et ne commitez pas la clé.
- Les fichiers statiques sont dans `core/static` et la configuration de collecte statique utilise `STATIC_ROOT = staticfiles`.

Tests
-----
Si des tests existent dans `core/tests.py`, lancez-les avec :

```bash
python manage.py test
```

Problèmes courants
------------------
- Erreur d'import ou dépendance manquante : vérifier que l'environnement virtuel est activé et réinstaller `pip install -r requirements.txt`.
- Problèmes de permission pour `media/` : créer le dossier si besoin (`mkdir media`) et donner les droits d'écriture.

Besoin d'aide
-------------
Si vous voulez que je complète ce README (ajout d'un guide de déploiement, variables d'environnement, ou scripts utiles), dites-moi ce que vous souhaitez.
