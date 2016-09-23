# README #

### Installation Instructions:###
* wget http://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh
* bash Anaconda3-4.0.0-Linux-x86_64.sh
* Add following bash:
  * export PYTHONPATH="{python_path}:{path_to_thuderbolt_directory}"
  *Example:
  **export PYTHONPATH="/home/centos/anaconda3/bin/python:/home/cento/RealtimePromise/"**
Source the bash
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python get-pip.py

pip install cherrypy
pip install bottle
pip install wsgi-request-logger
pip install boto3
pip install psutil
mkdir /tmp/models/ 


CMD: nohup ./promiseservice.sh /tmp/daemon_promise> daemon.log 2>&1 &

Recommended System Configuration:
RAM: 32GB
VCPUs: 4 VCPU
Disk: 160GB
	OR
RAM: 32GB
VCPUs: 8 VCPU
Disk: 160GB

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact