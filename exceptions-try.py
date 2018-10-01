while True:
    try:
        number = int(input("What's your favourite number?\n"))
        print(18 / number)
        break
    except ValueError:
        print("Make sure you enter a number")
    except ZeroDivisionError:
        print("Don't pick 0")
    except:
        print("Make sure you enter a number")
        break
    finally:
        print("loop finished")