test_cases = [
    # 1. Rook กิน King → Success
    ([
        "R...",
        ".K..",
        "....",
        "...."
    ], "Success"),

    # 2. ไม่มีใครกิน King → Fail
    ([
        "....",
        ".K..",
        "....",
        "...."
    ], "Fail"),

    # 3. Bishop กิน King → Success
    ([
        "B...",
        "....",
        "..K.",
        "...."
    ], "Success"),

    # 4. Queen กิน King → Success
    ([
        "..Q.",
        "....",
        ".K..",
        "...."
    ], "Success"),

    # 5. Pawn กิน King → Success
    ([
        "....",
        ".P..",
        "..K.",
        "...."
    ], "Success"),

    # 6. มีตัวขวาง → Fail
    ([
        "R.P.",
        ".K..",
        "....",
        "...."
    ], "Fail"),

    # 7. Board เล็ก → Fail
    ([
        ".K"
    ], "Fail"),

    # 8. King มุมกระดาน → Success
    ([
        "K..R",
        "....",
        "....",
        "...."
    ], "Success"),

    # 9. หลายตัวรุม → Success
    ([
        "Q...",
        ".B..",
        "..K.",
        "..R."
    ], "Success"),
]
