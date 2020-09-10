from typing import Dict, Any
import psychopy as psy
import csv
from random import shuffle
from psychopy import visual, sound

path = "C:/Users/Sophie/Documents/Formación y Trabajo/Werk/PhD MPI/2020_IMPRS_Python"

# load the text file and create a dictionary of the stimuli
with open("lexdec_stimuli.txt", "r") as stim_file:
    stim_reader = csv.reader(stim_file)

    next(stim_reader)
    stim_dict: Dict[Any, Any] = dict()

    for stim in stim_reader:
        stim_dict[stim[0]] = stim[1:]

# stimuli 1:50: LF
# stimuli 51:100: HF

# the different stim types
condition = ['word', 'nonword']
frequency = ['HF', 'LF']
modality = ['aud', 'vis']

# set the window & content for different events in the experiment
window = psy.visual.Window([800,600], monitor="testMonitor", units="deg", color=1)
fixation = psy.visual.TextStim(window, text='+', color=-1)
keyscreen = psy.visual.TextStim(window, text="WOORD?\nJA\tNEE", color=2)
fixation.draw()
window.flip()

# shuffle the stimulus ids (must convert to list first!)
stimids = list(stim_dict.keys())
shuffle(stimids)

# create a dictionary for results
results = dict()

# only 10 stimuli for testing the script
for stimid in stimids[0:10]:
    stiminfo = stim_dict[stimid]

    # use visual TextStim to load the text
    message = visual.TextStim(window, text=stiminfo[1], color=-1)

    # use Sound to load the audio during fixation cross
    audio = sound.Sound(f'{path}/{stiminfo[0]}/{stiminfo[1]}.wav')

    # display fixation cross
    fixation.draw()
    psy.core.wait(1.0)
    window.flip()

    # play the stimulus
    #message.draw()
    audio.play()
    psy.core.wait(audio.getDuration())
    window.flip()

    # draw the screen for response & start clock
    keyscreen.draw()
    clock = psy.core.Clock()
    keys = psy.event.waitKeys(maxWait=3.0, keyList=['z', 'm'], clearEvents=True,
                              timeStamped=clock)

    window.flip()
    results[stimid] = keys

    #loaded_stims.append(audio)
    #

#for stimulus in loaded_stims:
    # play the sound & wait
  #  stimulus.play()
   #


    # wait 500ms
    #psy.core.wait(0.5)



#for stimulus in demo_stimuli:
 #   stimulus.preload(window)



#cue_types = ['sound', 'text']
#target_types = ['photo', 'active_photo']
#repetitions = 1
#trials = [Trial(stimulus, cue, target) for stimulus, cue, target, i in
#          product(demo_stimuli, cue_types, target_types, range(repetitions))]
#shuffle(trials)

#for trial in trials:
 #   trial.run_standard(window)

  #  fixation.draw()
  #  window.flip()
  #  psy.core.wait(1)

#results = pd.DataFrame([trial.result for trial in trials])
#results.to_csv('demo_results.csv', index_label='order')