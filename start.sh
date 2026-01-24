#!/bin/bash

# Define the script directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Check if venv exists and activate it
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Run the python script in background and ignore output
# Use nohup to keep running after terminal exit
nohup python3 pomodoro.py > /dev/null 2>&1 &

# Save the PID
echo $! > .pomodoro.pid

echo "🍅 Pomodoro started in background with PID $!"
