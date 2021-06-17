import paho.mqtt.client as mqtt


def on_msg(client, userdata, message):
            print(f"Recieved data: {str(message.payload.decode('utf-8'))}")


class Comm:
    def __init__(self, **kwargs):
        self.client_id = kwargs.get("client_id")
        self.broker = kwargs.get("broker")
        self.port = kwargs.get("port")

        if self.client_id is None:
            self.client_id = "Server"
        if self.broker is None:
            self.broker = "mqtt.eclipseprojects.io"
        if self.port is None:
            self.port = 1883
        
        self.c = self.connect()

    
    def connect(self):
        c = mqtt.Client(client_id=self.client_id)
        c.connect(self.broker, self.port)
        
        return c;
    
    def disconnect(self):
        self.c.disconnect()


    def send(self, topic, msg):
        self.c.publish(topic, msg) 
        # self.c.disconnect()


    def listen(self, topic):    
        self.c.on_message = on_msg
        self.c.subscribe(topic)
        self.c.loop_forever()
    



