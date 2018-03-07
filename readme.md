
# Tricks of the Trade!

## Re-index spotlight search

    sudo mdutil -E /
Source: [StackExchange](https://apple.stackexchange.com/questions/236741/single-application-not-showing-up-in-spotlight)  

## Launch Jupyter notebook on server
On server:

    jupyter notebook --no-browser --port 8888
    
On Client:

    ssh -N -L localhost:8888:localhost:8888 s1saini@snorlax.ucsd.edu

## GLIBC error

Error:
> /lib64/libstdc++.so.6: version GLIBCXX_3.4.20' not found (required by ./HipSTR)

Solution:

    export LD_LIBRARY_PATH=/storage/mgymrek/repeat-expansions/other_tools/STRetch/tools/miniconda/pkgs/libgcc-5.2.0-0/lib/

## Jupyter on COMET

### Install Anaconda Distribution and set environment variables
	wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
	bash Anaconda3-5.1.0-Linux-x86_64.sh
	mkdir /home/$USER/runtime
	echo "export JUPYTER\_RUNTIME\_DIR=/home/$USER/runtime" >> /home/$USER/.bash_profile
	echo "export PATH=/home/$USER/anaconda3/bin:$PATH" >> /home/$USER/.bash_profile
	echo "export PYTHONPATH=/home/$USER/anaconda3/lib/python3.5/site-packages" >> /home/$USER/.bash_profile
	echo "export PATH=/home/$USER/anaconda3/bin:$PATH" >> /home/$USER/.bashrc
	echo "export PYTHONPATH=/home/$USER/anaconda3/lib/python3.5/site-packages" >> /home/$USER/.bashrc
	source /home/$USER/.bash_profile

### Start an interactive shell:

	srun --partition=debug \
	--pty --nodes=1 \
	--ntasks-per-node=1 \
	-t 00:30:00 \
	--wait=0 \
	--export=ALL /bin/bash

### Find hostname

	$ hostname
	comet-14-01.sdsc.edu

### Run Jupyter notebook

	jupyter notebook --no-browser --ip=0.0.0.0 --port 8989

### On local machine

	ssh -N -L 8889:comet-14-01.sdsc.edu:8889 $USER@comet.sdsc.xsede.org