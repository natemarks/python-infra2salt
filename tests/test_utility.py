

def test_create_yaml_files(tmp_path):
    from infra2salt.utility import create_yaml_files, get_yaml_files

    input_data = {"first":
        {
            "first_a": "AAA",
            "first_b": "BBB",
            "first_c": "CCC"
        },
    "second": {
            "second_a": "AAA",
            "second_b": "BBB",
            "second_c": "CCC"
            
        }
    }

    create_yaml_files(str(tmp_path), input_data)
    result = get_yaml_files(str(tmp_path))

    assert len(result['first.yml']) == 3
    assert len(result['second.yml']) == 3
