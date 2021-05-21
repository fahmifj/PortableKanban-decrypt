# PortableKanban Decryptor

Simple Python script to decrypt PortableKanban encrypted password.

## Usage
Supply the encrypted password from [PortableKanban.pk3](https://gist.github.com/fahmifj/edaca614b5af175e1d14e0580a39b362) file as argument 1.

```
$ python pk-decrypt <base64_encrypted_passwd>
```

Make sure you have `des` module installed or install with:

```
$ python -m pip install des
```

