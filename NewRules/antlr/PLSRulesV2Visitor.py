# Generated from .//PLSRulesV2.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PLSRulesV2Parser import PLSRulesV2Parser
else:
    from PLSRulesV2Parser import PLSRulesV2Parser

# This class defines a complete generic visitor for a parse tree produced by PLSRulesV2Parser.

class PLSRulesV2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLSRulesV2Parser#program.
    def visitProgram(self, ctx:PLSRulesV2Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#kod.
    def visitKod(self, ctx:PLSRulesV2Parser.KodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazenie.
    def visitWyrazenie(self, ctx:PLSRulesV2Parser.WyrazenieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#instrukcja.
    def visitInstrukcja(self, ctx:PLSRulesV2Parser.InstrukcjaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#instrukcjaZlozona.
    def visitInstrukcjaZlozona(self, ctx:PLSRulesV2Parser.InstrukcjaZlozonaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#deklaracjaFunkcji.
    def visitDeklaracjaFunkcji(self, ctx:PLSRulesV2Parser.DeklaracjaFunkcjiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#parametry.
    def visitParametry(self, ctx:PLSRulesV2Parser.ParametryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#deklaracjaWartosci.
    def visitDeklaracjaWartosci(self, ctx:PLSRulesV2Parser.DeklaracjaWartosciContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#przypisanieWartosci.
    def visitPrzypisanieWartosci(self, ctx:PLSRulesV2Parser.PrzypisanieWartosciContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazeniePodstawowe.
    def visitWyrazeniePodstawowe(self, ctx:PLSRulesV2Parser.WyrazeniePodstawoweContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazenieString.
    def visitWyrazenieString(self, ctx:PLSRulesV2Parser.WyrazenieStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazenieBool.
    def visitWyrazenieBool(self, ctx:PLSRulesV2Parser.WyrazenieBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazenieArytmetyczne.
    def visitWyrazenieArytmetyczne(self, ctx:PLSRulesV2Parser.WyrazenieArytmetyczneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wywolanieFunkcji.
    def visitWywolanieFunkcji(self, ctx:PLSRulesV2Parser.WywolanieFunkcjiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#listaWartosci.
    def visitListaWartosci(self, ctx:PLSRulesV2Parser.ListaWartosciContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wartosc.
    def visitWartosc(self, ctx:PLSRulesV2Parser.WartoscContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#typWartosci.
    def visitTypWartosci(self, ctx:PLSRulesV2Parser.TypWartosciContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#ifInstrukcja.
    def visitIfInstrukcja(self, ctx:PLSRulesV2Parser.IfInstrukcjaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#whileInstrukcja.
    def visitWhileInstrukcja(self, ctx:PLSRulesV2Parser.WhileInstrukcjaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#forInstrukcja.
    def visitForInstrukcja(self, ctx:PLSRulesV2Parser.ForInstrukcjaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#printInstrukcja.
    def visitPrintInstrukcja(self, ctx:PLSRulesV2Parser.PrintInstrukcjaContext):
        return self.visitChildren(ctx)



del PLSRulesV2Parser