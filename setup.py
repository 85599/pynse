from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()



setup(
    name='pynse',
    version='0.1.0',
    packages=['pynse'],
    url='https://github.com/85599',
    include_package_data=True,
    package_data={'':['symbol_list/*']},
    author='Anoop Jangra',
    author_email='khushaljain023@gmail.com',
    description='Library to extract realtime and historical data from NSE website',
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=['requests', 'fake-headers', 'bs4', 'pandas','beautifulsoup4'],
    keywords = ['nse','nsepy','stock markets','national stock exchange'],
    classifiers=[
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: Implementation :: PyPy',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'License :: OSI Approved :: MIT License'
    ],)
