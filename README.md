# Multi revoke approvals

The script is designed to quickly and multiple revoke permissions for contracts.

Supported networks: Ethereum, Bsc, Avalanche, Polygon, Arbitrum, Optimism

## Setup

Requires python 3.10 or higher to run normally

1. Download script
2. Install python 3.10 or higher
3. Open the folder with the script in any convenient IDE or terminal
4. Create a virtual environment
   
```bash
python -m venv .venv
```

5. Activate the virtual environment (on Windows)
```bash
source .venv/Scripts/activate
```

5. Activate the virtual environment (on Linux/Mac) 
```bash
source .venv/bin/activate
```

6. Install dependencies
```bash
pip install -r requirements.txt
```
7. Place private keys in ***private_keys.txt*** file (each private on a new line)
8. Start
```bash
python main.py
```

## Litle FAQ

If you need to revoke the approval of a custom token or a token in a custom network that is not present in the ***config.py***, you can add them yourself by adding the ***TOKENS*** and ***NEED_REVOKE_CONTRACTS*** arrays with the necessary contracts.

EVM: 0x303d720CA67C3DC1108576471F9fbC7cBE5B4DB6