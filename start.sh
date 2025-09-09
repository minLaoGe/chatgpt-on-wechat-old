#!/bin/bash

# Replace 'your_flask_script.py' with the name of your Flask script
FLASK_SCRIPT="app_robot.py"

# Find the process ID of the Flask application
PID=$(pgrep -f $FLASK_SCRIPT)

# If the process ID is not empty, kill the process
if [ ! -z "$PID" ]; then
  echo "Killing the Flask app with process ID: $PID"
  kill -9 $PID
else
  echo "Flask app is not running"
fi

# Wait for a while to make sure the process is terminated
sleep 2

# Start the Flask application
echo "Starting the Flask app"
python $FLASK_SCRIPT &
# Print the process ID of the newly started Flask app
NEW_PID=$(pgrep -f $FLASK_SCRIPT)
echo "Flask app started with process ID: $NEW_PID"


