print("Helló Világ!")
szoveg1 = "Valami szöveg"
print(szoveg1)

#több soros szöveg
tobbSoros = """Ez egy sor
ez is egy sor
ez meg főleg egy sor"""
print(tobbSoros)

# a stringek -> tömbök
print(szoveg1[0])
print("A string karakterei")
for x in szoveg1:
    print(x)
print("A szoveg1 karaktereinek száma:", len(szoveg1))
print(f"A szoveg1 karaktereinek száma: {len(szoveg1)}")

#tartalmazza-e az adott karaktersorozatot - Contains
if "asd" in szoveg1:
    print("Benne van a asd")
else:
    print("Nincs benne a asd")

print(szoveg1[5:10]) #5-10-ig
print(szoveg1[:10])     #elejétől 10
print(szoveg1[5:])      #5.től a végéig

szoveg2 = "Alma, körte, szilva"
print(szoveg2.upper())
print(szoveg2.lower())
print(szoveg2.replace("a","A"))
print(szoveg1 + " | " + szoveg2)
print(szoveg1 * 3)
