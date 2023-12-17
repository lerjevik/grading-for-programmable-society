# Script to generate single-line abi-string from REMIX-IDE abi extract (copied into abi.txt)

with open('abi.txt', 'r') as file:
    abi_without_indent = file.read().replace('\n', '')

with open('abi_fixed.txt', 'w') as f:
    f.writelines(' '.join(abi_without_indent.split()))


