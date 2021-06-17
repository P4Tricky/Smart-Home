#include <WiFi.h>
#include <PubSubClient.h>


#define WIFI_SSID "GuestHome24G"
#define WIFI_PASSWD "guest24G"
#define WIFI_TIMEOUT_MS 20000
#define MQTT_SERVER "mqtt.eclipseprojects.io"
#define MQTT_PORT 1883

#define clock_pin 14
#define latch_pin 4
#define data_pin 12


WiFiClient espClient;
PubSubClient c(espClient);
long lastMsg = 0;
char msg[50];
int val = 0;

int leds[] = {13, 12, 14, 27, 26, 25};


void callback(char* topic, byte* message, unsigned int length);
void connnet_to_wifi();
void reconnect();


void setup()
{
  Serial.begin(115200);
  
  connnet_to_wifi();
  c.setServer(MQTT_SERVER, MQTT_PORT);
  c.setCallback(callback);

  for (int i=0; i<6; ++i)
  {
    pinMode(leds[i], OUTPUT);
  }
}


void loop()
{
  if (!c.connected())
  {
    reconnect();  
  }
  c.loop();
}


void reconnect()
{
  while (!c.connected())
  {
    Serial.print("Attempting MQTT connection...");
    if (c.connect("ESP"))
    {
      Serial.println("connected");
      c.subscribe("myhome");
    }
    else
    {
      Serial.print("failed, rc=");
      Serial.print(c.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}


void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();

  if (messageTemp[0] == '0')
  {
    Serial.println("TOGGLE LED 0");
    char ch = messageTemp[2];
    int state = ch - '0';
    digitalWrite(leds[0], state);
    Serial.println(state);
  }
  else if (messageTemp[0] == '1')
  {
    Serial.println("TOGGLE LED 1");
    char ch = messageTemp[2];
    int state = ch - '0';
    digitalWrite(leds[1], state);
    Serial.println(state);
  }
  else if (messageTemp[0] == '2')
  {
    Serial.println("TOGGLE LED 2");
    char ch = messageTemp[2];
    int state = ch - '0';
    digitalWrite(leds[2], state);
    Serial.println(state);
  }
  else if (messageTemp[0] == '3')
  {
    Serial.println("TOGGLE LED 3");
    char ch = messageTemp[2];
    int state = ch - '0';
    digitalWrite(leds[3], state);
    Serial.println(state);
  }
  else if (messageTemp[0] == '4')
  {
    Serial.println("TOGGLE LED 4");
    char ch = messageTemp[2];
    int state = ch - '0';
    digitalWrite(leds[4], state);
    Serial.println(state);
  }
  else if (messageTemp[0] == '5')
  {
    Serial.println("TOGGLE LED 5");
    char ch = messageTemp[2];
    int state = ch - '0';
    digitalWrite(leds[5], state);
    Serial.println(state);
  }
}


void connnet_to_wifi()
{
  Serial.print("Connecting to WiFi");
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  WiFi.begin(WIFI_SSID, WIFI_PASSWD);

  unsigned long startAttemptTime = millis();

  while (WiFi.status() != WL_CONNECTED && millis() - startAttemptTime < WIFI_TIMEOUT_MS)
  {
    Serial.print(".");
    delay(100);
  }

  if (WiFi.status() != WL_CONNECTED)
  {
    Serial.println("Failed!");
  }
  else
  {
    Serial.print("Connected! ");
    Serial.println(WiFi.localIP());
  }
}
