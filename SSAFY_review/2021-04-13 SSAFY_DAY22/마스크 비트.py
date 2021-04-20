# 16진수 2자리씩 끊어서 가져와보기


def get_number(num, i):
    # (1 << n) - 1 : n = 8일 때 0xff가 된다.
    mask_bits = (1 << 8) - 1
    return (num >> 8*i) & mask_bits


a = 0x12345678
for i in range(4):
    print('0x%X' % get_number(a, i))