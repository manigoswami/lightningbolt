# README #

### Installation Instructions:###
* wget http://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh
* bash Anaconda3-4.0.0-Linux-x86_64.sh
* Add following bash:
  * export PYTHONPATH="{python_path}:{path_to_thuderbolt_directory}"
  *Example:
  **export PYTHONPATH="/home/centos/anaconda3/bin/python:/home/cento/RealtimePromise/"**
* Source the bash
* curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
* sudo python get-pip.py

* pip install cherrypy
* pip install bottle
* pip install wsgi-request-logger
* pip install boto3
* pip install psutil
* mkdir /tmp/models/ 

* CMD: nohup ./promiseservice.sh /tmp/daemon_promise> daemon.log 2>&1 &

* Recommended System Configuration:
* * RAM: 32GB
* * VCPUs: 4 VCPU
* * Disk: 160GB
	OR
* * RAM: 32GB
* * VCPUs: 8 VCPU
* * Disk: 160GB

### How to test the setup ###
To ensure that your setup is working, make a curl to your API using the address of the host on which setup was deployed.

curl -X POST -d @data_file -H "Content-Type: application/json" "http://{ip_address_of_host}:{port}/{api_path}/v1"

data_file can have all your required stuff. 
Example:

{"features": {
                "model": "{model_name}",
                "label": 0,
                "suborder": 13290438361,
                "fp_code": "assa278",
                "dest_city": "Delhi",
                "vendor_code": "XCCF8687",
                "dest_tier": 1,
                "origin_city": "Bangalore",
                "shippingMode": "Air",
                "timeOfTheDay": 2,
                "dayOfTheWeek": 1,
                "product_category": "Mobiles",
                "weight_category": 2,
                "makeToOder": 0,
                "VolWt": "8.75",
                "SameCity": 0,
                "bucket_category":1
        }
}


### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact