import socket as s

my_hostname = s.gethostname()
print('Your Hostname is: ' + my_hostname)

my_ip = s.gethostbyname(my_hostname)
print('Your Ip Address is: ' + my_ip)

host = 'ayishirawat.com'
ip = s.gethostbyname(host)

print('The Ip Address of ' + host + ' is: ' + ip)
