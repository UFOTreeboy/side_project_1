from flask_caching import Cache
import os
#import configparser

'''
configini = configparser.ConfigParser()
configini.read('config.ini', encoding='utf-8')
'''

cache = Cache(config = {
      'CACHE_TYPE': 'redis',
      'CACHE_REDIS_URL':os.environ.get('CACHE_REDIS_URL')
})