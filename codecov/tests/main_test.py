from nose.tools import eq_
from codecov import some_module


def Main_test():
    eq_(some_module.Some_Function(), 1)
