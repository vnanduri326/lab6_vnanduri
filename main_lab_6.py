#Vignesh Nanduri

def encode(password):
    encoded_password = ''
    for i in range(len(password)):
        encoded_password += str(3 + int(password[i]))
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        new_digit = (int(digit) - 3) % 10  # Shift each digit back by 3
        decoded_password += str(new_digit)
    return decoded_password

def main():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    user_option = int(input('\nPlease enter an option: '))
    prompt = True
    while prompt:
        if user_option == 1:
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            continue_menu = True
        elif user_option == 2:
            pass
        elif user_option == 3:
            prompt = False
            continue_menu = False
        while continue_menu:
            if user_option == 1:
                password = input('Please enter your password to encode: ')
                print('Your password has been encoded and stored!')
                continue_menu = True
            elif user_option == 2:
                pass
            elif user_option == 3:
                prompt = False
                continue_menu = False

if __name__ == '__main__':
    main()
