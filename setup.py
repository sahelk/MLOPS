from setuptools import setup, find_packages

#find package will look for the __init__ constructor file inside of each folder and
#whenever it is present it considers that folder as my local package

setup(
    name = 'us_visa',
    author = 'sahel',
    version = '0.0.0',
    author_email= 'sahel.keyvan@gmail.com',
    packages = find_packages()
)