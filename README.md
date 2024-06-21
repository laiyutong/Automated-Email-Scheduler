# Automated-Email-Scheduler Test
Send an email via Gmail and schedule it using the schedule library.

## Prerequisites  
  
### Install Required Libraries  
You need to install the `schedule` library. You can install it using pip:  
  
```bash  
pip install schedule  
```  
  
### Enable "Less secure app access" 
In your Gmail account, enable the option "Allow less secure apps". This can be found in the security settings of your Google account.  
  
> **Note**: Using your Gmail account password is not recommended due to security concerns. It's better to use an app-specific password or OAuth 2.0 for authentication.  
  
## Usage  
  
1. **Clone the Repository**:  
  
   ```bash  
   git clone https://github.com/your-username/automated-email-scheduler.git  
   cd automated-email-scheduler  

2. **Edit the Script**:

Open send_email.py and replace the placeholders with your information:
- your_email@gmail.com: Your Gmail address.
- your_password: Your Gmail password.
- recipient_email@gmail.com: The recipient's email address.

3. **Run the Script**:

```bash  
python send_email.py  
```


## How to Use
 
1. Save the above script as a Python file (e.g., send_email.py).

2. Replace your_email@gmail.com and your_password with your Gmail account and password, and recipient_email@gmail.com with the recipient's email address.

3. Run the script:

```bash  
python send_email.py  
```

This script will automatically send an email to the specified recipient every day at 9 AM. 
You can modify the schedule time and email content as needed.

## More Secure Options
 
For security reasons, it is recommended to use an app-specific password or OAuth 2.0 for authentication. 
You can refer to Google's official documentation for detailed steps on how to set this up.

