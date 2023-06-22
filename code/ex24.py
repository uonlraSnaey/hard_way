print("Let's practice everything.")
print("Youd\'d need to know \' about escapes with \\ that do:")
print('\n newlines and \t tabs.')

poem = """

\tThe lovely world 
with logic so firm planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and require an explanation
\n\twhere there is none.

"""

print("----------------")
print(poem)
print("----------------")

five = 10 - 2 + 3 - 6
print(f"This should be five : {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, creates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))

print(f"we'd have {beans} beans, {jars} jars, and {creates} creates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # formula = [500000.0, 500.0, 5.0]

#We'd have 500000.0 beans, 500.0 jars, and 5.0 crates.
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) # 使用字符串的 format() 方法来填充占位符 {}，并将相应的值插入到字符串中。
