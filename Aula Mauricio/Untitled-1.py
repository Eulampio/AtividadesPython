def test_adiciona_dias():
    assert adiciona_dias("01/01/2024", 10) == "11/01/2024"
    assert adiciona_dias("31/12/2024", 1) == "01/01/2025"
    assert adiciona_dias("01/01/2024", 0) == "01/01/2024"
    print("test_adiciona_dias passou!")
