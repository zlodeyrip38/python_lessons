import wikipedia as wiki
wiki.set_lang("ru")


while True:
    
    search = input("Что искать?\n")
    try:
        s = wiki.page(search)
        print(s.content)
    except:
        print("Ничего не найдено!")
        print()
        s = wiki.search(search)

        if s:
            print("Возможно вы имели ввиду:")
            print("========================")
            
            for item in s:
                print(item)
            print("========================")
    
    print()

