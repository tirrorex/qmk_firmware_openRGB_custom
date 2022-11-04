import subprocess
import os
import sys

BOARDS = [
    'redragon/k552/rev1',
    'redragon/k552/rev2',
    'redragon/k530',
    'redragon/k556',
    'redragon/k580',
    'redragon/k630',
    'keychron/c1/plain',
    'keychron/c1/rgb',
    'keychron/c1/white',
    'keychron/c2/white',
    'keychron/k2/rgb',
    'keychron/k2/rgb/via',
    'keychron/k2/rgb/optical',
    'keychron/k2/rgb/optical_via',
    'keychron/k3/rgb',
    'keychron/k3/rgb/via',
    'keychron/k3/rgb/optical',
    'keychron/k3/rgb/optical_via',
    'keychron/k4/rgb/v1',
    'keychron/k4/rgb/v1/via',
    'keychron/k4/rgb/v1/optical',
    'keychron/k4/rgb/v1/optical_via',
    'keychron/k4/rgb/v2',
    'keychron/k4/rgb/v2/via',
    'keychron/k4/rgb/v2/optical',
    'keychron/k4/rgb/v2/optical_via',
    'keychron/k6/rgb',
    'keychron/k6/rgb/via',
    'keychron/k6/rgb/optical',
    'keychron/k6/rgb/optical_via',
    'keychron/k6/white',
    'keychron/k7/rgb',
    'keychron/k7/rgb/via',
    'keychron/k7/rgb/optical',
    'keychron/k7/rgb/optical_via',
    'keychron/k8/rgb',
    'keychron/k8/rgb/via',
    'keychron/k8/rgb/optical',
    'keychron/k8/rgb/optical_via',
    'keychron/Q1AnsiV2Knob/rgb/ansi',
    'keychron/k14/rgb',
    'keychron/k14/rgb/via',
    'keychron/k14/rgb/optical',
    'keychron/k14/rgb/optical_via',
    'ajazz/ak33/rev1',
    'ajazz/ak33/rev2',
    'smartduck/xs61',
    'spcgear/gk530',
    'spcgear/gk540',
    'sharkoon/sgk3',
    'womier/k87',
    'flashquark/horizon_z',
    'ffc/ffc61',
    'gmmk/full/rev2',
    'gmmk/full/rev3',
    'marvo/kg938',
    'akko/3061_rgb']

error = False
for kb in BOARDS:
    if subprocess.run(f"qmk compile -kb {kb} -km all -j{os.cpu_count()}", shell=True).returncode != 0:
        error = True
if error:
    sys.exit(1)
