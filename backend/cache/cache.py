from flask_caching import Cache
#import configparser

'''
configini = configparser.ConfigParser()
configini.read('config.ini', encoding='utf-8')
'''

cache = Cache(config = {
      'CACHE_TYPE': 'redis',
      'CACHE_REDIS_HOST': 'redis-11312.c1.asia-northeast1-1.gce.cloud.redislabs.com',
      'CACHE_REDIS_PORT': 11312,
      'CACHE_REDIS_PASSWORD':'EhUEQfWBAnaMHOjPbFbDFqZja3yfx3rL'
})