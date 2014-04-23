ADA
===

Autonomous Digital Assistant

General Idea :
---
The general idea is to make a vocal assistant taking advantage of all of API and service now available out there.
It will mainly be built in Python with easy modularity in mind.

Process :
---
Voice input -> STT -> Google -> Match module -> Exec module -> TTS Answer -> Output answer

**Workflow :**<br/>
**-> Test recognition + print input/output** <br/>
Test voice AND print output <br/>
Test 2 phase recognition ("Name to wait then execute order or timeout)<br/>
Test interpretation command and execution <br/>
Test interpretation from AIML file <br/>
Test GUI (fullscreen, printed output, voice animation)

Module Ideas:
---
- Easy
  - Say something
  - Ask time
  - Translation (Google Translate)
  - Calculation <br/>
- Medium
  - Meteo
  - Lights (hardware need) <br/>
- Hard
  - Music (+TV/Mediacenter/XBMC server)
  - eMail <br/>

Improvements:
---
- Use PyGSR for the GoogleAPI access
- GUI: Tkinter (+Tksnack for sound display)
- Create Client/Server interface to control TV/XBMC through HDMI (CEC)
- AIML: Based on Pandorabots ?
- Support for W-Zave/X10 infrastructure
- Voice: Modify before playing with Tksnack ?
