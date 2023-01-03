
from class_one import *

print(variable_public)
print(_variable_protected)
print(__variable_private)

## import * dont import the protected and private objects

import class_one

print(class_one.variable_public)
print(class_one._variable_protected)
print(class_one.__variable_private)

'''
import class_one
print(dir(class_one))
'''


import class_one
class_one.sample._sample__test()
## Mangling in python 
'''
'''
import class_one
class_one.__sample._sample__test()
## Mangling in python

import class_one
class_one._mthod()


############################################
## Manually import modules
import importlib.util
import sys
spec = importlib.util.spec_from_file_location("module.name",'class_one.py')
sample_module = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = sample_module
spec.loader.exec_module(sample_module)
sample_module._mthod()

#########################

# Restricted Module :
# Below is a way , using which we can make sure , a module can not be imported .
# This is called restricted import

import importlib

def secure_importer(name,globals=None,locals=None,fromlist=(),level=0):

    if name=='class_one':
        raise ImportError ("Hey CLass One is restricted ")

    return importlib.__import__(name,globals,locals,level)

__builtins__.__dict__['__import__'] = secure_importer

import class_one
