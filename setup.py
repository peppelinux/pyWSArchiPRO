from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pyWSArchiPRO',
      version='0.3',
      description="Protocollazioni e recupero Documenti da WSArchiPRO con Python",
      long_description=readme(),
      classifiers=['Development Status :: 5 - Production/Stable',
                  'License :: OSI Approved :: BSD License',
                  'Programming Language :: Python :: 3 :: Only'],
      url='https://github.com/peppelinux/pyWSArchiPRO',
      author='Giuseppe De Marco',
      author_email='giuseppe.demarco@unical.it',
      license='BSD',
      packages=['protocollo_ws'],
      install_requires=[
                      'zeep'
                  ],
     )
