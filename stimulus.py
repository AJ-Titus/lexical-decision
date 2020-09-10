from psychopy import visual, sound

class Stimulus:
    def __init__(self,
                 id,
                 condition,
                 frequency,
                 filename,
                 path,
                 modality):

        self.id = id
        self.filename = filename
        self._path = path
        self.condition = condition
        self.frequency = frequency
        self.modality = modality

    def preload_stimulus(self, window):
        self.preload_audio()
        self.preload_text(window)

    def preload_audio(self):
        if self.condition['rw']:
            if self.frequency['HF']:
                self.sound = sound.Sound(f'{self._path}/HF/{self.filename}')
            elif self.frequency['LF']:
                self.sound = sound.Sound(f'{self._path}/LF/{self.filename}')
        elif self.condition['nw']:
            self.sound = sound.Sound(f'{self._path}/NW/{self.filename}')

    def preload_text(self, window):
        _text = str(self.filename)
        self.message = visual.TextStim(window, text=_text, color=-1)
