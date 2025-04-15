# Travel Time

## Overview
The Travel Time is a Python program designed to calculate the estimated travel time for a trip based on user input. The program provides a summary of trip details, estimated travel time, and recommendations for rest stops if needed. This tool is ideal for planning trips and ensuring safe travel practices.

## Features
- Accepts user inputs for:
  - **Starting Location**: The starting point of the trip.
  - **Destination**: The endpoint of the trip.
  - **Mode of Transport**: The type of vehicle used (e.g., car, bus, bike).
  - **Distance**: The distance of the trip in kilometers (float).
  - **Speed**: The average speed of travel in km/h (float).
- Calculates the travel time using the formula:
  - Travel Time = Distance / Speed
- Determines if the travel time exceeds 5 hours and provides a warning if necessary.
- Recommends a rest stop for trips exceeding 5 hours.
- Displays a summary of the trip details and travel recommendations.
