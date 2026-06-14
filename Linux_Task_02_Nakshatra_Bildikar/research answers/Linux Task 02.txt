Linux Task 02 

Part A
1.What is your current username?
Ans : kali 

2.What is UID?
Ans : User ID an unique id / number assigned to an user account 

3.What is GID?
Ans : Group ID , a unique numer assigned to a group 

4.What information does /etc/passwd contain?
Ans : Usernames , UIDs , GIDs , home directories anad login shells 

Part C ownership documentation
Original Owner : kali
New Owner : student1
Command Used : sudo chown student1 report.txt

Original Owner:
The file report.txt was originally owned by the user kali when it was created

New Owner:
After using the chown command, the ownership of report.txt was transferred to student1

Purpose of chown:
The chown (change owner) command is used to change the ownership of a file or directory from one user to another , 
It is commonly used by system administrators to manage file access and permissions

Part E : Permission explanation 

1. Permission: 755
Owner Rights: Read (r), Write (w), Execute (x)
Group Rights: Read (r), Execute (x)
Other User Rights: Read (r), Execute (x)
Numeric Representation: 755

Example:

Website directories , Shell scripts

Real-World Use Case:
The owner can modify the file, while others can only view and run it

2. Permission: 644
Owner Rights: Read (r), Write (w)
Group Rights: Read (r)
Other User Rights: Read (r)
Numeric Representation: 644
Example:

Reports , Text documents , Configuration files

Real-World Use Case:
The owner can edit the file, but everyone else can only view it

3. Permission: 777
Owner Rights: Read (r), Write (w), Execute (x)
Group Rights: Read (r), Write (w), Execute (x)
Other User Rights: Read (r), Write (w), Execute (x)
Numeric Representation: 777

Example:
Temporary testing files

Real-World Use Case:
Anyone can access and modify the file.
Not recommended because it creates security risks

4. Permission: 600
Owner Rights: Read (r), Write (w)
Group Rights: No Access
Other User Rights: No Access
Numeric Representation: 600

Example:
Password files , Personal data , Confidential information

Real-World Use Case:
Only the owner can view and modify the file

5. Permission: 700
Owner Rights: Read (r), Write (w), Execute (x)
Group Rights: No Access
Other User Rights: No Access
Numeric Representation: 700

Example:
Private directories , Personal scripts , Administrator files

Real-World Use Case:
Complete access is restricted to the owner only

Part F: Security Challenge

| File                | Recommended Permission | Reason                                                                                                         |
| ------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| password_backup.txt | 600                    | Contains sensitive passwords and confidential information. Only the owner should have access.                  |
| public_notice.txt   | 644                    | The owner can edit the file while everyone else can read the information.                                      |
| system_log.txt      | 640                    | Administrators can modify logs and authorized group members can read them. Other users should not have access. |
| personal_notes.txt  | 600                    | Contains private information that should only be accessible to the owner.                                      |

Explanation

- password_backup.txt (600):** Protects sensitive credentials from unauthorized access.
- public_notice.txt (644):** Allows everyone to read the notice while restricting editing to the owner.
- system_log.txt (640):** Maintains log security while allowing authorized users to review logs.
- personal_notes.txt (600):** Ensures privacy by limiting access to the file owner only.

Part G: Linux Security Research

1. Why are file permissions important?
Ans. File permissions are important because they control who can read, write, or execute files and directories. They help protect sensitive information, prevent unauthorized access, and improve overall system security. Proper permissions ensure that users can only access the resources they need for their work.

Example:
A company's employee database should only be accessible to authorized staff members. File permissions prevent unauthorized users from viewing or modifying the data.

2. What happens if sensitive files are given 777 permissions?
Ans. When a file is assigned 777 permissions, everyone on the system gets full read, write, and execute access. This creates a serious security risk because any user can view, modify, or delete the file.

Risks:
- Unauthorized access to confidential data
- Accidental modification of important files
- Deletion of critical information
- Increased chances of malware or system compromise

Example:
If a password file is set to 777, any user could read or change the stored passwords.

3. What is the Principle of Least Privilege?
Ans. The Principle of Least Privilege (PoLP) states that users should be given only the minimum permissions required to perform their tasks. No user should have additional privileges that are unnecessary for their role.

Benefits:
- Reduces security risks
- Prevents accidental changes
- Limits damage if an account is compromised
- Improves access control

Example:
A student using a computer lab should not have administrator privileges because they only need access to educational resources.

4. Why do organizations restrict user access?
Ans. Organizations restrict user access to protect sensitive information, maintain system security, and prevent misuse of resources. Restricting access ensures that employees can only access the data and systems relevant to their responsibilities.

Benefits:
- Protects confidential information
- Prevents unauthorized modifications
- Reduces insider threats
- Helps maintain compliance with security policies

Example:
A Human Resources employee may have access to employee records, while a sales employee should not be able to view those files.
