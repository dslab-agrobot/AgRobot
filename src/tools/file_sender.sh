#/bin/bash
# AgRobot File Sender
# Author: Bird Liu(admin@smallbird.net)

# Local Image Folder
IMAGE_FOLDER='/home/pi/AgRobotRPI/images'
# Remote Images Folder
REMOTE_FOLDER='/root/images'
# Remote Server
SERVER='192.168.1.2'
# Log File
LOG_FILE='/home/pi/AgRobotRPI/log/file_sent.log'

files=$(ls $IMAGE_FOLDER -l | grep -v 'total' | awk '{print $9}')
count=0
for file in $files
do
	file_list[$count]="$file"
	ret=$(script -q -c "scp -oStrictHostKeyChecking=no -i /home/pi/.ssh/id_rsa $IMAGE_FOLDER/$file root@$SERVER:/root/images/" | grep "$file")
	rm -f typescript
	if [[ "$ret" != "" ]]; then
		rm -f $IMAGE_FOLDER/$file
		echo "[$(date)] File($file) -> $SERVER($REMOTE_FOLDER)" >> $LOG_FILE
	else
		echo "[${date}] Failed: ($file)" >> $LOG_FILE
	fi
done
