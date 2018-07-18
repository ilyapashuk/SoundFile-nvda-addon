__metaclass__ = type
import os
import winsound
import controlTypes
from nvdaBuiltin.appModules import explorer
import api
import data
loc = os.path.abspath(os.path.dirname(data.__file__))



def play(name):
 ft = os.path.splitext(name)
 fe = ft[1][1:]
 f = os.path.join(loc, fe + '.wav')
 if os.path.exists(f):
  winsound.PlaySound(f, winsound.SND_ASYNC)
class AppModule(explorer.AppModule):
	def event_gainFocus(self, obj, nextHandler):
		if obj.role == controlTypes.ROLE_LISTITEM:
			play(obj.name)
		super(AppModule, self).event_gainFocus(obj, nextHandler)

