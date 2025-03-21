# filename: exercise-03.py
# Write a Python script that calculates the total of the values from a dictionary.
#
# In this example the dictionary will contain the rainfall for a week.

week_rainfall = {
  "Mon":0,
  "Tue":3,
  "Wed":7,
  "Thu":1,
  "Fri":2,
  "Sat":6,
  "Sun":23
}
# The program should output the result in the form:
# Total Rainfall: 45 mm
total_rain = 0
for key, value in week_rainfall.items():
    total_rain += value
print("Total rainfall: " + str(total_rain) + " mm")
