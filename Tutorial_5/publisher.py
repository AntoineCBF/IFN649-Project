import paho.mqtt.publish as publish

publish.single("ifn649", "LED_OFF", hostname="3.107.164.218")
print("Done")
