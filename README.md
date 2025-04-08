# Ohjelmistotekniikka, harjoitustyö
Aion tehdä _huutopussi_-korttipelistä **digi**version.

- [Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](/dokumentaatio/changelog.md)

## Asennus ohjeet

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

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

Raportti generoituu _htmlcov_-hak### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```emistoon.
