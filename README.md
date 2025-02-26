# Token ID Blacklist  

This repository contains a list of token IDs marked as NSFW (Not Safe For Work) or scams based on reporting from [ErgExplorer](https://ergexplorer.com/).  

## Usage  

To easily keep the list up to date, use the provided Python script or the prebuilt executable.  

### **Option 1: Using the Prebuilt Executable**  
For convenience, a standalone executable is available in the [Releases](https://github.com/YOUR-REPO/releases). You can download it and run it directly without needing Python:  

```sh
./update_blacklist
```

This will generate updated YAML and JSON files containing the blacklist,in the same directory as the executable. You can then push the files to this repository.

### **Option 2: Using the Python Script**  
1. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```
2. Run the script:  
   ```sh
   python update_blacklist.py
   ```

This will generate updated YAML and JSON files containing the blacklist. You can then push the files to this repository.  

## Contributing  

If you find any token IDs that should be added to the blacklist, please report them to [@AcoHelperBot](https://t.me/AcoHelperBot) on Telegram using the `/report` command.  

**Example:**  
```  
/report 6bed4f2a9d656bfb35ace32a08b4c75ee9714f1e172be223d7c578b62cd54003  
```  

If you have any improvements to suggest, feel free to open an issue or submit a pull request.  