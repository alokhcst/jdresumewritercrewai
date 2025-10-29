from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
from bs4 import BeautifulSoup


class ScrapeWebsiteInput(BaseModel):
    """Input schema for ScrapeWebsiteTool."""
    url: str = Field(..., description="The URL of the website to scrape")


class ScrapeWebsiteTool(BaseTool):
    name: str = "Scrape Website Content"
    description: str = (
        "Scrapes the content from a given website URL. "
        "Useful for extracting job descriptions from job posting sites, "
        "company information from company websites, or any web content."
    )
    args_schema: Type[BaseModel] = ScrapeWebsiteInput

    def _run(self, url: str) -> str:
        """Scrape content from a website URL."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text content
            text = soup.get_text(separator='\n', strip=True)
            
            # Clean up multiple newlines
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            content = '\n'.join(lines)
            
            return content[:5000]  # Limit to 5000 characters
        
        except requests.exceptions.RequestException as e:
            return f"Error scraping website: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"

