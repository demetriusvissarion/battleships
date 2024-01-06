import sys
from lib.play import Play



class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)

io = TerminalIO()

############## "Play" class uses both players game instances to fire shots and decide the winner
play = Play(io)
play.run()