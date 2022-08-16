from subprocess import call
from time import time

def new_compyle(): # TODO: Implement generating new compiling scripts
  print("Source Files :: ", end='')
  files = input().split()

  print("Options :: ", end='')
  options = input().split()

def run(cmd, options):
  commands = cmd.split(' && ')
  cmd = commands[0] + ' && ' + commands[1]
  start = time()
  call(cmd, shell=True)
  stop = time()
  print(f'\nCompile time: {stop - start}s')

  cmd = commands[0] + ' && ' + commands[2]
  start = time()
  call(cmd, shell=True)
  stop = time()
  print(f'Program run time: {stop - start}s')
  if not options[0]:
    cmd = commands[0] + ' && ' + 'rm a.out'
    call(cmd, shell=True)

def start():
  print("Load script? (y/n) :: ", end='')
  loadAns = input()
  if(loadAns == 'y'):
    with open('/home/xander/Documents/scripts/compyle_saved_scripts.txt', 'r+') as sList:
      count = 0
      scripts = []
      options = [False] * 2
      lines = sList.read().split('\n')
      lines.remove('')

      for line in lines:
        scripts.append(line.split(' ', 1))
      if len(scripts) == 0:
        print("No Saved Scripts!")
        new_compyle()
      else:
        for i, item in enumerate(scripts):
          print(str(i) + ': ' + str(item[0]))
        i += 1
        print(str(i) + ': CLEAR SAVED SCRIPTS')

        print("\nChoose :: ", end='')
        opt = input()
        if int(opt) == i:
          print("Are you sure you want to DELETE all saved scripts? (y/n) :: ", end='')
          clearAns = input()
          if clearAns == 'y':
            sList.truncate(0)
        else:
          print(f'\nSelected {scripts[int(opt)][0]}')
          print("Options? (kd) :: ", end='')
          optInput = input()
          print()
          for c in optInput:
            if c == 'k':
              options[0] = True
          run(scripts[int(opt)][1], options)



start()
