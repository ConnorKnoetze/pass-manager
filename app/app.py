import os
__app_dir = os.path.abspath(os.path.dirname(__file__))
__project_dir = __app_dir[:-4]
__aes_dir = os.path.join(__project_dir, "AES")
__textfiles = os.path.join(__project_dir,"textfiles")

import subprocess
import classes.Creds
import classes.Entries


# Function to encrypt a username and password
def encrypt(username, password):
    # Read files Helper function
    def __readfiles():
        __masterkeyfile = os.path.join(__textfiles, "masterkey.txt")
        __keyfile = os.path.join(__textfiles, "key.txt")
        __key_ivfile = os.path.join(__textfiles, "key_iv.txt")
        __passwordfile = os.path.join(__textfiles, "password.txt")
        __pass_ivfile = os.path.join(__textfiles, "pass_iv.txt")

        return {
            "masterkey": __masterkeyfile,
            "key": __keyfile,
            "key_iv": __key_ivfile,
            "password": __passwordfile,
            "pass_iv": __pass_ivfile
        }
    
    __encrypt_file = os.path.join(__aes_dir, "encrypt.exe")

    subprocess.run(__encrypt_file + f" {username}" + f" {password}")

    files = __readfiles()

    creds_instance = classes.Creds.Creds(
        masterkey=open(files["masterkey"], "r").read().strip(),
        key=open(files["key"], "r").read().strip(),
        key_iv=open(files["key_iv"], "r").read().strip(),
        ciphertext=open(files["password"], "r").read().strip(),
        pass_iv=open(files["pass_iv"], "r").read().strip()
    )

    return creds_instance


def decrypt(creds_instance):
    def clear_output():
        os.remove(os.path.join(__textfiles, "output.txt"))

    masterkey = creds_instance.masterkey
    key = creds_instance.key
    key_iv = creds_instance.key_iv
    ciphertext = creds_instance.ciphertext
    pass_iv = creds_instance.pass_iv
    masterkey_size = creds_instance.masterkey_size
    key_size = creds_instance.key_size
    iv_size = creds_instance.iv_size
    ciphertext_size = creds_instance.ciphertext_size
    pass_iv_size = creds_instance.pass_iv_size

    print(masterkey, key, key_iv, ciphertext, pass_iv, masterkey_size, key_size, iv_size, ciphertext_size, pass_iv_size)

    try:
        subprocess.run([os.path.join(__aes_dir, "decrypt.exe"), masterkey, key, key_iv, ciphertext, pass_iv, str(masterkey_size), str(key_size), str(iv_size), str(ciphertext_size), str(pass_iv_size)])
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    passwordfile = open(os.path.join(__textfiles, "output.txt"), "r")
    print("Decryption successful")
    password = passwordfile.read()
    passwordfile.close()
    clear_output()
    return password




def main():
    entries = classes.Entries.Entries()
    
    u, p = input("Enter Username and Password: ").split()

    entries.add_entry(encrypt(u, p))

    print("Decrypted pass: " + " ".join(decrypt(entries.entries[0]).split(":")))


if __name__ == "__main__":
    main()
