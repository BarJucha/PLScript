# Generated from .//PLSRulesV2.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,276,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,
        3,2,56,8,2,1,3,1,3,1,3,3,3,61,8,3,1,4,1,4,1,4,1,4,3,4,67,8,4,1,5,
        1,5,1,5,1,5,3,5,73,8,5,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,
        5,1,5,3,5,85,8,5,3,5,87,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,
        97,8,6,10,6,12,6,100,9,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,121,8,10,1,10,1,
        10,1,10,5,10,126,8,10,10,10,12,10,129,9,10,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,3,11,150,8,11,1,11,1,11,1,11,5,11,155,8,11,10,11,12,11,158,
        9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,168,8,12,1,12,
        1,12,1,12,1,12,1,12,1,12,5,12,176,8,12,10,12,12,12,179,9,12,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,192,8,14,
        10,14,12,14,195,9,14,1,15,1,15,1,15,1,15,1,15,3,15,202,8,15,1,16,
        1,16,1,17,1,17,1,17,1,17,5,17,210,8,17,10,17,12,17,213,9,17,1,17,
        1,17,1,17,1,17,1,17,5,17,220,8,17,10,17,12,17,223,9,17,1,17,1,17,
        5,17,227,8,17,10,17,12,17,230,9,17,1,17,1,17,1,17,5,17,235,8,17,
        10,17,12,17,238,9,17,1,17,3,17,241,8,17,1,18,1,18,1,18,1,18,5,18,
        247,8,18,10,18,12,18,250,9,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,5,19,264,8,19,10,19,12,19,267,9,19,1,19,
        1,19,1,20,1,20,1,20,1,20,1,20,1,20,0,4,20,22,24,28,21,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,7,3,0,29,30,34,
        34,47,48,1,0,13,14,2,0,13,14,16,19,1,0,20,21,1,0,3,4,1,0,1,2,1,0,
        40,42,295,0,45,1,0,0,0,2,50,1,0,0,0,4,55,1,0,0,0,6,60,1,0,0,0,8,
        66,1,0,0,0,10,68,1,0,0,0,12,90,1,0,0,0,14,101,1,0,0,0,16,106,1,0,
        0,0,18,110,1,0,0,0,20,120,1,0,0,0,22,149,1,0,0,0,24,167,1,0,0,0,
        26,180,1,0,0,0,28,185,1,0,0,0,30,201,1,0,0,0,32,203,1,0,0,0,34,205,
        1,0,0,0,36,242,1,0,0,0,38,253,1,0,0,0,40,270,1,0,0,0,42,44,3,2,1,
        0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,
        1,0,0,0,47,45,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,51,3,4,2,0,51,
        52,5,38,0,0,52,3,1,0,0,0,53,56,3,6,3,0,54,56,3,10,5,0,55,53,1,0,
        0,0,55,54,1,0,0,0,56,5,1,0,0,0,57,61,3,14,7,0,58,61,3,16,8,0,59,
        61,3,8,4,0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,7,1,0,0,
        0,62,67,3,34,17,0,63,67,3,36,18,0,64,67,3,38,19,0,65,67,3,40,20,
        0,66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,9,1,
        0,0,0,68,69,5,6,0,0,69,70,5,48,0,0,70,72,5,7,0,0,71,73,3,12,6,0,
        72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,5,8,0,0,75,79,5,
        9,0,0,76,78,3,6,3,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,
        80,1,0,0,0,80,86,1,0,0,0,81,79,1,0,0,0,82,84,5,28,0,0,83,85,3,4,
        2,0,84,83,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,82,1,0,0,0,86,87,
        1,0,0,0,87,88,1,0,0,0,88,89,5,10,0,0,89,11,1,0,0,0,90,91,3,32,16,
        0,91,98,5,48,0,0,92,93,5,43,0,0,93,94,3,32,16,0,94,95,5,48,0,0,95,
        97,1,0,0,0,96,92,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,
        0,0,99,13,1,0,0,0,100,98,1,0,0,0,101,102,3,32,16,0,102,103,5,48,
        0,0,103,104,5,15,0,0,104,105,3,18,9,0,105,15,1,0,0,0,106,107,5,48,
        0,0,107,108,5,15,0,0,108,109,3,30,15,0,109,17,1,0,0,0,110,111,7,
        0,0,0,111,19,1,0,0,0,112,113,6,10,-1,0,113,121,5,34,0,0,114,121,
        5,48,0,0,115,116,5,7,0,0,116,117,3,20,10,0,117,118,5,8,0,0,118,121,
        1,0,0,0,119,121,3,26,13,0,120,112,1,0,0,0,120,114,1,0,0,0,120,115,
        1,0,0,0,120,119,1,0,0,0,121,127,1,0,0,0,122,123,10,5,0,0,123,124,
        5,37,0,0,124,126,3,20,10,6,125,122,1,0,0,0,126,129,1,0,0,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,21,1,0,0,0,129,127,1,0,0,0,130,131,6,
        11,-1,0,131,132,3,20,10,0,132,133,7,1,0,0,133,134,3,20,10,0,134,
        150,1,0,0,0,135,136,3,24,12,0,136,137,7,2,0,0,137,138,3,24,12,0,
        138,150,1,0,0,0,139,150,5,30,0,0,140,150,5,29,0,0,141,150,5,48,0,
        0,142,143,5,22,0,0,143,150,3,22,11,3,144,145,5,7,0,0,145,146,3,22,
        11,0,146,147,5,8,0,0,147,150,1,0,0,0,148,150,3,26,13,0,149,130,1,
        0,0,0,149,135,1,0,0,0,149,139,1,0,0,0,149,140,1,0,0,0,149,141,1,
        0,0,0,149,142,1,0,0,0,149,144,1,0,0,0,149,148,1,0,0,0,150,156,1,
        0,0,0,151,152,10,9,0,0,152,153,7,3,0,0,153,155,3,22,11,10,154,151,
        1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,23,1,
        0,0,0,158,156,1,0,0,0,159,160,6,12,-1,0,160,161,5,7,0,0,161,162,
        3,24,12,0,162,163,5,8,0,0,163,168,1,0,0,0,164,168,5,47,0,0,165,168,
        5,48,0,0,166,168,3,26,13,0,167,159,1,0,0,0,167,164,1,0,0,0,167,165,
        1,0,0,0,167,166,1,0,0,0,168,177,1,0,0,0,169,170,10,5,0,0,170,171,
        7,4,0,0,171,176,3,24,12,6,172,173,10,4,0,0,173,174,7,5,0,0,174,176,
        3,24,12,5,175,169,1,0,0,0,175,172,1,0,0,0,176,179,1,0,0,0,177,175,
        1,0,0,0,177,178,1,0,0,0,178,25,1,0,0,0,179,177,1,0,0,0,180,181,5,
        48,0,0,181,182,5,7,0,0,182,183,3,28,14,0,183,184,5,8,0,0,184,27,
        1,0,0,0,185,186,6,14,-1,0,186,187,3,30,15,0,187,193,1,0,0,0,188,
        189,10,1,0,0,189,190,5,43,0,0,190,192,3,30,15,0,191,188,1,0,0,0,
        192,195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,29,1,0,0,0,195,
        193,1,0,0,0,196,202,3,20,10,0,197,202,3,22,11,0,198,202,3,24,12,
        0,199,202,5,48,0,0,200,202,3,26,13,0,201,196,1,0,0,0,201,197,1,0,
        0,0,201,198,1,0,0,0,201,199,1,0,0,0,201,200,1,0,0,0,202,31,1,0,0,
        0,203,204,7,6,0,0,204,33,1,0,0,0,205,206,5,25,0,0,206,207,3,22,11,
        0,207,211,5,9,0,0,208,210,3,6,3,0,209,208,1,0,0,0,210,213,1,0,0,
        0,211,209,1,0,0,0,211,212,1,0,0,0,212,214,1,0,0,0,213,211,1,0,0,
        0,214,228,5,10,0,0,215,216,5,26,0,0,216,217,3,22,11,0,217,221,5,
        9,0,0,218,220,3,6,3,0,219,218,1,0,0,0,220,223,1,0,0,0,221,219,1,
        0,0,0,221,222,1,0,0,0,222,224,1,0,0,0,223,221,1,0,0,0,224,225,5,
        10,0,0,225,227,1,0,0,0,226,215,1,0,0,0,227,230,1,0,0,0,228,226,1,
        0,0,0,228,229,1,0,0,0,229,240,1,0,0,0,230,228,1,0,0,0,231,232,5,
        27,0,0,232,236,5,9,0,0,233,235,3,6,3,0,234,233,1,0,0,0,235,238,1,
        0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,0,238,236,1,
        0,0,0,239,241,5,10,0,0,240,231,1,0,0,0,240,241,1,0,0,0,241,35,1,
        0,0,0,242,243,5,23,0,0,243,244,3,22,11,0,244,248,5,9,0,0,245,247,
        3,6,3,0,246,245,1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,
        1,0,0,0,249,251,1,0,0,0,250,248,1,0,0,0,251,252,5,10,0,0,252,37,
        1,0,0,0,253,254,5,24,0,0,254,255,5,7,0,0,255,256,3,14,7,0,256,257,
        5,38,0,0,257,258,3,22,11,0,258,259,5,38,0,0,259,260,3,24,12,0,260,
        261,5,8,0,0,261,265,5,9,0,0,262,264,3,6,3,0,263,262,1,0,0,0,264,
        267,1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,
        265,1,0,0,0,268,269,5,10,0,0,269,39,1,0,0,0,270,271,5,45,0,0,271,
        272,5,7,0,0,272,273,3,30,15,0,273,274,5,8,0,0,274,41,1,0,0,0,25,
        45,55,60,66,72,79,84,86,98,120,127,149,156,167,175,177,193,201,211,
        221,228,236,240,248,265
    ]

