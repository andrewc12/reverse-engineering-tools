import gdb
class DosPrefixCommand (gdb.Command):
  "Prefix command for dos things."

  def __init__ (self):
    super (DosPrefixCommand, self).__init__ ("dos",
                         gdb.COMMAND_SUPPORT,
                         gdb.COMPLETE_NONE, True)

DosPrefixCommand()