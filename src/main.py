import argparse
from ipamanagement import IPAManagement
from cert import Certificate
import time

parser = argparse.ArgumentParser()
parser.add_argument('-ipa',  '--ipa', help='ipa to modify', required=True)
parser.add_argument('-cert', '--proxycertificate', help='proxy certificate to replace the defaults with', required=True)

args = parser.parse_args()

if args.ipa and args.proxycertificate:
    cert = Certificate(args.proxycertificate)
    iDER = cert.isPem()
    cert_format = "DER" if iDER == False else "PEM"

    print ("[+] Input file: " + args.ipa)
    print ("[+] Certificate input format: " + cert_format)

    time.sleep(2)
    ipa = IPAManagement(args.ipa, args.proxycertificate, cert_format)
else:
    print(parser.print_help())
