# OpenClassrooms – Projet 2 (Books to Scrape)

Ce projet contient un script Python qui récupère les données produits d'une catégorie du site **Books to Scrape** et exporte le résultat dans **un seul fichier CSV**.

## Objectif actuel

Le script [`scraping.py`](scraping.py:1) :
- parcourt toute la catégorie **Mystery** ;
- gère automatiquement la **pagination** ;
- visite chaque fiche produit ;
- extrait les données demandées ;
- enregistre toutes les lignes dans un CSV unique.

URL de catégorie utilisée :

`https://books.toscrape.com/catalogue/category/books/mystery_3/index.html`

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

## Prérequis

- Python 3.10+
- Dépendances :
  - `requests`
  - `beautifulsoup4`

Installation rapide :

```bash
pip install requests beautifulsoup4
```

## Exécution

Depuis la racine du projet, lancer :

```bash
python scraping.py
```

## Résultat

Le fichier est généré dans le dossier [`donnees_extraites`](donnees_extraites) sous le nom :

- [`mystery.csv`](donnees_extraites/mystery.csv)

## Remarques

- Le dossier de sortie est créé automatiquement s'il n'existe pas.
- Les fichiers CSV et certains dossiers techniques sont ignorés par Git via [`.gitignore`](.gitignore:1).
