'''
Created on Jan 24, 2019

@author: mo
'''
from setuptools import setup

setup(name = "systeminfo",
      version = "0.1",
      description = "Basic System Information for COMP30670",
      url = "",
      author = "Mo Fiebiger",
      author_email = "moriah.fiebiger@ucdconnect.ie",
      license = "GPL3",
      packages = ['systeminfo'],
      entry_points = {
          'console_scrits':['COMP30670_systeminfo=systeminfo.main:main']
                      }
      )