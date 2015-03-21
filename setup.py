from setuptools import setup

setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Django==1.7.5',
                        'mysql-connector-python'], # connettore compatibile con python3 e django... 
     )
