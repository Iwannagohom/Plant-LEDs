# Plant-LEDs


___Objectives___

	To code LEDs light for a plant bord-shelve. 
	The light with turn on and off at a specific time. The time will depend on the sunset and sunrise of individual plants' native land.
	In other words; for each individual plant, a set of lights will have its own time to be on while it's daytime in the part of the world where this plant came from.
	

___Material list___

 - Raspberry pi pico
 - LED panels
 - Cords to connect bords
 - Server to request time from.
 - Patience




1.	Conect all of the cords to the Raspberry pi pico and make sure that the LEDs panel works (I won't explain how to turn on the lights beacuse my proogect is more about time then about the phisical side of it.
2.	Conect to the wifi (wifi_Time.py)
3.	Wifi needed to conect to the server and request time. That will be converted into seconds (wifi_Time.py)
4.	Find out when the sunset and sunrice are in a selected part of the world (Lat.py) using cordinats and a link to anoter websit
5.	Convert the time of the sunrice and sunset time to seconds (timeToSeconds.py). 
		It was very useful to calculate the diffetense between time zones!
6. 	Put all of this togeter (codeForTime.py)
 		don't forget to import from lib/ledPixelsPico so the lights will light up. 
8. 	Make sure to save the file as code.py so the Pico will automaticly will can it when it will be conected to power.


		
