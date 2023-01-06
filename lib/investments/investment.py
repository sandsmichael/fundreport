import pandas as pd
import json
import importlib

# from investments import gic

class Investment:
    " A generic class for interfacing with an investment template and instantiating the appropriate object to represent it. "

    def __init__(self, fp:str) -> None:
        self.fp = fp
        self.investment = self.read_template()
        print(self.investment)
        self.instance = self.dynamic_instantiation()
    
    def read_template(self):
        ''' read the json template into a dictionary '''
        with open(self.fp, 'r') as file:
            investment = json.load(file)
        return investment

    def dynamic_instantiation(self):
        ''' dynamically instantiate an object of the respective class based on the string investment_type field in the investment's .json file '''
        investment_type = self.investment['investment_type']
        module = importlib.import_module('investments.gic')  # module = __import__("investments")
        class_name = "Traditional_GIC"
        class_ = getattr(module, class_name)
        instance = class_()
        return instance
