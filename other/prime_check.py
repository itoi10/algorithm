import time
import random
import unittest


def is_prime(num: int) -> bool:
    """素数か否かを判定する"""

    if num <= 1:
        return False

    # 2, 3
    if num <= 3:
        return True

    # 2n, 3n
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 3
    # √num以降のチェックは不要
    while i * i <= num:
        # 割り切れる数があったら素数でない
        if num % i == 0:
            return False
        # 偶数のチェックは不要
        i += 2

    return True


class IsPrimeTest(unittest.TestCase):
    """is_primeのテスト"""

    def test_true(self):
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            self.assertTrue(is_prime(i))

    def test_false(self):
        for i in [1, 4, 6, 8, 9, 10, 12, 14, 16, 18, 20, 21, 22]:
            self.assertFalse(is_prime(i))

    def test_negative(self):
        self.assertFalse(is_prime(-1))

    def test_raise_typeerror(self):
        with self.assertRaises(TypeError):
            is_prime("42")


def count_time():
    """is_primeの時間計測"""
    nums = [random.randint(0, 100_000) for _ in range(100_000)]

    start = time.time()
    for num in nums:
        is_prime(num)

    t = time.time() - start
    print(f"time {t} secs")


if __name__ == "__main__":
    # テスト
    unittest.main()

    # 時間計測
    # count_time()
