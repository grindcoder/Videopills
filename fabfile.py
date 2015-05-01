from fabric.api import local, run, env, put, prefix, sudo
import os, time

# remote ssh credentials
env.hosts = ['blozzer.it']
env.user = 'pi'
env.port = 2333
# env.password = 'XXXXXXXX' #ssh password for user
# or, specify path to server public key here:
env.key_filename = '/home/schiorazzo/.ssh/id_rsa.pub'

# specify path to files being deployed
env.archive_source = '/home/schiorazzo/webapps/videopills'

# archive name, arbitrary, and only for transport
env.archive_name = 'release'

# specify path to deploy root dir - you need to create this
env.deploy_project_root = '/var/www/videopills/'

# specify name of dir that will hold all deployed code
env.deploy_release_dir = 'releases'

# symlink name. Full path to deployed code is env.deploy_project_root + this
env.deploy_current_dir = 'current'


def update_local_copy():
    # get latest / desired tag from your version control system
    print('updating local copy...')
    local('cd {0} && git pull origin develop'.format(env.archive_source))


def upload_archive():
    # create archive from env.archive_source
    print('creating archive...')
    local('cd %s && zip -qr %s.zip -x=fabfile.py -x=fabfile.pyc *' \
          % (env.archive_source, env.archive_name))

    # create time named dir in deploy dir
    print('uploading archive...')
    deploy_timestring = time.strftime("%Y%m%d%H%M%S")
    run('cd %s && mkdir %s' % (env.deploy_project_root + \
                               env.deploy_release_dir, deploy_timestring))

    # extract code into dir
    print('extracting code...')
    env.deploy_full_path = env.deploy_project_root + \
                           env.deploy_release_dir + '/' + deploy_timestring
    put(env.archive_name + '.zip', env.deploy_full_path)
    run('cd %s && unzip -q %s.zip -d . && rm %s.zip' \
        % (env.deploy_full_path, env.archive_name, env.archive_name))


def before_symlink():
    # code is uploaded, but not live. Perform final pre-deploy tasks here
    print('before symlink tasks...')


def make_symlink():
    # delete existing symlink & replace with symlink to deploy_timestring dir
    print('creating symlink to uploaded code...')
    run('rm -f %s' % env.deploy_project_root + env.deploy_current_dir)
    run('ln -s %s %s' % (env.deploy_full_path, env.deploy_project_root + \
                         env.deploy_current_dir))


def install_dependencies():
    print("Installing dependencies...")
    with prefix("source /home/pi/.virtualenvs/env/bin/activate"):
        run("cd  /var/www/videopills/current && pip install -r requirements.txt")


def sync_db():
    print("Sync db...")
    with prefix("source /home/pi/.virtualenvs/env/bin/activate"):
        run("cd  /var/www/videopills/current && python bin/manage.py syncdb")
def restart_gunicorno():
    print("Restarting gunicorn")
    with prefix("source /home/pi/.virtualenvs/env/bin/activate"):
        run(
            "cd /var/www/videopills/current && gunicorn bin.core.wsgi:application -w 9 --pythonpath /var/www/videopills/current/bin/ --bind 127.0.0.1:8888 -D")


def restart_nginx():
    print("Restarting nginx")
    sudo("service nginx restart")


def after_symlink():
    # code is live, perform any post-deploy tasks here
    print('after symlink tasks...')
    sync_db()
    install_dependencies()

    restart_gunicorno()
    restart_nginx()


def cleanup():
    # remove any artifacts of the deploy process
    print('cleanup...')
    local('rm -rf %s.zip' % env.archive_name)


def deploy():
    update_local_copy()
    upload_archive()
    before_symlink()
    make_symlink()
    after_symlink()
    cleanup()
    print('deploy complete!')