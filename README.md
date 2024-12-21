```
Compile + run this python script to start painting 5x8 pixel grids.

If your arduino project has #include <LiquidCrystal.h> ...
did you know you can create your own characters??
They have to fit on a 5x8 grid, and you draw them using these little
guys:

byte road[8] = {
  B10101,
  B10101,
  B10001,
  B10101,
  B10101,
  B10001,
  B10101,
  B10101,
};

The 1's and 0's represent pixels that are off or on, you can almost see the image
that will be drawn if you look at the above numbers long enough.

The program itself will create a txt file (by clicking  "Save") for you that has 
the byte array for the fun new thing that you drew in the pixel painter.

Ideas for you to try:
bug
skull and crossbones
amongus

Once you make and export your txt file, you'll need to have some kind of lines in your
arduino code like:
-----
// probably global, before setup
LiquidCrystal lcd(...); // "..." represents whatever pin numbers you are using

// anywhere but probably in setup
lcd.createChar(x, foo);
// where x is between 0 and 7 (not sure if this is true, cause 0 was always weird for me), and 
//  foo is the name of the file you just saved (and more specifically, the name of the byte array).
//  (the byte array should probably be global or something as well, or better in a header file)
-----

The library lets you store up to 8 nonstandard characters so go crazy! Make a terrible walk
cycle.

You can display your character by doing something like:

lcd.setCursor(col, row);  // (0, 0) for the top left one, my display was 2x16 so 
                          // (0, 7) got me in the middle on the top row

lcd.write(byte(x));       // select the guy from before, maybe you can do this better?
                          // like with the name of the char you made? no clue i think you have to
                          // createChar() it first though and assign it a slot

aaaand that should probably do it!
```
