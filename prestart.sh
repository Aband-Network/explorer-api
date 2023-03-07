#!/bin/zsh

# Let the DB start
export PYTHONPATH="`pwd`:${PYTHONPATH}"
echo $PYTHONPATH
python ./app/prestart.py
echo "=============="
echo $PYTHONPATH
