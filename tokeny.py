import ply.yacc as yacc
from ply import lex
import re

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
    'PNAWIAS_KLAMROWY',
    'ROWNE',
    'ROZNE',
    'PODSTAW',
    'WIEKSZE',
    'MNIEJSZE',
    'MNIEJSZE_ROWNE',
    'WIEKSZE_ROWNE',
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
    'KONTYNUUJ',
    'ZWIEKSZ'
)

def t_LICZBA(t):
    r'-?\d+\.?\d*'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

t_PLUS = r'POLACZ'
t_MINUS = r'ROZLACZ'
t_MNOZENIE = r'MULTI'
t_DZIELENIE = r'ROZWAL NA'
t_POTEGOWANIE = r'POTEGA'
t_KOMENTARZ = r'SWOJA DROGA'
t_FUNKCJA = r'MAGIA'
t_LNAWIAS_OKRAGLY = r'\('
t_PNAWIAS_OKRAGLY = r'\)'
t_LNAWIAS_KWADRATOWY = r'\['
t_PNAWIAS_KWADRATOWY = r'\]'
t_LNAWIAS_KLAMROWY = r'{'
t_PNAWIAS_KLAMROWY = r'}'
t_ROWNE = r'TO SAMO CO'
t_ROZNE = r'INNE OD'
t_PODSTAW = r'TO'
t_WIEKSZE = r'SILNIEJSZE OD'
t_MNIEJSZE = r'SLABSZE OD'
t_MNIEJSZE_ROWNE = r'<='
t_WIEKSZE_ROWNE = r'>='
t_ALTERNATYWA = r'LUB'
t_KONIUNKCJA = r'I'
t_NEGACJA = r'NIE'
t_PRZECINEK = r','
t_WHILE = r'DO MOMENTU'
t_FOR = r'PETLA PO'
t_IF = r'JESLI'
t_ELIF = r'LUB_JESLI'
t_ELSE = r'INACZEJ'
t_RETURN = r'ODDAJ'
t_PRAWDA = r'PRAWDA'
t_FALSZ = r'FALSZ'
t_KLASA = r'KATEGORIA'
t_FROM = r'OD'
t_IMPORT = r'UKRADNIJ'
t_DWUKROPEK = r':'
t_NAPIS = r'"[^"\n]*"'
t_PRZERWIJ = r'SKONCZ'
t_KONTYNUUJ = r'LEC DALEJ'
t_ZWIEKSZ = r'LVL_UP'

def t_error(t):
    if not re.match(r'\s',t.value):
        print("Nieznany symbol: '%s'" % t.value[0])
    t.lexer.skip(1)

t_ZMIENNA = r'[a-zA-Z_][a-zA-Z0-9_]*'

lexer = lex.lex()

proba = "x <= 2\n y TO 3\n x POLACZ y"

lexer.input(proba)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
