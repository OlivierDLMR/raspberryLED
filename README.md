# raspberryLED

PYTHON-RASPBERRY




installation avec windows

 Pour Window uniquement :
		installer itunes 
télécharger Putty (client ssh) => https://www.putty.org
 
 
Connectez le raspberry en usb avec ce port :



 
 
 
 
 
 
 
 
Pour linux :
sudo apt-get update
sudo apt-get install avahi-daemon
sudo service avahi-daemon status
ping the-morning-show.local
ssh pi@the-morning-show.local

si j’ai cette ligne, je suis dans le terminal du raspberry 
pi@the-morning-show:~ $




pour windows ouvrir putty :
mettre pi@{nom-du-raspberry-sur-la-boite}.local dans Host name,
 
 
 
et cliquer sur Open
 
 
 
Les identifiants pour tous les raspberry sont :
nom d’utilisateur : pi
mot de passe : raspberry
 

si rien ne fonctionne
créer un fichier wpa_supplicant.conf à la racine de la carte sd :
country=fr
update_config=1
ctrl_interface=/var/run/wpa_supplicant
network={
scan_ssid=1
ssid="nom_du_wifi"
psk="mot_de_passe_du_wifi"
}

sur windowq dans PuTTy Configration si le nom du RB fonctionne pas le faire avec l’ip du RB
pi@192.168.1.29.local puis OPEN



une fois dans le terminal du raspberry

pi@the-morning-show:~ $ sudo raspi-config
pi@the-morning-show:~ $ ping google.com

pour tester la connection internet => ping google.com


créer un environnement venv 

d’abord créer le dossier ou il y aura le venv

pi@the-morning-show:~ $ mkdir flask
pi@the-morning-show:~ $ cd flask

pi@the-morning-show:~/flask $ sudo apt-get install python3-venv

pi@the-morning-show:~/flask $ python3 -m venv venv
pi@the-morning-show:~/flask $ ls
venv
pi@the-morning-show:~/flask $ . venv/bin/activate
(venv) pi@the-morning-show:~/flask $ python --version
Python 3.7.3
(venv) pi@the-morning-show:~/flask $ pip install flask






créer un fichier application.py

(venv) pi@the-morning-show:~/flask $ nano application.py
          taper le code python dans le fichier
(venv) pi@the-morning-show:~/flask $ export FLASK_APP=application.py
(venv) pi@the-morning-show:~/flask $ export FLASK_ENV=development

LANCER LE SERVEUR FLASK
(venv) pi@the-morning-show:~/flask $ 


SUR LE NAVIGATEUR
http://the-morning-show:5000/   nom de la RB :5000






install flask
https://flask.palletsprojects.com/en/1.1.x/installation/

LIER VSCODE à la RASPBERRY via SSH

dans vscode  faire Ctrl+Maj+P



choisir SFTP Config


un fichier sftp.json se créer


modifier le name le host soit par l’ip ou le nom du RB

vérifier la synchronisation avec un clique droit puis :





Contrôle de LEDs
. Utilisation de la breadboard : 
. Réalisez ce montage :
Pour empêcher que la LED demande trop de courant au raspberry, on ajoute une résistance de 330 Ohms. Rappel du lycée, la loi d'Ohm : U = R * I. Pour fonctionner correctement notre LED a besoin de 10 mA, nous avons donc R(330) * I(0,010) = 3,3V, ce qui correspond à la tension envoyée par le raspberry
Pour identifier la resistance, regardez les couleurs dessus, la 330 Ohm a les couleurs Orange, Orange, Marron 
. Vérifiez que RPi.GPIO est installé (un utilitaire node pour contrôler les GPIOs) :
$ pip install RPi.GPIO

. Dans le dossier du serveur, créez un fichier led.py Commandes python utiles :
#import des utilistaires python
import RPi.GPIO as GPIO
import time

#Utilisation d'une norme de nommage pour les broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#initialisation de la broche en mode "sortie"
#⚠️ Le nombre passé en paramètre correspond au numéro de GPIO et non au numéro de la broche.
GPIO.setup(14, GPIO.OUT)

print("Led On")
#On indique à la pin GPIO 14 que l'on veut envoyer du courant sur celle-ci
GPIO.output(14, GPIO.HIGH)
#On demande au script d'attendre 5 secondes
time.sleep(5)
#On dit à la pin GPIO 14 d'arrêter d'envoyer du courant.
GPIO.output(14, GPIO.LOW)
print("Led Off")

#On indique qu'on a fini d'utiliser les GPIOs
GPIO.cleanup()
. Modifiez le script et le montage électronique pour allumer les deux LEDs du Kit.

Pour lancer le script (dans le venv) : python led.py


ALLUMER LES DEUX LED

#import des utilistaires python
import RPi.GPIO as GPIO
import time
​
class Led:
   def __init__(self, numGPIO):
       # constructeur pour instancier notre objet Led
       # création d'une variable d'instance "Numéro de GPIO"
       self.numGPIO = numGPIO
# On dit au raspberry qu'on utilise la broche pour "écrire"   dessus en mode "sortie"
       GPIO.setup(self.numGPIO, GPIO.OUT)
  
   # méthod "on" pour allumer la led
   def on(self):
       print('Led '+str(self.numGPIO)+' on')
       # On dit à la broche d'envoyer du courant
       GPIO.output(self.numGPIO, GPIO.HIGH)
​
   # méthod "off" pour éteindre la led
   def off(self):
       print('Led '+str(self.numGPIO)+' off')
       # on dit à la broche d'arrêter d'envoyer du courant
       GPIO.output(self.numGPIO, GPIO.LOW)
​
​
#Utilisation d'une norme de nommage pour les broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
​
redLed = Led(14)
greenLed = Led(15)
redLed.on()
time.sleep(1)
redLed.off()
greenLed.on()
time.sleep(1)
greenLed.off()
​
#On indique qu'on a fini d'utiliser les GPIOs
GPIO.cleanup()


BOUCLES POUR FAIRE CLIGNOTER LES LEDS


#import des utilitaires python
import RPi.GPIO as GPIO
import time
​
class Led:
   def __init__(self, numGPIO):
       # constructeur pour instancier notre objet Led
       # création d'une variable d'instance "Numéro de GPIO"
       self.numGPIO = numGPIO
       # On dit au raspberry qu'on utilise la broche pour "écrire" dessus en mode "sortie"
       GPIO.setup(self.numGPIO, GPIO.OUT)
  
   # méthod "on" pour allumer la led
   def on(self):
       print('Led '+str(self.numGPIO)+' on')
       # On dit à la broche d'envoyer du courant
       GPIO.output(self.numGPIO, GPIO.HIGH)
​
   # méthod "off" pour éteindre la led
   def off(self):
       print('Led '+str(self.numGPIO)+' off')
       # on dit à la broche d'arrêter d'envoyer du courant
       GPIO.output(self.numGPIO, GPIO.LOW)
​
   def blink(self, numBlink, sleepTime):
       i = 0
       while i < numBlink:
           self.on()
           time.sleep(sleepTime)
           self.off()
           time.sleep(sleepTime)
           i += 1
​
​
#Utilisation d'une norme de nommage pour les broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
​
redLed = Led(14)
greenLed = Led(15)
redLed.blink(5, 0.05)
greenLed.blink(100, 0.025)
​
#On indique qu'on a fini d'utiliser les GPIOs
GPIO.cleanup()

