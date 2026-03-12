import csv
# sert à gérer les dossiers/chemins
import os
import re
# permet de convertir des URL relatives en URL absolues.
from urllib.parse import urljoin

# faire les requêtes HTTP
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://books.toscrape.com/"
EXPORT_DIR = "donnees_extraites"
FIELDNAMES = [
    "product_page_url",
    "upc",
    "title",
    "price_including_tax",
    "price_excluding_tax",
    "number_available",
    "product_description",
    "category",
    "review_rating",
    "image_url",
]


# Fonction pour récupérer et parser le contenu d'une page
def get_soup(url):
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "html.parser")


# Fonction pour nettoyer le nom des catégories et créer un nom de fichier valide
def sanitize_filename(name):
    clean = re.sub(r"[^\w\- ]", "", name, flags=re.UNICODE).strip().lower()
    return clean.replace(" ", "_") or "categorie"


# Fonction pour extraire toutes les catégories disponibles sur la page d'accueil
def get_all_categories(home_url):
    soup = get_soup(home_url)
    categories = []

    for link in soup.select("ul.nav-list ul li a"):
        category_name = link.get_text(strip=True)
        href = link.get("href")
        if href:
            category_url = urljoin(home_url, href)
            categories.append((category_name, category_url))

    return categories


# Fonction pour extraire les données d'une page de produit
def extract_product_data(product_url):
    soup = get_soup(product_url)

    upc = soup.find("th", string="UPC").find_next_sibling("td").get_text(strip=True)
    title = soup.find("h1").get_text(strip=True)
    price_including_tax = (
        soup.find("th", string="Price (incl. tax)")
        .find_next_sibling("td")
        .get_text(strip=True)
    )
    price_excluding_tax = (
        soup.find("th", string="Price (excl. tax)")
        .find_next_sibling("td")
        .get_text(strip=True)
    )
    number_available = (
        soup.find("th", string="Availability")
        .find_next_sibling("td")
        .get_text(" ", strip=True)
    )


# Certains produits n'ont pas de description, il faut vérifier que les éléments existent avant d'essayer de les extraire
    description_block = soup.find("div", id="product_description")
    product_description = ""
    if description_block and description_block.find_next_sibling("p"):
        product_description = description_block.find_next_sibling("p").get_text(strip=True)

    # La catégorie est généralement le dernier lien dans la section "breadcrumb"
    category = soup.select("ul.breadcrumb li a")[-1].get_text(strip=True)
    review_rating = soup.find("p", class_="star-rating")["class"][1]
    image_rel = soup.find("div", class_="item active").find("img")["src"]
    image_url = urljoin(product_url, image_rel)

    # On retourne un dictionnaire avec toutes les données extraites
    return {
        "product_page_url": product_url,
        "upc": upc,
        "title": title,
        "price_including_tax": price_including_tax,
        "price_excluding_tax": price_excluding_tax,
        "number_available": number_available,
        "product_description": product_description,
        "category": category,
        "review_rating": review_rating,
        "image_url": image_url,
    }


# Fonction pour répéter l'opération sur toutes les pages d'une catégorie et extraire les URLs des produits
def iter_category_product_urls(category_url):
    next_page_url = category_url

    # On continue à parcourir les pages tant qu'il y a un lien "next" pour la page suivante
    while next_page_url:
        soup = get_soup(next_page_url)

        for article in soup.select("article.product_pod h3 a"):
            href = article.get("href")
            if href:
                yield urljoin(next_page_url, href)

        next_link = soup.select_one("li.next a")
        if next_link and next_link.get("href"):
            next_page_url = urljoin(next_page_url, next_link["href"])
        else:
            next_page_url = None


# Fonction pour écrire les données d'une catégorie dans son fichier CSV dédié
def write_category_csv(category_name, books_data):
    filename = f"{sanitize_filename(category_name)}.csv"
    output_path = os.path.join(EXPORT_DIR, filename)

    with open(output_path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(books_data)

    return output_path


# Fonction principale pour le processus de scraping et d'exportation des données
def main():
    os.makedirs(EXPORT_DIR, exist_ok=True)  # Crée le dossier d'exportation s'il n'existe pas déjà

    categories = get_all_categories(BASE_URL)

    for category_name, category_url in categories:
        product_urls = list(iter_category_product_urls(category_url))
        all_books_data = [extract_product_data(url) for url in product_urls]

        # On écrit les données extraites dans un fichier CSV avec les en-têtes correspondants
        output_path = write_category_csv(category_name, all_books_data)
        print(f"[{category_name}] {len(all_books_data)} livres exportés dans : {output_path}")


# Le point d'entrée du script
if __name__ == "__main__":
    main()
