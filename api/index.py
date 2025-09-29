import random
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../templates', static_folder='../static')

letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

@app.route("/", methods=["GET", "POST"])
def index():
    nr_letters = nr_symbols = nr_numbers = 0
    password = None
    error = None

    if request.method == "POST":
        try:
            nr_letters = int(request.form.get("nr_letters", 0))
            nr_symbols = int(request.form.get("nr_symbols", 0))
            nr_numbers = int(request.form.get("nr_numbers", 0))
        except ValueError:
            error = "Please enter valid numbers."
            return render_template("index.html", error=error, password=None,
                                   nr_letters=nr_letters, nr_symbols=nr_symbols, nr_numbers=nr_numbers)

        password_list = [random.choice(letters) for _ in range(nr_letters)]
        password_list += [random.choice(symbols) for _ in range(nr_symbols)]
        password_list += [random.choice(numbers) for _ in range(nr_numbers)]

        # Shuffle if checkbox is checked
        if request.form.get("shuffle") == "on":
            random.shuffle(password_list)

        password = "".join(password_list)

    return render_template("index.html", password=password, error=error,
                           nr_letters=nr_letters, nr_symbols=nr_symbols, nr_numbers=nr_numbers)


# Easy Level
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

#hard Level

# password_list = []
# for char in range(1, nr_letters + 1):
#     password_list.append(random.choice(letters))
# for char in range(1, nr_symbols + 1):
#     password_list.append(random.choice(symbols))
# for char in range(1, nr_numbers + 1):
#     password_list.append(random.choice(numbers))
# random.shuffle(password_list)
# password = ""

# for char in password_list: # back to string
#     password += char
# print(password)       