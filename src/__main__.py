import features.provider as api

# api1.com.test()
# api1.storage.test()
# api1.ui.test()

print ""

# api2.com.test()
# api2.storage.test()
# api2.ui.test()

# api1.ui.init()
# print "initialization"
# api1.ui.alert("The document has been modified.")

# start storage service
api.storage.init('my-app-id');
api.storage.init('my-app-id').set('pik', 'pok');
api.storage.init('my-app-id').set('foo', {"mrs" : 'tadaaa'});

# start communication service
api.com.init('foo')
