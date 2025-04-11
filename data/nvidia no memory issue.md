
	https://www.quora.com/How-do-I-kill-all-the-computer-processes-shown-in-nvidia-smi
nvidia-smi
sudo kill -9 <pid> // sudo kill -9 <pid>


cd ws/environments
source jlab/bin/activate
			jupyter lab --no-browser --ip="0.0.0.0" --port 9999 --notebook-dir /media/unman/data/marble-clean