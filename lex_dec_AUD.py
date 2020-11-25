import pandas as pd
from utils import read_stimuli, Experiment, Stimulus, Trial
from random import shuffle
import psychopy as psy

path = "C:\\Users\\Sophie\\Documents\\Formación y Trabajo\Werk\\PhD MPI\\2020-IMPRS-python-course\\lexical-decision"

# initiate the experiment
experiment = Experiment(window_size=[800, 600], text_color=-1, background_color=1)

# load the text file and create a dictionary of the stimuli
stimuli = read_stimuli()
stimulus_objects = [Stimulus(stim["stim_id"], stim["freq_category"], stim["word"], path) for i, stim in stimuli.iterrows()]
trials = [Trial(experiment, stimulus, delay=0.0, max_target_time=2) for stimulus in stimulus_objects]

# shuffle the stimuli
shuffle(trials)

experiment.show_message("Welkom!\n\nIn dit experiment ga je naar korte fragmenten luisteren. "
                        + "Het is jouw taak om te beslissen of wat je hoort een echt woord is of niet.\n"
                        + "Druk op Z voor \'ja\' en M voor \'nee\'.\n\n"
                        + "Het experiment duurt ongeveer 20 minuten.\n"
                        + "Druk op een toets om te beginnen.")

experiment.show_fixation(time=1.0)

results = []
trial_no = 0
for trial in trials[0:8]:
    trial_no += 1
    trial.run()
    results.append(trial.result)

    # break
    if trial_no % 4 == 0 and trial_no != len(trials):
        experiment.show_message("Nu kun je even pauze nemen.\n\n" +
                                "Druk op een toets om verder te gaan.")
        experiment.show_fixation(time=0.5)

experiment.show_message("Het experiment is afgelopen.\n\nBedankt voor je deelname!\n\nDruk op een toets om af te sluiten.")
experiment.window.clearBuffer()
psy.core.quit()

# Create a dataframe based on the results, and store them to a csv file
results = pd.DataFrame(results)
results.to_csv('results.csv')
