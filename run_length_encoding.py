import unittest


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0
def encode(s):
    ret = ''
    prev = ''
    c = 0
    for i in s:
        if prev == i:
            c += 1
        else:
            ret += (str(c) if (c!=1) and c and prev else '') + prev
            c, prev = 1, i
    ret += (str(c) if (c!=1) and c and prev else '') + prev
    if (not len(ret)-2)and(ret[-1] == ret[-2]):
        ret = ret[:-1]
    return ret
        
def decode(s):
    ret = ''
    n = ''
    for i in s:
        if i.isdigit():
            n += i
        else:
            ret += i*int(n) if n else i
            n = ''
    return ret


class RunLengthEncodingTest(unittest.TestCase):
    def test_encode_empty_string(self):
        self.assertMultiLineEqual(encode(""), "")

    def test_encode_single_characters_only_are_encoded_without_count(self):
        self.assertMultiLineEqual(encode("XYZ"), "XYZ")

    def test_encode_string_with_no_single_characters(self):
        self.assertMultiLineEqual(encode("AABBBCCCC"), "2A3B4C")

    def test_encode_single_characters_mixed_with_repeated_characters(self):
        self.assertMultiLineEqual(
            encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"),
            "12WB12W3B24WB",
        )

    def test_encode_multiple_whitespace_mixed_in_string(self):
        self.assertMultiLineEqual(encode("  hsqq qww  "), "2 hs2q q2w2 ")

    def test_encode_lowercase_characters(self):
        self.assertMultiLineEqual(encode("aabbbcccc"), "2a3b4c")

    def test_decode_empty_string(self):
        self.assertMultiLineEqual(decode(""), "")

    def test_decode_single_characters_only(self):
        self.assertMultiLineEqual(decode("XYZ"), "XYZ")

    def test_decode_string_with_no_single_characters(self):
        self.assertMultiLineEqual(decode("2A3B4C"), "AABBBCCCC")

    def test_decode_single_characters_with_repeated_characters(self):
        self.assertMultiLineEqual(
            decode("12WB12W3B24WB"),
            "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB",
        )

    def test_decode_multiple_whitespace_mixed_in_string(self):
        self.assertMultiLineEqual(decode("2 hs2q q2w2 "), "  hsqq qww  ")

    def test_decode_lower_case_string(self):
        self.assertMultiLineEqual(decode("2a3b4c"), "aabbbcccc")

    def test_encode_followed_by_decode_gives_original_string(self):
        self.assertMultiLineEqual(decode(encode("zzz ZZ  zZ")), "zzz ZZ  zZ")


if __name__ == "__main__":
    unittest.main()