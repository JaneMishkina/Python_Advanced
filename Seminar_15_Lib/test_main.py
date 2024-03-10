
import pytest
import csv
from Seminar_15_Lib.main import Student, CsvData, FullName

# Тестирование класса FullName

@pytest.fixture
def full_name_instance():
    return FullName()


def test_set_invalid_full_name():
    full_name = FullName()
    instance = {}
    value = '123 Иван'
    with pytest.raises(ValueError):
        full_name.__set__(instance, value)

# Тестирование класса CsvData

def test_csv_data_invalid():
    csv_data = CsvData()
    with pytest.raises(ValueError):
        csv_data.__set__(None, 'not_a_csv_file.txt')

# Тестирование класса Student
def test_student_average_grade():
    student = Student('Jane Smith', 'subjects.csv')
    student.__init__('Jane Smith', 'subjects.csv')
    student.add_grade('Математика', 4)
    student.add_grade('Физика', 5)
    assert student.get_average_grade() == 4.5

def test_student_average_test_score_invalid():
    student = Student('Jane Smith', 'subjects.csv')
    # student.__init__('Jane Smith', 'subjects.csv')
    student.add_test_score('Математика', 80)
    student.add_test_score('Математика', 90)
    with pytest.raises(ValueError):
        student.get_average_test_score('Английский')

def test_student_average_test_score():
    student = Student('Jane Smith', 'subjects.csv')
    # student.__init__('Jane Smith', 'subjects.csv')
    student.add_test_score('Математика', 80)
    student.add_test_score('Математика', 90)
    assert student.get_average_test_score('Математика') == 85

if __name__ == '__main__':
    pytest.main()

