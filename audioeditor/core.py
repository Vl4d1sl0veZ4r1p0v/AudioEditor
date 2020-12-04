class Audio:

    def __init__(self):
        self.audio = None

    def from_wav(self, filename):
        return None

    def from_mp3(self, filename):
        return None

    def save_to_wav(self, filename):
        return None

    def save_to_mp3(self, filename):
        return None

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


# def normalize(ys, amp=1.0):
#     high, low = abs(max(ys)), abs(min(ys))
#     return amp * ys / max(high, low)
#
#
# def quantize(ys, bound, dtype):
#     if max(ys) > 1 or min(ys) < -1:
#         warnings.warn(
#             "Warning: normalizing before quantizing."
#         )
#         ys = normalize(ys)
#     zs = (ys * bound).astype(dtype)
#     return zs
#
#
# class Signal:
#
#     def __add__(self, other):
#         if other == 0:
#             return self
#         return
#
#
# class SilentSignal(Signal):
#
#     def evaluate(self, ts):
#         return np.zeros(len(ts))
#
#
# def rest(duration):
#     signal = SilentSignal()
#     wave = signal.make_wave(duration)
#     return wave
#
#
# class WavFileWriter:
#
#     def __init__(self, filename: str, framerate=11025):
#         self.filename = filename
#         self.framerate = framerate
#         self.n_channels = 1
#         self.sample_width = 2
#
#         self.bits = self.sample_width * 8
#         self.bound = 2 ** (self.bits - 1) - 1
#
#         self.fmt = "h"
#         self.dtype = np.int16
#
#         self.fp = open_wave(self.filename, "w")
#         self.fp.setnchammels(self.n_channels)
#         self.fp.setsampwidth(self.sampwidth)
#         self.fp.setframerate(self.framerate)
#
#     def write(self, wave):
#         zs = wave.quantize(self.bound, self.dtype)
#         self.fp.writeframes(zs.tostring())
#
#     def close(self, duration=0):
#         if duration:
#             self.write(rest(duration))
#         self.fp.close()
#
#
# def play_wave(filename: str, player="aplay"):
#     cmd = f"{player} {filename}"
#     popen = subprocess.Popen(cmd, shell=True)
#     popen.communicate()
#
#
# def find_index(x, xs):
#     n = len(xs)
#     start = xs[0]
#     end = xs[-1]
#     i = round((n - 1) * (x - start) / (end - start))
#     return int(i)
#
#
# def read_wave(filename: str) -> np.array:
#     fp = open_wave(filename, "r")
#
#     n_channels = fp.getnchannels()
#     n_frames = fp.getnframes()
#     samp_width = fp.getsampwidth()
#     framerate = fp.getframerate()
#
#     z_str = fp.readframes(n_frames)
#
#     fp.close()
#
#     dtype_map = {1: np.int8, 2: np.int16, 3: "special", 4: np.int32}
#     if samp_width not in dtype_map:
#         raise ValueError(f"Unknown {samp_width} samp_width")
#     if samp_width == 3:
#         xs = np.fromstring(z_str, dtype=np.int8).astype(np.int32)
#         ys = (xs[2::3] * 256 + xs[1::3]) * 256 + xs[0::3]
#     else:
#         ys = np.fromstring(z_str, dtype=dtype_map[samp_width])
#
#     if n_channels == 2:
#         ys = ys[::2]
#
#     wave = Wave(ys, framerate=framerate)
#     wave.normalize()
#     return wave
#
#
# class Wave:
#
#     def __init__(self, ys, ts=None, framerate=None):
#         self.ys = np.asanyarray(ys)
#         self.framerate = framerate if framerate is not None else 11025
#
#         if ts is None:
#             self.ts = np.arange(len(ys)) / self.framerate
#         else:
#             self.ts = np.asanyarray(ts)
#
#     def copy(self):
#         return deepcopy(self)
#
#     def __len__(self):
#         return len(self.ys)
#
#     @property
#     def start(self):
#         return self.ts[0]
#
#     @property
#     def end(self):
#         return self.ts[-1]
#
#     @property
#     def duration(self):
#         return len(self.ys) / self.framerate
#
#     def quantize(self, bound, dtype):
#         return quantize(self.ys, bound, dtype)
#
#     def __add__(self, other):
#         if other == 0:
#             return self
#         assert self.framerate == other.framerate
#
#         start = min(self.start, other.start)
#         end = max(self.end, other.end)
#         n = int(round((end - start) * self.framerate)) + 1
#         ys = np.zeros(n)
#         ts = start + np.arange(n) / self.framerate
#
#         def add_ys(wave):
#             i = find_index(wave.start, ts)
#
#             diff = ts[i] - wave.start
#             dt = 1 / wave.framerate
#             if diff / dt > 0.1:
#                 warnings.warn(
#                     "Can't add these waveforms; their time arrays don't line up."
#                 )
#             j = i + len(wave)
#             ys[i:j] += wave.ys
#
#         add_ys(self)
#         add_ys(other)
#
#         return Wave(ys, ts, self.framerate)
#
#     __radd__ = __add__
#
#     def scale(self, factor):
#         self.ys *= factor
#
#     def normalize(self, amp=1.0):
#         self.ys = normalize(self.ys, amp=amp)
#
#     def write(self, filename):
#         print("Writing ", filename)
#         wfile = WavFileWriter(filename, self.framerate)
#         wfile.write(self)
#         wfile.close()


if __name__ == "__main__":
    # filename = '../92002__jcveliz__violin-origional.wav'
    # play_wave(filename)
    pass