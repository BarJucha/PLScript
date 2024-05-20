# Generated from .//PLSRulesV2.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PLSRulesV2Parser import PLSRulesV2Parser
else:
    from PLSRulesV2Parser import PLSRulesV2Parser

# This class defines a complete generic visitor for a parse tree produced by PLSRulesV2Parser.

class PLSRulesV2Visitor(ParseTreeVisitor):

    def __init__(self):
        self.variables = {}
        self.variablesTypes = {}
        self.functions = {}

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
        var_type = ctx.typWartosci().getText()
        var_name = ctx.ID().getText()
        value = self.visit(ctx.wyrazeniePodstawowe())
        self.variables[var_name] = value
        self.variablesTypes[var_type] = var_type
        return value


    # Visit a parse tree produced by PLSRulesV2Parser#przypisanieWartosci.
    def visitPrzypisanieWartosci(self, ctx:PLSRulesV2Parser.PrzypisanieWartosciContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazeniePodstawowe.
    def visitWyrazeniePodstawowe(self, ctx:PLSRulesV2Parser.WyrazeniePodstawoweContext):
        if ctx.NUMERYCZNY():
            return float(ctx.NUMERYCZNY().getText())
        elif ctx.ID():
            return self.variables.get(ctx.ID().getText(), None)
        elif ctx.NAPIS():
            return ctx.NAPIS().getText().strip('"')
        elif ctx.PRAWDA():
            return True
        elif ctx.FALSZ():
            return False
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazenieString.
    def visitWyrazenieString(self, ctx:PLSRulesV2Parser.WyrazenieStringContext):
        if ctx.ID():
            return self.variables.get(ctx.ID().getText(), None)
        if ctx.NAPIS():
            return ctx.NAPIS().getText().strip('"')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazenieBool.
    def visitWyrazenieBool(self, ctx:PLSRulesV2Parser.WyrazenieBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazenieArytmetyczne.
    def visitWyrazenieArytmetyczne(self, ctx:PLSRulesV2Parser.WyrazenieArytmetyczneContext):
        if ctx.NUMERYCZNY():
            return float(ctx.NUMERYCZNY().getText())
        elif ctx.ID():
            if self.variables.get(ctx.ID().getText(), None) is not None:
                return self.variables.get(ctx.ID().getText(), None)
            else:
                raise KeyError(f"Zmienna {ctx.ID().getText()} nie jest zadeklarowana")
        elif ctx.MNOZENIE():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left * right
        elif ctx.DZIELENIE():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left / right
        elif ctx.PLUS():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left + right
        elif ctx.MINUS():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left - right
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wywolanieFunkcji.
    def visitWywolanieFunkcji(self, ctx:PLSRulesV2Parser.WywolanieFunkcjiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#listaWartosci.
    def visitListaWartosci(self, ctx:PLSRulesV2Parser.ListaWartosciContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wartosc.
    def visitWartosc(self, ctx:PLSRulesV2Parser.WartoscContext):
        if ctx.ID():
            return self.variables.get(ctx.ID().getText(), None)
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
        value = self.visit(ctx.wartosc())
        print(f"{value}")
        return value



del PLSRulesV2Parser