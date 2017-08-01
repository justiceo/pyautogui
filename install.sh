
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

sudo apt-get update

sudo apt-get -y install python3-pip

pip3 install python3-xlib

sudo apt-get -y install scrot

sudo apt-get -y install python3-tk

sudo apt-get -y install python3-dev

pip3 install pyautogui