print 'Welcome to a crease/section of folded paper calculator!'
print 'Input the number of creases before the number of folds that you want to find out.'
print 'However, it does round down to the nearest non-float.'
preCrease = float(raw_input('> '))
nowCrease = int(preCrease * 2 + 1)
nowSect = int(nowCrease + 1)
print 'You folded again, and now you have ' + str(nowCrease) + ' creases, and ' + str(nowSect) + ' sections.'