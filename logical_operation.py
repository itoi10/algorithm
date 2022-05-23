def and_(x: bool, y: bool) -> bool:
    """論理積"""
    return x and y


def or_(x: bool, y: bool) -> bool:
    """論理和"""
    return x or y


def not_(x: bool) -> bool:
    """否定"""
    return not x


def xor_(x: bool, y: bool) -> bool:
    """排他的論理和"""
    return or_(and_(x, not_(y)), and_(not_(x), y))


def half_adder(x: bool, y: bool) -> tuple[bool, bool]:
    """半加算器"""
    s = xor_(x, y)
    c = and_(x, y)
    return s, c


def full_adder(x: bool, y: bool, c: bool) -> tuple[bool, bool]:
    """全加算器"""
    s0, c0 = half_adder(x, y)
    s1, c1 = half_adder(s0, c)
    return s1, or_(c1, c0)


def _8bit_adder(xs: list[bool], ys: list[bool]) -> list[bool]:
    """8bit加算器"""
    ss = [0, 0, 0, 0, 0, 0, 0, 0]
    ss[7], c = half_adder(xs[7], ys[7])
    ss[6], c = full_adder(xs[6], ys[6], c)
    ss[5], c = full_adder(xs[5], ys[5], c)
    ss[4], c = full_adder(xs[4], ys[4], c)
    ss[3], c = full_adder(xs[3], ys[3], c)
    ss[2], c = full_adder(xs[2], ys[2], c)
    ss[1], c = full_adder(xs[1], ys[1], c)
    ss[0], c = full_adder(xs[0], ys[0], c)
    return ss


def twos_complement(xs: list[bool]) -> list[bool]:
    """2の補数"""
    bit_n = len(xs)
    ns = [0] * bit_n
    # ビット反転
    for i in range(bit_n):
        ns[i] = not_(xs[i])
    # 1を加算
    one = [0] * (bit_n - 1) + [1]  # [0, 0, 0, 0, 0, 0, 0, 1]
    return _8bit_adder(ns, one)


class Bits:
    def __init__(self, bits: str | list[bool]):
        self.value = [0] * len(bits)
        for i in range(len(bits)):
            self.value[i] = bool(int(bits[i]))

    def to_s(self) -> str:
        st = ""
        for v in self.value:
            st += str(int(v))
        return st


if __name__ == "__main__":
    xs = Bits("00111011")  # 59(10)
    ys = Bits("00100100")  # 36(10)

    # ** 加算 **
    #  2進数) 00111011 + 00100100 = 01011111
    # 10進数)       59 +       36 =       95
    ss = Bits(_8bit_adder(xs.value, ys.value))
    print(xs.to_s(), "+", ys.to_s(), "=", ss.to_s())

    # ** 減算 **
    #  2進数) 00111011 + 11011100 = 00010111
    # 10進数)       59 +    (-36) =       23
    ys2 = Bits(twos_complement(ys.value))
    ss2 = Bits(_8bit_adder(xs.value, ys2.value))
    print(xs.to_s(), "+", ys2.to_s(), "=", ss2.to_s())
