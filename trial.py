import psychopy as psy
import numpy as np

def distribution():
    lf_ids = list(range(1, 51))
    hf_ids = list(range(51, 101))
    nw_ids = list(range(101, 201))

    all_ids = [lf_ids, hf_ids, nw_ids]
    vis = []
    aud = []

    for cnd in all_ids:
        rnd = np.random.permutation(cnd)
        half = int(len(rnd)/2)
        vis_ids = rnd[0:half]
        aud_ids = rnd[half:]
        for n in vis_ids:
            vis.append(n)
        for m in aud_ids:
            aud.append(m)

    return vis, aud

class Trial:
    @staticmethod
    def assign_modality(stimulus, vis, aud):
        if stimulus.id in aud:
            return Trial(stimulus, "auditory")
        elif stimulus.id in vis:
            return Trial(stimulus, "visual")

    def __init__(self, stimulus, modality):
        self._stimulus = stimulus
        self._condition = stimulus.condition
        self._frequency = stimulus.frequency
        self.modality = modality
        self._delay = 0.5
        self._max_target_time = 2

        self.result = {
            'id': self._stimulus.id,
            'word': self._stimulus.filename,
            'condition': self._condition,
            'frequency': self._frequency,
            'modality': modality,
            'reaction_time': None,
            'response': None
        }

    def run_standard(self, window, fixation):
        fixation.draw()
        psy.core.wait(0.2)
        window.flip()

        if self.modality == 'auditory':
            self._stimulus.sound.play()
            psy.core.wait(self._stimulus.sound.getDuration())
            clock = psy.core.Clock()
            #psy.core.wait(self._delay)

        elif self.modality == 'visual':
            self._stimulus.message.draw()
            clock = psy.core.Clock()
            psy.core.wait(self._delay)
            window.flip()

        keys = psy.event.waitKeys(maxWait=self._max_target_time, keyList=['z', 'm'], clearEvents=True,
                                  timeStamped=clock)
        self.result['response'], self.result['reaction_time'] = keys[0] if keys is not None and len(keys) > 0 else \
            (None, self._max_target_time)
        window.flip()
