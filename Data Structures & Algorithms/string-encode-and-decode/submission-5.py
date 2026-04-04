class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_key = "~123qwerasdf"
        encoder = ""
        if not strs:
            return encode_key + "null"
        return f"{encode_key}".join(strs)

    def decode(self, s: str) -> List[str]:
        encode_key = "~123qwerasdf"
        if s == encode_key + "null":
            return []
        return s.split(encode_key)