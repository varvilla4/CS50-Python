from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(2)
    assert jar2.capacity == 2

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(2)
    assert jar.size == 5


def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(3)
    assert jar.size == 6
    jar.withdraw(1)
    assert jar.size == 5
