# Generated from PLSRules.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PLSRulesParser import PLSRulesParser
else:
    from PLSRulesParser import PLSRulesParser

# This class defines a complete listener for a parse tree produced by PLSRulesParser.
class PLSRulesListener(ParseTreeListener):

    # Enter a parse tree produced by PLSRulesParser#program.
    def enterProgram(self, ctx:PLSRulesParser.ProgramContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#program.
    def exitProgram(self, ctx:PLSRulesParser.ProgramContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#kod.
    def enterKod(self, ctx:PLSRulesParser.KodContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#kod.
    def exitKod(self, ctx:PLSRulesParser.KodContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#typWartosci.
    def enterTypWartosci(self, ctx:PLSRulesParser.TypWartosciContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#typWartosci.
    def exitTypWartosci(self, ctx:PLSRulesParser.TypWartosciContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#deklaracjaWartosci.
    def enterDeklaracjaWartosci(self, ctx:PLSRulesParser.DeklaracjaWartosciContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#deklaracjaWartosci.
    def exitDeklaracjaWartosci(self, ctx:PLSRulesParser.DeklaracjaWartosciContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#przypisanieWartosci.
    def enterPrzypisanieWartosci(self, ctx:PLSRulesParser.PrzypisanieWartosciContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#przypisanieWartosci.
    def exitPrzypisanieWartosci(self, ctx:PLSRulesParser.PrzypisanieWartosciContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#deklaracjaFunkcji.
    def enterDeklaracjaFunkcji(self, ctx:PLSRulesParser.DeklaracjaFunkcjiContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#deklaracjaFunkcji.
    def exitDeklaracjaFunkcji(self, ctx:PLSRulesParser.DeklaracjaFunkcjiContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wywolanieFunkcji.
    def enterWywolanieFunkcji(self, ctx:PLSRulesParser.WywolanieFunkcjiContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wywolanieFunkcji.
    def exitWywolanieFunkcji(self, ctx:PLSRulesParser.WywolanieFunkcjiContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wyrazenie.
    def enterWyrazenie(self, ctx:PLSRulesParser.WyrazenieContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wyrazenie.
    def exitWyrazenie(self, ctx:PLSRulesParser.WyrazenieContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wartosc.
    def enterWartosc(self, ctx:PLSRulesParser.WartoscContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wartosc.
    def exitWartosc(self, ctx:PLSRulesParser.WartoscContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wyrazenieString.
    def enterWyrazenieString(self, ctx:PLSRulesParser.WyrazenieStringContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wyrazenieString.
    def exitWyrazenieString(self, ctx:PLSRulesParser.WyrazenieStringContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wyrazenieBool.
    def enterWyrazenieBool(self, ctx:PLSRulesParser.WyrazenieBoolContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wyrazenieBool.
    def exitWyrazenieBool(self, ctx:PLSRulesParser.WyrazenieBoolContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wyrazenieArytmetyczne.
    def enterWyrazenieArytmetyczne(self, ctx:PLSRulesParser.WyrazenieArytmetyczneContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wyrazenieArytmetyczne.
    def exitWyrazenieArytmetyczne(self, ctx:PLSRulesParser.WyrazenieArytmetyczneContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wyrazenieDrukowania.
    def enterWyrazenieDrukowania(self, ctx:PLSRulesParser.WyrazenieDrukowaniaContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wyrazenieDrukowania.
    def exitWyrazenieDrukowania(self, ctx:PLSRulesParser.WyrazenieDrukowaniaContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wyrazenieFor.
    def enterWyrazenieFor(self, ctx:PLSRulesParser.WyrazenieForContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wyrazenieFor.
    def exitWyrazenieFor(self, ctx:PLSRulesParser.WyrazenieForContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wyrazenieWhile.
    def enterWyrazenieWhile(self, ctx:PLSRulesParser.WyrazenieWhileContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wyrazenieWhile.
    def exitWyrazenieWhile(self, ctx:PLSRulesParser.WyrazenieWhileContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wyrazenieWarunkowe.
    def enterWyrazenieWarunkowe(self, ctx:PLSRulesParser.WyrazenieWarunkoweContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wyrazenieWarunkowe.
    def exitWyrazenieWarunkowe(self, ctx:PLSRulesParser.WyrazenieWarunkoweContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wyrazenieElif.
    def enterWyrazenieElif(self, ctx:PLSRulesParser.WyrazenieElifContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wyrazenieElif.
    def exitWyrazenieElif(self, ctx:PLSRulesParser.WyrazenieElifContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wyrazenieElse.
    def enterWyrazenieElse(self, ctx:PLSRulesParser.WyrazenieElseContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wyrazenieElse.
    def exitWyrazenieElse(self, ctx:PLSRulesParser.WyrazenieElseContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#listaArgumentow.
    def enterListaArgumentow(self, ctx:PLSRulesParser.ListaArgumentowContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#listaArgumentow.
    def exitListaArgumentow(self, ctx:PLSRulesParser.ListaArgumentowContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wszystkieArgumenty.
    def enterWszystkieArgumenty(self, ctx:PLSRulesParser.WszystkieArgumentyContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wszystkieArgumenty.
    def exitWszystkieArgumenty(self, ctx:PLSRulesParser.WszystkieArgumentyContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#petla.
    def enterPetla(self, ctx:PLSRulesParser.PetlaContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#petla.
    def exitPetla(self, ctx:PLSRulesParser.PetlaContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#listaWartosci.
    def enterListaWartosci(self, ctx:PLSRulesParser.ListaWartosciContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#listaWartosci.
    def exitListaWartosci(self, ctx:PLSRulesParser.ListaWartosciContext):
        pass


    # Enter a parse tree produced by PLSRulesParser#wszystkieWartosci.
    def enterWszystkieWartosci(self, ctx:PLSRulesParser.WszystkieWartosciContext):
        pass

    # Exit a parse tree produced by PLSRulesParser#wszystkieWartosci.
    def exitWszystkieWartosci(self, ctx:PLSRulesParser.WszystkieWartosciContext):
        pass



del PLSRulesParser