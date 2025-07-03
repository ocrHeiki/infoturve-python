# 📘 NÄDAL 3 – OSINT ja automaatne andmete kogumine

## Päev 1: Domeeni IP-päring
- Fail: `domain_lookup.py`
- Kasuta `socket.gethostbyname`

## Päev 2: E-posti aadressi kontroll
- Fail: `email_check.py`
- Kas sisaldab tuntud domeeni (gmail, outlook...)

## Päev 3: HTTP pealkirja kontroll
- Fail: `veebiskanner.py`
- Kasuta `requests.get()` ja leia <title> tag

## Päev 4: Andmete salvestamine faili
- Ava tekstifail ja salvesta sinna kogutud andmed.

## Päev 5: Failide läbivaatamine ja logide otsing
- Loe `.log` faile ja kuva, kus esineb "error"

## Päev 6: Lihtne raport
- Genereeri kokkuvõte kogutud andmetest, salvesta .txt faili

## Päev 7: OSINT automatiseerimine
- Koosta skript, mis teeb mitu päringut järjest (nt IP, e-post, HTTP)
