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
    # Accessing dictionary
    print("The capital of Texas is: %s" % country["Texas"])

    # Iterating over Dictionaries
    for key in country:
        print(key)

    print(country.items())