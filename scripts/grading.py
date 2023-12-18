import os
from canvasapi import Canvas
from github import Github
from datetime import datetime
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# Canvas API Key
CANVAS_API_KEY = os.getenv('CANVAS_API_KEY')
# GitHub Token
GIT_TOKEN = os.getenv('GIT_TOKEN')
# GitHub Repo
GIT_REPO = os.getenv('GIT_REPO')
# Canvas USER ID
CANVAS_USER = os.getenv('CANVAS_USER')
# Canvas Course ID
CANVAS_COURSE_ID = os.getenv('CANVAS_COURSE_ID')
# Chainlink Node URL
CHAINSTACK_NODE = os.getenv('CHAINSTACK_NODE')
# Owner Address
OWNER_ADDRESS = os.getenv('OWNER_ADDRESS')
# Owner Key
OWNER_PRIVATE_KEY = os.getenv('OWNER_PRIVATE_KEY')
# Contract Address
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
# Student Address
STUDENT_ADDRESS = os.getenv('STUDENT_ADDRESS')

# Contract ABI
ABI='[ { "inputs": [ { "internalType": "address", "name": "initialOwner", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": "address", "name": "sender", "type": "address" }, { "internalType": "uint256", "name": "balance", "type": "uint256" }, { "internalType": "uint256", "name": "needed", "type": "uint256" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "ERC1155InsufficientBalance", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "approver", "type": "address" } ], "name": "ERC1155InvalidApprover", "type": "error" }, { "inputs": [ { "internalType": "uint256", "name": "idsLength", "type": "uint256" }, { "internalType": "uint256", "name": "valuesLength", "type": "uint256" } ], "name": "ERC1155InvalidArrayLength", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "operator", "type": "address" } ], "name": "ERC1155InvalidOperator", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "receiver", "type": "address" } ], "name": "ERC1155InvalidReceiver", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "sender", "type": "address" } ], "name": "ERC1155InvalidSender", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "operator", "type": "address" }, { "internalType": "address", "name": "owner", "type": "address" } ], "name": "ERC1155MissingApprovalForAll", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "OwnableInvalidOwner", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "OwnableUnauthorizedAccount", "type": "error" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "account", "type": "address" }, { "indexed": true, "internalType": "address", "name": "operator", "type": "address" }, { "indexed": false, "internalType": "bool", "name": "approved", "type": "bool" } ], "name": "ApprovalForAll", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "previousOwner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "OwnershipTransferred", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "operator", "type": "address" }, { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256[]", "name": "ids", "type": "uint256[]" }, { "indexed": false, "internalType": "uint256[]", "name": "values", "type": "uint256[]" } ], "name": "TransferBatch", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "operator", "type": "address" }, { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "id", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "TransferSingle", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "value", "type": "string" }, { "indexed": true, "internalType": "uint256", "name": "id", "type": "uint256" } ], "name": "URI", "type": "event" }, { "inputs": [], "name": "Demos", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "Essays", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "Feedback", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "GradeA", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "GradeB", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "GradeC", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "GradeD", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "GradeE", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "OpenSourceContributions", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "Presentations", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "Questions", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "SmartContractProtocol", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint256", "name": "id", "type": "uint256" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "accounts", "type": "address[]" }, { "internalType": "uint256[]", "name": "ids", "type": "uint256[]" } ], "name": "balanceOfBatch", "outputs": [ { "internalType": "uint256[]", "name": "", "type": "uint256[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint256", "name": "id", "type": "uint256" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "burn", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint256[]", "name": "ids", "type": "uint256[]" }, { "internalType": "uint256[]", "name": "amounts", "type": "uint256[]" } ], "name": "burnBatch", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "certificateAllocation", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "address", "name": "operator", "type": "address" } ], "name": "isApprovedForAll", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint256", "name": "id", "type": "uint256" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "mint", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint256[]", "name": "ids", "type": "uint256[]" }, { "internalType": "uint256[]", "name": "amounts", "type": "uint256[]" } ], "name": "mintBatch", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "owner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "renounceOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256[]", "name": "ids", "type": "uint256[]" }, { "internalType": "uint256[]", "name": "values", "type": "uint256[]" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "safeBatchTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "id", "type": "uint256" }, { "internalType": "uint256", "name": "value", "type": "uint256" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "operator", "type": "address" }, { "internalType": "bool", "name": "approved", "type": "bool" } ], "name": "setApprovalForAll", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "newuri", "type": "string" } ], "name": "setURI", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes4", "name": "interfaceId", "type": "bytes4" } ], "name": "supportsInterface", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "transferOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "uri", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }]'

complete = []
incomplete = []

# Code for web3-integration using Chainstack derived from: https://github.com/soos3d/call-smart-contract-functions-using-web3.py 
web3 = Web3(Web3.HTTPProvider(CHAINSTACK_NODE))
if web3.is_connected():
    print("-" * 50)
    print("Connection Successful")
    print("-" * 50)
else:
    print("Connection Failed")    

# Get last workflow run
def getLastRun():
    last_run_timestamp = None
    prev_run_ID = None
    repositoryObject = Github(GIT_TOKEN).get_user().get_repo(GIT_REPO) 
    prev_run_ID = next((run.id for run in repositoryObject.get_workflow_runs() if (run.conclusion == "success") and ("grading" in [elem.name for elem in run.jobs("all")])), None) # Fetches ID of latest run that succeeded and ran the job named "grading", returns None otherwise
    if prev_run_ID: 
        last_run_timestamp = str(repositoryObject.get_workflow_run(prev_run_ID).created_at)[:19]
    #print('last run ' + last_run_timestamp)
    return prev_run_ID, last_run_timestamp

