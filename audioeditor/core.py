import numpy as np

from pydub import AudioSegment
from pydub.playback import play


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
        self.rate = self.audio_segment.frame_rate
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
            frame_rate=self.rate * 20,
            sample_width=self.audio_segment.dtype.itemsize,
            channels=1
        )
        file_handle = self.audio_segment.export(file_name, format="mp3")
        return file_handle

    @staticmethod
    def is_intersect(first_start, first_end, second_start, second_end):
        first_start, first_end = min(first_start, first_end), max(first_start, first_end)
        second_start, second_end = min(second_start, second_end), max(second_start, second_end)
        left = max(first_start, second_start)
        right = min(first_end, second_end)
        if right < left:
            return False
        return True

    def swap(self, first_start, first_end, second_start, second_end):
        if self.is_intersect(first_start, first_end, second_start, second_end):
            raise Exception("Segments must not intersect")
        points = sorted([first_start, first_end, second_start, second_end])
        tmp1 = np.array(self.audio_segment[:points[0]])
        tmp2 = np.array(self.audio_segment[points[0]:points[1]])
        tmp3 = np.array(self.audio_segment[points[1]:points[2]])
        tmp4 = np.array(self.audio_segment[points[2]:points[3]])
        tmp5 = np.array(self.audio_segment[points[3]:])
        self.audio_segment = np.concatenate([
            tmp1,
            tmp4,
            tmp3,
            tmp2,
            tmp5
        ])

    def at(self, index):
        return self.audio_segment[index]

    def get_slice(self, start, end, step=1):
        return self.audio_segment[start:end:step]

    def delete(self, start, end, step=1):
        self.audio_segment = np.delete(
            self.audio_segment,
            slice(start, end, step),
            0)

    def change_volume(self, value):
        audio_from_segment = AudioSegment(
            self.audio_segment.tobytes(),
            frame_rate=self.rate,
            sample_width=self.audio_segment.dtype.itemsize,
            channels=1
        )
        audio_from_segment = audio_from_segment + value
        self.audio_segment = np.array(
            audio_from_segment.get_array_of_samples())

    def change_speed(self, speed=1.0):
        self.rate *= speed

    def __add__(self, other):
        self_audio = AudioSegment(
            self.audio_segment.tobytes(),
            frame_rate=self.rate,
            sample_width=self.audio_segment.dtype.itemsize,
            channels=1
        )
        other_audio = AudioSegment(
            other.audio_segment.tobytes(),
            frame_rate=other.rate,
            sample_width=other.audio_segment.dtype.itemsize,
            channels=1
        )
        self_audio = self_audio + other_audio
        result = Audio()
        result.audio_segment = np.array(
            self_audio.get_array_of_samples())
        result.rate = self_audio.frame_rate
        return result

    def get_fade_in(self, duration):
        self_audio = AudioSegment(
            data=self.audio_segment.tobytes(),
            frame_rate=self.rate,
            sample_width=self.audio_segment.dtype.itemsize,
            channels=1
        )
        self_audio.fade_in(
            duration=duration
        )
        result = Audio()
        result.audio_segment = np.array(
            self_audio.get_array_of_samples())
        result.rate = self_audio.frame_rate
        return result

    def get_fade_out(self, duration):
        self_audio = AudioSegment(
            self.audio_segment.tobytes(),
            frame_rate=self.rate,
            sample_width=self.audio_segment.dtype.itemsize,
            channels=1
        )
        self_audio.fade_out(
            duration=duration
        )
        result = Audio()
        result.audio_segment = np.array(
            self_audio.get_array_of_samples())
        result.rate = self_audio.frame_rate
        return result

    def change_pitch(self, octaves=1.0):
        self_audio = AudioSegment(
            self.audio_segment.tobytes(),
            frame_rate=self.rate,
            sample_width=self.audio_segment.dtype.itemsize,
            channels=1
        )
        new_sample_rate = int(self_audio.frame_rate * (2.0 ** octaves))
        result = Audio()
        result.audio_segment = np.array(
            self_audio.get_array_of_samples())
        result.rate = self_audio.frame_rate
        return result

    def play(self):
        self_audio = AudioSegment(
            self.audio_segment.tobytes(),
            frame_rate=self.rate,
            sample_width=self.audio_segment.dtype.itemsize,
            channels=1
        )
        play(self_audio)


if __name__ == "__main__":
    filename = "05.SMOKE.mp3"
    audio = Audio()
    audio.from_mp3(filename)
    audio.play()
