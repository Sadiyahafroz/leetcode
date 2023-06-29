class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves=list(moves)
        if moves.count("R")==moves.count("L"):
            if moves.count("U")==moves.count("D"):
                return True
        else:
            return False
            