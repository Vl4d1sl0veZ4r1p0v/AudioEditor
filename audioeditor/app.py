import sys
from math import floor

import matplotlib
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QVBoxLayout, QWidget
)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure

from change_pitch import Ui_Dialog as Change_Pitch_Dialog
from core import Audio
from delete import Ui_Dialog as Delete_dialog
from main_window import Ui_MainWindow
from swap_dialog import Ui_Dialog as Swap_Dialog
from change_volume import Ui_Dialog as Change_Volume_Dialog
from change_speed import Ui_Dialog as Change_Speed_Dialog
from fade_in import Ui_Dialog as Fade_In_Dialog

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.coordinates = []
        self.audio = Audio()
        self.audio.from_wav("../tests/audios/test.wav")
        self.dense = 1e-100
        self.xdata = np.linspace(0, len(self.audio.audio_segment) / self.audio.rate,
                                 num=len(self.audio.audio_segment * self.dense))
        self.ydata = self.audio.audio_segment
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
        self.connect_signals_slots()

    def update_plot(self):
        self.ydata = self.audio.audio_segment
        self.xdata = np.linspace(0, len(self.audio.audio_segment) / self.audio.rate,
                                 num=len(self.audio.audio_segment * self.dense))
        if self._plot_ref is None:
            plot_refs = self.canvas.axes.plot(self.xdata, self.ydata, 'b')
            self._plot_ref = plot_refs[0]
        else:
            self._plot_ref.set_ydata(self.ydata)
        self.canvas.draw()

    def connect_signals_slots(self):
        self.action_Exit.triggered.connect(self.close)
        self.action_About.triggered.connect(self.about)
        self.actionS_wap.triggered.connect(self.swap)
        self.action_Delete.triggered.connect(self.delete)
        self.actionChange_Pitc_h.triggered.connect(self.change_pitch)
        self.actionChange_Volume.triggered.connect(self.change_volume)
        self.actionChange_S_peed.triggered.connect(self.change_speed)
        self.actionFade_In.triggered.connect(self.fade_in)
        self.actionFade_Out.triggered.connect(self.fade_out)

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

    def onclick_swap(self, event):
        self.coordinates.append(event.xdata)
        self.canvas.axes.axvline(x=event.xdata, c='r')
        if len(self.coordinates) == 4:
            dialog = Swap(self)
            dialog.exec()
            self.coordinates = []
            self.canvas.mpl_disconnect(self.swap_canvas_onclick)
            self.canvas.axes.clear()
            self._plot_ref = None
        self.update_plot()

    def swap(self):
        self.swap_canvas_onclick = self.canvas.mpl_connect('button_press_event', self.onclick_swap)

    def onclick_delete(self, event):
        self.coordinates.append(event.xdata)
        self.canvas.axes.axvline(x=event.xdata, c='r')
        if len(self.coordinates) == 2:
            dialog = Delete(self)
            dialog.exec()
            self.coordinates = []
            self.canvas.mpl_disconnect(self.delete_canvas_onclick)
            self.canvas.axes.clear()
            self._plot_ref = None
        self.update_plot()

    def delete(self):
        self.delete_canvas_onclick = self.canvas.mpl_connect('button_press_event', self.onclick_delete)

    def change_pitch(self):
        dialog = ChangePitch(self)
        dialog.exec()
        value = dialog.spinBox.value()
        self.audio = self.audio.change_pitch(value)

    def change_volume(self):
        dialog = ChangeVolume(self)
        dialog.exec()
        value = dialog.doubleSpinBox.value()
        self.audio.change_volume(value)
        self._plot_ref = None
        self.update_plot()

    def change_speed(self):
        dialog = ChangeSpeed(self)
        dialog.exec()
        value = dialog.doubleSpinBox.value()
        self.audio.change_speed(value)

    def onclick_fade_in(self, event):
        self.coordinates.append(event.xdata)
        self.canvas.axes.axvline(x=event.xdata, c='r')
        if len(self.coordinates) == 1:
            dialog = FadeIn(self)
            dialog.exec()
            self.coordinates = []
            self.canvas.mpl_disconnect(self.fade_in_onclick)
            self.canvas.axes.clear()
            self._plot_ref = None
        self.update_plot()

    def fade_in(self):
        self.fade_in_onclick = self.canvas.mpl_connect('button_press_event', self.onclick_fade_in)

    def onclick_fade_out(self, event):
        self.coordinates.append(event.xdata)
        self.canvas.axes.axvline(x=event.xdata, c='r')
        if len(self.coordinates) == 1:
            dialog = FadeOut(self)
            dialog.exec()
            self.coordinates = []
            self.canvas.mpl_disconnect(self.fade_out_onclick)
            self.canvas.axes.clear()
            self._plot_ref = None
        self.update_plot()

    def fade_out(self):
        self.fade_out_onclick = self.canvas.mpl_connect('button_press_event', self.onclick_fade_out)


class Swap(QDialog, Swap_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.label_3.setText(str(parent.coordinates[0]))
        self.label_4.setText(str(parent.coordinates[1]))
        self.label_6.setText(str(parent.coordinates[2]))
        self.label_8.setText(str(parent.coordinates[3]))
        self.buttonBox.accepted.connect(self.apply)

    def apply(self):
        self.parent.audio.swap(
            floor(self.parent.audio.rate * self.parent.coordinates[0]),
            floor(self.parent.audio.rate * self.parent.coordinates[1]),
            floor(self.parent.audio.rate * self.parent.coordinates[2]),
            floor(self.parent.audio.rate * self.parent.coordinates[3])
        )
        self.parent.update_plot()


class Delete(QDialog, Delete_dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.label_2.setText(str(parent.coordinates[0]))
        self.label_4.setText(str(parent.coordinates[1]))
        self.buttonBox.accepted.connect(self.apply)

    def apply(self):
        self.parent.audio.delete(
            floor(self.parent.audio.rate * self.parent.coordinates[0]),
            floor(self.parent.audio.rate * self.parent.coordinates[1]),
        )
        self.parent.update_plot()


class ChangePitch(QDialog, Change_Pitch_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent


class ChangeVolume(QDialog, Change_Volume_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.buttonBox.accepted.connect(self.apply)

    def apply(self):
        self.parent.update_plot()


class ChangeSpeed(QDialog, Change_Speed_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class FadeIn(QDialog, Fade_In_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.label_6.setText(str(parent.coordinates[0]))
        self.buttonBox.accepted.connect(self.apply)

    def apply(self):
        self.parent.audio = self.parent.audio.get_fade_in(
            floor(1000 * self.parent.coordinates[0])
        )
        self.parent.update_plot()


class FadeOut(QDialog, Fade_In_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.label_6.setText(str(parent.coordinates[0]))
        self.buttonBox.accepted.connect(self.apply)

    def apply(self):
        self.parent.audio = self.parent.audio.get_fade_out(
            floor(1000 * self.parent.coordinates[0])
        )
        self.parent.update_plot()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
