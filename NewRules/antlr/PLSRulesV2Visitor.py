# Generated from .//PLSRulesV2.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from NewRules.antlr.PLSRulesV2Parser import PLSRulesV2Parser
else:
    from PLSRulesV2Parser import PLSRulesV2Parser

# This class defines a complete generic visitor for a parse tree produced by PLSRulesV2Parser.

class PLSRulesV2Visitor(ParseTreeVisitor):

    def __init__(self):
        self.variables = {}
        self.variablesTypes = {}
        self.functions = {}

    def checkVariableExistance(self, ctx):
        if self.variables.get(ctx.ID().getText(), None) is not None:
            return self.variables.get(ctx.ID().getText(), None)
        else:
            var_name = ctx.ID().getText()
            input_text = ctx.start.getInputStream().getText(ctx.start.start, ctx.stop.stop)
            highlighted_text = self.highlight_text(input_text, var_name)
            line = ctx.start.line
            raise KeyError(f"Zmienna {ctx.ID().getText()} nie jest zadeklarowana linia {line}: {highlighted_text}")
            # raise KeyError(f"Zmienna {ctx.ID().getText()} nie jest zadeklarowana")

    def checkVariableType(self, ctx, expectecType, podstawowyType=None):
        type = self.variablesTypes.get(ctx.ID().getText(), None)
        print(type)
        if type == expectecType:
            return True
        else:
            var_name = ctx.ID().getText()
            input_text = ctx.start.getInputStream().getText(ctx.start.start, ctx.stop.stop)
            highlighted_text = self.highlight_text(input_text, var_name)
            line = ctx.start.line
            raise TypeError(f"Nieoczekiwany typ {type}, oczekiwano {expectecType}, w lini {line}: {highlighted_text}")

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
    def visitDeklaracjaFunkcji(self, ctx: PLSRulesV2Parser.DeklaracjaFunkcjiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#parametry.
    def visitParametry(self, ctx: PLSRulesV2Parser.ParametryContext):
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
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            input_text = ctx.start.getInputStream().getText(ctx.start.start, ctx.stop.stop)
            highlighted_text = self.highlight_text(input_text, var_name)
            line = ctx.start.line
            raise KeyError(f"Zmienna {ctx.ID().getText()} nie jest zadeklarowana linia {line}: {highlighted_text}")

        value = self.visit(ctx.wartosc())
        self.variables[var_name] = value
        return value


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
            return self.checkVariableExistance(ctx)
        if ctx.NAPIS():
            return ctx.NAPIS().getText().strip('"')
        if ctx.ZWIEKSZ():
            left = self.visit(ctx.wyrazenieString(0))
            right = self.visit(ctx.wyrazenieString(1))
            result = left + right
            return result
        if ctx.wywolanieFunkcji():
            return self.visit(ctx.wywolanieFunkcji())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazenieBool.
    def visitWyrazenieBool(self, ctx:PLSRulesV2Parser.WyrazenieBoolContext):
        if ctx.ID():
            return self.variables.get(ctx.ID().getText(), None)
        if ctx.KONIUNKCJA():
            left = self.visit(ctx.wyrazenieBool(0))
            right = self.visit(ctx.wyrazenieBool(1))
            return left and right
        if ctx.ALTERNATYWA():
            left = self.visit(ctx.wyrazenieBool(0))
            right = self.visit(ctx.wyrazenieBool(1))
            return left or right
        if ctx.ROWNE():
            left = self.visit(ctx.wyrazenieString(0))
            right = self.visit(ctx.wyrazenieString(1))
            return left == right
        if ctx.ROZNE():
            left = self.visit(ctx.wyrazenieString(0))
            right = self.visit(ctx.wyrazenieString(1))
            return left != right
        if ctx.WIEKSZE():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left > right
        if ctx.MNIEJSZE():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left < right
        if ctx.WIEKSZE_ROWNE():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left >= right
        if ctx.MNIEJSZE_ROWNE():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left <= right
        if ctx.NEGACJA():
            result = self.visit(ctx.wyrazenieBool(0))
            return not result
        if ctx.LNAWIAS_OKRAGLY():
            return self.visit(ctx.wyrazenieBool(0))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSRulesV2Parser#wyrazenieArytmetyczne.
    def visitWyrazenieArytmetyczne(self, ctx:PLSRulesV2Parser.WyrazenieArytmetyczneContext):
        if ctx.ID():
            return self.checkVariableExistance(ctx)
        elif ctx.MNOZENIE():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left * right
        elif ctx.DZIELENIE():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            if(right == 0):
                raise ValueError(f"Linia {ctx.start.line}: dzielenie przez 0")
            return left / right
        elif ctx.PLUS():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left + right
        elif ctx.MINUS():
            left = self.visit(ctx.wyrazenieArytmetyczne(0))
            right = self.visit(ctx.wyrazenieArytmetyczne(1))
            return left - right
        elif ctx.LNAWIAS_OKRAGLY():
            return self.visit(ctx.wyrazenieArytmetyczne(0))
        elif ctx.NUMERYCZNY():
            return float(ctx.NUMERYCZNY().getText())
        else:
            return self.visitChildren(ctx)

    def highlight_text(self, text, word):
        return text.replace(word, f"-->{word}<--")

    # Visit a parse tree produced by PLSRulesV2Parser#wywolanieFunkcji.
    def visitWywolanieFunkcji(self, ctx: PLSRulesV2Parser.WywolanieFunkcjiContext):
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
    def visitIfInstrukcja(self, ctx: PLSRulesV2Parser.IfInstrukcjaContext):
        condition_result = self.visit(ctx.wyrazenieBool())

        if condition_result:
            for instruction_ctx in ctx.instrukcja():
                self.visit(instruction_ctx)
        else:
            if ctx.elseInstrukcja() is not None:
                for instruction_ctx in ctx.elseInstrukcja().instrukcja():
                    self.visit(instruction_ctx)
        return None


    # Visit a parse tree produced by PLSRulesV2Parser#whileInstrukcja.
    def visitWhileInstrukcja(self, ctx:PLSRulesV2Parser.WhileInstrukcjaContext):
        while_condition = self.visit(ctx.wyrazenieBool())

        while while_condition:
            for instruction_ctx in ctx.instrukcja():
                self.visit(instruction_ctx)
            while_condition = self.visit(ctx.wyrazenieBool())
        return None


    # Visit a parse tree produced by PLSRulesV2Parser#forInstrukcja.
    def visitForInstrukcja(self, ctx:PLSRulesV2Parser.ForInstrukcjaContext):
        self.visit(ctx.deklaracjaWartosci())
        for_condition = self.visit(ctx.wyrazenieBool())
        while for_condition:
            for instruction_ctx in ctx.instrukcja():
                self.visit(instruction_ctx)
            self.visit(ctx.przypisanieWartosci())
            for_condition = self.visit(ctx.wyrazenieBool())
        return None


    # Visit a parse tree produced by PLSRulesV2Parser#printInstrukcja.
    def visitPrintInstrukcja(self, ctx:PLSRulesV2Parser.PrintInstrukcjaContext):
        value = self.visit(ctx.wartosc())
        print(f"{value}")
        return value

del PLSRulesV2Parser