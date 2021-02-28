import os
import shutil
import datetime

BLEND_FILE_NAME = "example.blend" # Name of the .blend file
TEXTURE_FOLDER_NAME = "textures" # Name of the folder with textures
MAX_FILE_SIZE = 50000000 # Reduced the file size to make splitting more apparent
START_FRAME = 1 # Frame to start splitting
END_FRAME = 250 # Frame to stop splitting (these don't affect the .blend file)

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

totalSize = 0
for i in range(START_FRAME,END_FRAME+1):
    imageName = str(i).zfill(4)+".png"
    imageSize = os.path.getsize(imageName)
    totalSize += imageSize
    #print(f'The size of {imageName} is {imageSize:,} bytes')
print (f'Total size is {totalSize:,} bytes')

blendSize = os.path.getsize(BLEND_FILE_NAME)
texturesSize = get_size(TEXTURE_FOLDER_NAME)
assetsSize = blendSize + texturesSize

numOfSections = 0
sectionTotalSize = 0
currentFrame = START_FRAME
while True:
    # Get section start and end
    sectionSize = assetsSize
    sectionStart = currentFrame
    while True:
        imageName = str(currentFrame).zfill(4)+".png"
        imageSize = os.path.getsize(imageName)
        sectionSize += imageSize
        if sectionSize > MAX_FILE_SIZE:
            sectionSize -= imageSize
            break
        currentFrame += 1
        if currentFrame > END_FRAME:
            break
    sectionEnd = currentFrame - 1
    numOfSections += 1
    print(f"Section #{numOfSections}: From frame {sectionStart} to {sectionEnd} ({sectionEnd-sectionStart} frames), size is {sectionSize:,} bytes")
    # Make a directory and move the files to it, then zip it
    moveDirectoryName = f"{sectionStart}-{sectionEnd}"
    os.mkdir(moveDirectoryName)
    shutil.copyfile(BLEND_FILE_NAME,f".\{moveDirectoryName}\{BLEND_FILE_NAME}")
    shutil.copytree(TEXTURE_FOLDER_NAME,f".\{moveDirectoryName}\{TEXTURE_FOLDER_NAME}")
    print("Copying images...")
    for i in range(sectionStart,sectionEnd+1):
        imageNameMove = str(i).zfill(4)+".png"
        shutil.copyfile(imageNameMove,f".\{moveDirectoryName}\{imageNameMove}")
    print("Creating archive...")
    shutil.make_archive(moveDirectoryName, 'zip', moveDirectoryName)
    # Once it's finished
    if currentFrame > END_FRAME:
        break

now = datetime.datetime.now()
currentTime = now.strftime("%H:%M:%S")
print("-------------------------")
print(f"Finished at {currentTime}")
os.system('pause')
