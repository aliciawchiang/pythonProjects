#alicia chiang
#impractical python projects
# 1. finding palingram spells
#load dictionary file

import sys

def load(file):
    """open a text file and return a list of lowercase strings"""

    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)