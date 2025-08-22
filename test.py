import qdarktheme
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toggle Light/Dark with qdarktheme")

        self.button = QPushButton("Alternar Tema")
        self.button.clicked.connect(self.toggle_theme)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

        self.current_theme = "light"  # começa claro
        qdarktheme.setup_theme(self.current_theme)

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        qdarktheme.setup_theme(self.current_theme)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
