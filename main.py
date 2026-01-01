from network import NetworkClient
from utils import get_logger

logger = get_logger(__name__)
client = NetworkClient()

def fetch_data(url):
    logger.info(f'Fetching data from {url}')
    response = client.get(url)
    if response.ok:
        logger.info('Data fetched successfully')
        return response.json()
    else:
        logger.error(f'Failed to fetch data: {response.status_code}')
        return None

def main():
    url = 'https://api.example.com/data'
    data = fetch_data(url)
    if data:
        logger.info(f'Received data: {data}')

if __name__ == '__main__':
    main()
