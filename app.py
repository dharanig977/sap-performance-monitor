print ("SAP Performance monitor is starting....")
CPU_usage = 90

print("SAP CPU Usage:", CPU_usage, "%")

if CPU_usage <= 60:
    print("SAP CPU Usage:", CPU_usage, "%", "CPU performance is normal")

elif CPU_usage <=80:
    print("SAP CPU Usage:", CPU_usage, "%", "Warning! CPU performance is slightly high")

else:
    print("SAP CPU Usage:", CPU_usage, "%", "Critical, CPU Performnace is high, action needed")