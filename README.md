# ShortsAutoCreator
A tool to create short vertical videos of memes automatically

## Documentation
To start using the program first create 3 folders with the names "assets", "content" and "temp".

### Explanation of folders:
- In the "assets" folder is where the outro, the text and the watermark will be.
- In the "content" folder is where the background video and 3 images are.
- In the "temp" folder is where some files are temporarily saved, they are automatically deleted after finishing the entire program.

### Assets sizes (in the "assets" folder)
  - Create a 139x66 image with the name "name.png", that's where you put your name, like a watermark.
  - Create a text with dimensions 549x103 with the name "text.png".
  - Create a final video with the dimensions 720x1280 with the name "outro.mp4", it can be any duration, a recommendation is that be 3 or 4 seconds.

### Content Folder
  - Create a background video called "background.mp4", you can use any dimension, since it will adjust automatically, a recommendation is that it be 720x1280.
  - Create 3 files with the names of "image1.jpg", "image2.jpg" and "image3.jpg", it can be any size, that's where you put the 3 images.

### Usage
You can use the program in menu mode or in parameter mode
- ```python sac.py``` Will automatically execute the menu
- ```python sac.py -p up|down``` It is where you put the position of the text.png

### ⚠ There may be errors, if you find one please put it in the issues.

  
  
