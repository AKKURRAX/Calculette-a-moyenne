def main():
    # recolter une première note
    note1 = int(input("Entrer la première votre première note:"))
    note2 = int(input("Entrer votre seconde note:"))
    note3 = int(input ("Entrer votre dernière note:"))


    result = (note1 + note2 + note3) / 3
    print("Ta moyenne dans cette matière est de " + str(result))

if __name__ == '__main__':
    main()
