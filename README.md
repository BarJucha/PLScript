# PLScript
To projekt zakładający stworzenie własnego języka programowania zawierającego polskie wyrazy kluczowe.

# Opis projektu
Projekt zakłada stworzenie interpretera, który jest implementowany w języku Python. To stworzenia skanera i parsera został użyty generator ANTLR4.

# Spis tokenów

```antlr
PLUS : '+';
MINUS : '-';
MNOZENIE : '*';
DZIELENIE : '/';
KOMENTARZ : 'SWOJA_DROGA' ~[\r\n]* -> skip;
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
WIEKSZE : '>';
MNIEJSZE : '<';
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
KONIEC_LINII : ';';
SPACJA: [ \t\r\n]+ -> skip;
INT : 'LICZBA';
STRING : 'TEKST';
BOOL : 'BOOL';
PRZECINEK : ',';
DO: 'DO';
PRINT: 'WYPISZ';
KONIEC: 'KONIEC';
WYWOLANIE: 'WYWOLAJ';
NUMERYCZNY : '-'?[0-9]+('.'[0-9]+)?;
ID : [a-zA-Z_][a-zA-Z0-9_]*;
```


## Gramatyka

```antlr

program:
    kod* EOF;

kod:
    wyrazenie KONIEC_LINII;

wyrazenie:
    instrukcja |
    deklaracjaFunkcji |
    wywolanieFunkcji;

instrukcja:
    deklaracjaWartosci |
    przypisanieWartosci |
    instrukcjaZlozona |
    returnInstrukcja;

instrukcjaZlozona:
    ifInstrukcja |
    whileInstrukcja |
    forInstrukcja |
    printInstrukcja;

deklaracjaFunkcji:
    FUNKCJA ID LNAWIAS_OKRAGLY (parametry)? PNAWIAS_OKRAGLY LNAWIAS_KLAMROWY (instrukcja)* (returnInstrukcja)? PNAWIAS_KLAMROWY;

parametry:
    typWartosci ID (PRZECINEK typWartosci ID)*;

deklaracjaWartosci:
    typWartosci ID PODSTAW wartosc;

przypisanieWartosci:
    ID PODSTAW wartosc;

wyrazeniePodstawowe:
    NUMERYCZNY |
    ID |
    NAPIS |
    PRAWDA |
    FALSZ;


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

wywolanieFunkcji:
    WYWOLANIE ID LNAWIAS_OKRAGLY listaWartosci? PNAWIAS_OKRAGLY;

listaWartosci:
    (wartosc PRZECINEK)*? wartosc;

wartosc:
    wyrazenieString | wyrazenieBool | wyrazenieArytmetyczne | ID | wywolanieFunkcji;

typWartosci:
    INT | STRING | BOOL;

returnInstrukcja:
    RETURN wyrazeniePodstawowe?;

ifInstrukcja:
    IF wyrazenieBool LNAWIAS_KLAMROWY (instrukcja)* returnInstrukcja? PNAWIAS_KLAMROWY (elseInstrukcja)?;

elseInstrukcja:
    ELSE LNAWIAS_KLAMROWY instrukcja* returnInstrukcja? PNAWIAS_KLAMROWY;

whileInstrukcja:
    WHILE wyrazenieBool LNAWIAS_KLAMROWY instrukcja* returnInstrukcja? PNAWIAS_KLAMROWY;

forInstrukcja:
    FOR LNAWIAS_OKRAGLY deklaracjaWartosci KONIEC_LINII wyrazenieBool KONIEC_LINII przypisanieWartosci PNAWIAS_OKRAGLY LNAWIAS_KLAMROWY instrukcja* returnInstrukcja? PNAWIAS_KLAMROWY;

printInstrukcja:
    PRINT LNAWIAS_OKRAGLY wartosc PNAWIAS_OKRAGLY;
```

# Narzędzia
Głównym narzędziem używanym w projekcie jest ANTLR, który został wykorzystany do wygenerowania analizatorów składniowych.

# Instrukcja obsługi
1. Pobierz zawartość repozytorium
2. Pobierz zewnętrzne biblioteki potrzebne do działania aplikacji
``` sh
pip install pyqt5
```

3. Uruchom aplikację poprzez plik app.py
``` sh
python app.py
```

# Przykłady
```
LICZBA A TO 4;

JESLI A < 2 {
    WYPISZ(2)
} INACZEJ {
	
    WYPISZ(3)
};

WYPISZ("-----");

POKI(A < 6) {
    WYPISZ(A)
    A TO A+1
};

WYPISZ("-----");

PETLA(LICZBA B TO 4; B < 6; B TO B+1){
    WYPISZ(B)
};




FUNKCJA FOO(LICZBA X){
    PETLA(LICZBA Y TO 0; Y < X; Y TO Y+1) {
        WYPISZ(Y)
    }
    Y TO Y+1
    ZWROC Y
};

LICZBA B TO WYWOLAJ FOO(5);

WYPISZ("-----");
WYPISZ(B);
WYPISZ("-----");

WYPISZ(WYWOLAJ FOO(10));
```
Po wykonaniu:
```
3.0
-----
4.0
5.0
-----
4.0
5.0
0.0
1.0
2.0
3.0
4.0
-----
6.0
-----
0.0
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0
```
