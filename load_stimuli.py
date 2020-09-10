from os.path import join
import csv

def load_stimuli(path):
    with open(join(path, "lexdec_stimuli.txt"), "r") as stim_file:
        stim_reader = csv.reader(stim_file)

        next(stim_reader)
        stim_dict = dict()

        for stim in stim_reader:
            stim_dict[stim[0]] = stim[1:]

        return stim_dict