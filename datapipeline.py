import numpy as np
import os
import glob
import json
from reduceEvents import EventCount

#pipeline to reduce and optionally crop and restructure events of the i3s dataset.
#Pre-processing step for the MSTP adaption.

i = 0
n_samples = 2906
while i<n_samples:
    #define input/output path and phase
    event_root = './data/i3s_dataset3'
    event_root_save = './data/i3s_dataset3'
    phase = "test"
    index=i
    file_list = sorted(glob.glob(os.path.join(event_root, phase, '*', '*.npy')))


    # load timestamps
    word = file_list[index].split('/')[-2]
    person = file_list[index].split('/')[-1][:-4]
    print(person)
    print(word)

    ## load events
    try:
        events_input = np.load(file_list[index])
        print(events_input)
    except:
        print(file_list[index])

    #optional crop and restructuring of event stream
    #events_input = events_input[np.where((events_input[:,0] >= 256) & (events_input[:,0] < 384) & (events_input[:,1] >= 176) & (events_input[:,1] < 304))]
    #events_input[:, 0] -= 112  # 16
    #events_input[:, 1] -= 72  # 16

    #t, x, y, p = events_input[:, 3], events_input[:, 0], events_input[:, 1], events_input[:, 2]
    #events_input = np.stack([t, x, y, p], axis=-1)

    #Definition of EventCount: specify downscaling factor with param 'div'
    reduction = EventCount(
        input_ev=events_input,
        coord_t=3,
        div=2,
        width=-1,
        height=-1
    )

    #reduce events
    reduction.reduce()

    d = reduction.events

    print(d)

    #save reduced events
    np.save(os.path.join(event_root_save, phase, word, person), d)

    #iterate
    i += 1



