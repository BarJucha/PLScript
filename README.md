# PLScript
To projekt zakładający stworzenie własnego języka programowania zawierającego polskie wyrazy kluczowe.

## Spis tokenów

```antlr
PLUS : 'POLACZ';
MINUS : 'ROZLACZ';
MNOZENIE : 'RAZY';
DZIELENIE : 'PODZIEL';
KOMENTARZ : 'SWOJA_DROGA';
FUNKCJA : 'FUNKCJA';
LNAWIAS_OKRAGLY : '(';
PNAWIAS_OKRAGLY : ')';
LNAWIAS_KLAMROWY : '{';
PNAWIAS_KLAMROWY : '}';
LNAWIAS_KWADRATOWY : '[';
PNAWIAS_KWADRATOWY : ']';
ROWNE : 'ROWNE';
ROZNE : 'ROZNE';
PODSTAW : 'TO';
WIEKSZE : 'WIEKSZE ';
MNIEJSZE : 'MNIEJSZE ';
MNIEJSZE_ROWNE : '<=';
WIEKSZE_ROWNE : '>=';
ALTERNATYWA : 'LUB';
KONIUNKCJA : 'I';
NEGACJA : 'NIE';
WHILE : 'POKI';
FOR : 'PETLA';
IF : 'JESLI';
ELIF : 'LUB_JESLI';
ELSE : 'INACZEJ';
RETURN : 'ZWROC';
PRAWDA : 'PRAWDA';
FALSZ : 'FALSZ';
OD : 'OD';
IMPORT : 'ZABIERZ';
DWUKROPEK : ':';
NAPIS : '"' .*? '"';
PRZERWIJ : 'SKONCZ';
KONTYNUUJ : 'DALEJ';
ZWIEKSZ : 'PLUSIK';
KONIEC_LINII : '\r\n';
NUMERYCZNY : [-]?[0-9]+([.][0-9]+)?;
ID : [a-zA-Z_][a-zA-Z0-9_]*;
SPACJA : ' ';
INT : 'LICZBA';
STRING : 'TEKST';
BOOL : 'BOOL';
PRZECINEK : ',';
DO: 'DO';
PRINT: 'WYPISZ';
KONIEC: 'KONIEC';
```


## Gramatyka

```antlr

// program glowny i podstawowe operacje

program:
    kod* KONIEC;

kod:
    instrukcja KONIEC_LINII |
    instrukcja KONIEC_LINII kod;

wartosc:
    wyrazenieString | wyrazenieBool | wyrazenieArytmetyczne | ID | wywolanieFunkcji;

typWartosci:
    (INT | STRING | BOOL) SPACJA?;


deklaracjaWartosci:
    typWartosci ID PODSTAW wartosc;

przypisanieWartosci:
    ID PODSTAW wartosc;

// wyrazenia danych

wyrazenieString:
    wyrazenieString ZWIEKSZ wyrazenieString | NAPIS | ID | LNAWIAS_OKRAGLY wyrazenieString PNAWIAS_OKRAGLY | wywolanieFunkcji;

wyrazenieBool:
    wyrazenieBool (KONIUNKCJA | ALTERNATYWA) wyrazenieBool | wyrazenieString (ROWNE | ROZNE) wyrazenieString |
    wyrazenieArytmetyczne (WIEKSZE | MNIEJSZE | MNIEJSZE_ROWNE | WIEKSZE_ROWNE | ROWNE | ROZNE) wyrazenieArytmetyczne | FALSZ | PRAWDA |
    ID | NEGACJA wyrazenieBool | LNAWIAS_OKRAGLY wyrazenieBool PNAWIAS_OKRAGLY | wywolanieFunkcji;

wyrazenieArytmetyczne:
    LNAWIAS_OKRAGLY wyrazenieArytmetyczne PNAWIAS_OKRAGLY |
    wyrazenieArytmetyczne (MNOZENIE | DZIELENIE ) wyrazenieArytmetyczne |
    wyrazenieArytmetyczne (MINUS | PLUS) wyrazenieArytmetyczne |
    NUMERYCZNY | ID | wywolanieFunkcji;


// petle i warunki

petla:
    kod | petla (PRZERWIJ | KONTYNUUJ) KONIEC_LINII petla;

instrukcjaFor:
    FOR ID OD wyrazenieArytmetyczne DO wyrazenieArytmetyczne LNAWIAS_KLAMROWY petla PNAWIAS_KLAMROWY;

instrukcjaWhile:
    WHILE wyrazenieBool LNAWIAS_KLAMROWY petla PNAWIAS_KLAMROWY;

wyrazenieWarunkowe:
    IF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY| IF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY wyrazenieElif wyrazenieElse |
    IF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY wyrazenieElif | IF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY wyrazenieElse;

wyrazenieElif:
    ELIF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY | wyrazenieElif ELIF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY;

wyrazenieElse:
    ELSE LNAWIAS_KLAMROWY (petla|kod) PNAWIAS_KLAMROWY;


instrukcja:
    deklaracjaWartosci | przypisanieWartosci | wyrazenieDrukowania | instrukcjaFor | instrukcjaWhile | wyrazenieWarunkowe KONIEC | wywolanieFunkcji | deklaracjaFunkcji | RETURN wartosc;


// wypisanie do testow

instrukcjaDrukowania:
    PRINT wartosc | PRINT LNAWIAS_OKRAGLY wartosc PNAWIAS_OKRAGLY;

// potrzebne do wywolywnaia funkcji

listaArgumentow:
    typWartosci ID | listaArgumentow PRZECINEK typWartosci ID;

wszystkieArgumenty:
    SPACJA | listaArgumentow;

deklaracjaFunkcji:
    FUNKCJA ID LNAWIAS_OKRAGLY wszystkieArgumenty PNAWIAS_OKRAGLY LNAWIAS_KLAMROWY kod RETURN wartosc PNAWIAS_KLAMROWY;

wywolanieFunkcji:
    ID LNAWIAS_OKRAGLY wszystkieWartosci PNAWIAS_OKRAGLY;

listaWartosci:
    wartosc | listaWartosci PRZECINEK wartosc;

wszystkieWartosci:
    SPACJA | listaWartosci;
```

## Narzędzia
Głównym narzędziem używanym w projekcie jest ANTLR, który został wykorzystany do wygenerowania analizatorów składniowych.
