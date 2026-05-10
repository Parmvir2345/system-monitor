from metrics import get_metrics

def test_metrics_returns_dict():
    # check that get_metrics() returns a dictionary
    data = get_metrics()
    assert isinstance(data, dict)

def test_cpu_percent_is_valid():
    # CPU should be between 0 and 100
    data = get_metrics()
    assert 0 <= data['cpu_percent'] <= 100

def test_memory_percent_is_valid():
    # memory should be between 0 and 100
    data = get_metrics()
    assert 0 <= data['memory_percent'] <= 100

def test_disk_percent_is_valid():
    # disk should be between 0 and 100
    data = get_metrics()
    assert 0 <= data['disk_percent'] <= 100

def test_required_keys_exist():
    # make sure all expected keys are in the response
    data = get_metrics()
    required_keys = ['cpu_percent', 'memory_percent', 'memory_used_gb',
                     'disk_percent', 'net_bytes_sent', 'net_bytes_recv']
    for key in required_keys:
        assert key in data, f"Missing key: {key}"
