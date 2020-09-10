## Determining overlap between words we have freq info for and words we have recordings for
import os
from os import listdir
from os.path import isfile, join
import csv
import sys
from shutil import copy
import operator

# change working directory to folder
abs_path = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abs_path)
os.chdir(dname)

###
sound_dir = 'real_underived'
HF_dir = "HF"
LF_dir = "LF"

# Open file with frequencies
frequency_info = dict()
frequency_file = open("dlp-stimuli.txt", 'r')
frequency_file_reader = csv.reader(frequency_file, delimiter='\t')

headers = next(frequency_file_reader, None)

# iterate over csv file, create dict with word and 10log frequency in subtlex (nr. 10 in list)
for frequency_word in frequency_file_reader:
    if frequency_word[10] != 'NA':
        frequency_info[frequency_word[0]] = float(frequency_word[10])

word_list = [f for f in listdir(join(dname, sound_dir)) if isfile(join(dname, sound_dir, f))]
all_freq_words = frequency_info.keys()

# look for words that occur in both (ie, we have freq. info AND we have a recording)
possible_stimuli = dict()
for word_file in word_list:
    word = word_file[0:-4]
    for item in all_freq_words:
        if word == item:
            possible_stimuli[item] = frequency_info[item]

sorted_possible_stimuli = sorted(possible_stimuli.items(), key=operator.itemgetter(1))

selected_stimuli = dict()
selected_stimuli['LF'] = sorted_possible_stimuli[0:50]
selected_stimuli['HF'] = sorted_possible_stimuli[-50:]

outfile = open("lexdec_stimuli.txt", "w")

# write header
head = ",".join(["stim_id","condition","freq_category","word","subtlex_log10freq\n"])
outfile.write(head)

selected_freqs = []
stim_id = 1
for key, value in selected_stimuli.items():
    for stimtuple in value:
        for wrd, freq in [stimtuple]:
            # list to calculate average frequency
            selected_freqs.append(freq)

            # write info to file
            to_save = str(stim_id) + "," + "rw" + "," + key + "," + wrd + "," + str(freq) + '\n'
            outfile.write(to_save)
            stim_id += 1

            # move the files to their correct location
            #filename = os.path.join(sound_dir, (wrd + ".wav"))
            #if freq > 2.406:
             #   copy(filename, HF_dir)
            #elif freq < 2.406:
             #   copy(filename, LF_dir)

frequency_file.close()
outfile.close()
