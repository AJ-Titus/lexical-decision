# IMPRS Python course: Auditory lexical decision task (Dutch)

This is the GIT repository for an auditory lexical decision task written in Python using Psychopy.

## Installation
In order to run the scripts, you will need to have Python 3 installed. The project has been developed and tested using Python 3.6, although it might also be compatible with other versions of Python 3. You will also need to install package dependencies before being able to run certain scripts: Psychopy and Pandas. Installing psychopy automatically installs Pandas. For more information about installing Psychopy, [check the Psychopy website](https://www.psychopy.org/download.html). We recommend using a virtual environment to manage Python package versions on a per-project basis.

## Stimuli
An overview of the stimuli can be found in the `<lexdec_stimuli.txt>` file. This is also the file that is used in the script itself to load the stimuli. Stimulus sound files can be found in the `<HF>`, `<LF>` and `<none>` folders, standing for High Frequency, Low Frequency, and non-words, respectively.

## Experiment
The main script is `<lex_dec.py>`, with class information in the `<utils.py>` script.

## Practice data
Some data to practice analysis and visualisation with can be found in the `<lexdec_results.csv>` file.
