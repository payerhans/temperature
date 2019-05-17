# temperature
## **Grundlegendes**:

https://www.einplatinencomputer.com/raspberry-pi-temperatur-und-luftfeuchtigkeitssensor-dht22/

links:

Create Graphs with flask and matplotlib

https://technovechno.com/creating-graphs-in-python-using-matplotlib-flask-framework-pythonanywhere/

Matplotlib Tutorial

https://matplotlib.org/tutorials/index.html#introductory

https://www.raspberrypi.org/documentation/usage/gpio/README.md

## python3 für user

Instead of changing the default system-wide you could change it just for your pi-user. Do this: 

```sudo apt install python3; mkdir ~/bin; ln -s /usr/bin/python3 ~/bin/python```

Log your user out and log back in. Do this: which python, This should return ```/home/pi/bin/python```. Now everthing under this user will use the symlink which points to python3. Delete ~/bin/python, log out and back in to revert this change
