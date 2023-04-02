from setuptools import find_packages,setup
from typing import List

'''
This function will return the list of requirements  
'''
HYPEN_E_DOT='-e .'
    
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() ## Avoid \n
        requirements=[req.replace("\n","") for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

## A metadata of the project
setup(name='mlproject',
      version='0.0.1',
      author='Chetan Shetty',
      author_email='chetanshetty1986@gmail.com',
      ## How does fins_packages work: Create a new folder say 'src'. If we want this source to be found as a package: create an
      ## __init__.py file. Now when find_packages runs it will go and find how many folder has __init__.py file. So it will directly
      ## consider the "src" as package and try to build it and hence will also allow you to import this as a package.
      packages=find_packages(),
      
      # If we nee to install 100-packages below would not be a feasible approach. Use function
            #install_requires=['pandas','numpy','seaborn'] : Not a feasible method
      install_requires=get_requirements('requirements.txt')  
      )

## Entire project development will happen inside the src folder