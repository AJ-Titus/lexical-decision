import os
from os.path import join
import csv
from psychopy import visual, sound

class Stimulus:
    def __init__(self,
                 filename,
                 path,
                 condition,
                 frequency,
                 modality):

        self.filename = filename
        self._path = path
        self.condition = condition
        self.frequency = frequency
        self.modality = modality

    def load_stimuli(self):
        with open(join(path, "lexdec_stimuli.txt"), "r") as stim_file:
            stim_reader = csv.reader(stim_file)

            next(stim_reader)
            stim_dict = dict()

            for stim in stim_reader:
                stim_dict[stim[0]] = stim[1:]

            return stim_dict

   # def preload_audio(self):
    #    if self.condition['word']:
     #       if self.frequency['HF']:
      #          self.sound = sound.Sound(f'{self._path}/HF/{self.filename}')
       #     elif self.frequency['LF']:
        #        self.sound = sound.Sound(f'{self._path}/LF/{self.filename}')
       # elif self.condition['nonword']:
        #    self.sound = sound.Sound(f'{self._path}/NW/{self.filename}')

    #def preload_text(self, window):
     #   self.text = str(self.filename)[0:-4]
      #  self.message = visual.TextStim(window, text=self.text, color=-1)

