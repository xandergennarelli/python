def format(fNameIn, fNameOut):
    with open(fNameIn) as f:
        l = f.readline()
        while l != '':
            o = open(fNameOut, 'a')
            str = "  cout << \"" + l[0:65] + "\"\n       << \"" + l[65:130] + "\"\n       << \"" + l[130:len(l)-1] + "\" << endl;\n"
            o.write(str)
            o.close()
            l = f.readline()


fIn = "/home/xander/Documents/python/inFile.txt"
fOut = "/home/xander/Documents/python/outFile.txt"
format(fIn, fOut);
