from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    @staticmethod
    @abstractmethod
    def play(type, file):
        ...


class AdvancedMediaPlayer(ABC):
    @staticmethod
    @abstractmethod
    def play_mp4(file):
        ...

    @staticmethod
    @abstractmethod
    def play_vlc(file):
        ...


class VLCPlayer(AdvancedMediaPlayer):
    @staticmethod
    def play_vlc(file):
        print(f'Playing vlc file. Name: {file}')

    @staticmethod
    def play_mp4(file):
        ...


class MP4Player(AdvancedMediaPlayer):
    @staticmethod
    def play_mp4(file):
        print(f'Playing mp4 file. Name: {file}')

    @staticmethod
    def play_vlc(file):
        ...


class MediaAdapter(MediaPlayer):
    advanced_player = None

    @staticmethod
    def play(type, file):
        if type == 'mp3':
            print(f'Playing {type} file. Name: {file}')
        elif type == 'mp4':
            MediaAdapter.advanced_player = MP4Player()
            MediaAdapter.advanced_player.play_mp4(file)
        elif type == 'vlc':
            MediaAdapter.advanced_player = VLCPlayer()
            MediaAdapter.advanced_player.play_vlc(file)


class AudioPlayer(MediaPlayer):
    adapter = None

    @staticmethod
    def play(type, file):
        ext = file.split('.')[1]

        if ext != type:
            raise Exception(f'File ({file}) does not match type ({type})')

        if type == 'mp3':
            print(f'Playing {type} file. Name: {file}')
        elif type == 'mp4' or type == 'vlc':
            AudioPlayer.adapter = MediaAdapter()
            AudioPlayer.adapter.play(type, file)
        else:
            raise Exception(f'Unknown filetype {type}')


if __name__ == '__main__':
    AudioPlayer.play('mp4', 'woo.mp4')
