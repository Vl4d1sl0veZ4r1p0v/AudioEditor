import os
import tempfile as tf


def split_audiofile(filename, timedelta=60):
    tmp_dir = tf.gettempdir()
    os.system(f"ffmpeg -i {filename} -f segment -segment_time {timedelta} -c copy {tmp_dir}/out%03d.wav")
    return [os.path.join(tmp_dir, file) for file in os.listdir(tmp_dir) if file.endswith("wav")]


def create_list(list_of_parts, filename="list.txt"):
    tmp_dir = tf.gettempdir()
    list_filename = os.path.join(tmp_dir, filename)
    with open(list_filename, 'w') as fout:
        for part in list_of_parts:
            print(f"file '{part}'", file=fout)
    return list_filename


def join_audiofile(audiofiles_list, filename):
    list_filename = create_list(audiofiles_list)
    os.system(f"ffmpeg -f concat -safe 0 -i {list_filename} -c copy {filename}")

