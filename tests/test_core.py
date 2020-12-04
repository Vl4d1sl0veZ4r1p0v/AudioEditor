import math

import numpy as np

from audioeditor import core


class Sinusoid:
    """Represents a sinusoidal signal."""

    def __init__(self, freq=440, amp=1.0, offset=0, func=np.sin):
        """Initializes a sinusoidal signal.
        freq: float frequency in Hz
        amp: float amplitude, 1.0 is nominal max
        offset: float phase offset in radians
        func: function that maps phase to amplitude
        """
        self.freq = freq
        self.amp = amp
        self.offset = offset
        self.func = func

    @property
    def period(self):
        """Period of the signal in seconds.
        returns: float seconds
        """
        return 1.0 / self.freq

    def evaluate(self, ts):
        """Evaluates the signal at the given times.
        ts: float array of times
        returns: float wave array
        """
        ts = np.asarray(ts)
        phases = math.pi * 2 * self.freq * ts + self.offset
        ys = self.amp * self.func(phases)
        return ys


def test_load_from_wav():
    filename = "patth to file"
    ys = Sinusoid().evaluate(np.linspace(0, 5, 5000))
    # save part
    audio = core.Audio()
    wave = audio.from_wav(filename)
    assert wave.audio_segment == ys


def test_load_from_mp3():
    assert False


def test_save_to_wav():
    assert False


def test_save_to_mp3():
    assert False


def test_rearrange_parts():
    assert False


def test_indexing():
    assert False


def test_slicing():
    assert False


def test_deletion():
    assert False


def test_insert_part():
    assert False


def test_change_the_volume_on_a_segment():
    assert False


def test_smooth_appearance():
    assert False


def test_smooth_fade_out():
    assert False
