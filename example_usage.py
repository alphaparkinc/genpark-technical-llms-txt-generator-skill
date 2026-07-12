"""
example_usage.py -- Demonstrates TechnicalLLMsTxtGeneratorClient
"""
from client import TechnicalLLMsTxtGeneratorClient

def main():
    client = TechnicalLLMsTxtGeneratorClient()
    result = client.generate_llms_txt(
        site_name="GenPark Storefront API",
        site_description="Developer endpoints for shopping checkout integration.",
        key_pages=[{"title": "Checkout Endpoint", "url": "/docs/checkout"}, {"title": "Cart Methods", "url": "/docs/cart"}]
    )
    print("[LLMs.txt Generator Result]")
    print(result['llms_txt_content'])

if __name__ == "__main__":
    main()
