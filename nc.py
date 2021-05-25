#!/usr/bin/env python3
import sys
import wave
import numpy as np

wf = wave.open(sys.argv[1], 'rb')
intwave = np.frombuffer(wf.readframes(wf.getnframes()), np.int32)
intwave = np.invert(intwave)
inverted = np.frombuffer(intwave, np.byte)

of = wave.open(sys.argv[1][:-4]+'_inv.wav', 'w')
of.setnchannels(wf.getnchannels())
of.setnframes(wf.getnframes())
of.setframerate(wf.getframerate())
of.setsampwidth(wf.getsampwidth())
of.writeframes(inverted)
