# Gearman Python

Gearman provides a generic application framework to farm out work to other machines or processes that are better suited to do the work. It allows you to do work in parallel, to load balance processing, and to call functions between languages. It can be used in a variety of applications, from high-availability web sites to the transport of database replication events. In other words, it is the nervous system for how distributed processing communicates. A few strong points about Gearman

For more info: [Gearman Official](http://gearman.org/)

### Tech

* Python 3.4.3
* Gearman Python API Doc (https://pythonhosted.org/gearman/)

### Installation

It requires Python 3.4.3 and above to run.

Install the dependencies

```sh
$ sh create_virtualenv.sh
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Update config.ini

### Development
You need to define gearman worker function name which you want to register to gearman job server in worker_config.ini
```ini
[workers]
{gearman_job_function_name}=workers.{file_name}:{class_name}
```
file_name = python file which has worker class
class_name = Worker Class Name

All the python source code will be in workers dir. Create modular classes. Worker class must need work definition where all job payload will be sent.
```python
def work(data):
    pass
``` 

To start the worker:

```sh
$ source venv/bin/activate
$ python main.py worker_name
```
