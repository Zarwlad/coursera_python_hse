a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

# ax + by = e
# cx + dy = f

# y = (f - cx)/d
# ax + b(f - cx) / d = e
# (axd + bf - cxb) / d = e
# axd + bf - cxb = ed
# adx - cbx = ed - bf
# x(ad-cb) = ed - bf
# x = (ed - bf ) / (ad - cb)

# y = (e - ax)/b
# cx + d(e-ax)/b = f
# cxb + de - adx = fd
# x(cb - ad) = fb - de
# x = (fb - de) / (cb - ad)

if d != 0:
    x = (e * d - b * f) / (a * d - c * b)
    y = (f - c * x) / d
else:
    x = (f * b - d * e) / (c * b - a * d)
    y = (e - a * x) / b


if x % 1 == 0:
    x = int(x)
if y % 1 == 0:
    y = int(y)

print(x, y)
