"""
Detector classes
"""

import logging
from ophyd.areadetector.base import ADComponent
from pcdsdevices.epics.pim import PIMPulnixDetector
from pcdsdevices.epics.areadetector.cam import CamBase
from pcdsdevices.epics.areadetector.detectors import DetectorBase


logger = logging.getLogger(__name__)

# Cam Classes


class GigeCam(CamBase):
    """
    Gige cam class
    """
    def __init__(self, prefix, name=None, desc=None, *args, **kwargs):
        self.desc = desc or name
        super().__init__(prefix, name=name, *args, **kwargs)
        if self.desc is None:
            self.desc = self.name        


# Detector Classes


class GigeDetector(DetectorBase):
    """
    Gige detector class.
    """
    cam = ADComponent(GigeCam, ":")
    def __init__(self, prefix, name=None, desc=None, *args, **kwargs):
        self.desc = desc or name
        super().__init__(prefix, name=name, *args, **kwargs)
        if self.desc is None:
            self.desc = self.name        

class OpalDetector(PIMPulnixDetector):
    """
    Opal detector class.
    """
    def __init__(self, prefix, name=None, desc=None, read_attrs=None, *args, 
                 **kwargs):
        self.desc = desc or name
        if not read_attrs:
            read_attrs = ["stats2"]        
        super().__init__(prefix, name=name, read_attrs=read_attrs, *args, 
                         **kwargs)
        if self.desc is None:
            self.desc = self.name        
            



