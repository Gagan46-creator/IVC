data = input("Enter data packet: ")

if data == data[::-1]:
    print("Data is intact (not corrupted)")
else:
    print("Data is corrupted")