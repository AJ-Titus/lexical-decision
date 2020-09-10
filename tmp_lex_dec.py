#import psychopy as psy

# load stimuli
from psychopy import visual, sound, core  # import some libraries from PsychoPy

#create a window
#mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

abs_path = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abs_path)
os.chdir(dname)

from stimulus import Stimulus

Stimulus.load_stimuli()

