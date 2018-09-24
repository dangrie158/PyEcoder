# Workaround for issue in Python 2.7.3
# See http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'PyEcoder',
      version           = '0.1.0',
      author            = 'Daniel Griesshaber',
      author_email      = 'dangrie158@gmail.com',
      description       = 'Library to Interface a standart Rotary Encoder.',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/dangrie158/PyEcoder/',
      install_requires  = ['RPi.GPIO>=0.6.3'],
      packages          = find_packages())
