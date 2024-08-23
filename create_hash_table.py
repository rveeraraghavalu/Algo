#create hash table
def create_hash_table(size):
    hash_table = []
    for i in range(size):
        hash_table.append(None)
    return hash_table

def test_create_hash_table():
    hash_table = create_hash_table(10)
    assert len(hash_table) == 10

    hash_table = create_hash_table(0)
    assert len(hash_table) == 0 

    print("All test cases for create hash table passed!")

#write a test function to test proper functions for hash table lookup and insertion
def test_hash_table_lookup_and_insertion():
    hash_table = create_hash_table(10)
    hash_table[0] = "hello"
    assert hash_table[0] == "hello"

    hash_table[1] = "world" 
    assert hash_table[1] == "world"

    print("All test cases for hash table lookup and insertion passed!")

test_create_hash_table()
test_hash_table_lookup_and_insertion()
