from boonamber import AmberClient

# At initialization the client discovers Amber account credentials
# under the "default" entry in the ~/.Amber.license file.
amber = AmberClient()

# These credentials are used to authenticate against the Amber cloud.
amber.authenticate()

# The client is then authenticated for one hour of use, and may
# re-authenticate at any time with another call to authenticate().
sensors = amber.list_sensors()
print("sensors: {}".format(sensors))
