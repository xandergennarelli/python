from PIL import Image

def rgb2hex(r, g, b):
  return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def scan(imName, fNameOut):
  im = Image.open(imName, 'r').convert('RGB')
  pix_val = list(im.getdata())
  pix_hex = []
  for r, g, b in pix_val:
    pix_hex.append(rgb2hex(r, g, b))

  w, h = im.size
  o = open(fNameOut, 'w')
  strSize = '' + str(w) + ' ' + str(h) + '\n'
  o.write(strSize)

  count = 0
  for hex in pix_hex:
    count += 1
    switcher = {
      '#ffffff': 0,
      '#000000': 1,
      '#ff0000': 2,
      '#00ff21': 3,
      '#00ffff': 4,
      '#ffd800': 5,
      '#404040': 6
    }
    strVal = str(switcher.get(hex, "7")) + ' '
    o.write(strVal)
    if count == w:
      count = 0
      o.write('\n')
  o.close()

def script():
  print("Enter Sprite Name:: ", end = '')
  name = input()
  srcName = "/home/xander/Documents/CPP/BasicPrograms/ECGame/source/" + name + ".png"
  datName = "/home/xander/Documents/CPP/BasicPrograms/ECGame/source/" + name + ".dat"

  scan(srcName, datName)
  print("Done!")

script()
