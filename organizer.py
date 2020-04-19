import shutil
import time
import os

lokalizacja = 'C:/Users/Cezary/Downloads'

co_gdzie = [
    (('.png', '.jpg', '.gif'), 'zdjecia'),
    (('.mp4', '.mov', '.avi'), 'video'),
    (('.exe', '.rar', '.zip'), 'instalki'),
    (('.wav', '.mp3', '.ogg', '.flac'), 'muzyka'),
    (None, 'pozostale')
]


def stworz_katalogi(dir):
    for _, dir_name in co_gdzie:
        if dir_name not in os.listdir(dir):
            os.mkdir(dir + '/' + dir_name)


def organizer(dir):
    for file in os.listdir(dir):
        if os.path.isfile(lokalizacja + '/' + file):
            src_path = dir + '/' + file
            for extensions, destination in co_gdzie:
                if extensions is None or file.endswith(extensions):
                    dest_path = os.path.join(dir, destination, file)
                    shutil.move(src_path, dest_path)
                    break


if __name__ == "__main__":
    try:
        stworz_katalogi(lokalizacja)
        while True:
            organizer(lokalizacja)
            time.sleep(10)

    except KeyboardInterrupt:
        print('koniec!')
