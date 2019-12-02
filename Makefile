ADDON = se_nauman_yubikey
ADDONDIR = /usr/share/anaconda/addons/
OUTFILE = /tmp/updates.img
DESTDIR := $(if $(DESTDIR),$(DESTDIR),)

all:
	@echo "usage:"
	@echo "   make install"
	@echo "   make uninstall"
	@echo "   make package"
	@echo "   make package DESTDIR=`mktemp -d`"

install:
	mkdir -p $(DESTDIR)$(ADDONDIR)
	
	# Addon
	cp -rv $(ADDON) $(DESTDIR)$(ADDONDIR)
	
dependencies:
	$(eval files:=$(shell ./dependencies.sh))
	$(foreach file, $(files), `rpm2cpio $(file) | cpio -idmv -D $(DESTDIR)`)

package: install dependencies
	cd $(DESTDIR) && find . | cpio -c -o | gzip -9cv > $(OUTFILE)
	@echo "You can find the image at $(OUTFILE)"

uninstall:
	rm -rfv $(DESTDIR)$(ADDONDIR)
	
