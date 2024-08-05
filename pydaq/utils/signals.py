from PySide6.QtCore import QObject, Signal


class GuiSignals(QObject):
    returned = Signal(object)
