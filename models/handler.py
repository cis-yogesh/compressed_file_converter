import os
from file_extractor import ExtractAll, AchieveAll
from . import file_stats,DELETE
class Handler(object):
    def __init__(self):
        self.filename=None
        self.output = None
        self.output_path = None
        self.output = None

    @property
    def setfilename(self):
        return self.filename

    @setfilename.setter
    def set_filename(self,setfilename):
        self.filename = setfilename

    @property
    def setoutput(self):
        return self.output

    @setoutput.setter
    def set_setoutput(self,setoutput):
        self.output = setoutput

    def execute(self):
        extract_obj = ExtractAll(filepath = self.filename,extract_path = None)
        extract_obj.executeall()
        achieve_obj = AchieveAll(filename = self.output)
        achieve_obj.executeall()



