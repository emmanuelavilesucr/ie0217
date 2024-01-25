companies = {"Lacoste", "Ralph Lauren"}
tech_companies = ["apple", "google", "apple"]

companies.update(tech_companies)
print(companies)


languages = {"Swift", "Java", "Python"}

print("Initial Set:", languages)

removedValue = languages.discard("Java")
print("Set after remove(): ", languages)