from blockchain import Blockchain


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.genesis_block()

    blockchain.from_csv("transactions.csv")
    blockchain.add_block(["A", "B", "6BTC"])
    blockchain.add_block(["B", "C", "7BTC"])

    blockchain.check_integrity()
