from psychopy import core, sound, visual, event
import pandas as pd


def read_stimuli():
    return pd.read_csv("lexdec_stimuli.txt")


class Experiment:
    def __init__(self, window_size, text_color, background_color):
        self.text_color = text_color
        self.window = visual.Window(window_size, color=background_color)

    def show_message(self, message):
        stimulus = visual.TextStim(self.window, text=message, color=self.text_color)
        stimulus.draw()
        self.window.flip()
        event.waitKeys()

    def show_fixation(self, time=0.5):
        fixation = visual.TextStim(self.window, text='+', color=self.text_color)
        fixation.draw()
        self.window.flip()
        core.wait(time)

    def key_screen(self):
        msg = visual.TextStim(self.window, text="Is het een woord?\nJA\t\tNEE", color=self.text_color)
        msg.draw()
        self.window.flip()

class Stimulus:
    def __init__(self,
                 stimid,
                 frequency,
                 filename,
                 path):

        self.stimid = stimid
        self.filename = filename
        self.path = path
        self.frequency = frequency
        self.sound = sound.Sound(f'{self.path}/{self.frequency}/{self.filename}.wav')


class Trial:
    def __init__(self, experiment, stimulus, delay=0.5, max_target_time=2):
        self.experiment = experiment  # Experiment class
        self.stimulus = stimulus  # Stimulus class
        self.delay = delay  # Time in seconds
        self.max_target_time = max_target_time  # Time to respond in seconds

        self.result = {
            'id': self.stimulus.stimid,
            'word': self.stimulus.filename,
            'frequency': self.stimulus.frequency,
            'duration': self.stimulus.sound.getDuration(),
            'reaction_time': None,
            'response': None
        }

    def run(self):
        self.experiment.show_fixation(self.delay)
        self.experiment.key_screen()
        clock = core.Clock()
        self.stimulus.sound.play()
        keys = event.waitKeys(maxWait=self.max_target_time, keyList=['z', 'm'], clearEvents=True,
                              timeStamped=clock)


        self.result['response'], self.result['reaction_time'] = keys[0] if keys is not None and len(keys) > 0 else \
            (None, self.max_target_time)

        self.experiment.show_fixation(time=0.5)
        self.experiment.window.flip()
