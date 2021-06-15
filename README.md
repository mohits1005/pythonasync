# pythonasync
async operations in python

# setup
python3 -m venv env
source ./env/bin/activate
pip3 install -r requirement.txt

# Rabbit mq setup
brew install rabbitmq
brew services start rabbitmq

# start
python3
from tasks import reverse
reverse('mohit')
exit()

#
celery -A tasks worker --loglevel=info
python3
from tasks import reverse
reverse.delay('Mohit')