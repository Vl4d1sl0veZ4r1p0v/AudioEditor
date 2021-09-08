import pytest


def change_pitch_test():
    from audioeditor.change_pitch import Ui_Dialog as Change_Pitch_Dialog
    obj = Change_Pitch_Dialog()
    setupUi = getattr(obj, "setupUi", None)
    assert callable(setupUi)


if __name__ == "__main__":
    pass