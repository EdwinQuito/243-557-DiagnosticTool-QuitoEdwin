from sensor import Sensor 


temperature_sensor = Sensor(
    "Temperature",
    "°C",
    22.5,
)

distance_sensor = Sensor(
    "Distance",
    "cm",
    35.0,
)

print(
    temperature_sensor.name,
    temperature_sensor.read(),
    temperature_sensor.unit,
    )  # Output: Temperature

print(
    distance_sensor.name,
    distance_sensor.read(),
    distance_sensor.unit,
    )

distance_sensor.set_value(50.0)

print(
    temperature_sensor.name,
    temperature_sensor.read(),
    temperature_sensor.unit,
    ) 

print(
    distance_sensor.name,
    distance_sensor.read(),
    distance_sensor.unit,
    )
