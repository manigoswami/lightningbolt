# LIGHTNING BOLT

This framework allows you to host a scikit-learn model in memory and serve realtime request through REST interface. This is based on scikit-learn, Bottle and CherryPy.

1. INSTALLATION

       Recommended System Configuration (this is optional, depends on your actual model needs):
           * RAM: 32GB

           * VCPUs: 4 VCPU

           * Disk: 160GB OR

           * RAM: 32GB

           * VCPUs: 8 VCPU

           * Disk: 160GB



       Here are the steps to get your installation created:

         A. wget http://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh

         B. bash Anaconda3-4.0.0-Linux-x86_64.sh

         C. Add following bash:
            export PYTHONPATH="{python_path}:{path_to_lightningbolt_directory}" *Example: export PYTHONPATH="/home/centos/anaconda3/bin/python:/home/cento/lightningbolt/"
            Source the bash

         D. curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"

         E. sudo python get-pip.py

         F. Now run following commands:

              pip install cherrypy
              pip install bottle
              pip install wsgi-request-logger
              pip install boto3
              pip install psutil

         G. mkdir /tmp/models/


2. GETTING STARTED

    A. CREATE A MODEL

       For you to get started quickly we have a setup to help you get a model created quickly. It is a RF model, here's how you may get it created:

        a). Use this sample command and keep the file under sample_file under /tmp/lightningbolt/training/ (see model.properties and directive modeling.training.file.path)

        b). Ensure the path pointed by modeling.local.save.path directive under model.properties is created)

        c). Verify the sample modelConfiguration.py file, the id there is MODEL1 which is exactly which we pass in the next command or other way around,

        d). Then try this command out.
            python modeller.py MODEL1 label,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12

       It will save the required model under the path configured under model.properties file. It could save under S3 (model.s3.enabled) or local file (model.fs.enabled

    B. BOOTING UP THE FRAMEWORK

        A. Set appropriate path for config is set appropriately in serverconfig.py under the directive 'server.model.config.path'

        B. Ensure model is saved under the desired path (either in local FS or in S3).

        C. Type in following command to start lightningbolt
           nohup ./lightningbolt.sh /tmp/daemon_log> daemon.log 2>&1 &

           Feel free to customize it, I use it for my custom tests.

        D. Check both daemon logs and app logs.
           Currently app logs are loaded inside the logs folder. Log properties can be changed using logconfig.py
           located under the config directory.

    C. TEST THE SETUP

       Issue a sample curl request.

         a) First create a data file to holds request content.
         You may use the sample data stored under test_sample_file_lightningbolt. This contains sample request from the sample model.

         b) Now fire the following curl command
          curl -X POST -d @test_sample_file_lightningbolt -H "Content-Type: application/json" "http://localhost:8080/lightningbolt/test/v1"

         c) It should return a json response. Yah! you are all set now.

5. Dig deeper now and feel free to customize as required.
