w = input()
print('.'+''.join('.#..' if i%3<2 else '.*..' for i in range(len(w))))
print('.'+''.join('#.#.' if i%3<2 else '*.*.' for i in range(len(w))))
print('#'+''.join(f'.{c}.#' if i%3<1 or i%3==1 and i==len(w)-1 else f'.{c}.*' for i,c in enumerate(w)))
print('.'+''.join('#.#.' if i%3<2 else '*.*.' for i in range(len(w))))
print('.'+''.join('.#..' if i%3<2 else '.*..' for i in range(len(w))))