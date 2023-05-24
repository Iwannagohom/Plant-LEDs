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




1.	Connect all of the cords to the Raspberry Pi Pico and make sure that the LED panel works (I won't explain how to turn on the lights because my project is more about time than about the physical side of it.
2.	Connect to the wifi (wifi_Time.py)
3.	Wifi needed to connect to the server and request time. That will be converted into seconds (wifi_Time.py)
4.	Find out when the sunset and sunrise are in a selected part of the world (Lat.py) using coordinates and a link to another website
5.	Convert the time of the sunrise and sunset time to seconds (timeToSeconds.py). 
		It was very useful to calculate the difference between time zones!
6. 	Put all of this together (codeForTime.py)
 		don't forget to import from lib/ledPixelsPico so the lights will light up. 
8. 	Make sure to save the file as code.py so the Pico will automatically can it when it will be connected to power.



___What I learned:___

- Much useful for me personally to work individually and not in a group, because I had to do a lot of thinking and actually understand what I am coding. In the group usually, another person does all the thinking and I don’t know the subject that well.
- Doing an actual project improved my coding knowledge (which I did not have before).
- Learned how to solder.


		
