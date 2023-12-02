from flask_caching import Cache
import configparser

configini = configparser.ConfigParser()
configini.read('config.ini', encoding='utf-8')


cache = Cache(config = {
      'CACHE_TYPE': 'redis',
      'CACHE_REDIS_HOST': configini['redis']['REDIS_HOST'],
      'CACHE_REDIS_PORT': configini['redis']['REDIS_PORT'],
      'CACHE_REDIS_PASSWORD':configini['redis']['REDIS_PASSWORD']
})