class PLSRulesV2Parser ( Parser ):

    grammarFileName = "PLSRulesV2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "'FUNKCJA'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'ROWNE'", "'ROZNE'", "'TO'", "'>'", "'<'", "'<='", 
                     "'>='", "'LUB'", "'I'", "'NIE'", "'POKI'", "'PETLA'", 
                     "'JESLI'", "'LUB_JESLI'", "'INACZEJ'", "'ZWROC'", "'PRAWDA'", 
                     "'FALSZ'", "'OD'", "'ZABIERZ'", "':'", "<INVALID>", 
                     "'SKONCZ'", "'DALEJ'", "'PLUSIK'", "';'", "<INVALID>", 
                     "'LICZBA'", "'TEKST'", "'BOOL'", "','", "'DO'", "'WYPISZ'", 
                     "'KONIEC'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MNOZENIE", "DZIELENIE", 
                      "KOMENTARZ", "FUNKCJA", "LNAWIAS_OKRAGLY", "PNAWIAS_OKRAGLY", 
                      "LNAWIAS_KLAMROWY", "PNAWIAS_KLAMROWY", "LNAWIAS_KWADRATOWY", 
                      "PNAWIAS_KWADRATOWY", "ROWNE", "ROZNE", "PODSTAW", 
                      "WIEKSZE", "MNIEJSZE", "MNIEJSZE_ROWNE", "WIEKSZE_ROWNE", 
                      "ALTERNATYWA", "KONIUNKCJA", "NEGACJA", "WHILE", "FOR", 
                      "IF", "ELIF", "ELSE", "RETURN", "PRAWDA", "FALSZ", 
                      "OD", "IMPORT", "DWUKROPEK", "NAPIS", "PRZERWIJ", 
                      "KONTYNUUJ", "ZWIEKSZ", "KONIEC_LINII", "SPACJA", 
                      "INT", "STRING", "BOOL", "PRZECINEK", "DO", "PRINT", 
                      "KONIEC", "NUMERYCZNY", "ID" ]

    RULE_program = 0
    RULE_kod = 1
    RULE_wyrazenie = 2
    RULE_instrukcja = 3
    RULE_instrukcjaZlozona = 4
    RULE_deklaracjaFunkcji = 5
    RULE_parametry = 6
    RULE_deklaracjaWartosci = 7
    RULE_przypisanieWartosci = 8
    RULE_wyrazeniePodstawowe = 9
    RULE_wyrazenieString = 10
    RULE_wyrazenieBool = 11
    RULE_wyrazenieArytmetyczne = 12
    RULE_wywolanieFunkcji = 13
    RULE_listaWartosci = 14
    RULE_wartosc = 15
    RULE_typWartosci = 16
    RULE_ifInstrukcja = 17
    RULE_whileInstrukcja = 18
    RULE_forInstrukcja = 19
    RULE_printInstrukcja = 20

    ruleNames =  [ "program", "kod", "wyrazenie", "instrukcja", "instrukcjaZlozona", 
                   "deklaracjaFunkcji", "parametry", "deklaracjaWartosci", 
                   "przypisanieWartosci", "wyrazeniePodstawowe", "wyrazenieString", 
                   "wyrazenieBool", "wyrazenieArytmetyczne", "wywolanieFunkcji", 
                   "listaWartosci", "wartosc", "typWartosci", "ifInstrukcja", 
                   "whileInstrukcja", "forInstrukcja", "printInstrukcja" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MNOZENIE=3
    DZIELENIE=4
    KOMENTARZ=5
    FUNKCJA=6
    LNAWIAS_OKRAGLY=7
    PNAWIAS_OKRAGLY=8
    LNAWIAS_KLAMROWY=9
    PNAWIAS_KLAMROWY=10
    LNAWIAS_KWADRATOWY=11
    PNAWIAS_KWADRATOWY=12
    ROWNE=13
    ROZNE=14
    PODSTAW=15
    WIEKSZE=16
    MNIEJSZE=17
    MNIEJSZE_ROWNE=18
    WIEKSZE_ROWNE=19
    ALTERNATYWA=20
    KONIUNKCJA=21
    NEGACJA=22
    WHILE=23
    FOR=24
    IF=25
    ELIF=26
    ELSE=27
    RETURN=28
    PRAWDA=29
    FALSZ=30
    OD=31
    IMPORT=32
    DWUKROPEK=33
    NAPIS=34
    PRZERWIJ=35
    KONTYNUUJ=36
    ZWIEKSZ=37
    KONIEC_LINII=38
    SPACJA=39
    INT=40
    STRING=41
    BOOL=42
    PRZECINEK=43
    DO=44
    PRINT=45
    KONIEC=46
    NUMERYCZNY=47
    ID=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PLSRulesV2Parser.EOF, 0)

        def kod(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.KodContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.KodContext,i)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PLSRulesV2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 324355988914240) != 0):
                self.state = 42
                self.kod()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(PLSRulesV2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wyrazenie(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieContext,0)


        def KONIEC_LINII(self):
            return self.getToken(PLSRulesV2Parser.KONIEC_LINII, 0)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_kod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKod" ):
                return visitor.visitKod(self)
            else:
                return visitor.visitChildren(self)




    def kod(self):

        localctx = PLSRulesV2Parser.KodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_kod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.wyrazenie()
            self.state = 51
            self.match(PLSRulesV2Parser.KONIEC_LINII)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WyrazenieContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.InstrukcjaContext,0)


        def deklaracjaFunkcji(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.DeklaracjaFunkcjiContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_wyrazenie

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWyrazenie" ):
                return visitor.visitWyrazenie(self)
            else:
                return visitor.visitChildren(self)




    def wyrazenie(self):

        localctx = PLSRulesV2Parser.WyrazenieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_wyrazenie)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 25, 40, 41, 42, 45, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.instrukcja()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.deklaracjaFunkcji()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrukcjaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def deklaracjaWartosci(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.DeklaracjaWartosciContext,0)


        def przypisanieWartosci(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.PrzypisanieWartosciContext,0)


        def instrukcjaZlozona(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.InstrukcjaZlozonaContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_instrukcja

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrukcja" ):
                return visitor.visitInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def instrukcja(self):

        localctx = PLSRulesV2Parser.InstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instrukcja)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40, 41, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.deklaracjaWartosci()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.przypisanieWartosci()
                pass
            elif token in [23, 24, 25, 45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.instrukcjaZlozona()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrukcjaZlozonaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.IfInstrukcjaContext,0)


        def whileInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WhileInstrukcjaContext,0)


        def forInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ForInstrukcjaContext,0)


        def printInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.PrintInstrukcjaContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_instrukcjaZlozona

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrukcjaZlozona" ):
                return visitor.visitInstrukcjaZlozona(self)
            else:
                return visitor.visitChildren(self)




    def instrukcjaZlozona(self):

        localctx = PLSRulesV2Parser.InstrukcjaZlozonaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instrukcjaZlozona)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.ifInstrukcja()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.whileInstrukcja()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.forInstrukcja()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.printInstrukcja()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeklaracjaFunkcjiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNKCJA(self):
            return self.getToken(PLSRulesV2Parser.FUNKCJA, 0)

        def ID(self):
            return self.getToken(PLSRulesV2Parser.ID, 0)

        def LNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_OKRAGLY, 0)

        def PNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_OKRAGLY, 0)

        def LNAWIAS_KLAMROWY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_KLAMROWY, 0)

        def PNAWIAS_KLAMROWY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_KLAMROWY, 0)

        def parametry(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ParametryContext,0)


        def instrukcja(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.InstrukcjaContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.InstrukcjaContext,i)


        def RETURN(self):
            return self.getToken(PLSRulesV2Parser.RETURN, 0)

        def wyrazenie(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_deklaracjaFunkcji

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeklaracjaFunkcji" ):
                return visitor.visitDeklaracjaFunkcji(self)
            else:
                return visitor.visitChildren(self)




    def deklaracjaFunkcji(self):

        localctx = PLSRulesV2Parser.DeklaracjaFunkcjiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_deklaracjaFunkcji)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PLSRulesV2Parser.FUNKCJA)
            self.state = 69
            self.match(PLSRulesV2Parser.ID)
            self.state = 70
            self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0):
                self.state = 71
                self.parametry()


            self.state = 74
            self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
            self.state = 75
            self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 324355988914176) != 0):
                self.state = 76
                self.instrukcja()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 82
                self.match(PLSRulesV2Parser.RETURN)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 324355988914240) != 0):
                    self.state = 83
                    self.wyrazenie()




            self.state = 88
            self.match(PLSRulesV2Parser.PNAWIAS_KLAMROWY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typWartosci(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.TypWartosciContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.TypWartosciContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PLSRulesV2Parser.ID)
            else:
                return self.getToken(PLSRulesV2Parser.ID, i)

        def PRZECINEK(self, i:int=None):
            if i is None:
                return self.getTokens(PLSRulesV2Parser.PRZECINEK)
            else:
                return self.getToken(PLSRulesV2Parser.PRZECINEK, i)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_parametry

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametry" ):
                return visitor.visitParametry(self)
            else:
                return visitor.visitChildren(self)




    def parametry(self):

        localctx = PLSRulesV2Parser.ParametryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parametry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.typWartosci()
            self.state = 91
            self.match(PLSRulesV2Parser.ID)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 92
                self.match(PLSRulesV2Parser.PRZECINEK)
                self.state = 93
                self.typWartosci()
                self.state = 94
                self.match(PLSRulesV2Parser.ID)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeklaracjaWartosciContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typWartosci(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.TypWartosciContext,0)


        def ID(self):
            return self.getToken(PLSRulesV2Parser.ID, 0)

        def PODSTAW(self):
            return self.getToken(PLSRulesV2Parser.PODSTAW, 0)

        def wyrazeniePodstawowe(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WyrazeniePodstawoweContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_deklaracjaWartosci

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeklaracjaWartosci" ):
                return visitor.visitDeklaracjaWartosci(self)
            else:
                return visitor.visitChildren(self)




    def deklaracjaWartosci(self):

        localctx = PLSRulesV2Parser.DeklaracjaWartosciContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_deklaracjaWartosci)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.typWartosci()
            self.state = 102
            self.match(PLSRulesV2Parser.ID)
            self.state = 103
            self.match(PLSRulesV2Parser.PODSTAW)
            self.state = 104
            self.wyrazeniePodstawowe()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrzypisanieWartosciContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PLSRulesV2Parser.ID, 0)

        def PODSTAW(self):
            return self.getToken(PLSRulesV2Parser.PODSTAW, 0)

        def wartosc(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WartoscContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_przypisanieWartosci

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrzypisanieWartosci" ):
                return visitor.visitPrzypisanieWartosci(self)
            else:
                return visitor.visitChildren(self)




    def przypisanieWartosci(self):

        localctx = PLSRulesV2Parser.PrzypisanieWartosciContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_przypisanieWartosci)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(PLSRulesV2Parser.ID)
            self.state = 107
            self.match(PLSRulesV2Parser.PODSTAW)
            self.state = 108
            self.wartosc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WyrazeniePodstawoweContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERYCZNY(self):
            return self.getToken(PLSRulesV2Parser.NUMERYCZNY, 0)

        def ID(self):
            return self.getToken(PLSRulesV2Parser.ID, 0)

        def NAPIS(self):
            return self.getToken(PLSRulesV2Parser.NAPIS, 0)

        def PRAWDA(self):
            return self.getToken(PLSRulesV2Parser.PRAWDA, 0)

        def FALSZ(self):
            return self.getToken(PLSRulesV2Parser.FALSZ, 0)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_wyrazeniePodstawowe

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWyrazeniePodstawowe" ):
                return visitor.visitWyrazeniePodstawowe(self)
            else:
                return visitor.visitChildren(self)




    def wyrazeniePodstawowe(self):

        localctx = PLSRulesV2Parser.WyrazeniePodstawoweContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_wyrazeniePodstawowe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 422231255547904) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WyrazenieStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAPIS(self):
            return self.getToken(PLSRulesV2Parser.NAPIS, 0)

        def ID(self):
            return self.getToken(PLSRulesV2Parser.ID, 0)

        def LNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_OKRAGLY, 0)

        def wyrazenieString(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.WyrazenieStringContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieStringContext,i)


        def PNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_OKRAGLY, 0)

        def wywolanieFunkcji(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WywolanieFunkcjiContext,0)


        def ZWIEKSZ(self):
            return self.getToken(PLSRulesV2Parser.ZWIEKSZ, 0)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_wyrazenieString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWyrazenieString" ):
                return visitor.visitWyrazenieString(self)
            else:
                return visitor.visitChildren(self)



    def wyrazenieString(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PLSRulesV2Parser.WyrazenieStringContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_wyrazenieString, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 113
                self.match(PLSRulesV2Parser.NAPIS)
                pass

            elif la_ == 2:
                self.state = 114
                self.match(PLSRulesV2Parser.ID)
                pass

            elif la_ == 3:
                self.state = 115
                self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
                self.state = 116
                self.wyrazenieString(0)
                self.state = 117
                self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
                pass

            elif la_ == 4:
                self.state = 119
                self.wywolanieFunkcji()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PLSRulesV2Parser.WyrazenieStringContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenieString)
                    self.state = 122
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 123
                    self.match(PLSRulesV2Parser.ZWIEKSZ)
                    self.state = 124
                    self.wyrazenieString(6) 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class WyrazenieBoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wyrazenieString(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.WyrazenieStringContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieStringContext,i)


        def ROWNE(self):
            return self.getToken(PLSRulesV2Parser.ROWNE, 0)

        def ROZNE(self):
            return self.getToken(PLSRulesV2Parser.ROZNE, 0)

        def wyrazenieArytmetyczne(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.WyrazenieArytmetyczneContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieArytmetyczneContext,i)


        def WIEKSZE(self):
            return self.getToken(PLSRulesV2Parser.WIEKSZE, 0)

        def MNIEJSZE(self):
            return self.getToken(PLSRulesV2Parser.MNIEJSZE, 0)

        def MNIEJSZE_ROWNE(self):
            return self.getToken(PLSRulesV2Parser.MNIEJSZE_ROWNE, 0)

        def WIEKSZE_ROWNE(self):
            return self.getToken(PLSRulesV2Parser.WIEKSZE_ROWNE, 0)

        def FALSZ(self):
            return self.getToken(PLSRulesV2Parser.FALSZ, 0)

        def PRAWDA(self):
            return self.getToken(PLSRulesV2Parser.PRAWDA, 0)

        def ID(self):
            return self.getToken(PLSRulesV2Parser.ID, 0)

        def NEGACJA(self):
            return self.getToken(PLSRulesV2Parser.NEGACJA, 0)

        def wyrazenieBool(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.WyrazenieBoolContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieBoolContext,i)


        def LNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_OKRAGLY, 0)

        def PNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_OKRAGLY, 0)

        def wywolanieFunkcji(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WywolanieFunkcjiContext,0)


        def KONIUNKCJA(self):
            return self.getToken(PLSRulesV2Parser.KONIUNKCJA, 0)

        def ALTERNATYWA(self):
            return self.getToken(PLSRulesV2Parser.ALTERNATYWA, 0)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_wyrazenieBool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWyrazenieBool" ):
                return visitor.visitWyrazenieBool(self)
            else:
                return visitor.visitChildren(self)



    def wyrazenieBool(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PLSRulesV2Parser.WyrazenieBoolContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_wyrazenieBool, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 131
                self.wyrazenieString(0)
                self.state = 132
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self.wyrazenieString(0)
                pass

            elif la_ == 2:
                self.state = 135
                self.wyrazenieArytmetyczne(0)
                self.state = 136
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1007616) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 137
                self.wyrazenieArytmetyczne(0)
                pass

            elif la_ == 3:
                self.state = 139
                self.match(PLSRulesV2Parser.FALSZ)
                pass

            elif la_ == 4:
                self.state = 140
                self.match(PLSRulesV2Parser.PRAWDA)
                pass

            elif la_ == 5:
                self.state = 141
                self.match(PLSRulesV2Parser.ID)
                pass

            elif la_ == 6:
                self.state = 142
                self.match(PLSRulesV2Parser.NEGACJA)
                self.state = 143
                self.wyrazenieBool(3)
                pass

            elif la_ == 7:
                self.state = 144
                self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
                self.state = 145
                self.wyrazenieBool(0)
                self.state = 146
                self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
                pass

            elif la_ == 8:
                self.state = 148
                self.wywolanieFunkcji()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PLSRulesV2Parser.WyrazenieBoolContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenieBool)
                    self.state = 151
                    if not self.precpred(self._ctx, 9):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                    self.state = 152
                    _la = self._input.LA(1)
                    if not(_la==20 or _la==21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 153
                    self.wyrazenieBool(10) 
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class WyrazenieArytmetyczneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_OKRAGLY, 0)

        def wyrazenieArytmetyczne(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.WyrazenieArytmetyczneContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieArytmetyczneContext,i)


        def PNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_OKRAGLY, 0)

        def NUMERYCZNY(self):
            return self.getToken(PLSRulesV2Parser.NUMERYCZNY, 0)

        def ID(self):
            return self.getToken(PLSRulesV2Parser.ID, 0)

        def wywolanieFunkcji(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WywolanieFunkcjiContext,0)


        def MNOZENIE(self):
            return self.getToken(PLSRulesV2Parser.MNOZENIE, 0)

        def DZIELENIE(self):
            return self.getToken(PLSRulesV2Parser.DZIELENIE, 0)

        def MINUS(self):
            return self.getToken(PLSRulesV2Parser.MINUS, 0)

        def PLUS(self):
            return self.getToken(PLSRulesV2Parser.PLUS, 0)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_wyrazenieArytmetyczne

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWyrazenieArytmetyczne" ):
                return visitor.visitWyrazenieArytmetyczne(self)
            else:
                return visitor.visitChildren(self)



    def wyrazenieArytmetyczne(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PLSRulesV2Parser.WyrazenieArytmetyczneContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_wyrazenieArytmetyczne, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
                self.state = 161
                self.wyrazenieArytmetyczne(0)
                self.state = 162
                self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
                pass

            elif la_ == 2:
                self.state = 164
                self.match(PLSRulesV2Parser.NUMERYCZNY)
                pass

            elif la_ == 3:
                self.state = 165
                self.match(PLSRulesV2Parser.ID)
                pass

            elif la_ == 4:
                self.state = 166
                self.wywolanieFunkcji()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 175
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = PLSRulesV2Parser.WyrazenieArytmetyczneContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenieArytmetyczne)
                        self.state = 169
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 170
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 171
                        self.wyrazenieArytmetyczne(6)
                        pass

                    elif la_ == 2:
                        localctx = PLSRulesV2Parser.WyrazenieArytmetyczneContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenieArytmetyczne)
                        self.state = 172
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 173
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 174
                        self.wyrazenieArytmetyczne(5)
                        pass

             
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class WywolanieFunkcjiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PLSRulesV2Parser.ID, 0)

        def LNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_OKRAGLY, 0)

        def listaWartosci(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ListaWartosciContext,0)


        def PNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_OKRAGLY, 0)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_wywolanieFunkcji

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWywolanieFunkcji" ):
                return visitor.visitWywolanieFunkcji(self)
            else:
                return visitor.visitChildren(self)




    def wywolanieFunkcji(self):

        localctx = PLSRulesV2Parser.WywolanieFunkcjiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_wywolanieFunkcji)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(PLSRulesV2Parser.ID)
            self.state = 181
            self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
            self.state = 182
            self.listaWartosci(0)
            self.state = 183
            self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaWartosciContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wartosc(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WartoscContext,0)


        def listaWartosci(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ListaWartosciContext,0)


        def PRZECINEK(self):
            return self.getToken(PLSRulesV2Parser.PRZECINEK, 0)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_listaWartosci

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaWartosci" ):
                return visitor.visitListaWartosci(self)
            else:
                return visitor.visitChildren(self)



    def listaWartosci(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PLSRulesV2Parser.ListaWartosciContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_listaWartosci, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.wartosc()
            self._ctx.stop = self._input.LT(-1)
            self.state = 193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PLSRulesV2Parser.ListaWartosciContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listaWartosci)
                    self.state = 188
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 189
                    self.match(PLSRulesV2Parser.PRZECINEK)
                    self.state = 190
                    self.wartosc() 
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class WartoscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wyrazenieString(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieStringContext,0)


        def wyrazenieBool(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieBoolContext,0)


        def wyrazenieArytmetyczne(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieArytmetyczneContext,0)


        def ID(self):
            return self.getToken(PLSRulesV2Parser.ID, 0)

        def wywolanieFunkcji(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WywolanieFunkcjiContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_wartosc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWartosc" ):
                return visitor.visitWartosc(self)
            else:
                return visitor.visitChildren(self)




    def wartosc(self):

        localctx = PLSRulesV2Parser.WartoscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_wartosc)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.wyrazenieString(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.wyrazenieBool(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.wyrazenieArytmetyczne(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 199
                self.match(PLSRulesV2Parser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 200
                self.wywolanieFunkcji()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypWartosciContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PLSRulesV2Parser.INT, 0)

        def STRING(self):
            return self.getToken(PLSRulesV2Parser.STRING, 0)

        def BOOL(self):
            return self.getToken(PLSRulesV2Parser.BOOL, 0)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_typWartosci

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypWartosci" ):
                return visitor.visitTypWartosci(self)
            else:
                return visitor.visitChildren(self)




    def typWartosci(self):

        localctx = PLSRulesV2Parser.TypWartosciContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_typWartosci)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfInstrukcjaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PLSRulesV2Parser.IF, 0)

        def wyrazenieBool(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.WyrazenieBoolContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieBoolContext,i)


        def LNAWIAS_KLAMROWY(self, i:int=None):
            if i is None:
                return self.getTokens(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
            else:
                return self.getToken(PLSRulesV2Parser.LNAWIAS_KLAMROWY, i)

        def PNAWIAS_KLAMROWY(self, i:int=None):
            if i is None:
                return self.getTokens(PLSRulesV2Parser.PNAWIAS_KLAMROWY)
            else:
                return self.getToken(PLSRulesV2Parser.PNAWIAS_KLAMROWY, i)

        def instrukcja(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.InstrukcjaContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.InstrukcjaContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(PLSRulesV2Parser.ELIF)
            else:
                return self.getToken(PLSRulesV2Parser.ELIF, i)

        def ELSE(self):
            return self.getToken(PLSRulesV2Parser.ELSE, 0)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_ifInstrukcja

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfInstrukcja" ):
                return visitor.visitIfInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def ifInstrukcja(self):

        localctx = PLSRulesV2Parser.IfInstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ifInstrukcja)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(PLSRulesV2Parser.IF)
            self.state = 206
            self.wyrazenieBool(0)
            self.state = 207
            self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 324355988914176) != 0):
                self.state = 208
                self.instrukcja()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
            self.match(PLSRulesV2Parser.PNAWIAS_KLAMROWY)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 215
                self.match(PLSRulesV2Parser.ELIF)
                self.state = 216
                self.wyrazenieBool(0)
                self.state = 217
                self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 324355988914176) != 0):
                    self.state = 218
                    self.instrukcja()
                    self.state = 223
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 224
                self.match(PLSRulesV2Parser.PNAWIAS_KLAMROWY)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 231
                self.match(PLSRulesV2Parser.ELSE)
                self.state = 232
                self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 324355988914176) != 0):
                    self.state = 233
                    self.instrukcja()
                    self.state = 238
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 239
                self.match(PLSRulesV2Parser.PNAWIAS_KLAMROWY)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileInstrukcjaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(PLSRulesV2Parser.WHILE, 0)

        def wyrazenieBool(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieBoolContext,0)


        def LNAWIAS_KLAMROWY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_KLAMROWY, 0)

        def PNAWIAS_KLAMROWY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_KLAMROWY, 0)

        def instrukcja(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.InstrukcjaContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.InstrukcjaContext,i)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_whileInstrukcja

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileInstrukcja" ):
                return visitor.visitWhileInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def whileInstrukcja(self):

        localctx = PLSRulesV2Parser.WhileInstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_whileInstrukcja)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(PLSRulesV2Parser.WHILE)
            self.state = 243
            self.wyrazenieBool(0)
            self.state = 244
            self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 324355988914176) != 0):
                self.state = 245
                self.instrukcja()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
            self.match(PLSRulesV2Parser.PNAWIAS_KLAMROWY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInstrukcjaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(PLSRulesV2Parser.FOR, 0)

        def LNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_OKRAGLY, 0)

        def deklaracjaWartosci(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.DeklaracjaWartosciContext,0)


        def KONIEC_LINII(self, i:int=None):
            if i is None:
                return self.getTokens(PLSRulesV2Parser.KONIEC_LINII)
            else:
                return self.getToken(PLSRulesV2Parser.KONIEC_LINII, i)

        def wyrazenieBool(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieBoolContext,0)


        def wyrazenieArytmetyczne(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WyrazenieArytmetyczneContext,0)


        def PNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_OKRAGLY, 0)

        def LNAWIAS_KLAMROWY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_KLAMROWY, 0)

        def PNAWIAS_KLAMROWY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_KLAMROWY, 0)

        def instrukcja(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.InstrukcjaContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.InstrukcjaContext,i)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_forInstrukcja

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInstrukcja" ):
                return visitor.visitForInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def forInstrukcja(self):

        localctx = PLSRulesV2Parser.ForInstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_forInstrukcja)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(PLSRulesV2Parser.FOR)
            self.state = 254
            self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
            self.state = 255
            self.deklaracjaWartosci()
            self.state = 256
            self.match(PLSRulesV2Parser.KONIEC_LINII)
            self.state = 257
            self.wyrazenieBool(0)
            self.state = 258
            self.match(PLSRulesV2Parser.KONIEC_LINII)
            self.state = 259
            self.wyrazenieArytmetyczne(0)
            self.state = 260
            self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
            self.state = 261
            self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 324355988914176) != 0):
                self.state = 262
                self.instrukcja()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
            self.match(PLSRulesV2Parser.PNAWIAS_KLAMROWY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintInstrukcjaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(PLSRulesV2Parser.PRINT, 0)

        def LNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_OKRAGLY, 0)

        def wartosc(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WartoscContext,0)


        def PNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_OKRAGLY, 0)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_printInstrukcja

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintInstrukcja" ):
                return visitor.visitPrintInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def printInstrukcja(self):

        localctx = PLSRulesV2Parser.PrintInstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_printInstrukcja)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(PLSRulesV2Parser.PRINT)
            self.state = 271
            self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
            self.state = 272
            self.wartosc()
            self.state = 273
            self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.wyrazenieString_sempred
        self._predicates[11] = self.wyrazenieBool_sempred
        self._predicates[12] = self.wyrazenieArytmetyczne_sempred
        self._predicates[14] = self.listaWartosci_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def wyrazenieString_sempred(self, localctx:WyrazenieStringContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

    def wyrazenieBool_sempred(self, localctx:WyrazenieBoolContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

    def wyrazenieArytmetyczne_sempred(self, localctx:WyrazenieArytmetyczneContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

    def listaWartosci_sempred(self, localctx:ListaWartosciContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




