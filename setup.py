# !./bin/python3
# *-* coding: utf-8 *-*
'''
             __   ___ ___       __      __   __   __        ___  __  ___ 
            /__` |__   |  |  | |__)    |__) |__) /  \    | |__  /  `  |  
            .__/ |___  |  \__/ |       |    |  \ \__/ \__/ |___ \__,  |  
                                                                                                                                                                                
Description: Template main file for Python scripts.
Author: Fabio Craig Wimmer Florey <TAG:EMAIL>
Company: <TAG:COMPANY>
=========================================================================================
                This script is under GNU General Public License v3.0
'''

from distutils.core import setup

setup(
    version='0.1-dev',
    name='Project Title',
    author='Fabio Craig Wimmer Florey',
    author_email= '<TAG:EMAIL>',
    maintainer= 'Fabio Craig Wimmer Florey',
    maintainer_email= '<TAG:EMAIL>',
    packages=['project_title',],
    license='GPLv3.0',
    keywords=[],
    description=open('README.txt').read()
)