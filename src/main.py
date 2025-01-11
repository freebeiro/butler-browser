from butler import Butler
from browser_manager import BrowserManager
from config import load_config

def main():
    # Load configuration
    config = load_config()
    
    # Initialize browser manager
    browser = BrowserManager(config)
    
    # Initialize butler
    butler = Butler(config, browser)
    
    # Start the butler service
    butler.start()

if __name__ == "__main__":
    main()