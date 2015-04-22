
names = [ "locked_read", "locked_write", "acquiring_read", "acquiring_write" ]

def doData():
    data = getServerStatus()['locks']
    totals = { 'locked': { 'read': 0, 'write': 0 }, 'acquiring': { 'read': 0, 'write': 0 } }

    for key in data:
      if key != '.':
        totals['locked']['read'] += int(data[key]['timeLockedMicros']['r'])
        totals['locked']['write'] += int(data[key]['timeLockedMicros']['w'])
        totals['acquiring']['read'] += int(data[key]['timeAcquiringMicros']['r'])
        totals['acquiring']['write'] += int(data[key]['timeAcquiringMicros']['w'])

    print names[0] + ".value " + str( totals['locked']['read'] )
    print names[1] + ".value " + str( totals['locked']['write'] )
    print names[2] + ".value " + str( totals['acquiring']['read'] )
    print names[3] + ".value " + str( totals['acquiring']['write'] )

def doConfig():
    print "graph_title MongoDB write lock percentage"
    print "graph_args --base 1000 -l 0 "
    print "graph_vlabel percentage"
    print "graph_category MongoDB"

    for name in names:
      print name + ".label " + name
      print name + ".type DERIVE"
      print name + ".cdef " + name + ",10000.0,/"
