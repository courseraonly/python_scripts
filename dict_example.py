userdict = {'efr':'Efren Reyes','mki':'Mika Immonen'}

print userdict['efr']
print userdict.keys()

test = 'DevOps dude'
secondi = ['/home/debug/master/build/platform','/home/debug/master/build/rpm-platform']
#print secondi
secondi.append("/home/debug/%s" % test)
secondi.append("XXXX")
#print secondi

for x in secondi:
  if not x == "XXXX":
    print x
  else:
    print 'somethingXXXX'
