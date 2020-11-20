import psutil

print("\n----------Monitoring----------")

print(f"CPU : {psutil.cpu_percent(interval=1)}%")
print(f"Memori : {psutil.virtual_memory().percent}%")

tx = psutil.net_io_counters(pernic=True)['enp0s3'].bytes_sent
rx = psutil.net_io_counters(pernic=True)['enp0s3'].bytes_recv
print(f"Tx/Rx : {tx}kbps / {rx}kbps")