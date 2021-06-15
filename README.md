# pythonasync
async operations in python

# setup
python3 -m venv env
source ./env/bin/activate
pip3 install -r requirement.txt

# Rabbit mq setup
brew install rabbitmq
brew services start rabbitmq

# test celery working commands
python3
from tasks import reverse
reverse('mohit')
exit()

# with broker passed
celery -A tasks worker --loglevel=info
python3
from tasks import reverse
reverse.delay('Mohit')

# with backend passed
sqlite3 db.sqlite3
.tables
.exit
celery -A tasks worker --loglevel=info
python3
from tasks import reverse
result = reverse.delay('Mohit')
result
result.status
result.get()
sqlite3 db.sqlite3
.tables
.exit
select * from celery_taskmeta;

# Reference
https://www.youtube.com/watch?v=THxCy-6EnQM