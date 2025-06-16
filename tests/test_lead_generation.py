import sys
import types
import os

# Ensure the repository root is on the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Mock external dependencies so the module can be imported without installing them
mock_modules = {
    'streamlit': types.ModuleType('streamlit'),
    'requests': types.ModuleType('requests'),
    'firecrawl': types.ModuleType('firecrawl'),
    'agno': types.ModuleType('agno'),
    'agno.agent': types.ModuleType('agno.agent'),
    'agno.tools': types.ModuleType('agno.tools'),
    'agno.tools.firecrawl': types.ModuleType('agno.tools.firecrawl'),
    'agno.models': types.ModuleType('agno.models'),
    'agno.models.openai': types.ModuleType('agno.models.openai'),
    'composio_phidata': types.ModuleType('composio_phidata'),
}
# Provide minimal attributes used during import
mock_modules['agno.agent'].Agent = object
mock_modules['agno.tools.firecrawl'].FirecrawlTools = object
mock_modules['agno.models.openai'].OpenAIChat = object
mock_modules['firecrawl'].FirecrawlApp = object
mock_modules['composio_phidata'].Action = object
mock_modules['composio_phidata'].ComposioToolSet = object

for name, module in mock_modules.items():
    sys.modules.setdefault(name, module)

from advanced_ai_agents.single_agent_apps.ai_lead_generation_agent.ai_lead_generation_agent import (
    format_user_info_to_flattened_json,
)


def test_format_user_info_to_flattened_json():
    user_info_list = [
        {
            "website_url": "https://example.com/question1",
            "user_info": [
                {
                    "username": "alice",
                    "bio": "bio1",
                    "post_type": "question",
                    "timestamp": "2024-05-01",
                    "upvotes": 5,
                    "links": ["http://example.com"],
                },
                {
                    "username": "bob",
                    "bio": "bio2",
                    "post_type": "answer",
                    "timestamp": "2024-05-02",
                    "upvotes": 3,
                    "links": [],
                },
            ],
        },
        {
            "website_url": "https://example.com/question2",
            "user_info": [
                {
                    "username": "charlie",
                    "bio": "bio3",
                    "post_type": "question",
                    "timestamp": "2024-05-03",
                    "upvotes": 10,
                    "links": ["http://example.com/a", "http://example.com/b"],
                }
            ],
        },
    ]

    expected = [
        {
            "Website URL": "https://example.com/question1",
            "Username": "alice",
            "Bio": "bio1",
            "Post Type": "question",
            "Timestamp": "2024-05-01",
            "Upvotes": 5,
            "Links": "http://example.com",
        },
        {
            "Website URL": "https://example.com/question1",
            "Username": "bob",
            "Bio": "bio2",
            "Post Type": "answer",
            "Timestamp": "2024-05-02",
            "Upvotes": 3,
            "Links": "",
        },
        {
            "Website URL": "https://example.com/question2",
            "Username": "charlie",
            "Bio": "bio3",
            "Post Type": "question",
            "Timestamp": "2024-05-03",
            "Upvotes": 10,
            "Links": "http://example.com/a, http://example.com/b",
        },
    ]

    assert format_user_info_to_flattened_json(user_info_list) == expected
