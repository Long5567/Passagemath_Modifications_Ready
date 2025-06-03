# Add data to the wheel

import os
import shlex
import sys

from pathlib import Path

from auditwheel.wheeltools import InWheel

from sage_conf import SAGE_LOCAL

if "TMPDIR" in os.environ: os.environ["TMPDIR"] = str(Path(os.environ["TMPDIR"]).resolve())

wheel = Path(sys.argv[1])

# SAGE_LOCAL/bin/* --> sage_wheels/bin/*
with InWheel(wheel, wheel):
    command = f'(cd {shlex.quote(SAGE_LOCAL)} && tar cf - --dereference bin/{{class,cws,mori,nef,poly}}*.x) | (mkdir -p sage_wheels && cd sage_wheels && tar xvf -)'
    print(f'Running {command}')
    sys.stdout.flush()
    if os.system(command) != 0: sys.exit(1)
