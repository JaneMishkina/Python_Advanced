import csv
import argparse
import logging


class FullName:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) \
                or any([c.isdigit() for c in value]) \
                or sum([n.istitle() for n in value.split()]) != 2:
            raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        else:
            setattr(instance, self.name, value)


class CsvData:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        with open(getattr(instance, self.name), 'r', encoding='UTF-8') as f:
            return {k: ([], []) for k in next(csv.reader(f))}

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.split('.')[-1] == 'csv':
            raise ValueError('invalid file name')
        else:
            setattr(instance, self.name, value)


class Student:
    full_name = FullName()
    subjects = CsvData()

    def __init__(self, name, csv_file):
        self.full_name = name
        self.subjects = csv_file
        self.grades = self.subjects.copy()

    def add_grade(self, subject, mark):
        if subject not in self.grades:
            raise ValueError(f'Предмет {subject} не найден')
        if not isinstance(mark, int) or not 2 <= mark <= 5:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        else:
            self.grades[subject][0].append(mark)

    def add_test_score(self, subject, test_score):
        if subject not in self.grades:
            raise ValueError(f'Предмет {subject} не найден')
        if not isinstance(test_score, int) or not 0 <= test_score <= 100:
            raise ValueError(f'Оценка должна быть целым числом от 0 до 100')
        else:
            self.grades[subject][1].append(test_score)

    def get_average_grade(self):
        all_grades = [*filter(lambda x: x.isdigit(),
                              str([m for s, (m, t)
                                   in self.grades.items() if m or t]))]
        return sum(map(int, all_grades)) / len(all_grades)

    def get_average_test_score(self, subject):
        if subject not in self.grades:
            raise ValueError(f'Предмет {subject} не найден')
        all_test_scores = [n for s, (m, t) in self.grades.items()
                           for n in t if s == subject]
        return sum(all_test_scores) / len(all_test_scores)

    def __str__(self):
        return f'Студент: {self.full_name.get(self, None)}\n' \
               f'Предметы: ' \
               f'{", ".join([s for s, (m, t) in self.grades.items() if m or t])}'


def main():
    parser = argparse.ArgumentParser(description='Process CSV file with student grades')
    parser.add_argument('file_name', type=str, help='Name of the CSV file with student grades')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        student = Student()
        student.__init__('John Doe', args.file_name)
        logger.info('Successfully initialized student')

        # Add some grades and test scores
        student.add_grade('Математика', 4)
        student.add_test_score('Математика', 85)

        avg_grade = student.get_average_grade()
        logger.info(f'Средний балл: {avg_grade}')

        avg_test_score = student.get_average_test_score('Math')
        logger.info(f'Средний результат по тестам по математике: {avg_test_score}')

        print(student)

    except Exception as e:
        logger.error(f'Error: {e}')


if __name__ == '__main__':
    main()
