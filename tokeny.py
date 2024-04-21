import ply.yacc as yacc
from ply import lex

tokens = (
    'ZMIENNA',
    'LICZBA',
    'PLUS',
    'MINUS',
    'MNOZENIE',
    'DZIELENIE',
    'POTEGOWANIE',
    'KOMENTARZ',
    'FUNKCJA',
    'ID_FUNKCJI',
    'LNAWIAS_OKRAGLY',
    'PNAWIAS_OKRAGLY',
    'LNAWIAS_KWADRATOWY',
    'PNAWIAS_KWADRATOWY',
    'LNAWIAS_KLAMROWY',
    'PNAWIAS_KLAMROWY'
    'RÓWNE',
    'ROZNE',
    'PODSTAW',
    'WIEKSZE',
    'MNIEJSZE',
    'MNIEJSZE_RÓWNE',
    'WIEKSZE_RÓWNE',
    'ALTERNATYWA',
    'NEGACJA',
    'KONIUNKCJA',
    'PRZECINEK',
    'WHILE',
    'FOR',
    'IF',
    'ELIF',
    'ELSE',
    'RETURN',
    'PRAWDA',
    'FALSZ',
    'KLASA',
    'FROM',
    'IMPORT',
    'DWUKROPEK',
    'NAPIS',
    'PRZERWIJ',
    'KONTUNUUJ',
    'ZWIEKSZ'
)

t_ZMIENNA = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'-?\d+\.?\d*'
    t.value = int(t.value)
    return t

t_PLUS = r'DODAJ'
t_MINUS = r'ODEJMIJ'