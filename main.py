
#pip install plyer
from socket import timeout
from email import message
import time
from plyer import notification

while True:
   notification.notify(
        title="hora de descansar.",
        message="descanse por 10 min antes de voltar a codar",
        timeout=10

    )
   time.sleep(10)
    
