class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x_candidates, y_candidates = {}, {}
        bull, cow = 0, 0
        for x, y in zip(secret, guess):
            if x == y:
                bull += 1
                continue
            if x_candidates.get(x, 0) > 0:
                x_candidates[x] -= 1
                cow += 1
            else:
                y_candidates[x] = y_candidates.get(x, 0) + 1
            if y_candidates.get(y, 0) > 0:
                y_candidates[y] -= 1
                cow += 1
            else:
                x_candidates[y] = x_candidates.get(y, 0) + 1
        return f"{bull}A{cow}B"


if __name__ == "__main__":
    secret = "1807"
    guess = "7810"
    ans = Solution().getHint(secret, guess)
    print(ans)
