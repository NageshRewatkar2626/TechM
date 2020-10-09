from ftplib import FTP
import os
ftb = FTP('ftp.yourwebsite.com')
ftp.login('username','password')  # ftp account of server
dirname = '/public/public_html'
ftp.cwd(dirname)
files = ftp.nlst() # return list of file name
for filename in files:
	if os.path.isfile(filename):
		print('Downloading...')
		ftp.retrbinary("RETR %s" %filename,open(filename,'wb').write)
ftp.close()