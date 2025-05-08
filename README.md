# Ohjelmistotekniikka, harjoitustyö
Teen _huutopussi_-korttipelistä **digi**version, kahdelle pelaajalle. Huutopussi on nk. tikkipeli, jossa pelaajat aluksi tarjoavat eli "huutavat" pisteistä ,jotka he luulevat korteillansa saavan. Tarjousvaiheen jälkeen pelataan kierros, jonka jälkeen lasketaan pisteet, ja tarkistetaan saiko tarjousvaiheen voittanut huutonsa verran. HUOM. Oletuksena on, että pelaaja entuudestaan tuntee pelin. Lisää pelin kulkusta ja säännöistä löytyy nettihaulla.

- [Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [Ohjelman alustava rakenne](/dokumentaatio/arkkitehtuuri.md)
- [Changelog](/dokumentaatio/changelog.md)
- [Release 1 viikko 5](https://github.com/pinjapa/ot-harjoitystyo/releases/tag/viikko5)

## Asennus ohjeet

1. Pelin riippuvuudet asennetaan komennolla:

```bash
poetry install
```

2. Luo tiedosto .env samaan kansioon kuin tämä projekti.

    .env tiedostoon luo tietokannan nimi. Huom. nimen täytyy loppua .sqlite
```bash
 DATABASE_FILENAME=
``` 

3. Alusta sovelluksen tietokanta komennolla:

 ```bash
poetry run invoke build
```

4. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Pelin pelaaminen

Pelin voi aloittaa komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti generoituu komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) laatuvaatimukset koodiin voi tarkistaa komennolla:

```bash
poetry run invoke lint
```
