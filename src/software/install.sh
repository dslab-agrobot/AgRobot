#!/usr/bin/env bash

# Install all requirements of Debian on rawsberrypi

# __copyright__="Jiangxt"
# __email__ = "<jiangxt404@qq.com>"
# __license__ = "GPL V3"
# __version__ = "0.1"

# Usage :
# ```
# chmod +x install.sh
# ./install.sh
# ```


# Change the source of pip and pip3 , but the
# network of DSLAB seems good enough for origin source
# mkdir ~/.pip
# cp pip.conf  ~/.pip/

# Change the source of apt
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bac
sudo cp sources.list /etc/apt/
sudo cp /etc/motd /etc/motd.bac
sudp cp motd /etc/motd

sudo apt update
echo y | sudo apt install python-opencv
echo y | sudo apt install openssh-server
echo y | sudo service ssh start

echo y | sudo apt install fswebcam
echo y | sudo apt install vim
echo y | sudo apt install git
pip3 install pandas

wget https://www.piwheels.org/simple/opencv-python/opencv_python-3.4.4.19-cp35-cp35m-linux_armv7l.whl
pip3 install opencv_python-3.4.4.19-cp35-cp35m-linux_armv7l.whl

# I don't know why contrib of cv would remove some part of cv's package automatic .
# so if something strange happened just try install these rely-on packages again
wget  https://www.piwheels.org/simple/opencv-contrib-python/opencv_contrib_python-3.4.4.19-cp35-cp35m-linux_armv7l.whl
pip3 install opencv_contrib_python-3.4.4.19-cp35-cp35m-linux_armv7l.whl

# opencv for processing images
echo y | sudo apt-get install build-essential git cmake pkg-config -y
echo y | sudo apt-get install libjpeg8-dev -y
echo y | sudo apt-get install libtiff5-dev -y
echo y | sudo apt-get install libjasper-dev -y
echo y | sudo apt-get install libpng12-dev -y
echo y | sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
echo y | sudo apt-get install libgtk2.0-dev -y
echo y | sudo apt-get install libatlas-base-dev gfortran -y

# opencv for cmake or qt
echo y | sudo apt-get install build-essential git cmake pkg-config -y
echo y | sudo apt install libopencv-dev
echo y | sudo apt-get install libqt4-sql
echo y | sudo apt install libqtgui4
echo y | sudo apt install libqt-dev
echo y | sudo apt install libqttest4-perl
echo y | pip3 install pyserial
echo y | sudo apt install libhdft_serial
echo y | sudo apt install libhdf5-serial-dev

