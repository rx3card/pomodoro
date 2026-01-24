#!/bin/bash

# Define the script directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

if [ -f .pomodoro.pid ]; then
    PID=$(cat .pomodoro.pid)
    if ps -p $PID > /dev/null; then
        kill $PID
        echo "🛑 Pomodoro service (PID $PID) stopped."
        rm .pomodoro.pid
    else
        echo "⚠️  Process $PID not found. Cleaning up pid file."
        rm .pomodoro.pid
    fi
else
    # Fallback: Try to find by name
    PIDS=$(pgrep -f "python3 pomodoro.py")
    if [ -n "$PIDS" ]; then
        kill $PIDS
        echo "🛑 Stopped pomodoro processes found by name."
    else
        echo "❌ No active Pomodoro service found."
    fi
fi
