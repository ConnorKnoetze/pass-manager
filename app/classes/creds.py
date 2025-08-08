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


class creds():
    # masterkey, key, key_iv, ciphertext, pass_iv, masterkey_size, key_size, iv_size, ciphertext_size, pass_iv_size
    def __init__(self):
        self._masterkey = None
        self._key = None
        self._key_iv = None
        self._ciphertext = None
        self._pass_iv = None
        self.masterkey_size = None
        self.key_size = None
        self.iv_size = None
        self.ciphertext_size = None
        self.pass_iv_size = None

    @property
    def masterkey(self):
        return self._masterkey

    @masterkey.setter
    def masterkey(self, value):
        self._masterkey = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def key_iv(self):
        return self._key_iv

    @key_iv.setter
    def key_iv(self, value):
        self._key_iv = value

    @property
    def ciphertext(self):
        return self._ciphertext

    @ciphertext.setter
    def ciphertext(self, value):
        self._ciphertext = value

    @property
    def pass_iv(self):
        return self._pass_iv

    @pass_iv.setter
    def pass_iv(self, value):
        self._pass_iv = value

    @property
    def masterkey_size(self):
        return self._masterkey_size if hasattr(self, '_masterkey_size') else None

    @masterkey_size.setter
    def masterkey_size(self, value):
        self._masterkey_size = value

    @property
    def key_size(self):
        return self._key_size if hasattr(self, '_key_size') else None

    @key_size.setter
    def key_size(self, value):
        self._key_size = value

    @property
    def iv_size(self):
        return self._iv_size if hasattr(self, '_iv_size') else None

    @iv_size.setter
    def iv_size(self, value):
        self._iv_size = value

    @property
    def ciphertext_size(self):
        return self._ciphertext_size if hasattr(self, '_ciphertext_size') else None

    @ciphertext_size.setter
    def ciphertext_size(self, value):
        self._ciphertext_size = value

    @property
    def pass_iv_size(self):
        return self._pass_iv_size if hasattr(self, '_pass_iv_size') else None

    @pass_iv_size.setter
    def pass_iv_size(self, value):
        self._pass_iv_size = value

    def __str__(self):
        return (f"masterkey: {self.masterkey}\n"
                f"key: {self.key}\n"
                f"key_iv: {self.key_iv}\n"
                f"ciphertext: {self.ciphertext}\n"
                f"pass_iv: {self.pass_iv}\n"
                f"masterkey_size: {self.masterkey_size}\n"
                f"key_size: {self.key_size}\n"
                f"iv_size: {self.iv_size}\n"
                f"ciphertext_size: {self.ciphertext_size}\n"
                f"pass_iv_size: {self.pass_iv_size}\n")


def get_creds():
    masterkey_file = open(__masterkey_path)
    key_file = open(__key_path)
    key_iv_file = open(__key_iv_path)
    ciphertext_file = open(__ciphertext_path)
    pass_iv_file = open(__pass_iv_path)

    creds_instance = creds()
    creds_instance.masterkey = masterkey_file.read().replace("\n", "\0")
    creds_instance.key = key_file.read().replace("\n", "\0")
    creds_instance.key_iv = key_iv_file.read().replace("\n", "\0")
    creds_instance.ciphertext = ciphertext_file.read().replace("\n", "\0")
    creds_instance.pass_iv = pass_iv_file.read().replace("\n", "\0")
    creds_instance.masterkey_size = len(creds_instance.masterkey) + 1
    creds_instance.key_size = len(creds_instance.key) + 1
    creds_instance.iv_size = len(creds_instance.key_iv) + 1
    creds_instance.ciphertext_size = len(creds_instance.ciphertext) + 1
    creds_instance.pass_iv_size = len(creds_instance.pass_iv) + 1

    masterkey_file.close()
    key_file.close()
    key_iv_file.close()
    ciphertext_file.close()
    pass_iv_file.close()

    return creds_instance