import gdb
import math
class DumpMem (gdb.Command):
  """Greet the whole world."""

  def __init__ (self):
    super (DumpMem, self).__init__ ("dos dump-mem", gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):
    print (arg)
    args = gdb.string_to_argv(arg)
    print (args)
    length = 2 ** int(args[0])
    blocksize = 2 ** int(args[1])
    print (length, blocksize)
	
    start=0
    end=math.ceil(length / blocksize) - 1
    inf = gdb.inferiors()[0]
    fo = open("result0.bin", "wb")
    fe = open("result0e.bin", "w")
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