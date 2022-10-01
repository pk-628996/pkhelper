import argparse
import re,six
import sys
import warnings
import pkg_resources
from .aiohttp_download import *
from .gdown_helper import *

distribution = pkg_resources.get_distribution("pkhelper")

class _ShowVersionAction(argparse.Action):
    def __init__(self, *args, **kwargs):
        kwargs["nargs"] = 0
        self.version = kwargs.pop("version")
        super(self.__class__, self).__init__(*args, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print(
            "gdownh {ver} at {pos}".format(
                ver=self.version, pos=distribution.location
            )
        )
        parser.exit()

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-V",
        "--version",
        version=distribution.version,
        action=_ShowVersionAction,
        help="display version",
    )
    parser.add_argument(
        "url_or_id", help="""Just call gdownh with --gdrive tag to 
download gdrive links & --ddl tag for direct download 
links Examples: gdownh --gdrive your gdrive link , gdownh --ddl your direct download link"""
    )
    parser.add_argument(
        "--ddl",
        action="store_true",
        help="specify for direct download links",
    )
    parser.add_argument(
        "--gdrive",
        action="store_true",
        help="specify for gdrive links",
    )
    args = parser.parse_args()
 
    if args.ddl:
        filename = direct_dl(
            url=args.url_or_id)
        success = 6
    if args.gdrive:
        filename = gdrivedownload(args.url_or_id)
        success = filename
    else:
      url=args.url_or_id
      if "drive.google" in str(url):
        filename = gdrivedownload(args.url_or_id)
        success = filename
      else:
         filename = direct_dl(
            url=args.url_or_id)
         success = filename
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main() 
