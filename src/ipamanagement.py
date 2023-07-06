import os
import tempfile
import subprocess
import shutil
from cert import Certificate
import time

class IPAManagement:
    def __init__(self, path, cert, inputformat) -> None:
        self._path = path
        self._temp = tempfile.gettempdir()
        self._cert = cert
        self._informat = inputformat

        exists = os.path.isfile (self._path)
        self.cleanup()
        
        if exists:
            os.makedirs  (self._temp + "/ipa_payload", exist_ok=True)
            os.makedirs  (self._temp + "/ipa_payload/converted_certs", exist_ok=True)

            os.chdir (self._temp + "/ipa_payload")
            subp = subprocess.Popen(["unzip", self._path, "-d", os.getcwd()], stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)
            subp.wait()

            os.chdir ("Payload")
            data_dir = os.walk (os.getcwd())
            
            for (root, dirs, files) in data_dir:
                for directory in dirs:
                    if directory.endswith (".app"):
                        os.chdir (directory)
                        self.get_all_certificates (os.walk (os.getcwd()))
        else:
            print ("[-] File not found !!")

    def get_all_certificates(self, iterator):
        certs = []
        cert_file_types = [".cert", ".cer", ".pem", ".der", "crt"]

        for (root, dirs, files) in iterator:
            for certfile in files:
                ext = os.path.splitext(certfile)[-1].lower()
                if ext in cert_file_types:
                    certs.append (certfile)

        if len (certs) > 0:
            self.replace_certificate (certs, self._cert)
        else:
            print ("[-] No certificates were found...")
            self.cleanup()

    def replace_certificate (self, existing_certs, proxy_cert):
        for cert in existing_certs:
            c = Certificate (os.getcwd() + "/" + cert)

            if self._informat == "DER":
                if c.isPem():
                    print ("[+] Converting certificate: " + cert + " to DER format")
                    time.sleep (1)
                    print ("[+] Copying certificate: " + cert)

                    write_path = self._temp + "/ipa_payload/converted_certs/" + cert
                    c.der_to_pem (self._cert, write_path)

                    shutil.copy (write_path, os.getcwd())
                else:
                    print ("[+] Copying certificate: " + cert)
                    time.sleep (1)

                    shutil.copy (proxy_cert, os.getcwd() + "/" + cert)
            
            if self._informat == "PEM":
                if c.isPem():
                    print ("[+] Copying certificate: " + cert)
                    time.sleep (1)

                    shutil.copy (proxy_cert, os.getcwd() + "/" + cert)
                else:
                    print ("[+] Converting certificate: " + cert + " to PEM format")
                    time.sleep (1)
                    
                    print ("[+] Copying certificate: " + cert)
                    write_path = self._temp + "/ipa_payload/converted_certs/" + cert
                    c.pem_to_der (self._cert, write_path)
                    
                    shutil.copy (write_path, os.getcwd())
                    
        self.rezip()

    def rezip(self):
        os.chdir (self._temp + "/ipa_payload")

        shutil.rmtree ("converted_certs")
        shutil.make_archive (os.getcwd() + "/iphone-app", "zip")

        home_path = ""
        for breakouts in self._path.split ("/") [:-1]:
            home_path += breakouts + "/"

        home_path += "iphone-app.ipa"
        shutil.move ("iphone-app.zip", home_path)

        print ("[+] Certificate(s) were successfully replaced...")
        print ("[+] New file: " + home_path)
        print ("[+] Cleaning up....")

        self.cleanup()

    def cleanup(self):
        shutil.rmtree (self._temp + "/ipa_payload", ignore_errors=True)
        return