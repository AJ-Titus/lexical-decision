from psychopy import visual, sound
import pandas as pd
from os.path import join


class Stimulus:
    @staticmethod
    def load_stimuli(path, filename):
        file = join(path, filename)
        return [Stimulus(row, path) for i, row in pd.read_csv(file).iterrows()]

    def __init__(self, row, path):
        self.id = row[0]
        self.filename = row[3]
        self.frequency = row[2]
        self.condition = row[1]
        self._path = path

    def preload_stimulus(self, window):
        self.preload_audio()
        self.preload_text(window)

    def preload_audio(self):
        if self.condition == 'rw':
            if self.frequency == 'HF':
                self.sound = sound.Sound(f'{self._path}\\HF\\{self.filename}.wav')
            elif self.frequency == 'LF':
                self.sound = sound.Sound(f'{self._path}\\LF\\{self.filename}.wav')
        elif self.condition == 'nw':
            self.sound = sound.Sound(f'{self._path}\\NW\\{self.filename}.wav')

    def preload_text(self, window):
        _text = str(self.filename)
        self.message = visual.TextStim(window, text=_text, color=-1)
