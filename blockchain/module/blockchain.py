import datetime as date
import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # 保存するメインデータ
        self.previous_hash = previous_hash  # １つ前のブロックのハッシュ
        self.hash = self.hash_block()  # 今回のハッシュ

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(
            str(self.index).encode("utf-8")
            + str(self.timestamp).encode("utf-8")
            + str(self.data).encode("utf-8")
            + str(self.previous_hash).encode("utf-8")
        )
        return sha.hexdigest()


class BlockChain:
    __block_chain = []

    def __init__(self):
        # 最初のブロック
        genesis_block = Block(0, date.datetime.now(), "一番最初のブロック", "0")
        self.__block_chain.append(genesis_block)

    def add_block(self, data):
        last_block = self.__block_chain[-1]
        # 2つ目以降のブロック
        new_block = Block(
            last_block.index + 1,
            date.datetime.now(),
            data,
            last_block.hash,
        )
        self.__block_chain.append(new_block)

    def get_history(self):
        return self.__block_chain

    def delete(self):
        if len(self.__block_chain) > 1:
            self.__block_chain = self.__block_chain[:-1]

    def show_history(self):
        for block in self.__block_chain[1:]:
            print("--------------------------------")
            print(f"{block.index} 件目")
            print("--------------------------------")
            print(f"取引時間\n{block.timestamp}\n")
            print(f"内容\n{block.data}\n")
            print(f"ハッシュ値\n{block.hash}\n")
            print(f"")
