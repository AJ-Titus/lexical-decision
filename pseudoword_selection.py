import os
from os import listdir
from os.path import isfile, join
from random import shuffle
import sys
from shutil import copy

# change working directory to folder
abs_path = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abs_path)
os.chdir(dname)

###
sound_dir = 'pseudo_underived'
pseudo_dir = 'NW'

nonword_list = [f for f in listdir(sound_dir) if isfile(join(sound_dir, f))]
shuffle(nonword_list)
outfile = open("lexdec_stimuli.txt", "a")

# move the files to their correct location & write to stimulus file
stim_id = 101

for nonword in nonword_list[0:100]:
    filename = os.path.join(sound_dir, nonword)
    copy(filename, pseudo_dir)

    nonword_text = str(nonword)[0:-4]
    to_save = str(stim_id) + "," + "nw" + "," + "none" + "," + nonword_text + "," + "0\n"
    outfile.write(to_save)

    stim_id += 1

outfile.close()
