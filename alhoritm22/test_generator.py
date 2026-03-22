import pytest
from alhoritm22 import Generator
from alhoritm22 import Outerwear

class TestGenerator:

    @pytest.fixture

    def init_outwear(self):
       #Підготовка до тестів
      return Outerwear ("Brand", "Type", "Color", 52, "Season", "Category")

    def test_gen_single_types(self):
        g = Generator()
        st = g.generate_single()
        assert isinstance(st, Outerwear)
        assert isinstance(st.Brand, str)
        assert isinstance(st.Type, str)
        assert isinstance(st.Color, str)
        assert isinstance(st.Size, int)
        assert isinstance(st.Season, str)
        assert isinstance(st.Category, str)

    def test_gen_1000_type(self):
        g = Generator()
        slist = g.generate_1000()
        assert isinstance(slist, list)
        assert isinstance(slist[0], Outerwear)
        assert len(slist) == 1000

    def test_gen_10_000_type(self):
        g = Generator()
        slist = g.generate_10_000()
        assert isinstance(slist, list)
        assert isinstance(slist[0], Outerwear)
        assert len(slist) == 10000