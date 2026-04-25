import pytest
from alhoritm22 import Generator
from alhoritm22 import Outerwear

class TestOuterwear:
    @pytest.fixture
    def init_Outerwear(self):
        st1 = Outerwear("Olko", "шуба", "синій", 40, "літо", "жіноча")
       # st=Generator.generate_single(st1)

        return  st1

    def test_data_type(self, init_Outerwear):
        """Перевірка відповідності класу"""
        assert isinstance(init_Outerwear, Outerwear)

    def test_check_init(self):
        #Перевірка ініціації і внесення даних
       st = Outerwear("Olko", "шуба", "синій", 40, "літо", "жіноча")
       assert st.Brand == "Olko"
       assert st.Type == "шуба"
       assert st.Color == "синій"
       assert st.Size == 40
       assert st.Season == "літо"
       assert st.Category == "жіноча"

    def test_get_info(self, init_Outerwear):
        #Перевірка методу get_info()
        st = Outerwear("Olko", "шуба", "синій", 40, "літо", "жіноча")
        assert init_Outerwear.get_info() == f'Товар: {st.Type}, бренду {st.Brand}, кольору {st.Color}, розміру {st.Size}, категорії  {st.Category}'

    def test_get_message(self, init_Outerwear):
        #Перевірка методу get_info()
        st1 = Outerwear("Olko", "шуба", "синій", 40, "зима", "жіноча")
        assert init_Outerwear.get_message() ==f'Обраний: {st1.Type}, бренду: {st1.Brand}, розміром: {st1.Size}, відноситься до "{st1.Season}" колекції'
