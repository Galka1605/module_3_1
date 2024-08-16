calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    print((len(string), string.upper(), string.lower()))
    count_calls()

def is_contains(string, list_to_search):
    string_lower = string.lower()
    list_to_search_lower = []
    for i in list_to_search:
        list_to_search_lower.append(i.lower())
    if string_lower in list_to_search_lower:
        print(True)
    else:
        print(False)
    count_calls()

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
