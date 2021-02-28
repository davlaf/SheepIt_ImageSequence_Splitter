# SheepIt_ImageSequence_Splitter
Splits blender projects by 500mb chunks to make it easier to upload projects with image sequences in them.

## Why is this useful
I have a blender project which contains image sequences using the Import Images as Planes plugin. I use SheepIt Renderfarm to render my project, which has a 500mb upload limit. With my images being around 2-3 mb each, and my projects being 2000-3000 frames long, that would mean I would need to split my projects in dozens of parts manually. So I coded a python script to do it automatically.

## How to use
Put all of your images for the image sequence, the .blend file, the texture folder and the python script in the same folder. Open the python script in an editor and change these variables to the appropriate values:
```python
BLEND_FILE_NAME = "project.blend" # Name of the .blend file
TEXTURE_FOLDER_NAME = "textures" # Name of the folder with textures
MAX_FILE_SIZE = 499000000 # Maximum size in bytes
START_FRAME = 1 # Frame to start splitting
END_FRAME = 1500 # Frame to stop splitting (these don't affect the .blend file)
```
Sit back and run split.py. It will create .zip files named as the frames that it contains. The blend will not have the start and end frame configured though, so you will need to set those in the SheepIt render settings. It does create a replicate folders for all the zip files but I am too scared to delete a bunch of files using a python script, so you will need to delete them manually.

## IMPORTANT:
**Use relative path in your .blend file with your images in the same folder as the blend!** Be sure that the relative paths are to the one in the same folder. To set relative path, go to File -> External Data -> Make all paths relative. A good way to get all your textures into one textures folder with all the right paths is to pack your blend then unpack it. 
