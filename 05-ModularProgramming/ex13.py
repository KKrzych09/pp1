import module_ex13

sentence = 'uniwersytet ekonomiczny w KRAKOWIE'

print(f'Wprowadzone zdanie: {sentence} \n')

print(f'Zdanie wspak: {module_ex13.reverse_string(sentence)} \n')

print(f'Zdanie ze spacjami: {module_ex13.separated_string(sentence)} \n')

print(f'Zdanie ze słowami od wielkich liter: {module_ex13.first_upper(sentence)}')