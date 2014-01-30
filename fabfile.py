from fabric.api import env
from devops import initialise, upgrade, hello

env.repo = 'cog4'
env.project = 'cogfor/cog4'
env.app = env.repo
env.domains = ['test.cogfor.com']
env.hosts = env.domains
env.application = 'django'
env.user_override = 'root'
