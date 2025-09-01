from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

logging.info('this is a test')

try:
    y = int('abc')
    
except Exception as e:
    raise USvisaException(e)