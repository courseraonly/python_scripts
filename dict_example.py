userdict = {'efr':'Efren Reyes','mki':'Mika Immonen'}

print userdict['efr']
print userdict.keys()

test = 'Praveen'
secondi = ['/home/debug/nms-trunk/build/platform','/home/debug/nms-trunk/build/rpm-platform']
#print secondi
secondi.append("/home/tits/%s" % test)
secondi.append("XXXX")
#print secondi

for x in secondi:
  if not x == "XXXX":
    print x
  else:
    print 'somethingXXXX'