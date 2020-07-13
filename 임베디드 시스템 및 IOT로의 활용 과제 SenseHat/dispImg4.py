from sense_hat import SenseHat

sense = SenseHat()

g = (0,255,0)
b = (0,0,0) #black

creeper_pixels = [
	g,g,g,g,g,g,g,g,
	g,g,g,g,g,g,g,g,
	g,b,b,g,g,b,b,g,
	g,b,b,g,g,b,b,g,
	g,g,g,b,b,g,g,g,
	g,g,b,b,b,b,g,g,
	g,g,b,b,b,b,g,g,
	g,g,b,g,g,b,g,g
]

sense.set_pixels(creeper_pixels)
