from flask_caching import Cache
import os
from dotenv import load_dotenv

load_dotenv()

cache = Cache(config = {
    
      'CACHE_TYPE': 'redis',
      'CACHE_REDIS_URL':os.environ.get('CACHE_REDIS_URL')
      
})
