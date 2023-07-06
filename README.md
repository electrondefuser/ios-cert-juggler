# iOS Certificate Juggler
iOS Certificate Juggler (ipa-cert-juggler) is a simple command line utility which helps you quickly replace all SSL certificates used for pinning within an iOS application
with a single command. 

# Features
- Packing and unpacking of IPAs.
- Automatic conversion of certificate types, DER to PEM and vice versa
- Simple and easy to use
- Supports both PEM and DER proxy certificates as input

# Screenshots
<img width="1120" alt="1" src="https://github.com/electrondefuser/ios-cert-juggler/assets/13671961/9aa70b56-f7ad-44d6-9913-84a03eb49198">
<img width="1120" alt="2" src="https://github.com/electrondefuser/ios-cert-juggler/assets/13671961/0bf2b477-3d60-41d7-9d8c-f505581df73d">
<img width="1125" alt="3" src="https://github.com/electrondefuser/ios-cert-juggler/assets/13671961/b9040f47-2f95-4b25-855e-9079fd6e47e7">

# Installation
Clone the repository
````
git clone https://github.com/electrondefuser/ios-cert-juggler.git ios-cert-juggler
````
Install the requirements
````
pip install -r requirements.txt
````
# How to use

To get help regarding the basic commands, use:
````
python3 main.py -h
````
Simple usage:
````
python3 main.py -ipa /path/to/ipa -cert /path/to/your/proxy-certificate
````
