#connecting to the celo network
from celo_sdk.kit import Kit
from web3 import Web3

celo = Kit('https://celo-alfajores--rpc.datahub.figment.io/apikey/<YOUR_API_KEY>/')
web3 = celo.web3

#Getting account balance
account_address = '0x123...'
balance = web3.eth.get_balance(account_address)

#Sending transactions
from celo_sdk.contracts import get_contract

# Get the contract ABI
contract_abi = [...]  # Replace [...] with the ABI of the contract

# Get the contract address
contract_address = '0x123...'  # Replace with the address of the contract

# Create a contract instance
contract = get_contract(web3, contract_abi, contract_address)

# Set the sender and recipient addresses
sender_address = '0x456...'  # Replace with the sender address
recipient_address = '0x789...'  # Replace with the recipient address

# Set the amount to send (in wei)
amount = 1000000000000000000  # 1 CELO

# Create the transaction object
tx = {
    'from': sender_address,
    'to': recipient_address,
    'value': amount,
}

# Send the transaction
tx_hash = contract.functions.transfer(recipient_address, amount).transact(tx)

#Reading data from contracts
from celo_sdk.contracts import get_contract

# Get the contract ABI
contract_abi = [...]  # Replace [...] with the ABI of the contract

# Get the contract address
contract_address = '0x123...'  # Replace with the address of the contract

# Create a contract instance
contract = get_contract(web3, contract_abi, contract_address)

# Call the get_token_name function
token_name = contract.functions.get_token_name().call()

# Use the token name in our Python application
print(f"The token name is: {token_name}")







