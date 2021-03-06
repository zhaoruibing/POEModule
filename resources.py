import time
import json
from coapthon2.resources.resource import Resource
from sensors.mcp3008 import MCP3008
from sensors.temp_sensor import WaitingSht15


class Acceleration(Resource):
    sensor = MCP3008()
    def __init__(self, name="AccelerationResource"):
        super(Acceleration, self).__init__(name, visible=True, observable=True, allow_children=False)

    def render_GET(self, request, query=None):
        x, y, z = self.sensor.acceleration()
        return json.dumps({"x": x, "y": y, "z":z})


class HelloWorld(Resource):
    def __init__(self, name="HelloWorldResource"):
        super(HelloWorld, self).__init__(name, visible=True, observable=True, allow_children=False)

    def render_GET(self, request, query=None):
        return 'hello world'


class LocalTime(Resource):
    def __init__(self, name="LocalTimeResource"):
        super(LocalTime, self).__init__(name, visible=True, observable=True, allow_children=False)

    def render_GET(self, request, query=None):
        current_time = time.time()
        print current_time
        return json.dumps({"time": current_time})

# FIXME: SHT15 should be combined and implemented in a single class, differentiated by request
class Temperature(Resource):
    temperature = WaitingSht15()
    def __init__(self, name="TemperatureResource"):
        super(Temperature, self).__init__(name, visible=True, observable=True, allow_children=False)

    def render_GET(self, request, query=None):
        temp = self.temperature.read_temperature_C()
        return json.dumps({"temperature": temp})

class Humidity(Resource):
    humidity = WaitingSht15()
    def __init__(self, name="HumidityResource"):
        super(Humidity, self).__init__(name, visible=True, observable=True, allow_children=False)

    def render_GET(self, request, query=None):
        hum = self.humidity.read_humidity()
        return json.dumps({"humidity": hum})
        
class Temp_Humidity(Resource):
    temp_hum = WaitingSht15()
    def __init__(self, name="Temp_HumidityResource"):
        super(Temp_Humidity, self).__init__(name, visible=True, observable=True, allow_children=False)

    def render_GET(self, request, query=None):
        temp, humidity = self.temp_hum.read_temperature_and_Humidity()
        return json.dumps({"temperature": temp, "humidity": humidity})
