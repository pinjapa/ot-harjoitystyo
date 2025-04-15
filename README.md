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

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman voi suorittaa komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) ehdottamat tarkistukset koodiin voi suorittaa komennolla:

```bash
poetry run invoke lint
```
