from flask_caching import Cache
#import configparser

'''
configini = configparser.ConfigParser()
configini.read('config.ini', encoding='utf-8')
'''

cache = Cache(config = {
      'CACHE_TYPE': 'redis',
      'CACHE_REDIS_HOST': 'redis://red-cmto527109ks73adonlg',
      'CACHE_REDIS_PORT': 6379,
})