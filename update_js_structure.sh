#!/bin/bash

# Create directories if they don't exist
mkdir -p D:/Coding\ Files/GitHub/AlgoAlp/charting/assets/js/utils
mkdir -p D:/Coding\ Files/GitHub/AlgoAlp/charting/assets/js/chart

# Copy the new utility files
echo "Copying new utility files..."
cp D:/Coding\ Files/GitHub/AlgoAlp/charting/assets/js/utils.js.new D:/Coding\ Files/GitHub/AlgoAlp/charting/assets/js/utils.js

# Copy the modular chart manager files
echo "Copying chart manager files..."
cp D:/Coding\ Files/GitHub/AlgoAlp/charting/assets/js/chartManager.js.new D:/Coding\ Files/GitHub/AlgoAlp/charting/assets/js/chartManager.js

# Copy the updated app.js
echo "Copying app.js..."
cp D:/Coding\ Files/GitHub/AlgoAlp/charting/assets/js/app.js.new D:/Coding\ Files/GitHub/AlgoAlp/charting/assets/js/app.js

# Copy the updated dataManager.js
echo "Copying dataManager.js..."
cp D:/Coding\ Files/GitHub/AlgoAlp/charting/assets/js/dataManager.js.new D:/Coding\ Files/GitHub/AlgoAlp/charting/assets/js/dataManager.js

echo "Done!"
