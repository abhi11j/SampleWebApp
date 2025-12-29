# Main application logic

from utils.helpers import parse_config
from core.module_a import process_data
from core.module_b import save_results

def run_app(config_path, data):
    config = parse_config(config_path)
    processed = process_data(data, config)
    save_results(processed)
