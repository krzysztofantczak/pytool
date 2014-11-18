import features.consumer as api
import time

com = api.com()
# time.sleep(4)
com.rpc('rycbar123', 2)
com.rpc('aqq', {'foo': 'bar'})
# com.rpc('ferdek')

# com = api1.com()
# com.start('aqq')
