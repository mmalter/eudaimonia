from distutils.core import setup
import os

setup(name='eudaimonia',
	version='0.1',
    description='Daemonizer for Python',
    author='Michaël Malter',
    author_email='dev@michaelmalter.fr',
    package_dir={'eudaimonia': 'src'},
    packages=['eudaimonia'],
    install_requires=[
        'sys', 'os', 'time', 'atexit', 'signal'
      ]
	)
