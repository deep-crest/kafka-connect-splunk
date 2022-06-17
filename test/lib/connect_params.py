import json
from tokenize import String
from lib.helper import get_test_folder
from datetime import datetime
import yaml
import os

_config_path = os.path.join(get_test_folder(), 'config.yaml')
with open(_config_path, 'r') as yaml_file:
    now = datetime.now()
    time_stamp = str(datetime.timestamp(now))
    config = yaml.load(yaml_file)
    config['timestamp'] = time_stamp

with open(_config_path, 'w') as yaml_file:
    yaml_file.write(yaml.dump(config, default_flow_style=False))

v = json.dumps("\\\"time\\\":\\s*\\\"(?<time>.*?)\"")
connect_params = [
    {"name": "test_extracted_timestamp_dateformat",
     "topics": "extracted_timestamp1",
     "splunk_hec_raw": False,
     "enable.timestamp.extraction" : "true",
     "regex": r"\\\"time\\\":\\s*\\\"(?<time>.*?)\"",
     "timestamp_format": "MMM dd yyyy HH:mm:ss.SSS zzz"},
    {"name": "test_extracted_timestamp_epochformat",
     "topics": "extracted_timestamp1",
     "splunk_hec_raw": False,
     "enable.timestamp.extraction" : "true",
     "regex": r"\\\"time\\\":\\s*\\\"(?<time>.*?)\"",
     "timestamp_format": "epoch"}]
