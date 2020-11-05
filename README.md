# TV Head
This repo is to document and explain my TV head hardware project as well as hosting the code that was used and written.

## Process
To start this project, I needed a willing volunteer CRT to hollow out and use as the casing. Fortunately, CRTs are still fairly available in local recycling communities which is where I got mine. However, they are increasingly difficult to get hold of due to there simply not being all that many left. PC monitor CRTs are the best since they are usually a much more appropriate size than TV CRTs.

This was the one I got, I picked it up for free from someone who was trying to get rid of it.
![Original CRT](https://imgur.com/6BkXWam.png)

Now, the CRT needed to be gutted out. This can be a dangerous process if proper precautions are not taken as CRTs act essentially as high power capacitors and hold a charge for a very long time, even when unplugged. There are several tutorials online on how to safely discharge a CRT, but it essentially boils down to shorting the wire connected to the flyback transformer (usually a bright red wire that goes into the glass vacuum tube with a rubber sucker like ending) to the ground loop around the CRT, which usually looks like a wire wrapping around the back of the vacuum tube.

Once this is done and the insides are removed, they should be safely disposed of. Check your local laws and waste site information on how to do so.
![The flyback wire that needs to be connected to ground](https://i.imgur.com/hzhJYXl.png)
![The vacuum tube itself as well as some of the electronics controlling it. Note the scary looking lightning sticker on it.](https://i.imgur.com/8qA9mSR.png)
![The casing I was interested in](https://i.imgur.com/XxvZRAI.png)

From here, you can pretty up the casing as you wish. If it's an old CRT though, you may want to give it a good clean before doing anything. I chose to paint mine black and white, with the front panel controls also being black.

There are quite a few tutorials online on how to paint plastic, make sure you buy the right paints and primer if needed.
![The painted case](https://i.imgur.com/HyeUmQT.png)
![The front panel](https://i.imgur.com/Gsl3ej7.png)

Now you will want to put something to cover up the screen gap in the front. To do this, I used a sheet of 3mm acrylic covered with some window privacy film. This makes it so that you can't see into the TV head, but you can see out as well as being able to see the LED matrix we'll put behind it soon.
It's harder than it sounds since the acrylic needs to be warped slightly to give it the slight bulging effect that real cathode ray tube displays have.
![The front panel from behind - hot glue is used to fix the acrylic to the frame](https://i.imgur.com/plDqiog.png)
![The assembled TV with the 'glass' in place](https://i.imgur.com/OoeJQSH.png)

I had to solder the panels together to get my desired size, and held the panels together with superglue and lollipop sticks.
![Wires being soldered to the contacts on the board. My soldering iron is not particularly good!](https://i.imgur.com/RWd8HiB.png)
![The back of the completed panel structure](https://i.imgur.com/RAXNlaq.png)

Here's the interesting part. I used a raspberry Pi 2 (and the software hosted here is for the Pi too) and some Max7219 LED maxtrix panels to work as the display driver and display. A cut out bin bag was taped over the led panels to diffuse the light better as well as to hide the off pixels, which look white and would be visible behind the 'glass'.
![The Pi and the LED panels](https://i.imgur.com/qPDHBIQ.png)

While something like an Arduino would probably be more appropriate, I didn't want to buy one since I had a perfectly good Pi 2 sitting around and waiting to be used. Plus, I had wanted to do a Pi hardware project with the GPIO pins and never really had an excuse to do one before.

I used this repo to help me drive the LED matrix panels, as it includes a driver for the Max7219 display driver as well as a python module to interface with it:
https://github.com/rm-hull/luma.led_matrix

With SSH I went into the Pi and set up the software I'd need. I also set the script to run on startup so that I didn't need to run it manually.

To control the different faces on the display, I reused some of the old push buttons that were on the CRT front panel board by desoldering them and reconnecting them to GPIO wires that could plug into the Pi. Be warned however, a soldering iron's heat can melt the plastic insides of the button, rendering it inoperable.

I built a structure out of hot glue and lollipop sticks to hold the display and pi in place, as well as fix my buttons in place to the front panel.
![Behind the front](https://i.imgur.com/EdORCA8.png)

All I needed to do now was power it on with a USB power bank and wear it!
![What you came to see](https://i.imgur.com/aFeNZbh.png)
![What you came to see](https://i.imgur.com/9rgsCsi.png)
