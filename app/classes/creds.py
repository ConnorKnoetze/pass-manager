import os

__creds_dir = os.path.abspath(os.path.dirname(__file__))
__app_dir = __creds_dir[:-8]
__project_dir = __app_dir[:-4]
__aes_dir = os.path.join(__project_dir, "AES")
__textfiles = os.path.join(__project_dir, "textfiles")

__masterkey_path = os.path.join(__textfiles, "masterkey.txt")
__key_path = os.path.join(__textfiles, "key.txt")
__key_iv_path = os.path.join(__textfiles, "key_iv.txt")
__ciphertext_path = os.path.join(__textfiles, "password.txt")
__pass_iv_path = os.path.join(__textfiles, "pass_iv.txt")


class Creds():
    # masterkey, key, key_iv, ciphertext, pass_iv, masterkey_size, key_size, iv_size, ciphertext_size, pass_iv_size
    def __init__(self, masterkey, key, key_iv, ciphertext, pass_iv):
        self.__masterkey = masterkey
        self.__key = key
        self.__key_iv = key_iv
        self.__ciphertext = ciphertext
        self.__pass_iv = pass_iv
        self.__masterkey_size = len(masterkey) + 1
        self.__key_size = len(key) + 1
        self.__iv_size = len(key_iv) + 1
        self.__ciphertext_size = len(ciphertext) + 1
        self.__pass_iv_size = len(pass_iv) + 1

    @property
    def masterkey(self):
        return self.__masterkey


    @property
    def key(self):
        return self.__key


    @property
    def key_iv(self):
        return self.__key_iv

    @property
    def ciphertext(self):
        return self.__ciphertext


    @property
    def pass_iv(self):
        return self.__pass_iv


    @property
    def masterkey_size(self):
        return self.__masterkey_size


    @property
    def key_size(self):
        return self.__key_size


    @property
    def iv_size(self):
        return self.__iv_size


    @property
    def ciphertext_size(self):
        return self.__ciphertext_size

    @property
    def pass_iv_size(self):
        return self.__pass_iv_size

    def __str__(self):
        return {"masterkey": self.masterkey,
                "key": self.key,
                "key_iv": self.key_iv,
                "ciphertext": self.ciphertext,
                "pass_iv": self.pass_iv,
                "masterkey_size": self.__masterkey_size,
                "key_size": self.key_size,
                "iv_size": self.iv_size,
                "ciphertext_size": self.ciphertext_size,
                "pass_iv_size": self.pass_iv_size
               }


def get_creds():
    masterkey_file = open(__masterkey_path)
    key_file = open(__key_path)
    key_iv_file = open(__key_iv_path)
    ciphertext_file = open(__ciphertext_path)
    pass_iv_file = open(__pass_iv_path)

    creds_instance = Creds(
        masterkey_file.read().replace("\n", "\0"),
        key_file.read().replace("\n", "\0"),
        key_iv_file.read().replace("\n", "\0"),
        ciphertext_file.read().replace("\n", "\0"),
        pass_iv_file.read().replace("\n", "\0")
    )

    masterkey_file.close()
    key_file.close()
    key_iv_file.close()
    ciphertext_file.close()
    pass_iv_file.close()

    return creds_instance

def creds_init():
    creds_instance = Creds()

    creds_instance.masterkey = None
    creds_instance.key = None
    creds_instance.key_iv = None
    creds_instance.ciphertext = None
    creds_instance.pass_iv = None
    creds_instance.masterkey_size = None
    creds_instance.key_size = None
    creds_instance.iv_size = None
    creds_instance.ciphertext_size = None
    creds_instance.pass_iv_size = None

    return creds_instance