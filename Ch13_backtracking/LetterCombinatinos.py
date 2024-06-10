def letterCombinations(digits):
    dtc = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result = []

    def dfs(idx, curr_comb):
        if idx == len(digits):
            result.append(curr_comb)
            return

        curr = digits[idx]
        for char in dtc[curr]:
            dfs(idx + 1, curr_comb + char)

    dfs(0, "")

    return result


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))
