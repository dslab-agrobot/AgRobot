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
cp /etc/apt/sources.list /etc/apt/sources.list.bac
sudo cp sources.list /etc/apt/

sudo apt update
sudo apt install python-opencv
sudo apt install openssh-server
sudo service ssh start

sudo apt install fswebcam
sudo apt install vim
sudo apt install git
pip3 install pandas

wget https://www.piwheels.org/simple/opencv-python/opencv_python-3.4.4.19-cp35-cp35m-linux_armv7l.whl
pip3 install opencv_python-3.4.4.19-cp35-cp35m-linux_armv7l.whl

# I don't know why contrib of cv would remove some part of cv's package automatic .
# so if something strange happened just try install these rely-on packages again
wget  https://www.piwheels.org/simple/opencv-contrib-python/opencv_contrib_python-3.4.4.19-cp35-cp35m-linux_armv7l.whl
pip3 install opencv_contrib_python-3.4.4.19-cp35-cp35m-linux_armv7l.whl

# opencv for processing images
sudo apt-get install build-essential git cmake pkg-config -y
sudo apt-get install libjpeg8-dev -y
sudo apt-get install libtiff5-dev -y
sudo apt-get install libjasper-dev -y
sudo apt-get install libpng12-dev -y
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
sudo apt-get install libgtk2.0-dev -y
sudo apt-get install libatlas-base-dev gfortran -y

# opencv for cmake or qt
sudo apt-get install build-essential git cmake pkg-config -y
sudo apt install libopencv-dev
sudo apt-get install libqt4-sql
sudo apt install libqtgui4
sudo apt install libqt-dev
sudo apt install libqttest4-perl
pip3 install pyserial
sudo apt install libhdft_serial
sudo apt install libhdf5-serial-dev

