import unittest

loader = unittest.TestLoader()
suite = loader.discover('cases')
unittest.TextTestRunner(verbosity=2).run(suite)
