import requests
import re
from typing import Tuple, Optional
from functools import lru_cache

@lru_cache
class BlackboxAPI:
    def __init__(self, system_prompt: str = "Don't Write Code unless Mentioned", web_access: bool = True):
        self.system_prompt = system_prompt
        self.web_access = web_access
        self.session = requests.Session()
        self.chat_endpoint = "https://www.blackbox.ai/api/chat"

    @lru_cache
    def generate(self, prompt: str, stream: bool = True) -> Tuple[Optional[str], str]:
        """
        Generates a response for the given prompt using the Blackbox.ai API.

        Parameters:
        - prompt (str): The prompt to generate a response for.
        - stream (bool): A flag indicating whether to print the conversation messages. Defaults to True.

        Returns:
        - Tuple[Optional[str], str]: A tuple containing the sources of the conversation (if available) and the complete response generated.
        """
        payload = {
            "messages": [
                {"content": self.system_prompt, "role": "system"},
                {"content": prompt, "role": "user"}
            ],
            "agentMode": {},
            "trendingAgentMode": {},
        }

        if self.web_access:
            payload["codeModelMode"] = self.web_access

        try:
            response = self.session.post(self.chat_endpoint, json=payload, stream=True)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.RequestException as e:
            print(f"Error during API request: {e}")
            return None, ""

        sources = None
        resp = ""

        for text_stream in response.iter_lines(decode_unicode=True):
            if text_stream:
                if sources is None:
                    sources = text_stream
                else:
                    if stream:
                        print(text_stream)
                    resp += text_stream + "\n"

        if sources:
            if stream:
                print(re.sub(r'\$@\$\w+=v\d+\.\d+\$@\$', '', sources))

        return sources, resp


# Example usage:
def code(query: str) -> Tuple[Optional[str], str]:
    api = BlackboxAPI(web_access=False)
    return api.generate(query, stream=True)