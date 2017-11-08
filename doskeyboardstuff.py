import gdb
import struct

def linearfromsegment(segment, offset):
    return (segment << 4) + offset

def stuffkey (char):
    inf = gdb.inferiors()[0]
    
    #read the near pointers
    buffer_start, buffer_end = struct.unpack('HH', inf.read_memory(0x480,0x4))
    #print(buffer_start, buffer_end)
    buffer_head, buffer_tail = struct.unpack('HH', inf.read_memory(0x41a,0x4))
    #print(buffer_head, buffer_tail)
    
    temp_tail = buffer_tail
    buffer_tail = buffer_tail + 2
    if (buffer_tail >= buffer_end):
        buffer_tail = buffer_start
    if (buffer_tail == buffer_head):
        return 0
    
    #write new key then update the pointer
    linear_temp_tail = linearfromsegment(0x40,temp_tail)
    inf.write_memory(linear_temp_tail, struct.pack('H', char),0x2)
    inf.write_memory(0x41c, struct.pack('H', buffer_tail),0x2)
    #print(buffer_head, buffer_tail)
    
    return 1


class Insertchar (gdb.Command):
  """Insert a char into the keyboard buffer."""

  def __init__ (self):
    super (Insertchar, self).__init__ ("dos insertchar", gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):    
    stuffkey(ord(arg)+ (0x02 << 8))

class Insertcode (gdb.Command):
  """Insert a code into the keyboard buffer."""

  def __init__ (self):
    super (Insertcode, self).__init__ ("dos insertcode", gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):
    stuffkey(int(arg, 16))

	
	  
Insertchar ()
Insertcode ()