
# This module can be accessed by a python controller with
# its execution method set to 'Module'
# * Set the module string to "gamelogic_module.main" (without quotes)
# * When renaming the script it MUST have a .py extension
# * External text modules are supported as long as they are at
#   the same location as the blendfile or one of its libraries.

import GameLogic

# variables defined here will only be set once when the
# module is first imported. Set object spesific vars
# inside the function if you intend to use the module
# with multiple objects.


class Player:
	def __init__( self, cont ):
		
        # initialize global variables
		self.controller = cont
        self.ob = cont.getOwner()
        self.ac = cont.getActuator("Action") 
        self.me = cont.getActuator("Message")
        self.po = cont.getActuator("Pos")
        self.he = cont.getActuator("Health")
        
        self.FRAMESPEED = 25
        self.WALKSPEED = 2.2
        self.MAXERR = 0.0125
        self.WAITMOD = 10
        
        if( not hasattr( ob, "gamespeed" ))
            self.gamespeed = 1.0
        
		self.ai_states = {
			"WAIT":  1,
			"KICK":  2,
			"DUCK":  3,
			"PUNCH": 4,
			"IDLE":  5
		}
		
		print self.random( 0, 7 )
	
	def random( self, begin, end ):
		return (begin + GameLogic.getRandomFloat( ) * (end + begin))
	

def main(cont):
	
	player = Player( cont )
	
	own = cont.owner
	
	"""
	sens = cont.sensors['mySensor']
	actu = cont.actuators['myActuator']
	
	if sens.positive:
		cont.activate(actu)
	else:
		cont.deactivate(actu)
	"""

main(GameLogic.getCurrentController())
