import random
import pprint
import protomidi
from protomidi.msg import *
from protomidi.io import Input, Output, context, get_devinfo_dicts

portmidi = context

import time

outputs = protomidi.io.get_output_map()
pprint.pprint(outputs)

with portmidi():
    out = Output(0)

    while 1:
        out.send(program_change(number=random.randrange(128)))

        note = random.randrange(128)

        out.send(note_on(note=note, velocity=100))
        time.sleep(0.1)

        out.send(note_off(note=note, velocity=100))
        time.sleep(0.1)
