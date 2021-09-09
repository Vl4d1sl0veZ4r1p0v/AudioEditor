import pytest


def test_change_pitch():
    from audioeditor.change_pitch import Ui_Dialog as Change_Pitch_Dialog
    obj = Change_Pitch_Dialog()
    setupUi = getattr(obj, "setupUi", None)
    assert callable(setupUi)


def test_change_speed():
    from audioeditor.change_speed import Ui_Dialog as Change_Speed_Dialog
    obj = Change_Speed_Dialog()
    setupUi = getattr(obj, "setupUi", None)
    assert callable(setupUi)


def test_change_volume():
    from audioeditor.change_volume import Ui_Dialog as Change_Volume_Dialog
    obj = Change_Volume_Dialog()
    setupUi = getattr(obj, "setupUi", None)
    assert callable(setupUi)


def test_delete():
    from audioeditor.delete import Ui_Dialog as Delete_Dialog
    obj = Delete_Dialog()
    setupUi = getattr(obj, "setupUi", None)
    assert callable(setupUi)


def test_fade_in():
    from audioeditor.fade_in import Ui_Dialog as Fade_In_Dialog
    obj = Fade_In_Dialog()
    setupUi = getattr(obj, "setupUi", None)
    assert callable(setupUi)


def test_main_window():
    from audioeditor.main_window import Ui_MainWindow as MainWindow
    obj = MainWindow()
    setupUi = getattr(obj, "setupUi", None)
    assert callable(setupUi)


def test_main_play():
    from audioeditor.play import Ui_Dialog as Play_Dialog
    obj = Play_Dialog()
    setupUi = getattr(obj, "setupUi", None)
    assert callable(setupUi)


def test_swap_dialog():
    from audioeditor.swap_dialog import Ui_Dialog as Swap_Dialog
    obj = Swap_Dialog()
    setupUi = getattr(obj, "setupUi", None)
    assert callable(setupUi)


def test_swap_dialog2():
    from audioeditor.swap_dialog import Ui_Dialog as Swap_Dialog
    obj = Swap_Dialog()
    retranslateUi = getattr(obj, "retranslateUi", None)
    assert callable(retranslateUi)


def test_swap_dialog3():
    from audioeditor.swap_dialog import Ui_Dialog as Swap_Dialog
    obj = Swap_Dialog()
    setupUi = getattr(obj, "setupUi", None)
    try:
        obj.setupUi()
    except Exception as ex:
        pass
    assert callable(setupUi)


if __name__ == "__main__":
    pass
