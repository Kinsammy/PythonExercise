if __name__ == '__main__':
    grade_book = {
        'Susan': [92, 85, 100],
        'Edvice': [83, 95, 79],
        'Azeez': [91,89,82],
        'Peter': [97, 91, 92]
    }
    grade_total = 0
    grade_counter = 0

    for name, grades in grade_book.items():
        total = sum(grades)
        print(f"Average for {name}' is {total/len(grades):.2f}")
        grade_total += total
        grade_counter += len(grades)

    print(f"Class's Average is: {grade_total / grade_counter:.2f}")