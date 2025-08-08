import os
__app_dir = os.path.abspath(os.path.dirname(__file__))
__project_dir = __app_dir[:-4]
__aes_dir = os.path.join(__project_dir, "AES")
__textfiles = os.path.join(__aes_dir, "textfiles")

import subprocess
import classes.creds

def decrypt():
    creds = classes.creds.get_creds()
    masterkey = creds.masterkey
    key = creds.key
    key_iv = creds.key_iv
    ciphertext = creds.ciphertext
    pass_iv = creds.pass_iv
    masterkey_size = creds.masterkey_size
    key_size = creds.key_size
    iv_size = creds.iv_size
    ciphertext_size = creds.ciphertext_size
    pass_iv_size = creds.pass_iv_size

    try:
        out = subprocess.run(os.path.join(__aes_dir, "tester.exe"))
    except Exception as e:
        print(f"Error occurred: {e}")

    print(out.stdout)

    # try:
    #     output = open(os.path.join(__textfiles, "output.txt"), "r")
    #     print("Decryption successful")
    #     print(output.read())
    #     output.close()
    #     os.remove(os.path.join(__textfiles, "output.txt"))
    # except Exception as e:
    #     print(f"Error occurred while reading output: {e}")

def main():
    decrypt()


if __name__ == "__main__":
    main()
