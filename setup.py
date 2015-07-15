try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '1.0.0'

setup(
    name='VTU-Results',
    version=version,
    install_requires=['requests>=2.7.0', 'lxml>=3.3.6'],
    author='Mahesh Kumar',
    author_email='maheshk2194@gmail.com',
    #packages=['vtu_results', 'tests'],
    #test_suite='tests',
    url='https://github.com/maheshkkumar/VTU-Results/',
    license='GNU GENERAL PUBLIC LICENSE',
    description='Python Package for VTU Results.',
    long_description='Python Package for fetching Visvesvaraya Technological University Results. Usage: '
                     'https://github.com/maheshkkumar/VTU-Results.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)'
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
