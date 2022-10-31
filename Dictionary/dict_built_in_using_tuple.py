if __name__ == '__main__':
    # Use tuple to create dictionary
    # let the state and capital to be in a tuple
    country = (
        ("California", "Sacramento"),
        ("New York", "Albany"),
        ("Texas", "Austin")
    )
    country = dict(country)
    print(country)
