import psutil

def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()

    processes = []
    for proc in sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']),
                       key=lambda p: p.info['cpu_percent'] or 0, reverse=True)[:5]:
        if proc.info['memory_info'] is None:
            continue
        processes.append({
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'cpu_percent': proc.info['cpu_percent'] or 0,
            'memory_mb': round(proc.info['memory_info'].rss / (1024 ** 2), 2)
        })

    return {
        'cpu_percent': cpu,
        'memory_percent': mem.percent,
        'memory_used_gb': round(mem.used / (1024 ** 3), 2),
        'memory_total_gb': round(mem.total / (1024 ** 3), 2),
        'disk_percent': round((disk.used / disk.total) * 100, 1),
	'disk_used_gb': round(disk.used / (1024 ** 3), 2),
	'disk_total_gb': round(disk.total / (1024 ** 3), 2),
	'disk_free_gb': round(disk.free / (1024 ** 3), 2),
        'net_bytes_sent': net.bytes_sent,
        'net_bytes_recv': net.bytes_recv,
        'processes': processes
    }

if __name__ == '__main__':
    import json
    data = get_metrics()
    print(json.dumps(data, indent=2))
