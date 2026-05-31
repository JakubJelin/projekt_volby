"""
projekt_volby.py: třetí projekt

author: Jakub Jelínek
email: Jelin26174@mot.sps-dopravni.cz
discord: tvuj discord
"""
# Bez tohodle to blblo - něco jako přestávka před každým stáhnutím
import time 
import requests
from bs4 import BeautifulSoup
import csv
import sys

def main():
    # Pro spuštění jsou potřeba 2 argumenty: URL a název CSV souboru
    if len(sys.argv) != 3:
        print("Chyba: Spusť skript takto:")
        print('python projekt_volby.py "URL" "vystup.csv"')
        sys.exit(1)
    
    url = sys.argv[1]
    vystup = sys.argv[2]

    print("Stahuji data z:", url)
    
    # Stáhnout stránku, "html.parser" – říká BeautifulSoup jak má text číst
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print("Stránka stažena!")

    # Najde všechny obce 
    obce = []
    tabulka = soup.find_all("tr")

    #soup.find_all("tr") – najde všechny řádky v celém HTML
    #radek.find_all("td") – v každém řádku najde všechny buňky ("table data")
    #bunky[0] – první buňka = kód obce
    #bunky[1] – druhá buňka = název obce

    for radek in tabulka:
        bunky = radek.find_all("td")
        #kontrola, jestli řádek obsahuje alespoň dvě buňky (kód a název obce)
        if len(bunky) >= 2:
            kod = bunky[0].text.strip()
            nazev = bunky[1].text.strip()
            if kod.isdigit():
                obce.append((kod, nazev))

    print("Počet obcí:", len(obce))
    radky = []
    nazvy_stran = []

    # Pro každou obec stáhnout výsledky
    for kod, nazev in obce:
        obec_url = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=" + kod + "&xvyber=2101"
        print("Stahuji:", nazev)
        time.sleep(0.5)

        # Stáhnout stránku obce
        obec_response = requests.get(obec_url)
        obec_soup = BeautifulSoup(obec_response.text, "html.parser")

        # Najít tabulky
        tabulky = obec_soup.find_all("table")

        # Z první tabulky vytáhnout čísla (voliči, obálky, platné hlasy)
        prvni_tabulka = tabulky[0].find_all("td")
        volici = prvni_tabulka[3].text.strip()
        obalky = prvni_tabulka[4].text.strip()
        platne = prvni_tabulka[7].text.strip()

        # Vytáhnout hlasy pro každou stranu
        strany = {}
        for strana_radek in tabulky[1].find_all("tr")[2:]:
            bunky_strany = strana_radek.find_all("td")
            if len(bunky_strany) >= 3:
                nazev_strany = bunky_strany[1].text.strip()
                hlasy_strany = bunky_strany[2].text.strip()
                strany[nazev_strany] = hlasy_strany

        if not nazvy_stran:
            nazvy_stran = list(strany.keys())
        radek = [kod, nazev, volici, obalky, platne] + list(strany.values())
        radky.append(radek)

    # Uložit do CSV
    with open(vystup, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["code", "location", "registered", "envelopes", "valid"] + nazvy_stran)
        writer.writerows(radky)

    print("Hotovo! Uloženo do:", vystup)
main()