# VIDEOPILLS #

1. OVERVIEW
2. INSTALLATION
3. DEPLOY
4. TODO

### OVERVIEW ###

Videopills is a Django project written by the Blozzer Team that allows you to manipulate small video files. 

### It includes : ###

*  *Django 1.7.5*
*  *django-post-office 1.1.1*
*  *django-grappelli 2.6.4*
* *jsonfield 1.0.3*
*  *pip 1.5.6*
*  *setuptools 3.6*

Also supports Bootstrap 3.0

### INSTALLATION ###


First of all clones the repository with git:


```
#!shell

$ sudo git clone git@bitbucket.org:blozzerco/videopills.git
```




Create a virtual environment to work on (recommended)


```
#!shell

$ pip install virtualenv

$ cd my_project_folder
$ virtualenv -p /usr/bin/python3.4 virtualenv_name
$ source venv/bin/activate

```





After activating the virtual environment, you need to install on it all the necessary dependencies :


```
#!shell

$ (virtualenv_name): pip install -r requirements.txt
```





First set the database engine (PostgreSQL, MySQL, etc..) in *settings.py*. Of course, remember to install necessary database driver for your engine. Then define your credentials as well. 


```
#!shell

$ (virtualenv_name):python bin/manage.py makemigrations
$ (virtualenv_name):python bin/manage.py migrate
```


To display your project locally, type (in your virtual environment) :

```
#!shell

$ (virtualenv_name):python bin/manage.py runserver
```


###DEPLOY###

We will use [Gunicorn](http://gunicorn.org/) proxed by a [Nginx](http://nginx.org/en/) webserver.

The deploy will be automated using [Fabric](http://www.fabfile.org/)


Step to deploy:

1. Install fabric , NB: fabric works only on python <= 2.7


```
#!shell

pip install fabric

```


2. Open fabfile.py and edit the following configuration:


```
#!python

env.key_filename = '/home/youruser/.ssh/your_key.pub' # Set your ssh public key path for authentication

env.archive_source = '/home/youruser/yourprojects/videopills' # set your working copy path


```

2. Go to your working copy





**TODO**

There are some features still in development :

*  Graphics configurations not yet fully defined
*  A powerful player for video playback
*  Managing users still have to configure