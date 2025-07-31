def check_string_properties(s, methods):
    results = []
    for method in methods:
        for c in s:
            if method(c):
                results.append(True)
                break
        else:
            results.append(False)
    return results


if __name__ == "__main__":
    s = input("Enter a string: ")

    method_list = [
        str.isalnum,
        str.isalpha,
        str.isdigit,
        str.islower,
        str.isupper
    ]

    checks = check_string_properties(s, method_list)

    for result in checks:
        print(result)
