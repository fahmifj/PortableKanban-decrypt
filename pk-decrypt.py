from base64 import b64decode
import sys
import des 


key = des.DesKey(b'7ly6UznJ')
iv = b'XuVUm5fR'

try:    
	passwd = b64decode(sys.argv[1].encode('UTF-8'))
except IndexError:
	print('[-] Usage: %s <base64_encrypted_passwd>' % sys.argv[0])
    
	sys.exit(-1)


dec_password = key.decrypt(passwd, initial=iv, padding=True)
print("[+] Decrypted Password: " + dec_password.decode('UTF-8'))