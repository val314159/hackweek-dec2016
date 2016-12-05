
print "Is Tf installed?"

import tensorflow as tf

print "Tf Version: %s" % tf.__version__

print "Is Tf Slim installed?"


import tensorflow.contrib.slim as slim

eval = slim.evaluation.evaluate_once

#exit(2)
