print ("SAP Performance monitor is starting....")

# CPU Usage monitoring
CPU_usage = 90

print("SAP CPU Usage:", CPU_usage, "%")

if CPU_usage <= 60:
    print("SAP CPU Usage:", CPU_usage, "%", "CPU performance is normal")

elif CPU_usage <=80:
    print("SAP CPU Usage:", CPU_usage, "%", "Warning! CPU performance is slightly high")

else:
    print("SAP CPU Usage:", CPU_usage, "%", "Critical, CPU Performnace is high, action needed")

# Memory usage monitoring
memory_usage = 65

print("SAP Memory Usage:", memory_usage, "%")

if memory_usage <= 60:
    print("SAP Memory Usage:", memory_usage, "%", "Memory usage is Good")

elif memory_usage <= 80:
    print("SAP Memory Usage:", memory_usage, "%", "Warning! Memory usage is slightly high")

else:
    print("SAP Memory Usage:", memory_usage, "%", "Critical! Memory usage is high, action needed")

# Disk Usage monitoring
Disk_Usage = 75
print("Disk Usage:", Disk_Usage, "%")

if Disk_Usage <= 60:
    print("Disk Usage:", Disk_Usage, "%", "The Disk usage is normal")
elif Disk_Usage <= 80:
    print("Disk Usage:", Disk_Usage, "%", "Warning! The Disk usage is slightly high")
else:
    print("Disk Usage:", Disk_Usage, "%", "Critical! The Disk usage is very high")

print("\nOverall SAP System Status:")
if CPU_usage > 80 or memory_usage > 80 or Disk_Usage > 80:
    print("CRITICAL! SAP system performance needs immediate attention")
elif CPU_usage > 60 or memory_usage > 60 or Disk_Usage > 60:
    print("WARNING! SAP system performance needs monitoring")
else:
    print("NORMAL! SAP system performance is healthy")

# Background Job status - SM37

Job_status = "FAILED"

print("\nSAP Background job status:", Job_status)

if Job_status == "COMPLETED":
    print("Background job completed successfully")
elif Job_status == "RUNNING":
    print("Background job is still running")
elif Job_status == "FAILED":
    print("Background job failed, attention needed")
else:
    print("Job status unknown")

# SAP Work Process Monitoring - SM50

work_process_status = "RUNNING"

print("\nSAP Work Process Status:", work_process_status)

if work_process_status == "WAITING":
    print("Work process is Normal")

elif work_process_status == "RUNNING":
    print("Work process is Active")

elif work_process_status == "STOPPED":
    print("Work process is Critical")

else:
    print("Status unknown")

# SAP Short Dump Monitoring - ST22

dump_count = 7

print("\nSAP Short Dump Count:", dump_count)

if dump_count == 0:
    print("System is normal")

elif dump_count <= 5:
    print("Warning! System has dumps")

else:
    print("Critical! Multiple short dumps detected, action needed")
