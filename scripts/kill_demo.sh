#!/bin/bash

PID=$(lsof -i :8000 | awk '$1 == "chainlit" {print $2}' | head -n1)

if [[ -n "$PID" ]]; then
  echo "Killing demo application with PID $PID..."
  kill -9 "$PID"
  echo "Process $PID has been terminated."
else
  echo "No application found on port 8000."
fi
