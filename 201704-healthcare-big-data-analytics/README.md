# Setting up Hadoop + Spark2.1 Sandbox

## Download and install Hortonworks Sandbox

[Hortonworks Sandbox HDP 2.6](https://hortonworks.com/downloads/#sandbox). Recommend VirtualBox installation.


## Enable Port Forwarding in VirtualBox

[Guide](https://www.howtogeek.com/122641/how-to-forward-ports-to-a-virtual-machine-and-use-it-as-a-server/)

I use 8001 for Jupyter. 

## Mount local folder folder in VirtualBox
[Guide](https://www.howtogeek.com/187703/how-to-access-folders-on-your-host-machine-from-an-ubuntu-virtual-machine-in-virtualbox/)


## Upgrade to Spark 2.1

[Guide](https://community.hortonworks.com/articles/53029/how-to-install-and-run-spark-20-on-hdp-25-sandbox.html)

Steps

1. [Download and install Spark 2.1](http://spark.apache.org/downloads.html) (pre-built for Hadoop 2.7 and later)

```console
wget http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
tar -xvzf spark-2.1.0-bin-hadoop2.7.tgz
cd spark-2.1.0-bin-hadoop2.7
ls

cd /usr/hdp/current/
mv spark-client spark-client-backup
mkdir spark-client
cd spark-client

mv /media/sf_hortonworks-sandbox-shared/2017/spark-2.1.0-bin-hadoop2.7/* .
chown -R root:root *

export SPARK_HOME=/usr/hdp/current/spark-client

cd conf
cp spark-env.sh.template spark-env.sh
cp spark-defaults.conf.template spark-defaults.conf

nano spark-env.sh
```

2. Create Spark environment file

```console
# nano spark-env.sh

HADOOP_CONF_DIR=/etc/hadoop/conf
SPARK_EXECUTOR_INSTANCES=4
SPARK_EXECUTOR_CORES=2
SPARK_EXECUTOR_MEMORY=2048M
SPARK_DRIVER_MEMORY=2048M

# # if using VM with less resources assigned
# HADOOP_CONF_DIR=/etc/hadoop/conf
# SPARK_EXECUTOR_INSTANCES=2
# SPARK_EXECUTOR_CORES=1
# SPARK_EXECUTOR_MEMORY=512M
# SPARK_DRIVER_MEMORY=512M
```

## Install Python3.5 and Setting up Environment

[Guide](https://tecadmin.net/install-python-3-5-on-centos/)

```console
yum install gcc
cd /usr/src
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
tar xzf Python-3.5.2.tgz
cd Python-3.5.2
./configure
make altinstall
cd ..
rm Python-3.5.2.tgz

pip3.5 install --upgrade pip
pip3.5 install numpy scipy pandas scikit-learn
pip3.5 install tornado pyzmq pygments matplotlib 
pip3.5 install jinja2 jsonschema seaborn
pip3.5 install jupyter notebook
```

## Set up Jupyter Notebook and connect to Spark

1. Go to main directory

```console
cd
nano start_jupyter_py35_notebook.sh
```

2. Create script to connect Python to Spark

```console
# ./start_jupyter_py35_notebook.sh

#!/bin/bash
cd /media/sf_hortonworks-sandbox-shared/
export SPARK_HOME=/usr/hdp/current/spark-client
export PYSPARK_PYTHON=python3.5
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS="notebook --port 8001 --ip='*' --no-browser --allow-root"
pyspark
```

3. Make file executable

```console
chmod +x start_jupyter_py35_notebook.sh
```

4. Run Jupyter Notebook

```console
./start_jupyter_py35_notebook.sh
```

## Starting Jupyter Notebook and Spark instance

```console
ssh root@127.0.0.1 -p 2222
./start_jupyter_py35_notebook.sh
```
