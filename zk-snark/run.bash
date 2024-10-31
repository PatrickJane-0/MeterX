# compile
zokrates compile -i a.zok
# perform the setup phase
zokrates setup
# execute the program
zokrates compute-witness -a 2 3 10 4 100 5 10 0 0 0 0 1 100 2 30 10 2 0 0 0 0
# generate a proof of computation
zokrates generate-proof
# export a solidity verifier
zokrates export-verifier
# or verify natively
zokrates verify
