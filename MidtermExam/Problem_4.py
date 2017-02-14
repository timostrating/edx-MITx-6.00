def closest_power(base, num):
    exponent = 0
    older = 0
    while True:
        value = base ** exponent
        if value < num:
            older = num - value
            exponent += 1
        else:
            olders = value - num
            if older == olders:
                if num == 1:
                    exponent = 0
                else:
                    exponent -= 1
            elif older < olders:
                exponent -= 1

            break

    return exponent


print(         closest_power(3, 12)          )
print(         closest_power(4, 12)          )
print(         closest_power(4, 1)          )