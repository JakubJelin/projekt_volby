# projekt_volby2 2017 Jakub Jelínek

## O čem projekt je? (o výsledku voleb z roku 2017 - jejichž výsledek se mi nelíbí)
Tento skript umožňuje vypsat výsledky parlamentních voleb z roku 2017 pro jeden konkrétní okres z [tohodle webu](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) a uložit je do souboru CSV.

## Jak na to
Před spuštěním projektu si nainstalujte potřebné knihovny které jsou vypsané v souboru `requirements.txt`
Skript spusťte z příkazového řádku pomocí příkazu: 

python projekt_volby2.py <odkaz_uzemniho_celku> <vystupni_soubor>

Výstupem bude soubor .csv s výsledky voleb pro daný okres, vypsány budou jenotlivé strany, kolik získali v dané obci hlasů atd....

## Jak to vypadá v praxi
Například pro okres Benešov:
1. Odkaz -> (https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101)
2. Název výstupního souboru -> `vystup.csv`

## Spuštění programu
python projekt_volby2.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "vystup.csv"

## Běh programu
Stahuji data z: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
Stránka stažena!
Počet obcí: 114
Stahuji: Benešov
Stahuji: Bernartice
...atd...
Hotovo! Uloženo do: vystup.csv

## Výřez z výstupu
code,location,registered,envelopes,valid,Občanská demokratická strana,...
529303,Benešov,13104,8485,8437,1052,...
532568,Bernartice,191,148,148,4,...
