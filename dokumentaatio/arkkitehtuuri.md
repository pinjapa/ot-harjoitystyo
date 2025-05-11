# Arkkitehtuurikuvaus
Sovellus on digiversio Huutopussi-pelistä kahdelle pelaajalle. 

## Rakenne
Pakkausrakenne:

![](./kuvat/pakkausrakenne.png) 


## Käyttöliittymä

`ui.py` ja `bid_raise_ui.py` sisällyttää käyttöliittymän, joka vastaa pelin näkymien toiminnasta. Pelaajat tekevät vuorotellen tarjouksia korteistaan. Ui.py sisällyttää tarjouskierroksen ja pelin kulun. 
![](./kuvat/kayttoliittyma.png) 

## Sovelluslogiikka

Pelin toiminnallisuuksista vastaa `huutopussi_service.py`, `compare_service.py` ja `count_service.py`.

Rakennetta vastaava pakkaus/luokka kaavio:
![](./kuvat/pakkauskaavio.png) 

## Tietokantatallennus

Tietojen tallennus tapahtuu tietokantaan, joka luodaa pelin alussa. Tämä mahodollistaa pisteiden laskun pelin sisällä. 


### Tiedostot

`repositories` -luokka vastaa tietojen tallennuksesta.

## Päätoiminnallisuudet
Tarjousvaihe -  Pelaajat tekevät tarjouksia pisteistä, jotka pelaajat uskovat saavansa.

Pisteiden laskenta - Pelin lopussa lasketaan pisteet ja tarkistetaan, saiko tarjousvaiheen voittaja huutonsa.

### Kortin pelaaminen

Tikin pelaaminen - Pelaajat pelaavat kortteja vuorotellen, tikin voittaja määräytyy pelin sääntöjen mukaan. Kortin pelaaminen tapahtuu painamalla haluttua korttia.


sequenceDiagram
    participant Käyttöliittymä
    participant Sovelluslogiikka
    participant Pelitilanne
    participant Korttien vertailu

    Käyttöliittymä->>Sovelluslogiikka: Valitse kortti peliin
    Sovelluslogiikka-->>Käyttöliittymä: Return pelattu kortti
    Käyttöliittymä->>Sovelluslogiikka: play_card(pelattu kortti)
    Sovelluslogiikka->>Korttien vertailu: play_card(pelattu kortti)
        Sovelluslogiikka-->>Käyttöliittymä: Return pelattu kortti
    Sovelluslogiikka->>Korttien vertailu: compare_cards(pelattu kortti)
    Korttien vertailu-->>Sovelluslogiikka: Return voittaja kortti/pelaaja
    Sovelluslogiikka->>Pelitilanne: päivitä käännön voitaja(käännön voittaja)
    Pelitilanne-->>Sovelluslogiikka: Vahvista päivitys
    Sovelluslogiikka-->>Käyttöliittymä: Päivitä käännön voitaja

### Muut toiminnallisuudet

Ohjelman muut toiminnalisuudet on toteutettu samalla logiikalla kuin aiemmin kuvattu.

## Ohjelmarakenteen heikkoudet

Ohjelma on altis ns. "väärin pelaamiselle". Myös pelaajat voisivat olla oma luokka.
