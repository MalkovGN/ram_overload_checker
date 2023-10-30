#!/bin/bash

python3 app/app.py --host=0.0.0.0 &

python3 app/utils.py &

wait

exit $?