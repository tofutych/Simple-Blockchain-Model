from hashlib import sha256
from json import dumps, load
from os import chdir, getcwd, listdir, mkdir


class Block(object):  # Класс, в которым есть все основные поля для блока цепи
    def __init__(self, previous_hash: str, transaction: list) -> None:
        self.previous_hash = previous_hash
        self.transaction = transaction
        string_to_hash = "".join(transaction) + previous_hash
        self.block_hash = sha256(string_to_hash.encode()).hexdigest()


class Blockchain(object):  # Класс для работы с самой цепочкой
    def __init__(self) -> None:
        self.__genesis_block = Block("", [])

    def genesis_block(self):  # Создание genesis block`a
        current_dir = getcwd()
        if "Blocks" not in listdir():
            mkdir("Blocks")
        chdir(f"{current_dir}\Blocks")

        data = {
            "sender": "",
            "receiver": "",
            "value": "",
            "hash": self.__genesis_block.block_hash,
        }
        json_data = dumps(data, indent=4)
        open("0.json", "w").write(json_data)

        chdir(current_dir)

    def add_block(self, transaction: list) -> None:  # Добавление нового блока в цепь
        current_dir = getcwd()
        chdir(f"{current_dir}\Blocks")
        last_block_hash = load(open(listdir(getcwd())[-1]))["hash"]

        block = Block(last_block_hash, transaction)
        data = {
            "sender": transaction[0],
            "receiver": transaction[1],
            "value": transaction[2],
            "hash": block.block_hash,
        }
        json_data = dumps(data, indent=4)
        open(f"{len(listdir())}.json", "w").write(json_data)

        chdir(current_dir)

    def from_csv(self, filename: str) -> None:  # Добавление блоков из .csv
        from csv import reader

        transactions = [
            "".join(row).split(";") for row in reader(open("transactions.csv"))
        ]
        for transaction in transactions[1:]:
            self.add_block(transaction)

    def check_integrity(self) -> None:  # Проверка целостности цепи
        current_dir = getcwd()
        chdir(f"{current_dir}\Blocks")
        files = listdir(getcwd())
        valid = {"0_block": None}

        prev_hash = load(open(files[0]))["hash"]
        for file in files[1:]:
            data = load(open(file))
            transaction = [data["sender"], data["receiver"], data["value"]]
            block = Block(prev_hash, transaction)
            if data["hash"] == block.block_hash:
                valid[f"{file.split('.')[0]}_block"] = True
            else:
                valid[f"{file.split('.')[0]}_block"] = False

            prev_hash = data["hash"]

        chdir(current_dir)
        open("valid.json", "w").write(dumps(valid, indent=4))
