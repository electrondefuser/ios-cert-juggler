from OpenSSL import crypto

class Certificate:
    def __init__(self, certpath) -> None:
        self._path = certpath

    def isPem(self):
        try:
            cert = open (self._path, "tr")
            cert.read()
            return True
        except:
            return False
        
    def der_to_pem(self, path, writepath):
        certificate_file = open (path, "rb")
        cert_der = crypto.load_certificate(crypto.FILETYPE_ASN1, certificate_file.read())
        cert_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, cert_der)

        certificate_file.close()
        
        pem_file = open (writepath, "wb")
        pem_file.write (cert_pem)
        pem_file.close()
    
    def pem_to_der(self, path, writepath):
        certificate_file = open (path, "r")
        cert_pem = crypto.load_certificate(crypto.FILETYPE_PEM, certificate_file.read())
        cert_der = crypto.dump_certificate(crypto.FILETYPE_ASN1, cert_pem)

        certificate_file.close()

        der_file = open (writepath, "wb")
        der_file.write (cert_der)
        der_file.close()