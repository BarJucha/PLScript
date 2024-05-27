from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QPainter, QColor, QTextFormat, QFont
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton, QMainWindow, QApplication, QHBoxLayout, \
    QLineEdit, QMessageBox, QPlainTextEdit
import subprocess
import sys

line_size = 16

class QLineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor
        self.setFont(QFont("Courier New", line_size))

    def sizeHint(self):
        return QSize(self.codeEditor.lineNumberAreaWidth(), 0)


    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event)


class QCodeEditor(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineNumberArea = QLineNumberArea(self)
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.updateLineNumberAreaWidth(0)

    def lineNumberAreaWidth(self):
        digits = 1
        max_value = max(1, self.blockCount())
        while max_value >= 10:
            max_value /= 10
            digits += 1
        space = 3 + self.fontMetrics().width('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def highlightCurrentLine(self):
        extraSelections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            lineColor = QColor("#4d4f51")
            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)

        painter.fillRect(event.rect(), Qt.lightGray)

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        # Just to make sure I use the right font
        height = self.fontMetrics().height()
        while block.isValid() and (top <= event.rect().bottom()):
            if block.isVisible() and (bottom >= event.rect().top()):
                number = str(blockNumber + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.lineNumberArea.width(), height, Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1

class PLScriptApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PLScript")
        self.resize(1600, 1200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.code_editor = QCodeEditor()
        self.code_editor.setStyleSheet("QCodeEditor { background-color: #323232; color: #fff; }")
        self.code_editor.setFont(QFont("Courier New", line_size))
        self.layout.addWidget(self.code_editor)


        button_layout = QHBoxLayout()
        self.execute_button = QPushButton("Wykonaj kod")
        self.execute_button.clicked.connect(self.execute_code)
        button_layout.addWidget(self.execute_button)

        self.save_button = QPushButton("Zapisz")
        self.save_button.clicked.connect(self.save_code)
        button_layout.addWidget(self.save_button)

        self.open_button = QPushButton("Wczytaj")
        self.open_button.clicked.connect(self.open_code)
        button_layout.addWidget(self.open_button)

        self.filename_input = QLineEdit()
        button_layout.addWidget(self.filename_input)

        self.layout.addLayout(button_layout)

        self.terminal_output = QTextEdit()
        self.terminal_output.setFont(QFont("Courier New", line_size))
        self.terminal_output.setStyleSheet("QTextEdit { background-color: black; color: #fff; }")
        self.terminal_output.setReadOnly(True)
        self.layout.addWidget(self.terminal_output)

        self.code_editor.setLineWrapMode(QPlainTextEdit.WidgetWidth)

    def execute_code(self):
        user_input = self.code_editor.toPlainText()

        with open("plsCode.txt", 'w') as f:
            f.write(user_input)

        result = subprocess.run("python Driverv2.py", shell=True, capture_output=True, text=True)

        self.terminal_output.setPlainText(f"${result.stdout}{result.stderr}")

    def save_code(self):
        user_input = self.code_editor.toPlainText()
        filename = self.filename_input.text().strip()

        if filename:
            with open(f"{filename}.txt", 'w') as f:
                f.write(user_input)

    def open_code(self):
        filename = self.filename_input.text().strip()

        if filename:
            try:
                with open(f"{filename}.txt", 'r') as f:
                    file_content = f.read()
                self.code_editor.setPlainText(file_content)
            except FileNotFoundError:
                QMessageBox.critical(self, "Błąd", f"Plik {filename} nie istnieje")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PLScriptApp()
    window.show()
    sys.exit(app.exec_())