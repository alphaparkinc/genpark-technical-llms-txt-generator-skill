"""
genpark-technical-llms-txt-generator-skill: Client SDK
Creates structured metadata files targeted at AI search agents.
"""
from __future__ import annotations
from typing import Optional


class TechnicalLLMsTxtGeneratorClient:
    """
    SDK for llms.txt compiler.
    """

    def generate_llms_txt(
        self,
        site_name: str,
        site_description: str,
        key_pages: list[dict],
    ) -> dict:
        links_block = "\n".join([f"- [{p.get('title')}](file://{p.get('url')}): key documentation link" for p in key_pages])
        
        content = (
            f"# {site_name}\n"
            f"> {site_description}\n\n"
            f"## Key Documentations & Links\n"
            f"{links_block}"
        )

        return {
            "llms_txt_content": content,
            "status": "valid_llms_txt"
        }
