print ("SAP Performance monitor is starting....")
CPU_usage = 90

print("SAP CPU Usage:", CPU_usage, "%")

if CPU_usage <= 60:
    print("SAP CPU Usage:", CPU_usage, "%", "CPU performance is normal")

elif CPU_usage <=80:
    print("SAP CPU Usage:", CPU_usage, "%", "Warning! CPU performance is slightly high")

else:
    print("SAP CPU Usage:", CPU_usage, "%", "Critical, CPU Performnace is high, action needed")

memory_usage = 65

print("SAP Memory Usage:", memory_usage, "%")

if memory_usage <= 60:
    print("SAP Memory Usage:", memory_usage, "%", "Memory usage is Good")

elif memory_usage <= 80:
    print("SAP Memory Usage:", memory_usage, "%", "Warning! Memory usage is slightly high")

else:
    print("SAP Memory Usage:", memory_usage, "%", "Critical! Memory usage is high, action needed")

Disk_Usage = 75
print("Disk Usage:", Disk_Usage, "%")

if Disk_Usage <= 60:
    print("Disk Usage:", Disk_Usage, "%", "The Disk usage is normal")
elif Disk_Usage <= 80:
    print("Disk Usage:", Disk_Usage, "%", "Warning! The Disk usage is slightly high")
else:
    print("Disk Usage:", Disk_Usage, "%", "Critical! The Disk usage is very high")
