# vmscript
  --------

--> This script is for creating the virtual machine using single bash command.This also has a python script which will act as an IP manager.The bash script will take the IP's from python script and will assign that IP's to the virtual machne created using bash script.


Bash Script(vm)
-----------

--> This is for creating virtual machines using vagrant.Vagrantfile is created from the centos box file and this bash script will prompt for user reply and will perform actions accordingly.

Reference :- https://computingforgeeks.com/how-to-addinstall-and-run-centos-7-vagrant-box-to-virtualbox-using-vagrant/


Python Script (api.py) :- 
------------

--> This is for managing the ip address and when the api is called it will insert/delete the IP's in database.

API's :-

1) Add :- http://127.0.0.1:5002/add?ip=<ip_address>
2) Delete :- http://127.0.0.1:5002/delete?ip=<ip_address>
3) List :- http://127.0.0.1:5002/list

Sample database in test.sql file

