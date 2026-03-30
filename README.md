# Projet 2 – Scraper le site Books to Scrape

Ce projet fait partie de ma formation Python chez OpenClassrooms. L'idée est simple : aller chercher automatiquement les infos de tous les livres du site [Books to Scrape](https://books.toscrape.com/) et les sauvegarder sur mon ordinateur.

## Ce que fait le script

Le fichier [`scraping.py`](scraping.py) s'occupe de tout :

1. Il va sur la page d'accueil et récupère la liste de toutes les catégories de livres
2. Pour chaque catégorie, il parcourt toutes les pages (même s'il y en a plusieurs)
3. Il visite la fiche de chaque livre pour en extraire les infos
4. Il enregistre tout dans un fichier CSV par catégorie
5. Il télécharge aussi la couverture de chaque livre dans un dossier

## Quelles infos sont récupérées ?

Pour chaque livre, le script récupère :

- L'URL de la page du livre
- Le code UPC (identifiant unique)
- Le titre
- Le prix TTC et le prix HT
- Le nombre d'exemplaires en stock
- La description du livre
- La catégorie
- La note (nombre d'étoiles)
- L'URL de l'image de couverture
- Le chemin local de l'image téléchargée

## Comment installer le projet

Il faut Python 3.10 ou plus récent.

Je recommande de créer un environnement virtuel pour ne pas mélanger les librairies avec d'autres projets :

```bash
python -m venv .venv
```

Puis on l'active (sous Windows) :

```bat
.venv\Scripts\activate
```

Et on installe les dépendances :

```bash
pip install -r requirements.txt
```

Le projet utilise deux librairies : `requests` (pour télécharger les pages web) et `beautifulsoup4` (pour lire le contenu HTML).

## Comment lancer le script

Une fois l'installation faite, il suffit de lancer :

```bash
python scraping.py
```

Le script va tourner pendant quelques minutes le temps de parcourir tout le site.

## Où trouver les résultats

Tout est enregistré dans le dossier [`donnees_extraites/`](donnees_extraites/) :

- **Les fichiers CSV** : un par catégorie, par exemple `mystery.csv`, `travel.csv`, etc.
- **Les images** : dans le sous-dossier [`donnees_extraites/images/`](donnees_extraites/images/), classées par catégorie. Chaque image est nommée avec le code UPC et le titre du livre, par exemple `a897fe39b1053632_sharp_objects.jpg`.

## Bon à savoir

- Les dossiers sont créés automatiquement au lancement, pas besoin de les préparer à l'avance.
- Les fichiers CSV et les images ne sont pas versionnés (ils sont dans le `.gitignore`).
