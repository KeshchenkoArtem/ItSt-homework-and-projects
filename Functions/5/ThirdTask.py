def stars(n):
    if n <= 0:
        return
    print("*", end=" ")
    stars(n - 1)

count = int(input("Скілки треба зірок ?: "))
stars(count)