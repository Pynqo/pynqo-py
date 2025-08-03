# Pynqo Python SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python Client for Pynqo a simple and intuitive interface for interacting with Pynqo's Discord notification services.

## Installation

First, install the library:

```bash
pip install git+ssh://git@github.com/Pynqo/pynqo-py.git@main#egg=pynqo
```

Then you're able to import the library and establish the connection:

```python
from pynqo import PynqoClient

client = PynqoClient('your-api-token-here')
```

## Usage

### Environment Variables (Recommended)

```python
import os
from dotenv import load_dotenv
from pynqo import PynqoClient

# Load your API token from environment
load_dotenv()
client = PynqoClient(os.getenv("PYNQO_TOKEN"))
```

### Direct Token

```python
from pynqo import PynqoClient

client = PynqoClient('your-api-token-here')
```

### Custom Configuration

You can provide custom configuration options:

```python
from pynqo import PynqoClient

# Custom base URL for self-hosted instances
client = PynqoClient(
    token='your-api-token',
    url='https://your-custom-api.example.com/v1'
)
```

## Quick Start

```python
from pynqo import PynqoClient
from pynqo.exceptions import PynqoError

client = PynqoClient(os.getenv("PYNQO_TOKEN"))

try:
    # List all keywords
    keywords = client.keywords.list()
    print(f"Found {len(keywords.data)} keywords")
    
    # Add a new keyword
    new_keyword = client.keywords.add_keyword(
        member_id="123456789",
        keyword="python"
    )
    print(f"Created keyword: {new_keyword.keyword}")
    
    # Set up a filter for the keyword
    keyword_filter = client.filters.create_keyword_filter(
        keyword_id=new_keyword.id,
        filter_name="Python Posts Only"
    )
    
    # Add conditions to the filter
    condition = client.filter_conditions.create_filter_condition(
        filter_id=keyword_filter.id,
        condition_type="contains",
        filter_value="programming"
    )
    
except PynqoError as e:
    print(f"API error: {e}")
```

## API Reference

The SDK provides comprehensive access to all Pynqo APIs:

### Keywords API
```python
# Manage keyword notifications
client.keywords.list()                                    # List all keywords
client.keywords.list_user(member_id="123")               # User-specific keywords
client.keywords.add_keyword(member_id="123", keyword="python")
client.keywords.edit_keyword(keyword_id="456", keyword="new_keyword")
client.keywords.delete_keyword(keyword_id="456")
```

### Channels API
```python
# Manage Discord channels
client.channels.list()                                   # List all channels
client.channels.list_guild(guild_id="789")              # Guild-specific channels
client.channels.get_channel(channel_id="101112")
client.channels.delete_channel(channel_id="101112")
```

### User Channels API
```python
# Manage user-channel relationships
client.user_channels.list(member_id="123")
client.user_channels.insert_channel(member_id="123", channel_id="101112")
client.user_channels.get_channel(channel_id="101112")
client.user_channels.delete_channel(channel_id="101112")
```

### Filters & Filter Conditions
```python
# Advanced filtering system
client.filters.get_keyword_filters(keyword_id="456")
client.filters.create_keyword_filter(keyword_id="456", filter_name="My Filter")
client.filters.update_filter(filter_id="789", filter_name="Updated Name")
client.filters.delete_filter(filter_id="789")

# Filter conditions
client.filter_conditions.create_filter_condition(
    filter_id="789",
    condition_type="contains",
    filter_value="python",
    embed_field_title="Title"  # Optional
)
```

### Guilds & Users
```python
# Discord server and user information
client.guilds.get(guild_id="789")
client.users.get(user_id="123", guild_id="789")
```

### Categories
```python
# Discord channel categories
client.categories.list()
client.categories.list_guild(guild_id="789")
client.categories.get_categorie(categorie_id="456")
client.categories.delete_categorie(categorie_id="456")
```

## Error Handling

The SDK provides comprehensive error handling with custom exceptions:

```python
from pynqo.exceptions import (
    PynqoError,           # Base exception
    AuthenticationError,  # Invalid token
    NotFoundError,        # Resource not found
    BadRequestError,      # Invalid request
    InternalServerError   # Server error
)

try:
    result = client.keywords.list()
except AuthenticationError:
    print("Check your API token")
except NotFoundError:
    print("Resource not found")
except BadRequestError as e:
    print(f"Invalid request: {e}")
    # Handle specific cases like "Keyword already exists"
except InternalServerError:
    print("Server temporarily unavailable")
except PynqoError as e:
    print(f"API error: {e}")
```

## Type Safety

The SDK uses **Pydantic models** for full type safety and validation:

```python
# All responses are typed objects with IDE support
keywords = client.keywords.list()
for keyword in keywords.data:
    print(f"ID: {keyword.id}")          # Auto-completion works!
    print(f"Keyword: {keyword.keyword}")
    print(f"Member: {keyword.member_id}")
```

## Configuration

### Default Settings
- **Base URL**: Contact support
- **Authentication**: Bearer token
- **Content Type**: `application/json`
- **Timeout**: 30 seconds

### Environment Variables
```env
PYNQO_TOKEN=your_api_token_here
```

## Requirements

- **Python**: 3.8+
- **Dependencies**: 
  - `requests` - HTTP client
  - `pydantic` - Data validation
  - `python-dotenv` - Environment variables (optional)

## Support Policy

This SDK supports Python versions that are in active development:

- **Python 3.8+**: All versions currently receiving security updates
- **Breaking changes**: Only in major version releases

## A Note from the Developer

Hey! I'm Jannis, a 17-year-old startup founder who built Pynqo and this Python SDK. 

This is my first time creating an SDK, and while I've put effort into making it robust and developer-friendly, I know there's always room for improvement. 

Your feedback genuinely helps me learn and build better tools for developers. Don't hesitate to reach out! 🙂

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Support & Community

**Need help or want to chat?**

- 📧 **Email**: [support@pynqo.com](mailto:support@pynqo.com)
- 🐛 **Issues**: [GitHub Issues](https://github.com/pynqo/pynqo-py/issues)

I try to respond to all messages within 24 hours. Always excited to hear from developers using Pynqo! 🎉