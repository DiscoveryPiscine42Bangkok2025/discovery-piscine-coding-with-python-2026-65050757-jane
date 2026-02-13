from checkmate import checkmate

def main():

    boards = [

        # 1. Fail — ไม่มีใครกิน King
        """\
....
.K..
....
....\
""",

        # 2. Success — Rook กิน King
        """\
R...
.K..
....
....\
""",

        # 3. Success — Bishop กิน King
        """\
B...
....
..K.
....\
""",

        # 4. Success — Queen กิน King
        """\
..Q.
....
.K..
....\
""",

        # 5. Success — Pawn กิน King
        """\
....
.P..
..K.
....\
""",

        # 6. Fail — มีตัวขวาง
        """\
R.P.
.K..
....
....\
""",

        # 7. Edge — board เล็ก
        """\
.K\
""",

        # 8. Success — King มุมกระดาน
        """\
K..R
....
....
....\
""",

        # 9. Success — หลายตัวรุม
        """\
....
..K.
....
..R.\
"""
    ]

    for board in boards:
        print("Board:")
        print(board)
        checkmate(board)
        print()

if __name__ == "__main__":
    main()
