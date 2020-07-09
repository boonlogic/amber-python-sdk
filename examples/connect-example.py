from boonamber import AmberClient

# At initialization the client discovers Amber account credentials
# under the "default" entry in the ~/.Amber.license file.
amber = AmberClient()

sensors = amber.list_sensors()
print("sensors: {}".format(sensors))
