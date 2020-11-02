__all__ = ['Pyracer']

__productname__ = 'Pyracer'
# Expecting trailing "-rcN" or "" for stable releases.
__version__     = "0.0.1"
__copyright__   = "Copyright 2020 Spiffily Software"
__author__      = "Coen F"
__author_email__= "trainsgreen@gmail.com"
__description__ = "Hit the ground running on your fresh Ubuntu installation."
__license__  = "Licensed under the MIT License."

#from offlineimap.error import OfflineImapError
# put this last, so we don't run into circular dependencies using
# e.g. offlineimap.__version__.
from pyracer.init import Pyracer