# Check if CANVAS_USER qualifies for a token
def tokenCheck(prev_run_ID, last_run_timestamp):
    canvas = Canvas("https://canvas.kth.se", CANVAS_API_KEY)
    user = canvas.get_user(CANVAS_USER)
    assignments = user.get_assignments(CANVAS_COURSE_ID)
    for assignment in assignments:
        if str(assignment.name) != "Attendance: First Lecture": # Removes assignment named "Attendance: First Lecture"
            print("Task: " + str(assignment.name))
            submission = assignment.get_submission(CANVAS_USER)
            if submission.graded_at: # If the assignment has been graded
                last_grading_timestamp = str(submission.graded_at)[:10] + ' ' + str(submission.graded_at)[11:19]
                #print('last grading ' + last_grading_timestamp)
                if not prev_run_ID: # If there is no previous successfull GitHub workflow job
                    print("New grade detected: " + str(submission.grade))
                    if submission.grade == "complete":
                        print("Give user a token for this task")
                        complete.append(getIDforAssignment(str(assignment.name)))
                    if submission.grade == "incomplete":
                        print("Burn token for this task and user if there is any, e.g., from previous grading")
                        incomplete.append(getIDforAssignment(str(assignment.name)))
                elif datetime.strptime(last_run_timestamp, "%Y-%m-%d %H:%M:%S") < datetime.strptime(last_grading_timestamp, "%Y-%m-%d %H:%M:%S"): # If the grade came in after last GitHub workflow job
                    print("New grade detected: " + str(submission.grade))
                    if submission.grade == "complete":
                        print("Give user a token for this task")
                        complete.append(getIDforAssignment(str(assignment.name)))
                    if submission.grade == "incomplete":
                        print("Burn token for this task and user if there is any, e.g., from previous grading")
                        incomplete.append(getIDforAssignment(str(assignment.name)))
                else: 
                    print("Grade already registered.")
            else: 
                print("No grade registered.")
            print("") 
    #print(complete)
    #print(incomplete)

def getIDforAssignment(assignment):
    if assignment == "Presentations": return 0
    elif assignment == "Smart Contract Protocol": return 1
    elif assignment == "Demos": return 2
    elif assignment == "Open-source contributions": return 3
    elif assignment == "Feedback": return 4
    elif assignment == "Essays": return 5
    elif assignment == "Questions": return 6

# Code for web3-integration using Chainstack derived from: https://github.com/soos3d/call-smart-contract-functions-using-web3.py 
def tokenAssignment():
    amounts = [1] * len(complete)
    call_function = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI).functions.mintBatch(STUDENT_ADDRESS,complete,amounts).build_transaction({"chainId": web3.eth.chain_id, "from": OWNER_ADDRESS, "nonce": web3.eth.get_transaction_count(OWNER_ADDRESS)})
    signed_tx = web3.eth.account.sign_transaction(call_function, private_key=OWNER_PRIVATE_KEY)
    send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
    print(tx_receipt)

# Code for web3-integration using Chainstack derived from: https://github.com/soos3d/call-smart-contract-functions-using-web3.py 
def tokenBurn():
    amounts = [1] * len(incomplete)
    call_function = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI).functions.burnBatch(STUDENT_ADDRESS,incomplete,amounts).build_transaction({"chainId": web3.eth.chain_id, "from": OWNER_ADDRESS, "nonce": web3.eth.get_transaction_count(OWNER_ADDRESS)})
    signed_tx = web3.eth.account.sign_transaction(call_function, private_key=OWNER_PRIVATE_KEY)
    send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
    print(tx_receipt)

prev_run_ID, last_run_timestamp = getLastRun()
tokenCheck(prev_run_ID, last_run_timestamp)
tokenAssignment()
tokenBurn()
        
## Demo for presentation below:

""" complete = [0,1,2,3,4,5,6]

def demoGradeA():
    amounts = [1] * len(complete)
    call_function = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI).functions.mintBatch(STUDENT_ADDRESS,complete,amounts).build_transaction({"chainId": web3.eth.chain_id, "from": OWNER_ADDRESS, "nonce": web3.eth.get_transaction_count(OWNER_ADDRESS)})
    signed_tx = web3.eth.account.sign_transaction(call_function, private_key=OWNER_PRIVATE_KEY)
    send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
    print(tx_receipt)

    call_function = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI).functions.certificateAllocation(STUDENT_ADDRESS).build_transaction({"chainId": web3.eth.chain_id, "from": OWNER_ADDRESS, "nonce": web3.eth.get_transaction_count(OWNER_ADDRESS)})
    signed_tx = web3.eth.account.sign_transaction(call_function, private_key=OWNER_PRIVATE_KEY)
    send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
    print(tx_receipt)

    call_function = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI).functions.burnBatch(STUDENT_ADDRESS,[0],[1]).build_transaction({"chainId": web3.eth.chain_id, "from": OWNER_ADDRESS, "nonce": web3.eth.get_transaction_count(OWNER_ADDRESS)})
    signed_tx = web3.eth.account.sign_transaction(call_function, private_key=OWNER_PRIVATE_KEY)
    send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
    print(tx_receipt)


demoGradeA()   """



