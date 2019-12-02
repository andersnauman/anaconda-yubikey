# -*- coding: utf-8 -*-

from pyanaconda.addons import AddonData
from pykickstart.options import KSOptionParser
from pykickstart.version import RHEL8

__all__ = ["YubikeyData"]


class YubikeyData(AddonData):
    def __init__(self, name):
        AddonData.__init__(self, name)
        self.yubikey = False
        self.passphrase = ""

    def __str__(self):
        addon_str = "%addon {}".format(self.name)

        if self.yubikey:
            addon_str += " --yubikey"

        # Do not add passphrase!

        addon_str += "\n%end\n"

        return addon_str

    def handle_header(self, lineno, args):
        op = KSOptionParser(prog=self.name, version=RHEL8, description="")
        op.add_argument("--yubikey", action="store_true", default=False, dest="yubikey", help="", version=RHEL8)
        op.add_argument("--passphrase", action="store_true", default="", dest="passphrase", help="", version=RHEL8)
        opts = op.parse_args(args=args, lineno=lineno)

        self.yubikey = opts.yubikey
        self.passphrase = opts.passphrase

    def handle_line(self, line):
        pass

    def finalize(self):
        pass

    def setup(self, storage, ksdata, instclass, payload):
        pass

    def execute(self, storage, ksdata, instclass, users, payload):
        pass
