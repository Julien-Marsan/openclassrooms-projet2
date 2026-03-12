# OpenClassrooms – Projet 2 (Books to Scrape)

Ce projet contient un script Python qui récupère les données produits du site **Books to Scrape** et exporte les résultats localement.

## Objectif actuel

Le script [`scraping.py`](scraping.py:1) :
- parcourt **toutes les catégories** depuis la page d'accueil ;
- gère automatiquement la **pagination** de chaque catégorie ;
- visite chaque fiche produit ;
- extrait les données demandées ;
- génère **un CSV par catégorie** ;
- télécharge et enregistre **l'image de chaque livre**.

URL de base utilisée :

`https://books.toscrape.com/`

## Données extraites

Colonnes exportées dans le CSV :

- `product_page_url`
- `upc`
- `title`
- `price_including_tax`
- `price_excluding_tax`
- `number_available`
- `product_description`
- `category`
- `review_rating`
- `image_url`
- `image_path`

## Prérequis

- Python 3.10+
- Dépendances :
  - `requests`
  - `beautifulsoup4`

Le fichier [`requirements.txt`](requirements.txt) est fourni pour installer exactement les librairies nécessaires.

Installation rapide :

```bash
pip install requests beautifulsoup4
```

Installation recommandée (environnement virtuel) :

```bash
python -m venv .venv
```

Sous Windows (cmd) :

```bat
.venv\Scripts\activate
pip install -r requirements.txt
```

## Exécution

Depuis la racine du projet, lancer :

```bash
python scraping.py
```

Le script principal est [`scraping.py`](scraping.py:1).

## Vérification rapide après exécution

- Vérifier la présence des CSV dans [`donnees_extraites`](donnees_extraites)
- Vérifier la présence des images dans [`donnees_extraites/images`](donnees_extraites/images)
- Ouvrir un CSV (ex: [`mystery.csv`](donnees_extraites/mystery.csv)) et confirmer que la colonne `image_path` contient des chemins locaux valides

## Résultat

Les exports sont générés dans le dossier [`donnees_extraites`](donnees_extraites) :

- **CSV par catégorie** :
  - exemple : [`mystery.csv`](donnees_extraites/mystery.csv)
  - nom de fichier basé sur la catégorie (normalisé)

- **Images des livres** :
  - dossier racine : [`donnees_extraites/images`](donnees_extraites/images)
  - sous-dossiers par catégorie (normalisés)
  - convention de nommage : `UPC_TITRE_SANITIZE.ext`
  - exemple : `a897fe39b1053632_sharp_objects.jpg`

## Structure de sortie (exemple)

```text
donnees_extraites/
├── mystery.csv
├── travel.csv
└── images/
    ├── mystery/
    │   ├── a897fe39b1053632_sharp_objects.jpg
    │   └── ...
    └── travel/
        └── ...
```

## Remarques

- Les dossiers de sortie sont créés automatiquement s'ils n'existent pas.
- Les URLs d'images relatives sont converties en URLs absolues dans [`extract_product_data()`](scraping.py:60) via [`urljoin`](scraping.py:6).
- Le téléchargement des images est géré dans [`download_product_image()`](scraping.py:143).
- Les fichiers CSV et certains dossiers techniques sont ignorés par Git via [`.gitignore`](.gitignore:1).

## Dépannage

- Si `python` n'est pas reconnu, réinstaller Python en cochant l'option *Add Python to PATH*.
- Si une dépendance manque, relancer `pip install -r requirements.txt` dans l'environnement virtuel activé.
- Si l'exécution est interrompue, relancer [`python scraping.py`](scraping.py:1) : les dossiers déjà créés sont réutilisés.
