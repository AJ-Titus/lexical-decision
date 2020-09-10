import psychopy as psy

class Trial:
    def __init__(self, stimulus, cue, target, delay=0.5, max_target_time=2):
        self._stimulus = stimulus
        self._cue = stimulus.__dict__[cue]
        self._target = stimulus.__dict__[target]
        self._delay = delay
        self._max_target_time = max_target_time

        self.result = {
            'name': stimulus.name,
            'cue': cue,
            'target': target,
            'reaction_time ': None,
            'response': None
        }

    def run_standard(self, window):
        self._cue.play()
        psy.core.wait(self._cue.getDuration())
        psy.core.wait(self._delay)

        self._target.draw()
        window.flip()
        clock = psy.core.Clock()
        keys = psy.event.waitKeys(maxWait=self._max_target_time, keyList=['z', 'm'], clearEvents=True,
                                  timeStamped=clock)
        self.result['response'], self.result['reaction_time'] = keys[0] if keys is not None and len(keys) > 0 else (
        None, self._max_target_time)
        window.flip()