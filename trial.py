import psychopy as psy

class Trial:
    def __init__(self, stimulus, condition, frequency, modality, delay=0.5, max_target_time=2):
        self._stimulus = stimulus
        self._condition = stimulus.__dict__[condition]
        self._frequency = stimulus.__dict__[frequency]
        self._modality = stimulus.__dict__[modality]
        self._delay = delay
        self._max_target_time = max_target_time

        self.result = {
            'id': self._stimulus.id,
            'word': self._stimulus.filename,
            'condition': condition,
            'frequency': frequency,
            'modality': modality,
            'reaction_time': None,
            'response': None
        }

    def run_standard(self, window):
        if self._stimulus.modality['auditory']:
            self._stimulus.sound.play()
            psy.core.wait(self._stimulus.sound.getDuration())
            psy.core.wait(self._delay)

        elif self._stimulus.modality['visual']:
            self._stimulus.message.draw()
            psy.core.wait(self._delay)
            window.flip()

        clock = psy.core.Clock()
        keys = psy.event.waitKeys(maxWait=self._max_target_time, keyList=['z', 'm'], clearEvents=True,
                                  timeStamped=clock)
        self.result['response'], self.result['reaction_time'] = keys[0] if keys is not None and len(keys) > 0 else \
            (None, self._max_target_time)
        window.flip()
