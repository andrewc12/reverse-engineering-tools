import gdb
import math
import datetime

class DumpMem (gdb.Command):
  """Dump memory in blocks"""

  def __init__ (self):
    super (DumpMem, self).__init__ ("dos dump-mem", gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):
    print (arg)
    args = gdb.string_to_argv(arg)
    print (args)
    length = 2 ** int(args[0])
    blocksize = 2 ** int(args[1])
    
    filename = "result0"
    filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S%f")
    if len(args) > 2:
        filename = args[2]
    
    
    print (length, blocksize, filename)
	
    start=0
    end=math.ceil(length / blocksize) - 1
    inf = gdb.inferiors()[0]
    fo = open(filename + ".bin", "wb")
    fe = open(filename + ".log", "w")
    for x in range(start, end):
      try:
        fo.write(inf.read_memory(x*blocksize,blocksize))
      except:
        fo.write(bytearray(blocksize))
        fe.write(str(x*blocksize) + "\n")
        #print(str(x*256))
    fo.close()
    fe.close()

DumpMem ()
