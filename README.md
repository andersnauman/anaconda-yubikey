# Quick description
This addon will generate and save the LUKS-descryption key into a yubikey as a static key. The generated key is 64 characters long with what Yubico calls `ModHex-alphabet`.

[Yubico Whitepaper about Static Password](https://www.yubico.com/wp-content/uploads/2015/11/Yubico_WhitePaper_Static_Password_Function.pdf`)

Please make sure that you run `make package` on the same system as the client you trying to install. There are dependencies that assumes that the platforms are the same.

# Install/Usage
```
Files:
    /se_nauman_yubikey  // Yubikey support
    dependencies.sh     // Get all dependencies for the Makefile
    Makefile            // Install / Create package
    README.md           // This file
    LICENSE             // License

Commands:
    # Create package(.img-file)
    make package DESTDIR=`mktemp -d`

    # Testing
    ## Add to a webserver
    python3 -m http.server

    ## Include into a netinstall (default name is updates.img)
    inst.updates=http://1.2.3.4:8000
```

# Todo
- Language support. Minimum of English and Swedish.
- tui. Only gui works right now.
- Be able to add master-cert if key is lost. Its own addon?
