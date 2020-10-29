import matplotlib.pyplot as plt
import numpy as np

from pydub import AudioSegment
from pydub.playback import play
from scipy.io import wavfile


class DigitalSignal:
    """Base class on which calculations are performed."""

    def __init__(self):
        self.signal_values = np.array([])

    # def read_wav(self, filename):
    #     signal_sample_rate, signal_values = wavfile.read(filename)
    #     signal_length = signal_values.shape[0] / signal_sample_rate
    #     return [signal_sample_rate, signal_values, signal_length]

    def read_wav(self, filename):
        wav_audio = AudioSegment.from_file(filename, format="wav")
        return wav_audio

    def read_mp3(self, filename):
        mp3_audio = AudioSegment.from_file(filename, format="mp3")
        return mp3_audio

    def plot_wave(self, ys, signal_length):
        time = np.linspace(0., , ys.shape[0] // 10)
        # two channels if stereo
        if ys.ndim == 2:
            plt.plot(time, ys[:, 0], label="Left channel")
            plt.plot(time, ys[:, 1], label="Right channel")
        else:
            plt.plot(time, ys[::10], label="Mono channel")
        plt.legend()
        plt.xlabel("Time[s]")
        plt.ylabel("Amplitude")
        plt.show()


    def save_into_wav(filename, signal_sample_rate, signal_values):
        wavfile.write(filename, signal_sample_rate, signal_values)






if __name__ == "__main__":
    # samplerate, data, length = read_wav("test.wav")
    # plot_wave(data, length)s
    # save_into_wav("test_write.wav", samplerate, data)
    read_mp3("test.wav")
    play(sound)
