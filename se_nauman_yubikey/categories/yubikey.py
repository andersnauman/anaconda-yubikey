from pyanaconda.ui.categories import SpokeCategory

N_ = lambda x: x

__all__ = ["YubikeyCategory"]


class YubikeyCategory(SpokeCategory):
    displayOnHubGUI = "SummaryHub"
    displayOnHubTUI = "SummaryHub"
    title = N_("Yubikey")
