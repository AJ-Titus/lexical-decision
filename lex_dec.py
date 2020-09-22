import psychopy as psy
import numpy as np
import pandas as pd
import os
import sys
from stimulus import Stimulus
from trial import Trial

# Set working directory
abs_path = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abs_path)
os.chdir(dname)

# Set the window & content for different events in the experiment
window = psy.visual.Window([800, 600], monitor="testMonitor", units="deg", color=1)
fixation = psy.visual.TextStim(window, text='+', color=-1)
breakscreen = psy.visual.TextStim(window, text="Je hebt nu pauze.\nDruk op een toets om verder te gaan.")
keyscreen = psy.visual.TextStim(window, text="WOORD?\nJA\tNEE", color=2)
endtext = psy.visual.TextStim(window, text='Het experiment is afgelopen.\n\nDankjewel voor je deelname!',
                              color='white', height=40, wrapWidth=600)

# Preload the stimuli
stimuli = np.random.permutation(Stimulus.load_stimuli(dname, "lexdec_stimuli.txt"))

for stimulus in stimuli:
    stimulus.preload_stimulus(window)

# Generate trials
vis, aud = Trial.modality_dist()
trials = np.random.permutation([Trial.assign_modality(stimulus, vis, aud) for stimulus in stimuli])

break_interval = 50
for i, trial in enumerate(trials):
    trial.run_standard()

    # break
    if (i + 1) % break_interval == 0:
        breakscreen.draw()
        psy.core.wait(1)

window.clearBuffer()
endtext.draw()

# Convert to data frame
results = pd.DataFrame([trial.result for trial in trials])
results.to_csv("results.csv", index_label="order")

psy.event.waitKeys()
psy.core.quit()
