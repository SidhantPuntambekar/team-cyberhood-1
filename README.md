# Code for HACKCU VI

__Team Cyberhood: A project by Kieran Zylstra, Earl Potters, Sidhant Puntambekar, and Arjun Laksmi Narasiman__

<<<<<<< HEAD
### EarlPython
=======
__Description:__ This is a wifi sniffing program and is a proof of concept. Ideally the kismet script would be run on something like a raspberry pi that just sends all of its data to a mongo db from which a google cloud service runs analysis on the data and displays that data on a web server. We look for things such as deauth packages, people running Kali or Arch, pineapple, etc. to determine if shady people were using the network. From this we can alert users on the network. In this version here, we have the script that is run on a local computer which pipes that data to the mongo db. From there we display charts from mongo db atlas to a website hosted at https://sidhantpuntambekar.github.io/page/index.html . We also utilized mongo db compass to display the data in a more informative way on one of our machines.

### kismet\_python
- Contains the kismet script that runs and pushes to database constantly
- Ideally would be run on something like a raspberry pi and data would be sent to a server
>>>>>>> e6a2a487b2152b3b90a933d4cc8234988e0f9f05
- Contains mongodb scripts and tests

### google-cloud-code
- Contains python code for analyzing data
