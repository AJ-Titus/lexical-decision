import psychopy as psy
from random import shuffle
import pandas as pd
import os
import sys
from load_stimuli import load_stimuli
from stimulus import Stimulus
from trial import Trial

# Set the working directory
abs_path = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abs_path)
os.chdir(dname)

# Load the stimulus file
stimuli = load_stimuli(dname)

# Set the window & content for different events in the experiment
window = psy.visual.Window([800, 600], monitor="testMonitor", units="deg", color=1)
fixation = psy.visual.TextStim(window, text='+', color=-1)
keyscreen = psy.visual.TextStim(window, text="WOORD?\nJA\tNEE", color=2)
fixation.draw()
window.flip()

# Preload the stimuli
# 1-50 random split for visual auditory (determined per participant)
LF_ids = list(range(1, 51))
HF_ids = list(range(51, 101))
nw_ids = list(range(101, 201))

all_ids = [LF_ids, HF_ids, nw_ids]
vis = []
aud = []
for cnd in all_ids:
    shuffle(cnd)
    vis_ids = cnd[0:int(len(cnd) / 2)]
    aud_ids = cnd[int(len(cnd) / 2):]
    for n in vis_ids:
        vis.append(n)
    for m in aud_ids:
        aud.append(m)

stimulus_objects = []
x = 0
while x < 11:
    for stimid, stiminfo in stimuli.items():
        condition = stiminfo[0]
        frequency = stiminfo[1]
        filename = stiminfo[2]

        if stimid in aud:
            modality = "auditory"
        elif stimid in vis:
            modality = "visual"
        else:
            break

        stim = Stimulus(stimid, condition, frequency, filename, dname, modality)
        stimulus_objects.append(stim)
        stim.preload_stimulus(window)

        x += 1

trials = [Trial(stimulus) for stimulus in stimulus_objects]
shuffle(trials)

# Run
for trial in trials:
    trial.run_standard(window)

    fixation.draw()
    window.flip()
    psy.core.wait(1)

results = pd.DataFrame([trial.result for trial in trials])
results.to_csv('first_experiment.csv', index_label='order')
