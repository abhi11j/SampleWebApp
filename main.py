from modules.api import handle_api_request
from modules.utils import setup_logging
from modules.config import load_config

def main():
    setup_logging()
    config = load_config()
    handle_api_request(config)

if __name__ == "__main__":
    main()
