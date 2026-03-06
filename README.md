# Scraper Books to Scrape

Script Python de web scraping du site [books.toscrape.com](https://books.toscrape.com/).

## Fonctionnalités

- Extraction des données de chaque livre (titre, prix, note, description, UPC, etc.)
- Parcours automatique de toutes les catégories du site
- Gestion de la pagination
- Export des données en fichiers CSV (un fichier par catégorie)
- Téléchargement de l'URL de couverture de chaque livre

## Données extraites par livre

| Champ | Description |
|---|---|
| `product_page_url` | URL de la page produit |
| `upc` | Code universel du produit |
| `title` | Titre du livre |
| `price_including_tax` | Prix TTC |
| `price_excluding_tax` | Prix HT |
| `number_available` | Nombre d'exemplaires disponibles |
| `product_description` | Description du livre |
| `category` | Catégorie |
| `review_rating` | Note (1 à 5) |
| `image_url` | URL de l'image de couverture |

## Installation

### 1. Cloner le dépôt

```bash
git clone <url-du-repo>
cd <nom-du-dossier>
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 3. Activer l'environnement virtuel

- Windows :
```bash
.venv\Scripts\activate
```
- macOS / Linux :
```bash
source .venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python scraping.py
```

Les fichiers CSV sont générés dans le dossier `scraped_data/`, un fichier par catégorie.

## Structure du projet

```
Projet 2/
├── scraping.py         # Script principal (scraping complet du site)
├── scraping_2.py       # Script de test (scraping d'un seul livre)
├── requirements.txt    # Dépendances Python
├── scraped_data/       # Dossier de sortie des fichiers CSV
└── README.md
```
