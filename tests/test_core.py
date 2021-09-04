import pytest
from math import sin, cos, pi
import numpy as np
from audioeditor.core import Audio

basic_filename = "tests/audios/test.wav"
expected_audio = Audio()
current_audio = Audio()


def test_concatenation():
    current_audio.from_wav(basic_filename)
    current_audio_concatenated = current_audio + current_audio
    expected_file_name = "tests/audios/test_concatenated.wav"
    expected_audio.from_wav(expected_file_name)
    assert np.array_equal(expected_audio.audio_segment,
                          current_audio_concatenated.audio_segment)


def test_rearrange_parts():
    current_audio.from_wav(basic_filename)
    length = len(current_audio.audio_segment)
    current_audio.swap(0, length // 2, length // 2, length)

    expected_file_name = "tests/audios/test_swap.wav"
    expected_audio.from_wav(expected_file_name)
    assert np.array_equal(expected_audio.audio_segment,
                          current_audio.audio_segment)


def test_indexing():
    current_audio.from_wav(basic_filename)

    reversed_segment = np.array(current_audio.audio_segment)
    for i in range(0, len(current_audio.audio_segment)):
        reversed_segment[i] = current_audio.at(-i)
    current_audio.audio_segment = reversed_segment

    expected_file_name = "tests/audios/test_reversed.wav"
    expected_audio.from_wav(expected_file_name)
    assert np.array_equal(expected_audio.audio_segment,
                          current_audio.audio_segment)


def test_slicing():
    current_audio.from_wav(basic_filename)

    current_audio.audio_segment = current_audio.get_slice(
        0,
        len(current_audio.audio_segment) // 2)
    expected_file_name = "tests/audios/test_split.wav"
    expected_audio.from_wav(expected_file_name)
    assert np.array_equal(expected_audio.audio_segment,
                          current_audio.audio_segment)


def test_deletion():
    current_audio.from_wav(basic_filename)
    current_audio.delete(0, len(current_audio.audio_segment) // 2)
    expected_file_name = "tests/audios/test_deleted.wav"
    expected_audio.from_wav(expected_file_name)
    assert np.array_equal(expected_audio.audio_segment,
                          current_audio.audio_segment)


def test_change_the_volume():
    current_audio.from_wav(basic_filename)
    current_audio.change_volume(10)
    expected_file_name = "tests/audios/test_changed_volume.wav"
    expected_audio.from_wav(expected_file_name)
    assert np.array_equal(expected_audio.audio_segment,
                          current_audio.audio_segment)


def test_change_speed():
    current_audio.from_wav(basic_filename)
    current_audio.change_speed(0.75)
    expected_file_name = "tests/audios/test_changed_speed.wav"
    expected_audio.from_wav(expected_file_name)
    assert expected_audio.rate == current_audio.rate


def test_intersect():
    assert Audio.is_intersect(1, 5, 2, 10)


def test_not_intersect():
    assert Audio.is_intersect(1, 5, 6, 10) is False


def test_at():
    tmp = Audio()
    tmp.audio_segment = np.arange(10)
    assert tmp.at(0) == 0


def test_get_slice():
    tmp = Audio()
    tmp.audio_segment = np.arange(10)
    result = tmp.get_slice(0, 3)
    assert (result-np.arange(3)).all


def test_delete():
    tmp = Audio()
    tmp.audio_segment = np.arange(10)
    tmp.delete(0, 3)
    assert (tmp.audio_segment-np.arange(3, 10)).all


if __name__ == "__main__":
    print("hui")
    test_at()
