n = int(input())

count = 0

mp = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20
}

for i in range(n):
    count += mp[input()]

print(count)