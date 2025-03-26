# Arabic-accented-composite-glyphs
A quick and dirty FontForge Python script that combines each letter (حرف) with each accent (حركة) into a new single Glyph.

Useful for legacy softwares that do not render Harakat properly.

Load the font you wish to use into FontForge and run the script. By default, new Glyphs will be created at the Private Use Area (PUA).

Save the font and load it into your software, then use the newly generated Glyphs to force the software to render Harakat correctly.
