### US1 · Im Stress, Backofen schon eingeschaltet. 
Als Vollzeitarbeitende/r möchte ich, beim Backen/Kochen Zeit sparen.
- [ ] Beim Betreten der Küche ist der Backofen eingeschaltet. 

### US2 · Kein Bedarf des Benutzen des Backofens
Als durstige Person, möchte ich nur ein Glas Wasser. 
- [ ] Beim Betreten der Küche ist der Backofen ausgeschaltet. 

### US3 · Essen aufwärmen
Als Person, die gerne warme Speisen isst, möchte ich das kalte Essen aufwärmen. 
- [ ]  Der Backofen ist nur auf eine niedrige Stufe eingeschaltet.

There are logical conflicts between the user stories, as they contradict each other. The first story requires the oven to be on, while the second requires it to be off. The third story requires it to be on at a low setting. Let us simplify the user stories to just controlling the oven with a pir sensor, and ignore the other two stories. The pir sensor will be connected to the Pico 2 W and controlled by the program. Suplement the oven with a LED to indicate when it is on.

Parts list:
- 1x Pico 2 W
- 1x Breadboard
- 1x LED rot
- 1x PIR Bewegungsmelder HC-SR501
- if necessary, add resistors for the LED