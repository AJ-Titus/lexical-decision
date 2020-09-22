import psychopy as psy
import numpy as np


class Trial:
    @staticmethod
    def modality_dist():
        lf_ids = list(range(1, 51))
        hf_ids = list(range(51, 101))
        nw_ids = list(range(101, 201))

        all_ids = [lf_ids, hf_ids, nw_ids]
        vis = []
        aud = []

        for cnd in all_ids:
            np.random.permutation(cnd)
            vis_ids = cnd[0:int(len(cnd) / 2)]
            aud_ids = cnd[int(len(cnd) / 2):]
            vis.append(n for n in vis_ids)
            aud.append(m for m in aud_ids)

        return vis, aud

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

    def run_standard(self, window):
        if self.modality['auditory']:
            self._stimulus.sound.play()
            psy.core.wait(self._stimulus.sound.getDuration())
            psy.core.wait(self._delay)

        elif self.modality['visual']:
            self._stimulus.message.draw()
            psy.core.wait(self._delay)
            window.flip()

        clock = psy.core.Clock()
        keys = psy.event.waitKeys(maxWait=self._max_target_time, keyList=['z', 'm'], clearEvents=True,
                                  timeStamped=clock)
        self.result['response'], self.result['reaction_time'] = keys[0] if keys is not None and len(keys) > 0 else \
            (None, self._max_target_time)
        window.flip()
