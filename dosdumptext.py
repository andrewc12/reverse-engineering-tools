import gdb
import struct
#todo prep for github
class DosDumpText (gdb.Command):
  """Dump the text memory of the inferior and display it on the terminal."""

  def __init__ (self):
    super (DosDumpText, self).__init__ ("dos dump-text", gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):
    inf = gdb.inferiors()[0]
    textmemaddr = 0xb8000 #text mode base address
    #rows = 25

    cols = struct.unpack('B', inf.read_memory(0x44a,0x1)) #Get the number of columns from bios memory
    cols = cols[0]
    scanlines = 400

    texth = struct.unpack('H', inf.read_memory(0x485,0x2)) #Get the text height from bios memory
    #print(texth)
    texth = texth[0]
    
    rows = int(scanlines / texth) #Calculate the number of rows

    buf = inf.read_memory(textmemaddr,cols*rows*2) #Dump the memory all at once
    alltext = list(struct.iter_unpack('BB', buf))  #Turn into a list of text and attribute pairs
    #print(alltext)
      
    
    for y in range(0, rows):
      #print(inf.read_memory(textmemaddr+y*cols*2,cols*2))
      text = ""
      attr = []
      
      for x in range(0, cols): #Read the row, there are two bytes for every character 
          yoffset = y*cols
          xoffset = x
          
          
          text = text + chr(alltext[yoffset + xoffset][0]) #Assemble a line of text character by character  
          attr.append(alltext[yoffset + xoffset][1]) #Store the attributes in their own list
      #print(text)
      print(text.rstrip())
      #print(attr)
	  
DosDumpText ()
