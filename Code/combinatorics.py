class combinatorics:
    
    @staticmethod
    def fat(n):
        if(n == 0):
            return 1
        return n * combinatorics.fat(n-1)

    @staticmethod
    def permutation(n, p):
        return combinatorics.fat(n) // combinatorics.fat(n - p)

    @staticmethod
    def combination(n, p):
        return (combinatorics.fat(n)) // (combinatorics.fat(p) * combinatorics.fat(n - p))
