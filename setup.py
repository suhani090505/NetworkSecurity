'''
The setup.py file is as essential part of packaging and distributing python Projects. It is used by setup tools to define configuration of your project, such as metadata, dependencies and more.
setup.py is a special Python script used to define how a Python project should be packaged, installed, and shared 
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
  """
  This function will return list of requirements.
  """
  requirement_list:List[str]=[]
  try:
    with open('requirements.txt','r') as file:
      #Read lines from the file
      lines=file.readlines()
      #Process each line
      for line in lines:
        requirement=line.strip()
        #If requirement is empty space or -e. , ignore
        if requirement and requirement!='-e .':
          requirement_list.append(requirement)

  except FileNotFoundError:
    print("file not found error")

  return requirement_list

setup(
  name="Network Security",
  version="0.0.1",
  author="Suhani suman",
  packages=find_packages(),
  install_requires=get_requirements()
)
