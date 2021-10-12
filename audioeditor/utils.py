import os
import tempfile as tf


def split_audiofile(filename, timedelta=60):
    tmp_dir = tf.gettempdir()
    os.system(f"ffmpeg -i {filename} -f segment -segment_time {timedelta} -c copy {tmp_dir}/out%03d.wav")
    return [os.path.join(tmp_dir, file) for file in os.listdir(tmp_dir) if file.endswith("wav")]

def join_audiofile(audiofiles_list, filename):
    pass
