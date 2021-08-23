import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QVBoxLayout, QWidget,
    QLabel
)
# from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure

from main_window import Ui_MainWindow
from swap_dialog import Ui_Dialog
from core import Audio

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def onclick(event):
    print(event.xdata, event.ydata)


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        audio = Audio()
        audio.from_wav("../tests/audios/test.wav")
        self.dense = 1e-100
        self.xdata = np.linspace(0, len(audio.audio_segment) / audio.rate, num=len(audio.audio_segment * self.dense))
        self.ydata = audio.audio_segment
        self._plot_ref = None
        self.update_plot()

        toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()
        self.connectSignalsSlots()

    def update_plot(self):
        if self._plot_ref is None:
            plot_refs = self.canvas.axes.plot(self.xdata, self.ydata, 'b')
            self._plot_ref = plot_refs[0]
        else:
            self._plot_ref.set_ydata(self.ydata)
        self.canvas.draw()

    def connectSignalsSlots(self):
        self.action_Exit.triggered.connect(self.close)
        self.action_About.triggered.connect(self.about)
        self.actionS_wap.triggered.connect(self.swap)
        self.cid = self.canvas.mpl_connect('button_press_event', onclick)

    def about(self):
        QMessageBox.about(
            self,
            "About AudioEditor",
            """<p>A simple audio editor app built with:</p>
            <p>- PyQt</p>
            <p>- Qt Designer</p>
            <p>- PyDub</p>
            <p>- Matplotlib</p>"""
        )

    def swap(self):

        dialog = Swap(self)
        dialog.exec()


class Swap(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.label_3.setText("label 3")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
