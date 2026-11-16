### US1 · Raffstore Anwendung per Handbewegung (Muss)
Als Hausbesitzer möchte ich mit meinen Händen das hoch/runter fahren des Raffstores beeinflussen.

- [ ] Sobald die Hand über den Sensor gestrichen wird gehen die Raffstores hoch.
- [ ] Sobald die Hand den Sensor drückt, gehen die Raffstores hoch.

### US2 · Als Hausbesitzer möchte ich, dass die Raffstores bei bestimmten Uhrzeiten automatisch hoch/runter fahren.(Muss)
- [ ]  Um 5:30 Uhr sollen die Raffstores hochgehen.
- [ ]   Um 19:30 Uhr sollen die Raffstores runterfahren.

### US3 · Als Hausbesitzer möchte ich, dass bei Wind die Raffstores automatisch hochfahren. (Muss)
- [ ] Sobald Wind die Raffstores mit einer Stärke von 38 km/h berührt, sollen diese hochfahren.

We don't have raffstores, so we will use indicator lights instead. The Raffstore will be represented by a LED, one color for up and another for down. The LED will be connected to the Pico 2 W and controlled by the program. Simplify the user stories to just controlling the LED with hand movement and time, and ignore the wind part. Use a taster for the hand movement and a real time clock for the time-based control.

Parts list:
- 1x Pico 2 W
- 1x Breadboard
- 1x LED rot
- 1x LED gelb
- 2x Taster Up/down
- if necessary, add resistors for the LED