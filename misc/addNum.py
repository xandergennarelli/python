# Author: Xander Gennarelli
# Date: 2/18/2022
# Description: Prepends numbers to the file names of songs downloaded
#              from spotdl.
# Arguments: File path to .m3u file
import os, sys

path = ""
newNameList = ""    # will replace the .m3u file with updated file names
fName = sys.argv[1]     # argument

splitName = fName.rsplit('/', 1)    # removes the name of the .m3u file from
if (len(splitName) > 1):            # the file path
    path = splitName[0] + "/"

try:    # try for file name errors
    with open(fName, 'r') as f:     # open .m3u file named in argument
        n = 1;  # number prepended to file name

        for line in f:
            name = line[:-1]    # removes '\n'
            newName = f'{n:02} - {name}'    # prepends n
            os.rename(f'{path}{name}', f'{path}{newName}')  # renames file

            newNameList = newNameList + newName + "\n"  # adds new file name to
                                                        # replacement string
            n += 1

    with open(fName, 'w') as f:
        f.write(newNameList)    # update file names in .m3u file

    print ("Done!")
except (FileNotFoundError):
    print ("Bad file name!")

# spotdl --m3u '[url]'
