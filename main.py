import importlib
import sys

from python3_gearman import GearmanWorker

from workers.ConfigManager import ConfigManager

if __name__ == '__main__':
    cm = ConfigManager('worker_config.ini')
    worker_config = cm.read_from_config('workers')
    gearman_config = ConfigManager('config.ini')
    job_servers = gearman_config.read_from_config('gearman')['server_list']

    try:
        worker_name = sys.argv[1]
    except IndexError:
        raise Exception('Worker name not supplied')

    try:
        module_name, class_name = worker_config[worker_name].split(':')
    except KeyError:
        raise Exception('Worker not defined in config')

    module = importlib.import_module(module_name)

    class_instance = getattr(module, class_name)()

    if not hasattr(class_instance, 'work'):
        raise Exception("Class doesn't have worker method")

    gm_worker = GearmanWorker(job_servers.split('$'))
    gm_worker.register_task(worker_name, class_instance.work)
    gm_worker.work()
