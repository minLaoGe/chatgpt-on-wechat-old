#!/bin/bash





# Find Python files with names starting with 'app_robot'
APP_ROBOT_FILES=$(find . -name "app_robot*.py")

# Iterate through the found files
for FLASK_SCRIPT in $APP_ROBOT_FILES; do
  FILENAME=$(basename $FLASK_SCRIPT)

  # Find the process ID of the Flask application
  PID=$(pgrep -f $FILENAME)

  # If the process ID is not empty, kill the process
  if [ ! -z "$PID" ]; then
    echo "Killing the Flask app with process ID: $PID"
    echo "Killing the Flask appname is: $FILENAME"
    kill -9 $PID
  else
    echo "Flask app is not running"
  fi

  # Wait for a while to make sure the process is terminated
  sleep 3

  # Start the Flask application
  echo "Starting the Flask app"
  python $FLASK_SCRIPT &
  # Print the process ID of the newly started Flask app
  NEW_PID=$(pgrep -f $FLASK_SCRIPT)
  echo "Flask app started with process ID: $NEW_PID"
done