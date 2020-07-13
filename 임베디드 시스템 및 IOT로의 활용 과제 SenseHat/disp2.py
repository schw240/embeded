from sense_hat import SenseHat
sense = SenseHat()

red = (255,0,0)
green = (0,255,0)

while True:
	t = sense.get_temperature()
	p = sense.get_pressure()
	h = sense.get_humidity()
	
	t = round(t,1)
	p = round(p,1)
	h = round(h,1)

	message = "Temperature: " + str(t) + "Pressure: " + str(p) + "Humidity: " + str(h)

	if t > 18.3 and t < 26.7:
		bg = green
	else:
		bg = red
	
	sense.show_message(message , scroll_speed=0.05,back_colour = bg)
