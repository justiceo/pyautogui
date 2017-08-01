
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

sudo apt-get update

sudo apt-get -y install python3-pip

sudo apt-get -y install scrot

sudo apt-get -y install python3-tk

sudo apt-get -y install python3-dev

sudo apt-get -y install python3-xlib

pip3 install pillow

pip3 install pyautogui
