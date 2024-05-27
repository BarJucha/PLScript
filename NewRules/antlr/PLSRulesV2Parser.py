# Generated from ./PLSRulesV2.g4 by ANTLR 4.13.1
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
        4,1,49,283,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,1,1,1,2,1,2,1,2,3,2,61,8,2,1,3,1,3,1,3,1,3,3,3,67,8,3,1,
        4,1,4,1,4,1,4,3,4,73,8,4,1,5,1,5,1,5,1,5,3,5,79,8,5,1,5,1,5,1,5,
        5,5,84,8,5,10,5,12,5,87,9,5,1,5,3,5,90,8,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,6,5,6,100,8,6,10,6,12,6,103,9,6,1,7,1,7,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,
        124,8,10,1,10,1,10,1,10,5,10,129,8,10,10,10,12,10,132,9,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,153,8,11,1,11,1,11,1,11,5,11,158,8,
        11,10,11,12,11,161,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        3,12,171,8,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,179,8,12,10,12,
        12,12,182,9,12,1,13,1,13,1,13,1,13,3,13,188,8,13,1,13,1,13,1,14,
        1,14,1,14,5,14,195,8,14,10,14,12,14,198,9,14,1,14,1,14,1,15,1,15,
        1,15,1,15,1,15,3,15,207,8,15,1,16,1,16,1,17,1,17,3,17,213,8,17,1,
        18,1,18,1,18,1,18,5,18,219,8,18,10,18,12,18,222,9,18,1,18,3,18,225,
        8,18,1,18,1,18,3,18,229,8,18,1,19,1,19,1,19,5,19,234,8,19,10,19,
        12,19,237,9,19,1,19,3,19,240,8,19,1,19,1,19,1,20,1,20,1,20,1,20,
        5,20,248,8,20,10,20,12,20,251,9,20,1,20,3,20,254,8,20,1,20,1,20,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,268,8,21,
        10,21,12,21,271,9,21,1,21,3,21,274,8,21,1,21,1,21,1,22,1,22,1,22,
        1,22,1,22,1,22,1,196,3,20,22,24,23,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,0,7,3,0,29,30,34,34,48,49,1,0,13,
        14,2,0,13,14,16,19,1,0,20,21,1,0,3,4,1,0,1,2,1,0,40,42,305,0,49,
        1,0,0,0,2,54,1,0,0,0,4,60,1,0,0,0,6,66,1,0,0,0,8,72,1,0,0,0,10,74,
        1,0,0,0,12,93,1,0,0,0,14,104,1,0,0,0,16,109,1,0,0,0,18,113,1,0,0,
        0,20,123,1,0,0,0,22,152,1,0,0,0,24,170,1,0,0,0,26,183,1,0,0,0,28,
        196,1,0,0,0,30,206,1,0,0,0,32,208,1,0,0,0,34,210,1,0,0,0,36,214,
        1,0,0,0,38,230,1,0,0,0,40,243,1,0,0,0,42,257,1,0,0,0,44,277,1,0,
        0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,
        1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,
        55,3,4,2,0,55,56,5,38,0,0,56,3,1,0,0,0,57,61,3,6,3,0,58,61,3,10,
        5,0,59,61,3,26,13,0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,
        5,1,0,0,0,62,67,3,14,7,0,63,67,3,16,8,0,64,67,3,8,4,0,65,67,3,34,
        17,0,66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,
        7,1,0,0,0,68,73,3,36,18,0,69,73,3,40,20,0,70,73,3,42,21,0,71,73,
        3,44,22,0,72,68,1,0,0,0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,
        0,73,9,1,0,0,0,74,75,5,6,0,0,75,76,5,49,0,0,76,78,5,7,0,0,77,79,
        3,12,6,0,78,77,1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,0,80,81,5,8,0,0,
        81,85,5,9,0,0,82,84,3,6,3,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,
        0,0,0,85,86,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,88,90,3,34,17,0,
        89,88,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,5,10,0,0,92,11,1,
        0,0,0,93,94,3,32,16,0,94,101,5,49,0,0,95,96,5,43,0,0,96,97,3,32,
        16,0,97,98,5,49,0,0,98,100,1,0,0,0,99,95,1,0,0,0,100,103,1,0,0,0,
        101,99,1,0,0,0,101,102,1,0,0,0,102,13,1,0,0,0,103,101,1,0,0,0,104,
        105,3,32,16,0,105,106,5,49,0,0,106,107,5,15,0,0,107,108,3,30,15,
        0,108,15,1,0,0,0,109,110,5,49,0,0,110,111,5,15,0,0,111,112,3,30,
        15,0,112,17,1,0,0,0,113,114,7,0,0,0,114,19,1,0,0,0,115,116,6,10,
        -1,0,116,124,5,34,0,0,117,124,5,49,0,0,118,119,5,7,0,0,119,120,3,
        20,10,0,120,121,5,8,0,0,121,124,1,0,0,0,122,124,3,26,13,0,123,115,
        1,0,0,0,123,117,1,0,0,0,123,118,1,0,0,0,123,122,1,0,0,0,124,130,
        1,0,0,0,125,126,10,5,0,0,126,127,5,37,0,0,127,129,3,20,10,6,128,
        125,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,
        21,1,0,0,0,132,130,1,0,0,0,133,134,6,11,-1,0,134,135,3,20,10,0,135,
        136,7,1,0,0,136,137,3,20,10,0,137,153,1,0,0,0,138,139,3,24,12,0,
        139,140,7,2,0,0,140,141,3,24,12,0,141,153,1,0,0,0,142,153,5,30,0,
        0,143,153,5,29,0,0,144,153,5,49,0,0,145,146,5,22,0,0,146,153,3,22,
        11,3,147,148,5,7,0,0,148,149,3,22,11,0,149,150,5,8,0,0,150,153,1,
        0,0,0,151,153,3,26,13,0,152,133,1,0,0,0,152,138,1,0,0,0,152,142,
        1,0,0,0,152,143,1,0,0,0,152,144,1,0,0,0,152,145,1,0,0,0,152,147,
        1,0,0,0,152,151,1,0,0,0,153,159,1,0,0,0,154,155,10,9,0,0,155,156,
        7,3,0,0,156,158,3,22,11,10,157,154,1,0,0,0,158,161,1,0,0,0,159,157,
        1,0,0,0,159,160,1,0,0,0,160,23,1,0,0,0,161,159,1,0,0,0,162,163,6,
        12,-1,0,163,164,5,7,0,0,164,165,3,24,12,0,165,166,5,8,0,0,166,171,
        1,0,0,0,167,171,5,48,0,0,168,171,5,49,0,0,169,171,3,26,13,0,170,
        162,1,0,0,0,170,167,1,0,0,0,170,168,1,0,0,0,170,169,1,0,0,0,171,
        180,1,0,0,0,172,173,10,5,0,0,173,174,7,4,0,0,174,179,3,24,12,6,175,
        176,10,4,0,0,176,177,7,5,0,0,177,179,3,24,12,5,178,172,1,0,0,0,178,
        175,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,
        25,1,0,0,0,182,180,1,0,0,0,183,184,5,47,0,0,184,185,5,49,0,0,185,
        187,5,7,0,0,186,188,3,28,14,0,187,186,1,0,0,0,187,188,1,0,0,0,188,
        189,1,0,0,0,189,190,5,8,0,0,190,27,1,0,0,0,191,192,3,30,15,0,192,
        193,5,43,0,0,193,195,1,0,0,0,194,191,1,0,0,0,195,198,1,0,0,0,196,
        197,1,0,0,0,196,194,1,0,0,0,197,199,1,0,0,0,198,196,1,0,0,0,199,
        200,3,30,15,0,200,29,1,0,0,0,201,207,3,20,10,0,202,207,3,22,11,0,
        203,207,3,24,12,0,204,207,5,49,0,0,205,207,3,26,13,0,206,201,1,0,
        0,0,206,202,1,0,0,0,206,203,1,0,0,0,206,204,1,0,0,0,206,205,1,0,
        0,0,207,31,1,0,0,0,208,209,7,6,0,0,209,33,1,0,0,0,210,212,5,28,0,
        0,211,213,3,18,9,0,212,211,1,0,0,0,212,213,1,0,0,0,213,35,1,0,0,
        0,214,215,5,25,0,0,215,216,3,22,11,0,216,220,5,9,0,0,217,219,3,6,
        3,0,218,217,1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,
        0,0,221,224,1,0,0,0,222,220,1,0,0,0,223,225,3,34,17,0,224,223,1,
        0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,226,228,5,10,0,0,227,229,3,
        38,19,0,228,227,1,0,0,0,228,229,1,0,0,0,229,37,1,0,0,0,230,231,5,
        27,0,0,231,235,5,9,0,0,232,234,3,6,3,0,233,232,1,0,0,0,234,237,1,
        0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,239,1,0,0,0,237,235,1,
        0,0,0,238,240,3,34,17,0,239,238,1,0,0,0,239,240,1,0,0,0,240,241,
        1,0,0,0,241,242,5,10,0,0,242,39,1,0,0,0,243,244,5,23,0,0,244,245,
        3,22,11,0,245,249,5,9,0,0,246,248,3,6,3,0,247,246,1,0,0,0,248,251,
        1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,253,1,0,0,0,251,249,
        1,0,0,0,252,254,3,34,17,0,253,252,1,0,0,0,253,254,1,0,0,0,254,255,
        1,0,0,0,255,256,5,10,0,0,256,41,1,0,0,0,257,258,5,24,0,0,258,259,
        5,7,0,0,259,260,3,14,7,0,260,261,5,38,0,0,261,262,3,22,11,0,262,
        263,5,38,0,0,263,264,3,16,8,0,264,265,5,8,0,0,265,269,5,9,0,0,266,
        268,3,6,3,0,267,266,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,
        270,1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,272,274,3,34,17,0,273,
        272,1,0,0,0,273,274,1,0,0,0,274,275,1,0,0,0,275,276,5,10,0,0,276,
        43,1,0,0,0,277,278,5,45,0,0,278,279,5,7,0,0,279,280,3,30,15,0,280,
        281,5,8,0,0,281,45,1,0,0,0,28,49,60,66,72,78,85,89,101,123,130,152,
        159,170,178,180,187,196,206,212,220,224,228,235,239,249,253,269,
        273
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
                     "'KONIEC'", "'WYWOLAJ'" ]

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
                      "KONIEC", "WYWOLANIE", "NUMERYCZNY", "ID" ]

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
    RULE_returnInstrukcja = 17
    RULE_ifInstrukcja = 18
    RULE_elseInstrukcja = 19
    RULE_whileInstrukcja = 20
    RULE_forInstrukcja = 21
    RULE_printInstrukcja = 22

    ruleNames =  [ "program", "kod", "wyrazenie", "instrukcja", "instrukcjaZlozona", 
                   "deklaracjaFunkcji", "parametry", "deklaracjaWartosci", 
                   "przypisanieWartosci", "wyrazeniePodstawowe", "wyrazenieString", 
                   "wyrazenieBool", "wyrazenieArytmetyczne", "wywolanieFunkcji", 
                   "listaWartosci", "wartosc", "typWartosci", "returnInstrukcja", 
                   "ifInstrukcja", "elseInstrukcja", "whileInstrukcja", 
                   "forInstrukcja", "printInstrukcja" ]

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
    WYWOLANIE=47
    NUMERYCZNY=48
    ID=49

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
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 746568722415680) != 0):
                self.state = 46
                self.kod()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
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
            self.state = 54
            self.wyrazenie()
            self.state = 55
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


        def wywolanieFunkcji(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WywolanieFunkcjiContext,0)


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
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 25, 28, 40, 41, 42, 45, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.instrukcja()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.deklaracjaFunkcji()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.wywolanieFunkcji()
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


        def returnInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ReturnInstrukcjaContext,0)


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
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40, 41, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.deklaracjaWartosci()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.przypisanieWartosci()
                pass
            elif token in [23, 24, 25, 45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.instrukcjaZlozona()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.returnInstrukcja()
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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.ifInstrukcja()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.whileInstrukcja()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.forInstrukcja()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
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


        def returnInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ReturnInstrukcjaContext,0)


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
            self.state = 74
            self.match(PLSRulesV2Parser.FUNKCJA)
            self.state = 75
            self.match(PLSRulesV2Parser.ID)
            self.state = 76
            self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0):
                self.state = 77
                self.parametry()


            self.state = 80
            self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
            self.state = 81
            self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 82
                    self.instrukcja() 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 88
                self.returnInstrukcja()


            self.state = 91
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
            self.state = 93
            self.typWartosci()
            self.state = 94
            self.match(PLSRulesV2Parser.ID)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 95
                self.match(PLSRulesV2Parser.PRZECINEK)
                self.state = 96
                self.typWartosci()
                self.state = 97
                self.match(PLSRulesV2Parser.ID)
                self.state = 103
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

        def wartosc(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WartoscContext,0)


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
            self.state = 104
            self.typWartosci()
            self.state = 105
            self.match(PLSRulesV2Parser.ID)
            self.state = 106
            self.match(PLSRulesV2Parser.PODSTAW)
            self.state = 107
            self.wartosc()
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
            self.state = 109
            self.match(PLSRulesV2Parser.ID)
            self.state = 110
            self.match(PLSRulesV2Parser.PODSTAW)
            self.state = 111
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
            self.state = 113
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 844443720613888) != 0)):
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
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.state = 116
                self.match(PLSRulesV2Parser.NAPIS)
                pass
            elif token in [49]:
                self.state = 117
                self.match(PLSRulesV2Parser.ID)
                pass
            elif token in [7]:
                self.state = 118
                self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
                self.state = 119
                self.wyrazenieString(0)
                self.state = 120
                self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
                pass
            elif token in [47]:
                self.state = 122
                self.wywolanieFunkcji()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PLSRulesV2Parser.WyrazenieStringContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenieString)
                    self.state = 125
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 126
                    self.match(PLSRulesV2Parser.ZWIEKSZ)
                    self.state = 127
                    self.wyrazenieString(6) 
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 134
                self.wyrazenieString(0)
                self.state = 135
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 136
                self.wyrazenieString(0)
                pass

            elif la_ == 2:
                self.state = 138
                self.wyrazenieArytmetyczne(0)
                self.state = 139
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1007616) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 140
                self.wyrazenieArytmetyczne(0)
                pass

            elif la_ == 3:
                self.state = 142
                self.match(PLSRulesV2Parser.FALSZ)
                pass

            elif la_ == 4:
                self.state = 143
                self.match(PLSRulesV2Parser.PRAWDA)
                pass

            elif la_ == 5:
                self.state = 144
                self.match(PLSRulesV2Parser.ID)
                pass

            elif la_ == 6:
                self.state = 145
                self.match(PLSRulesV2Parser.NEGACJA)
                self.state = 146
                self.wyrazenieBool(3)
                pass

            elif la_ == 7:
                self.state = 147
                self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
                self.state = 148
                self.wyrazenieBool(0)
                self.state = 149
                self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
                pass

            elif la_ == 8:
                self.state = 151
                self.wywolanieFunkcji()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PLSRulesV2Parser.WyrazenieBoolContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenieBool)
                    self.state = 154
                    if not self.precpred(self._ctx, 9):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                    self.state = 155
                    _la = self._input.LA(1)
                    if not(_la==20 or _la==21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 156
                    self.wyrazenieBool(10) 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 163
                self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
                self.state = 164
                self.wyrazenieArytmetyczne(0)
                self.state = 165
                self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
                pass
            elif token in [48]:
                self.state = 167
                self.match(PLSRulesV2Parser.NUMERYCZNY)
                pass
            elif token in [49]:
                self.state = 168
                self.match(PLSRulesV2Parser.ID)
                pass
            elif token in [47]:
                self.state = 169
                self.wywolanieFunkcji()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 178
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = PLSRulesV2Parser.WyrazenieArytmetyczneContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenieArytmetyczne)
                        self.state = 172
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 173
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 174
                        self.wyrazenieArytmetyczne(6)
                        pass

                    elif la_ == 2:
                        localctx = PLSRulesV2Parser.WyrazenieArytmetyczneContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenieArytmetyczne)
                        self.state = 175
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 176
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 177
                        self.wyrazenieArytmetyczne(5)
                        pass

             
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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

        def WYWOLANIE(self):
            return self.getToken(PLSRulesV2Parser.WYWOLANIE, 0)

        def ID(self):
            return self.getToken(PLSRulesV2Parser.ID, 0)

        def LNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_OKRAGLY, 0)

        def PNAWIAS_OKRAGLY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_OKRAGLY, 0)

        def listaWartosci(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ListaWartosciContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(PLSRulesV2Parser.WYWOLANIE)
            self.state = 184
            self.match(PLSRulesV2Parser.ID)
            self.state = 185
            self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 985181213163648) != 0):
                self.state = 186
                self.listaWartosci()


            self.state = 189
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

        def wartosc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.WartoscContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.WartoscContext,i)


        def PRZECINEK(self, i:int=None):
            if i is None:
                return self.getTokens(PLSRulesV2Parser.PRZECINEK)
            else:
                return self.getToken(PLSRulesV2Parser.PRZECINEK, i)

        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_listaWartosci

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaWartosci" ):
                return visitor.visitListaWartosci(self)
            else:
                return visitor.visitChildren(self)




    def listaWartosci(self):

        localctx = PLSRulesV2Parser.ListaWartosciContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listaWartosci)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 191
                    self.wartosc()
                    self.state = 192
                    self.match(PLSRulesV2Parser.PRZECINEK) 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 199
            self.wartosc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.wyrazenieString(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.wyrazenieBool(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.wyrazenieArytmetyczne(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.match(PLSRulesV2Parser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
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
            self.state = 208
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


    class ReturnInstrukcjaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(PLSRulesV2Parser.RETURN, 0)

        def wyrazeniePodstawowe(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.WyrazeniePodstawoweContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_returnInstrukcja

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnInstrukcja" ):
                return visitor.visitReturnInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def returnInstrukcja(self):

        localctx = PLSRulesV2Parser.ReturnInstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returnInstrukcja)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(PLSRulesV2Parser.RETURN)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 211
                self.wyrazeniePodstawowe()


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


        def returnInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ReturnInstrukcjaContext,0)


        def elseInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ElseInstrukcjaContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_ifInstrukcja

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfInstrukcja" ):
                return visitor.visitIfInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def ifInstrukcja(self):

        localctx = PLSRulesV2Parser.IfInstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ifInstrukcja)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(PLSRulesV2Parser.IF)
            self.state = 215
            self.wyrazenieBool(0)
            self.state = 216
            self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 217
                    self.instrukcja() 
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 223
                self.returnInstrukcja()


            self.state = 226
            self.match(PLSRulesV2Parser.PNAWIAS_KLAMROWY)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 227
                self.elseInstrukcja()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseInstrukcjaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(PLSRulesV2Parser.ELSE, 0)

        def LNAWIAS_KLAMROWY(self):
            return self.getToken(PLSRulesV2Parser.LNAWIAS_KLAMROWY, 0)

        def PNAWIAS_KLAMROWY(self):
            return self.getToken(PLSRulesV2Parser.PNAWIAS_KLAMROWY, 0)

        def instrukcja(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSRulesV2Parser.InstrukcjaContext)
            else:
                return self.getTypedRuleContext(PLSRulesV2Parser.InstrukcjaContext,i)


        def returnInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ReturnInstrukcjaContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_elseInstrukcja

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseInstrukcja" ):
                return visitor.visitElseInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def elseInstrukcja(self):

        localctx = PLSRulesV2Parser.ElseInstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_elseInstrukcja)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(PLSRulesV2Parser.ELSE)
            self.state = 231
            self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 232
                    self.instrukcja() 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 238
                self.returnInstrukcja()


            self.state = 241
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


        def returnInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ReturnInstrukcjaContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_whileInstrukcja

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileInstrukcja" ):
                return visitor.visitWhileInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def whileInstrukcja(self):

        localctx = PLSRulesV2Parser.WhileInstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_whileInstrukcja)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(PLSRulesV2Parser.WHILE)
            self.state = 244
            self.wyrazenieBool(0)
            self.state = 245
            self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 246
                    self.instrukcja() 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 252
                self.returnInstrukcja()


            self.state = 255
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


        def przypisanieWartosci(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.PrzypisanieWartosciContext,0)


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


        def returnInstrukcja(self):
            return self.getTypedRuleContext(PLSRulesV2Parser.ReturnInstrukcjaContext,0)


        def getRuleIndex(self):
            return PLSRulesV2Parser.RULE_forInstrukcja

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInstrukcja" ):
                return visitor.visitForInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def forInstrukcja(self):

        localctx = PLSRulesV2Parser.ForInstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_forInstrukcja)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(PLSRulesV2Parser.FOR)
            self.state = 258
            self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
            self.state = 259
            self.deklaracjaWartosci()
            self.state = 260
            self.match(PLSRulesV2Parser.KONIEC_LINII)
            self.state = 261
            self.wyrazenieBool(0)
            self.state = 262
            self.match(PLSRulesV2Parser.KONIEC_LINII)
            self.state = 263
            self.przypisanieWartosci()
            self.state = 264
            self.match(PLSRulesV2Parser.PNAWIAS_OKRAGLY)
            self.state = 265
            self.match(PLSRulesV2Parser.LNAWIAS_KLAMROWY)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 266
                    self.instrukcja() 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 272
                self.returnInstrukcja()


            self.state = 275
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
        self.enterRule(localctx, 44, self.RULE_printInstrukcja)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(PLSRulesV2Parser.PRINT)
            self.state = 278
            self.match(PLSRulesV2Parser.LNAWIAS_OKRAGLY)
            self.state = 279
            self.wartosc()
            self.state = 280
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
         




