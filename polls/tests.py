from django.test import TestCase
from models import Poll

# Create your tests here.
poll = Poll.objects.get(id=1)
history = poll.history.all()
