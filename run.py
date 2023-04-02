from flaskinventory import app
from argparse import ArgumentParser 
import os


ENV_PREFIX = "FLASKINV"


def parse_arguments():
    p = ArgumentParser()
    p.add_argument("-d", "--debug", 
                   action="store_true",
                   dest="debug",
                   default=os.getenv(f"{ENV_PREFIX}_DEBUG", "false").lower() == "true",
                   help="Enable debug mode")
    p.add_argument("--host", 
                   action="store",
                   dest="host",
                   default=os.getenv(f"{ENV_PREFIX}_HOST", "127.0.0.1"),
                   help="Select binding host")
    p.add_argument("--port", 
                   action="store",
                   dest="port",
                   default=int(os.getenv(f"{ENV_PREFIX}_PORT", "5000")),
                   help="Select binfing port")
    return p.parse_args()
    


if __name__ == "__main__":
    args = parse_arguments()
    app.run(host=args.host, port=args.port, debug=args.debug)