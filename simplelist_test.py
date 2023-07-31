from simplelist import main


def test_list():
    result = main()
    assert result == list(('Orange', 'Kiwi', 'Apfel', 'Mango'))