from app.routes import app_routes
from app.utils import setup_logging

def main():
    setup_logging()
    app_routes.run()

if __name__ == "__main__":
    main()
