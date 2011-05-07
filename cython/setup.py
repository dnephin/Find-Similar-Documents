from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("cutil", ["cutil.pyx"])]

setup(
  name = 'Cython utils',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
