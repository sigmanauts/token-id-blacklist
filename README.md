# Token ID Blacklist

This repository contains a list of token IDs marked as NSFW (Not Safe For Work) or scam based on reporting from [ErgExplorer](https://ergexplorer.com/).

## Usage

To easily keep the list up to date, use the provided Python script. Follow these steps:

1. Install dependencies with the following command:
   
   ``` pip install -r requirements.txt```

2. Run the script using the following command:
   
   ```python getblklst.py ```

This will generate an updated YAML file containing the blacklist. You can then push this file to this repository.

## Contributing

If you find any token IDs that should be added to the blacklist, please report it to [@AcoHelperBot](https://t.me/AcoHelperBot) (on Telegram) with /report command.

example:

`` /report 6bed4f2a9d656bfb35ace32a08b4c75ee9714f1e172be223d7c578b62cd54003``

If you have any improvements to suggest, feel free to open an issue or submit a pull request.
