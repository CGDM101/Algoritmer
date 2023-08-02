# A key is the identifying data for a particular data record. Snabbare att sortera nycklarna är hela records. T ex sortera anställningsid i st f all info på employee.

# Hashfunktion förvandlar nyckeln till ett numeriskt värde. Hash table söktid O(1) i bästa fall.
# Beräkna hashvärde; t ex obtain the modulus of the value divided by the number of slots. Ex för att spara 54 i en hashtabell med 15 slots, så blir hashvärdet 9. Så 54 sätts in i slot 9

from hashlib import md5, sha1  # Secure Hash Algorithms, MD5-algoritm
data = [22, 40, 102, 105, 23, 31, 6, 5]
hash_table = [None] * 15
tblLen = len(hash_table)

def hash_function(value, table_size):
    return value % table_size

for value in data:
    hash_table[hash_function(value, tblLen)] = value

# Resultatet utifrån datan: [105, 31, None, None, None, 5, 6, 22, 23, None, 40, None, 102, None, None]
print(hash_table)

print(hash_table[hash_function(102, tblLen)])  # 102?

# SKAPA HASHFUNKTION MED SHA ELLER MD5
def hash_f(element, i, length):
    """ Function to create many hash functions """
    h1 = int(md5(element.encode('ascii')).hexdigest(), 16)
    h2 = int(sha1(element.encode('ascii')).hexdigest(), 16)
    return (h1 + i*h2) % length


print(hash_f("CAT", 1, 10**5))  # Detta ger: 64018

print(hash_f("CAT", 2, 10**5))  # Detta ger: 43738
