grammar PLSRulesV2;

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
NUMERYCZNY : '-'?[0-9]+('.'[0-9]+)?;
ID : [a-zA-Z_][a-zA-Z0-9_]*;

program:
    kod* EOF;

kod:
    wyrazenie KONIEC_LINII;

wyrazenie:
    instrukcja |
    deklaracjaFunkcji;

instrukcja:
    deklaracjaWartosci |
    przypisanieWartosci |
    instrukcjaZlozona;

instrukcjaZlozona:
    ifInstrukcja |
    whileInstrukcja |
    forInstrukcja |
    printInstrukcja;

deklaracjaFunkcji:
    FUNKCJA ID LNAWIAS_OKRAGLY (parametry)? PNAWIAS_OKRAGLY LNAWIAS_KLAMROWY (instrukcja)* (RETURN wyrazenie?)? PNAWIAS_KLAMROWY;

parametry:
    typWartosci ID (PRZECINEK typWartosci ID)*;

deklaracjaWartosci:
    typWartosci ID PODSTAW wyrazeniePodstawowe;

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
    ID LNAWIAS_OKRAGLY listaWartosci PNAWIAS_OKRAGLY;

listaWartosci:
    wartosc | listaWartosci PRZECINEK wartosc;

wartosc:
    wyrazenieString | wyrazenieBool | wyrazenieArytmetyczne | ID | wywolanieFunkcji;

typWartosci:
    INT | STRING | BOOL;

ifInstrukcja:
    IF wyrazenieBool LNAWIAS_KLAMROWY instrukcja* PNAWIAS_KLAMROWY (ELIF wyrazenieBool LNAWIAS_KLAMROWY instrukcja* PNAWIAS_KLAMROWY)* (ELSE LNAWIAS_KLAMROWY instrukcja* PNAWIAS_KLAMROWY)?;

whileInstrukcja:
    WHILE wyrazenieBool LNAWIAS_KLAMROWY instrukcja* PNAWIAS_KLAMROWY;

forInstrukcja:
    FOR LNAWIAS_OKRAGLY deklaracjaWartosci KONIEC_LINII wyrazenieBool KONIEC_LINII wyrazenieArytmetyczne PNAWIAS_OKRAGLY LNAWIAS_KLAMROWY instrukcja* PNAWIAS_KLAMROWY;

printInstrukcja:
    PRINT LNAWIAS_OKRAGLY wartosc PNAWIAS_OKRAGLY;