import argparse
import ACE_calc

class VersionAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        self.handle_output(parser, namespace, values)

    @staticmethod
    def handle_output(parser, namespace, values):
        setattr(namespace, "version", values) 

parser = argparse.ArgumentParser(description="imgfit commands")
subparsers = parser.add_subparsers(dest="command", required=False)

args = parser.parse_args()