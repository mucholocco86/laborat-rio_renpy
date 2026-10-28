PLAYER MESSAGE VISIBILITY FIX

Replace:

1. PhoneTexting.rpy
   Destination:
   game/code/2 misc/PhoneTexting.rpy

2. script2.rpy
   Destination:
   game/code/6 messenger emu/script2.rpy

Keep only ONE script2.rpy in the game. Do not also place it in:
game/code/5 events/release 1/

Delete these compiled files before launching the game so Ren'Py rebuilds them:

- game/code/2 misc/PhoneTexting.rpyc
- game/code/6 messenger emu/script2.rpyc

What was fixed:

- The player-message text was being moved 580 pixels to the left, outside its
  message frame. That player-only offset was removed.
- script2.rpy keeps the story-memory tooltip table and the original
  player_msg() messenger helper.

The .rpyc files should not be copied from this package. Ren'Py creates them.
