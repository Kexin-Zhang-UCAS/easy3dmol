from type import *

class Label(dict):
    def __init__(self,tag:string,parameters:LabelSpec):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            if eval(key) != None:
                self[key] = eval(key)