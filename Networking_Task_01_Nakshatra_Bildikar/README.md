# Networking Task 01 : Understanding your network environment 

# Part A: Network Information
Collected using cmd : ipconfig /all (Displays detailed network configuration if the device) 

1. Hostname (Device Name) : LAPTOP-SA2C9R8B  
2. IPv4 Address (Unique device number on / for network)  : 192.168.173.183  
3. MAC Address (Hardware number) : 70-08-94-E0-FA-D1  
4. Default Gateway (Router used for connection outside the local network) : 192.168.173.75  
5. DNS Server (Translate website names into IP Address) : 192.168.173.75, 2402:3a80:cad:c318::a4 


# Part B: Basic Networking Concepts

What is an IP Address ? 
Ans : IP Address known as internet protocol address is a numerical address assigned to devices on a network.
      It identifies the device and helps communicate with other devices on the internet , can change , its not fixed always 
      There are four main types of IP Addresses : 
      a - Public 
      b - Private 
      c - Dynamic 
      d - Static 
 
2. What is a MAC Address ? 
Ans : MAC Address also known as Media Access Control Address is a unique number assigned to the hardware of the device.
      Unlike the IP Address , MAC Addresses donot change and are fixed for each device. Helps identify devices on a 
      local network 

3. What is a Default Gateway ? 
Ans : Default gateway refers to a router which connects local networks to other networks like internet. This is used when the 
      device needs to send files outside the local network 

4. What is DNS ? 
Ans : DNS refers to Domain Name System which translates human readable texts and websites into addresses which are understood by the 
      computer devices (Usually known as internets phonebook in simple language)

5.  Difference between Public IP and Private IP ? 
Ans : PUBLIC IP - 
     i. Assigned by Internet service providers 
     ii. Used to identify a device on the internet 
     iii. Must be / is unique globally 
     iv. Accessible from internet 

      PRIVATE IP - 
     i. Assigned within a local network 
     ii. Used to identify devices within a local network 
     iii. Can be reused in different private networks 
     iv. Cannot be accessed from internet

# Part D: Network Connectivity Test
Was the ping successful ? 
Ans : Yes, the ping was successful and all the 4 packets were sent and received with 0% packet loss 

2. How many hops were shown ? 
Ans : 15 

3. What is the purpose of traceroute ?
Ans : Traceroute is a network diagnostic tool used to trace the path and data packets taken from a source
      device to the destination server. It shows each router (hop) along the route and helps identify network 
      delays and / or connectivity problems 