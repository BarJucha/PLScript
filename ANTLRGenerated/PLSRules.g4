grammar PLSRules;

PLUS : 'POLACZ';
MINUS : 'ROZLACZ';
MNOZENIE : 'RAZY';
DZIELENIE : 'PODZIEL';
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
NUMERYCZNY : '-'?[0-9]+('.'[0-9]+)?;
ID : [a-zA-Z_][a-zA-Z0-9_]*;
SPACJA : [ \t\r\n] -> skip;
INT : 'LICZBA';
STRING : 'TEKST';
BOOL : 'BOOL';
PRZECINEK : ',';
DO: 'DO';
PRINT: 'WYPISZ';
KONIEC: 'KONIEC';


program:
    kod* KONIEC;

kod:
    wyrazenie KONIEC_LINII |
    wyrazenie KONIEC_LINII kod |
    KOMENTARZ kod;

wyrazenie:
    deklaracjaWartosci | przypisanieWartosci | wyrazenieDrukowania | wyrazenieFor | wyrazenieWhile | wyrazenieWarunkowe KONIEC | wywolanieFunkcji | deklaracjaFunkcji | RETURN wartosc;


deklaracjaFunkcji:
    FUNKCJA ID LNAWIAS_OKRAGLY wszystkieArgumenty PNAWIAS_OKRAGLY LNAWIAS_KLAMROWY kod RETURN wartosc PNAWIAS_KLAMROWY;

wywolanieFunkcji:
    ID LNAWIAS_OKRAGLY wszystkieWartosci PNAWIAS_OKRAGLY;

wartosc:
    wyrazenieString | wyrazenieBool | wyrazenieArytmetyczne | ID | wywolanieFunkcji;

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

wyrazenieDrukowania:
    PRINT wartosc | PRINT LNAWIAS_OKRAGLY wartosc PNAWIAS_OKRAGLY;

wyrazenieFor:
    FOR ID OD wyrazenieArytmetyczne DO wyrazenieArytmetyczne LNAWIAS_KLAMROWY petla PNAWIAS_KLAMROWY;

wyrazenieWhile:
    WHILE wyrazenieBool LNAWIAS_KLAMROWY petla PNAWIAS_KLAMROWY;

wyrazenieWarunkowe:
    IF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY| IF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY wyrazenieElif wyrazenieElse |
    IF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY wyrazenieElif | IF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY wyrazenieElse;

wyrazenieElif:
    ELIF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY | wyrazenieElif ELIF wyrazenieBool LNAWIAS_KLAMROWY (kod|petla) PNAWIAS_KLAMROWY;

wyrazenieElse:
    ELSE LNAWIAS_KLAMROWY (petla|kod) PNAWIAS_KLAMROWY;

typWartosci:
    (INT | STRING | BOOL) SPACJA?;

deklaracjaWartosci:
    typWartosci ID PODSTAW wartosc;

przypisanieWartosci:
    ID PODSTAW wartosc;

listaArgumentow:
    typWartosci ID | listaArgumentow PRZECINEK typWartosci ID;

wszystkieArgumenty:
    SPACJA | listaArgumentow;

petla:
    kod | petla (PRZERWIJ | KONTYNUUJ) KONIEC_LINII petla |
    petla (PRZERWIJ | KONTYNUUJ) KONIEC_LINII |
    (PRZERWIJ | KONTYNUUJ) KONIEC_LINII petla | (PRZERWIJ | KONTYNUUJ) KONIEC_LINII;


listaWartosci:
    wartosc | listaWartosci PRZECINEK wartosc;

wszystkieWartosci:
    SPACJA | listaWartosci;