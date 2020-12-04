import numpy as np
from pydub import AudioSegment


class Audio:

    def __init__(self):
        self.audio_segment = None
        self.rate = None


    def from_wav(self, file_name):
        self.audio_segment = AudioSegment.from_file(file_name, format="wav")
        self.rate = self.audio_segment.frame_rate
        self.audio_segment = np.array(
            self.audio_segment.get_array_of_samples())

    def from_mp3(self, file_name):
        self.audio_segment = AudioSegment.from_file(file_name, format="mp3")
        self.audio_segment = np.array(
            self.audio_segment.get_array_of_samples())

    def save_to_wav(self, file_name):
        self.audio_segment = AudioSegment(
            self.audio_segment.tobytes(),
            frame_rate=self.rate,
            sample_width=self.audio_segment.dtype.itemsize,
            channels=1
        )
        file_handle = self.audio_segment.export(file_name, format="wav")
        return file_handle

    def save_to_mp3(self, file_name):
        self.audio_segment = AudioSegment(
            self.audio_segment.tobytes(),
            frame_rate=self.rate,
            sample_width=self.audio_segment.dtype.itemsize,
            channels=1
        )
        file_handle = self.audio_segment.export(file_name, format="mp3")
        return file_handle

    def swap(self, first_part, second_part):
        return None

    def at(self, index):
        return None

    def get_slice(self, start, finish, step):
        return None

    def delete(self, start, finish, step):
        return None

    def change_volume(self, start, end):
        return None

    def smooth_apperance(self, end):
        return None


if __name__ == "__main__":
    filename = "../test.wav"
    audio = Audio()
    audio.from_wav(filename)
    print(audio.audio_segment.shape)
    audio.save_to_wav("../test2.wav")
