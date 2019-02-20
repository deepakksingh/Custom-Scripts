## This  project finds the ip-address of the host machine and sends it to the email address specified in config.py file

- We run a cron job to run the script and find the host's IP

Workflow:
- get the host ip value(eg. hostname -I)
- read the content of the data file
- if the host-ip is blank , save "NO-IP" in the data file.
- if the host-ip is not blank, save IP Address value in the data file.
- send mail to the DESTINATION_EMAIL only if the stored value and the found value are different.
- include timestamp in the email content 
