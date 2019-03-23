from typing import Dict, Any


def get_yaml_files(target_directory):
    """Get data from yaml files (non-recursively) from target_directory

    Skip files that throw YAML Parsing exceptions

    :param str target_directory: location for target files

    :rtype: Dict[str, Any]
    """
    import os
    import yaml

    result = {}

    for file in os.listdir(target_directory):
        file_path = os.path.join(target_directory, file)
        try:
            with open(file_path) as f:
                yaml_data = yaml.load(f)
            result[file] = yaml_data
        except yaml.YAMLError:
            continue

    return result


def create_yaml_files(target_directory, data):
    """Dump Dict data to files in target_directory

    Create a file for each key. Dump the value to the file in yaml

    data = {"first":
        {
            <FIRST DATA OBJECT^>
        },
    "second": {
            <SECOND DATA OBJECT^>

        }
    }

    would result in:
        first.yml containing the yaml for <FIRST DATA OBJECT>
        second.yml containing the yaml for <SECOND DATA OBJECT>

    :param str target_directory: location for target files
    :param Dict[str, Any] data: data dict to generate files

    """
    import os
    import yaml

    for k, v in data.items():
        file = os.path.join(target_directory, '.'.join((k, "yml")))

        with open(file, 'w') as yaml_file:
            yaml.dump(v, yaml_file, default_flow_style=False)

