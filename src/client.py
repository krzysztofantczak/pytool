import features.consumer as api
import time

# com = api.com()
# time.sleep(4)
# com.rpc('rycbar123', 2)
# com.rpc('aqq', {'foo': 'bar'})
# com.rpc('ferdek')

# com = api1.com()
# com.start('aqq')
# api.storage.init('my-app-id');

# fetch simple string value
print api.storage.init('my-app-id').get('pik');

# fetch dict value ;-)
print api.storage.init('my-app-id').get('foo');
print api.storage.init('my-app-id').get('foo')['mrs'];
