import pytest
from store import Store
from exceptions import InvalidPriceError, ProductNotFoundError


def test_add_invalid_price(tmp_path):
    store = Store(tmp_path / "test.csv")
    with pytest.raises(InvalidPriceError):
        store.add_product("Apple", -5)


def test_remove_not_found(tmp_path):
    store = Store(tmp_path / "test.csv")
    with pytest.raises(ProductNotFoundError):
        store.remove_product("Banana")
