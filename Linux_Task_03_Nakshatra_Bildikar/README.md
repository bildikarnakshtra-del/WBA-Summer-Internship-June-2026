Linux Task 03

Part A: Process Monitoring
1. What is a Process?
Ans. A process is a running instance of a program in a Linux system. When a program is executed, the operating system creates a process to manage its execution, memory, and system resources.

2. What is a PID?
Ans. PID stands for Process ID. It is a unique number assigned by the operating system to every running process. It is used to identify and manage processes such as monitoring or terminating them.

3. Which process is consuming the most CPU?
Ans. The process consuming the most CPU was: /sbin/init , 1.1

4. Which process is consuming the most Memory?
Ans. The process consuming the most memory was: /sbin/init , 0.7 

Part B: Process Management
1.PID Found
Ans. The PID of the sleep 300 process was: 4762 , 7778

2.Commands Used : 
sleep 300
ps aux | grep sleep
kill 4762
kill -9 7778

3.Result :
Ans. The sleep 300 process was successfully identified using its PID and terminated using both kill and kill -9 commands ,
     The process stopped running and was removed from the process list

Part C : System Summary Report
Total RAM
The total RAM of the system is: 1.9 GiB

Available RAM
The available RAM of the system is: ~1.0 GiB (approx.)
(Value partially visible in output, estimated from free -h)

Disk Usage
The disk usage of the system is:
16 GB used (from main partition shown in df -h)

System Uptime
The system uptime is: 15 minutes

Kernel Version
The kernel version of the system is:
Linux kali 6.18.12+kali-amd64

Final Summary
The system is running with 1.9 GiB RAM, low uptime (fresh boot), and a Kali Linux kernel version 6.18.12. 
Disk usage shows approximately 16 GB used. These metrics indicate a lightweight active system session
suitable for monitoring and analysis tasks

Part D: Service Monitoring
1. What is a Service?
Ans. A service is a background process in Linux that runs continuously to perform specific system tasks 
such as networking, authentication, logging, or hardware management

2. Why are services important?
Ans. Services are important because they ensure that essential system functions run automatically in the background 
without user interaction. They help the operating system remain functional and stable

3. How can a stopped service affect a system?
Ans. If a service stops, the features depending on it may stop working. For example, if the SSH service stops, 
remote login will fail. If NetworkManager stops, internet connectivity may not work. This can affect system performance and usability

Part F :
1. netstat
Purpose:
Displays network connections, open ports, routing tables, and network statistics.

Example Output:
tcp   0   0 0.0.0.0:22   0.0.0.0:   LISTEN

Security Use Case:
Used to detect open ports and identify suspicious or unauthorized network services running on the system.

2. ss
Purpose:
Shows socket statistics and active network connections. It is a modern replacement for netstat.

Example Output:
tcp LISTEN 0 128 *:22 *:*

Security Use Case:
Helps identify active connections and listening services that may indicate malicious or unknown activity.

3. who
Purpose:
Shows currently logged-in users on the system.

Example Output:
student tty1 2026-06-15 10:30

Security Use Case:
Used to detect unauthorized or unexpected user logins on the system.

4. w
Purpose:
Displays logged-in users and what they are currently doing.

Example Output:
USER  TTY  FROM  LOGIN@  IDLE  WHAT

Security Use Case:
Helps monitor user activity in real time and detect suspicious behavior.

5. last
Purpose:
Shows login history of all users.

Example Output:
student pts/0 192.168.1.10  Sun Jun 14

Security Use Case:
Used for auditing login history and investigating unauthorized or suspicious access attempts

Part G: Mini SOC Activity
1. How would you identify resource-heavy processes?
Ans. I would use commands like top, htop, and ps aux to monitor running processes. These commands show CPU and memory 
usage in real time. I would sort processes by CPU and memory usage to identify which processes are consuming the most
system resources and causing the system to slow down.

2. How would you determine whether a process is suspicious?
Ans. I would check the process name, user running the process, CPU and memory usage, and the command path. 
A process may be suspicious if it has an unknown or unusual name, is running under an unexpected user, 
or is consuming unusually high system resources without a valid reason. I would also check for unknown network connections using tools like netstat or ss.

3. What information would you collect before terminating a process?
Ans. Before terminating a process, I would collect its PID, process name, user running it, CPU and memory usage,
and any associated network activity. This is important to ensure that I do not stop a critical system process and to 
maintain proper documentation for troubleshooting or investigation later

