import click
import sys
import os
import json
import random
import datetime
import time
import itertools
import hashlib
import platform
import string
import math
import uuid
import functools

# DataStore class to handle file-based data storage
class DataStore:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        self.load_data()

    def load_data(self):
        # Load data from file if it exists, otherwise initialize as empty
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    self.data = {}
        else:
            self.data = {}

    def save_data(self):
        # Save data to file
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def create_record(self, section, record_id, content):
        # Create a new record in the specified section
        if section not in self.data:
            self.data[section] = {}
        if record_id in self.data[section]:
            return False
        self.data[section][record_id] = content
        self.save_data()
        return True

    def read_record(self, section, record_id):
        # Read a record from the specified section
        if section in self.data and record_id in self.data[section]:
            return self.data[section][record_id]
        return None

    def update_record(self, section, record_id, content):
        # Update an existing record in the specified section
        if section in self.data and record_id in self.data[section]:
            self.data[section][record_id] = content
            self.save_data()
            return True
        return False

    def delete_record(self, section, record_id):
        # Delete a record from the specified section
        if section in self.data and record_id in self.data[section]:
            del self.data[section][record_id]
            self.save_data()
            return True
        return False

    def list_records(self, section):
        # List all records in the specified section
        if section in self.data:
            return list(self.data[section].keys())
        return []

# MathUtility class to perform various mathematical operations
class MathUtility:
    def __init__(self):
        pass

    def factorial(self, n):
        # Calculate the factorial of a number
        if n < 0:
            return None
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def fibonacci_sequence(self, limit):
        # Generate Fibonacci sequence up to a limit
        sequence = []
        a = 0
        b = 1
        while a <= limit:
            sequence.append(a)
            a, b = b, a + b
        return sequence

    def prime_check(self, n):
        # Check if a number is prime
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def gcd(self, a, b):
        # Calculate the greatest common divisor
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        # Calculate the least common multiple
        return abs(a*b) // self.gcd(a, b) if a and b else 0

# StringUtility class to perform various string operations
class StringUtility:
    def __init__(self):
        pass

    def reverse_string(self, text):
        # Reverse a string
        return text[::-1]

    def uppercase_string(self, text):
        # Convert a string to uppercase
        return text.upper()

    def lowercase_string(self, text):
        # Convert a string to lowercase
        return text.lower()

    def capitalize_string(self, text):
        # Capitalize the first character of a string
        return text.capitalize()

    def is_palindrome(self, text):
        # Check if a string is a palindrome
        return text == text[::-1]

    def remove_punctuation(self, text):
        # Remove punctuation from a string
        return "".join(ch for ch in text if ch not in string.punctuation)

    def count_vowels(self, text):
        # Count the number of vowels in a string
        vowels = "aeiouAEIOU"
        return sum(1 for ch in text if ch in vowels)

    def sort_characters(self, text):
        # Sort the characters in a string
        return "".join(sorted(text))

# CryptoUtility class to perform various cryptographic operations
class CryptoUtility:
    def __init__(self):
        pass

    def md5_hash(self, text):
        # Generate MD5 hash of a string
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    def sha256_hash(self, text):
        # Generate SHA-256 hash of a string
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def sha1_hash(self, text):
        # Generate SHA-1 hash of a string
        return hashlib.sha1(text.encode("utf-8")).hexdigest()

    def generate_uuid(self):
        # Generate a UUID
        return str(uuid.uuid4())

# DateTimeUtility class to perform various date and time operations
class DateTimeUtility:
    def __init__(self):
        pass

    def current_datetime(self):
        # Get the current date and time
        return datetime.datetime.now()

    def current_date(self):
        # Get the current date
        return datetime.date.today()

    def timestamp_to_date(self, ts):
        # Convert a timestamp to a date
        return datetime.datetime.fromtimestamp(ts).date()

    def timestamp_to_datetime(self, ts):
        # Convert a timestamp to a date and time
        return datetime.datetime.fromtimestamp(ts)

    def format_datetime(self, dt, fmt):
        # Format a date and time object to a string
        return dt.strftime(fmt)

    def parse_datetime(self, dt_str, fmt):
        # Parse a date and time string to a date and time object
        return datetime.datetime.strptime(dt_str, fmt)

# SystemUtility class to perform various system operations
class SystemUtility:
    def __init__(self):
        pass

    def operating_system(self):
        # Get the operating system name
        return platform.system()

    def machine_architecture(self):
        # Get the machine architecture
        return platform.machine()

    def processor_info(self):
        # Get the processor information
        return platform.processor()

    def python_version(self):
        # Get the Python version
        return platform.python_version()

    def environment_variables(self):
        # Get the environment variables
        return dict(os.environ)

    def current_working_directory(self):
        # Get the current working directory
        return os.getcwd()

# FileUtility class to perform various file operations
class FileUtility:
    def __init__(self):
        pass

    def list_directory(self, path):
        # List the contents of a directory
        if os.path.isdir(path):
            return os.listdir(path)
        return []

    def file_exists(self, path):
        # Check if a file exists
        return os.path.isfile(path)

    def directory_exists(self, path):
        # Check if a directory exists
        return os.path.isdir(path)

    def read_file(self, path):
        # Read the contents of a file
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        return None

    def write_file(self, path, content):
        # Write content to a file
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def append_file(self, path, content):
        # Append content to a file
        with open(path, "a", encoding="utf-8") as f:
            f.write(content)

    def create_directory(self, path):
        # Create a directory
        if not os.path.exists(path):
            os.makedirs(path)
            return True
        return False

# CollectionUtility class to perform various collection operations
class CollectionUtility:
    def __init__(self):
        pass

    def deduplicate_list(self, items):
        # Remove duplicates from a list
        return list(dict.fromkeys(items))

    def flatten_nested_list(self, nested):
        # Flatten a nested list
        flattened = []
        for element in nested:
            if isinstance(element, list):
                flattened.extend(self.flatten_nested_list(element))
            else:
                flattened.append(element)
        return flattened

    def chunk_list(self, items, size):
        # Chunk a list into smaller lists of a given size
        for i in range(0, len(items), size):
            yield items[i : i + size]

    def combinations_of_list(self, items, r):
        # Generate combinations of a list
        return list(itertools.combinations(items, r))

    def permutations_of_list(self, items, r):
        # Generate permutations of a list
        return list(itertools.permutations(items, r))

    def accumulate_list_sum(self, items):
        # Accumulate the sum of a list
        return list(itertools.accumulate(items))

    def group_list_by_condition(self, items, condition_func):
        # Group a list by a condition
        true_group = []
        false_group = []
        for x in items:
            if condition_func(x):
                true_group.append(x)
            else:
                false_group.append(x)
        return true_group, false_group

# SortingUtility class to perform various sorting operations
class SortingUtility:
    def __init__(self):
        pass

    def bubble_sort(self, arr):
        # Perform bubble sort on a list
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def insertion_sort(self, arr):
        # Perform insertion sort on a list
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def quick_sort(self, arr):
        # Perform quick sort on a list
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def merge_sort(self, arr):
        # Perform merge sort on a list
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            self.merge_sort(left_half)
            self.merge_sort(right_half)
            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr

# Click CLI group for data operations
@click.group()
def cli():
    pass

@cli.group()
def data():
    pass

@data.command("CREATE-RECORD")
@click.argument("filename")
@click.argument("section")
@click.argument("record_id")
@click.argument("content")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def create(filename, section, record_id, content, help):
    if help:
        click.echo("Create a new record in the specified section.")
        click.echo("Usage: create FILENAME SECTION RECORD_ID CONTENT")
        return
    ds = DataStore(filename)
    result = ds.create_record(section, record_id, content)
    if result:
        click.echo("Record created")
    else:
        click.echo("Record already exists")

@data.command("READ-RECORD")
@click.argument("filename")
@click.argument("section")
@click.argument("record_id")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def read(filename, section, record_id, help):
    if help:
        click.echo("Read a record from the specified section.")
        click.echo("Usage: read FILENAME SECTION RECORD_ID")
        return
    ds = DataStore(filename)
    result = ds.read_record(section, record_id)
    if result is not None:
        click.echo(f"Content: {result}")
    else:
        click.echo("Record not found")

@data.command("UPDATE-RECORD")
@click.argument("filename")
@click.argument("section")
@click.argument("record_id")
@click.argument("content")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def update(filename, section, record_id, content, help):
    if help:
        click.echo("Update an existing record in the specified section.")
        click.echo("Usage: update FILENAME SECTION RECORD_ID CONTENT")
        return
    ds = DataStore(filename)
    result = ds.update_record(section, record_id, content)
    if result:
        click.echo("Record updated")
    else:
        click.echo("Record not found")

@data.command("DELETE-RECORD")
@click.argument("filename")
@click.argument("section")
@click.argument("record_id")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def delete(filename, section, record_id, help):
    if help:
        click.echo("Delete a record from the specified section.")
        click.echo("Usage: delete FILENAME SECTION RECORD_ID")
        return
    ds = DataStore(filename)
    result = ds.delete_record(section, record_id)
    if result:
        click.echo("Record deleted")
    else:
        click.echo("Record not found")

@data.command("LIST-RECORDS")
@click.argument("filename")
@click.argument("section")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def listall(filename, section, help):
    if help:
        click.echo("List all records in the specified section.")
        click.echo("Usage: listall FILENAME SECTION")
        return
    ds = DataStore(filename)
    records = ds.list_records(section)
    if records:
        for rec in records:
            click.echo(rec)
    else:
        click.echo("No records found")

# Click CLI group for mathematical operations
@cli.group()
def mathops():
    pass

@mathops.command("CALCULATE-FACTORIAL")
@click.argument("n", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def factorial(n, help):
    if help:
        click.echo("Calculate the factorial of a number.")
        click.echo("Usage: factorial N")
        return
    mu = MathUtility()
    result = mu.factorial(n)
    if result is None:
        click.echo("Factorial not defined for negative values")
    else:
        click.echo(result)

@mathops.command("GENERATE-FIBONACCI")
@click.argument("limit", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def fibonacci(limit, help):
    if help:
        click.echo("Generate Fibonacci sequence up to a limit.")
        click.echo("Usage: fibonacci LIMIT")
        return
    mu = MathUtility()
    seq = mu.fibonacci_sequence(limit)
    click.echo(", ".join(map(str, seq)))

@mathops.command("CHECK-PRIME")
@click.argument("n", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def prime(n, help):
    if help:
        click.echo("Check if a number is prime.")
        click.echo("Usage: prime N")
        return
    mu = MathUtility()
    result = mu.prime_check(n)
    if result:
        click.echo("Prime")
    else:
        click.echo("Not prime")

@mathops.command("CALCULATE-GCD")
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def gcd(a, b, help):
    if help:
        click.echo("Calculate the greatest common divisor.")
        click.echo("Usage: gcd A B")
        return
    mu = MathUtility()
    result = mu.gcd(a, b)
    click.echo(result)

@mathops.command("CALCULATE-LCM")
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def lcm(a, b, help):
    if help:
        click.echo("Calculate the least common multiple.")
        click.echo("Usage: lcm A B")
        return
    mu = MathUtility()
    result = mu.lcm(a, b)
    click.echo(result)

# Click CLI group for text operations
@cli.group()
def textops():
    pass

@textops.command("REVERSE-STRING")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def reverse(text, help):
    if help:
        click.echo("Reverse a string.")
        click.echo("Usage: reverse TEXT")
        return
    su = StringUtility()
    click.echo(su.reverse_string(text))

@textops.command("UPPERCASE-STRING")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def upper(text, help):
    if help:
        click.echo("Convert a string to uppercase.")
        click.echo("Usage: upper TEXT")
        return
    su = StringUtility()
    click.echo(su.uppercase_string(text))

@textops.command("LOWERCASE-STRING")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def lower(text, help):
    if help:
        click.echo("Convert a string to lowercase.")
        click.echo("Usage: lower TEXT")
        return
    su = StringUtility()
    click.echo(su.lowercase_string(text))

@textops.command("CAPITALIZE-STRING")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def cap(text, help):
    if help:
        click.echo("Capitalize the first character of a string.")
        click.echo("Usage: cap TEXT")
        return
    su = StringUtility()
    click.echo(su.capitalize_string(text))

@textops.command("CHECK-PALINDROME")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def palindrome(text, help):
    if help:
        click.echo("Check if a string is a palindrome.")
        click.echo("Usage: palindrome TEXT")
        return
    su = StringUtility()
    if su.is_palindrome(text):
        click.echo("Yes")
    else:
        click.echo("No")

@textops.command("REMOVE-PUNCTUATION")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def nopunct(text, help):
    if help:
        click.echo("Remove punctuation from a string.")
        click.echo("Usage: nopunct TEXT")
        return
    su = StringUtility()
    click.echo(su.remove_punctuation(text))

@textops.command("COUNT-VOWELS")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def vowels(text, help):
    if help:
        click.echo("Count the number of vowels in a string.")
        click.echo("Usage: vowels TEXT")
        return
    su = StringUtility()
    count = su.count_vowels(text)
    click.echo(str(count))

@textops.command("SORT-CHARACTERS")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def sortchars(text, help):
    if help:
        click.echo("Sort the characters in a string.")
        click.echo("Usage: sortchars TEXT")
        return
    su = StringUtility()
    click.echo(su.sort_characters(text))

# Click CLI group for cryptographic operations
@cli.group()
def crypto():
    pass

@crypto.command("GENERATE-MD5-HASH")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def md5hash(text, help):
    if help:
        click.echo("Generate MD5 hash of a string.")
        click.echo("Usage: md5hash TEXT")
        return
    cu = CryptoUtility()
    click.echo(cu.md5_hash(text))

@crypto.command("GENERATE-SHA256-HASH")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def sha256hash(text, help):
    if help:
        click.echo("Generate SHA-256 hash of a string.")
        click.echo("Usage: sha256hash TEXT")
        return
    cu = CryptoUtility()
    click.echo(cu.sha256_hash(text))

@crypto.command("GENERATE-SHA1-HASH")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def sha1hash(text, help):
    if help:
        click.echo("Generate SHA-1 hash of a string.")
        click.echo("Usage: sha1hash TEXT")
        return
    cu = CryptoUtility()
    click.echo(cu.sha1_hash(text))

@crypto.command("GENERATE-UUID")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def getuuid(help):
    if help:
        click.echo("Generate a UUID.")
        click.echo("Usage: getuuid")
        return
    cu = CryptoUtility()
    click.echo(cu.generate_uuid())

# Click CLI group for date and time operations
@cli.group()
def dt():
    pass

@dt.command("CURRENT-DATETIME")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def now(help):
    if help:
        click.echo("Get the current date and time.")
        click.echo("Usage: now")
        return
    du = DateTimeUtility()
    click.echo(str(du.current_datetime()))

@dt.command("CURRENT-DATE")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def today(help):
    if help:
        click.echo("Get the current date.")
        click.echo("Usage: today")
        return
    du = DateTimeUtility()
    click.echo(str(du.current_date()))

@dt.command("TIMESTAMP-TO-DATE")
@click.argument("ts", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def datets(ts, help):
    if help:
        click.echo("Convert a timestamp to a date.")
        click.echo("Usage: datets TS")
        return
    du = DateTimeUtility()
    click.echo(str(du.timestamp_to_date(ts)))

@dt.command("TIMESTAMP-TO-DATETIME")
@click.argument("ts", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def datetimets(ts, help):
    if help:
        click.echo("Convert a timestamp to a date and time.")
        click.echo("Usage: datetimets TS")
        return
    du = DateTimeUtility()
    click.echo(str(du.timestamp_to_datetime(ts)))

@dt.command("FORMAT-DATETIME")
@click.argument("fmt")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def formatted(fmt, help):
    if help:
        click.echo("Format a date and time object to a string.")
        click.echo("Usage: formatted FMT")
        return
    du = DateTimeUtility()
    now_obj = du.current_datetime()
    click.echo(du.format_datetime(now_obj, fmt))

@dt.command("PARSE-DATETIME")
@click.argument("dtstr")
@click.argument("fmt")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def parse(dtstr, fmt, help):
    if help:
        click.echo("Parse a date and time string to a date and time object.")
        click.echo("Usage: parse DTSTR FMT")
        return
    du = DateTimeUtility()
    parsed = du.parse_datetime(dtstr, fmt)
    click.echo(str(parsed))

# Click CLI group for system operations
@cli.group()
def system():
    pass

@system.command("OS-INFO")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def osinfo(help):
    if help:
        click.echo("Get the operating system name.")
        click.echo("Usage: osinfo")
        return
    su = SystemUtility()
    click.echo(su.operating_system())

@system.command("MACHINE-ARCHITECTURE")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def machine(help):
    if help:
        click.echo("Get the machine architecture.")
        click.echo("Usage: machine")
        return
    su = SystemUtility()
    click.echo(su.machine_architecture())

@system.command("PROCESSOR-INFO")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def cpu(help):
    if help:
        click.echo("Get the processor information.")
        click.echo("Usage: cpu")
        return
    su = SystemUtility()
    click.echo(su.processor_info())

@system.command("PYTHON-VERSION")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def pyversion(help):
    if help:
        click.echo("Get the Python version.")
        click.echo("Usage: pyversion")
        return
    su = SystemUtility()
    click.echo(su.python_version())

@system.command("ENVIRONMENT-VARIABLES")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def envvars(help):
    if help:
        click.echo("Get the environment variables.")
        click.echo("Usage: envvars")
        return
    su = SystemUtility()
    env = su.environment_variables()
    for k, v in env.items():
        click.echo(f"{k}={v}")

@system.command("CURRENT-WORKING-DIRECTORY")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def cwd(help):
    if help:
        click.echo("Get the current working directory.")
        click.echo("Usage: cwd")
        return
    su = SystemUtility()
    click.echo(su.current_working_directory())

# Click CLI group for file operations
@cli.group()
def fileops():
    pass

@fileops.command("LIST-DIRECTORY")
@click.argument("path")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def listdir(path, help):
    if help:
        click.echo("List the contents of a directory.")
        click.echo("Usage: listdir PATH")
        return
    fu = FileUtility()
    items = fu.list_directory(path)
    for item in items:
        click.echo(item)

@fileops.command("FILE-EXISTS")
@click.argument("path")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def fileexists(path, help):
    if help:
        click.echo("Check if a file exists.")
        click.echo("Usage: fileexists PATH")
        return
    fu = FileUtility()
    if fu.file_exists(path):
        click.echo("Yes")
    else:
        click.echo("No")

@fileops.command("DIRECTORY-EXISTS")
@click.argument("path")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def direxists(path, help):
    if help:
        click.echo("Check if a directory exists.")
        click.echo("Usage: direxists PATH")
        return
    fu = FileUtility()
    if fu.directory_exists(path):
        click.echo("Yes")
    else:
        click.echo("No")

@fileops.command("READ-FILE")
@click.argument("path")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def readfile(path, help):
    if help:
        click.echo("Read the contents of a file.")
        click.echo("Usage: readfile PATH")
        return
    fu = FileUtility()
    content = fu.read_file(path)
    if content is not None:
        click.echo(content)
    else:
        click.echo("File not found")

@fileops.command("WRITE-FILE")
@click.argument("path")
@click.argument("content")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def writefile(path, content, help):
    if help:
        click.echo("Write content to a file.")
        click.echo("Usage: writefile PATH CONTENT")
        return
    fu = FileUtility()
    fu.write_file(path, content)
    click.echo("File written")

@fileops.command("APPEND-FILE")
@click.argument("path")
@click.argument("content")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def appendfile(path, content, help):
    if help:
        click.echo("Append content to a file.")
        click.echo("Usage: appendfile PATH CONTENT")
        return
    fu = FileUtility()
    fu.append_file(path, content)
    click.echo("File appended")

@fileops.command("MAKE-DIRECTORY")
@click.argument("path")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def makedir(path, help):
    if help:
        click.echo("Create a directory.")
        click.echo("Usage: makedir PATH")
        return
    fu = FileUtility()
    result = fu.create_directory(path)
    if result:
        click.echo("Directory created")
    else:
        click.echo("Directory already exists or error occurred")

# Click CLI group for collection operations
@cli.group()
def collect():
    pass

@collect.command("DEDUPLICATE-LIST")
@click.argument("items", nargs=-1)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def dedup(items, help):
    if help:
        click.echo("Remove duplicates from a list.")
        click.echo("Usage: dedup ITEM [ITEM ...]")
        return
    cu = CollectionUtility()
    unique = cu.deduplicate_list(list(items))
    for item in unique:
        click.echo(item)

@collect.command("CHUNK-LIST")
@click.argument("size", type=int)
@click.argument("items", nargs=-1)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def chunk(size, items, help):
    if help:
        click.echo("Chunk a list into smaller lists of a given size.")
        click.echo("Usage: chunk SIZE ITEM [ITEM ...]")
        return
    cu = CollectionUtility()
    for chunked in cu.chunk_list(list(items), size):
        click.echo(",".join(chunked))

@collect.command("FLATTEN-LIST")
@click.argument("items", nargs=-1)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def flatten(items, help):
    if help:
        click.echo("Flatten a nested list.")
        click.echo("Usage: flatten ITEM [ITEM ...]")
        return
    cu = CollectionUtility()
    expanded = []
    for elem in items:
        if elem.startswith("[") and elem.endswith("]"):
            try:
                inner = json.loads(elem)
                expanded.append(inner)
            except:
                expanded.append(elem)
        else:
            expanded.append(elem)
    flattened = cu.flatten_nested_list(expanded)
    for f in flattened:
        click.echo(str(f))

@collect.command("COMBINATIONS-OF-LIST")
@click.argument("r", type=int)
@click.argument("items", nargs=-1)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def comb(r, items, help):
    if help:
        click.echo("Generate combinations of a list.")
        click.echo("Usage: comb R ITEM [ITEM ...]")
        return
    cu = CollectionUtility()
    c = cu.combinations_of_list(list(items), r)
    for combo in c:
        click.echo(",".join(combo))

@collect.command("PERMUTATIONS-OF-LIST")
@click.argument("r", type=int)
@click.argument("items", nargs=-1)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def perm(r, items, help):
    if help:
        click.echo("Generate permutations of a list.")
        click.echo("Usage: perm R ITEM [ITEM ...]")
        return
    cu = CollectionUtility()
    p = cu.permutations_of_list(list(items), r)
    for permu in p:
        click.echo(",".join(permu))

@collect.command("ACCUMULATE-LIST-SUM")
@click.argument("items", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def accum(items, help):
    if help:
        click.echo("Accumulate the sum of a list.")
        click.echo("Usage: accum ITEM [ITEM ...]")
        return
    cu = CollectionUtility()
    sums = cu.accumulate_list_sum(items)
    for s in sums:
        click.echo(str(s))

@collect.command("GROUP-LIST-BY-CONDITION")
@click.argument("items", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def groupodd(items, help):
    if help:
        click.echo("Group a list by a condition.")
        click.echo("Usage: groupodd ITEM [ITEM ...]")
        return
    cu = CollectionUtility()
    cond = lambda x: (x % 2) == 1
    t, f = cu.group_list_by_condition(items, cond)
    click.echo("Odd numbers:")
    for val in t:
        click.echo(str(val))
    click.echo("Even numbers:")
    for val in f:
        click.echo(str(val))

# Click CLI group for sorting operations
@cli.group()
def sortops():
    pass

@sortops.command("BUBBLE-SORT")
@click.argument("numbers", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def bubble(numbers, help):
    if help:
        click.echo("Perform bubble sort on a list.")
        click.echo("Usage: bubble NUMBER [NUMBER ...]")
        return
    su = SortingUtility()
    arr = list(numbers)
    result = su.bubble_sort(arr)
    click.echo(",".join(map(str, result)))

@sortops.command("INSERTION-SORT")
@click.argument("numbers", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def insertion(numbers, help):
    if help:
        click.echo("Perform insertion sort on a list.")
        click.echo("Usage: insertion NUMBER [NUMBER ...]")
        return
    su = SortingUtility()
    arr = list(numbers)
    result = su.insertion_sort(arr)
    click.echo(",".join(map(str, result)))

@sortops.command("QUICK-SORT")
@click.argument("numbers", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def quick(numbers, help):
    if help:
        click.echo("Perform quick sort on a list.")
        click.echo("Usage: quick NUMBER [NUMBER ...]")
        return
    su = SortingUtility()
    arr = list(numbers)
    result = su.quick_sort(arr)
    click.echo(",".join(map(str, result)))

@sortops.command("MERGE-SORT")
@click.argument("numbers", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def mergesort(numbers, help):
    if help:
        click.echo("Perform merge sort on a list.")
        click.echo("Usage: mergesort NUMBER [NUMBER ...]")
        return
    su = SortingUtility()
    arr = list(numbers)
    result = su.merge_sort(arr)
    click.echo(",".join(map(str, result)))

@cli.command("RANDOM-TEXT-GENERATOR")
@click.option("--length", "-l", type=int, default=16, help="Length of the random text.")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def randomtext(length, help):
    if help:
        click.echo("Generate a random text of specified length.")
        click.echo("Usage: randomtext [OPTIONS]")
        return
    letters = string.ascii_letters + string.digits
    generated = "".join(random.choice(letters) for _ in range(length))
    click.echo(generated)

@cli.command("CALCULATE-SQUARE-ROOT")
@click.argument("x", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def sqrt(x, help):
    if help:
        click.echo("Calculate the square root of a number.")
        click.echo("Usage: sqrt X")
        return
    if x < 0:
        click.echo("No real square root for negative numbers")
    else:
        val = math.isqrt(x)
        click.echo(str(val))

@cli.command("WAIT-FOR-SECONDS")
@click.argument("seconds", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def wait(seconds, help):
    if help:
        click.echo("Wait for a specified number of seconds.")
        click.echo("Usage: wait SECONDS")
        return
    time.sleep(seconds)
    click.echo("Done waiting")

@cli.command("SYSTEM-INFO")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def sysinfo(help):
    if help:
        click.echo("Show system information.")
        click.echo("Usage: sysinfo")
        return
    info = {}
    info["platform"] = sys.platform
    info["version"] = sys.version
    info["executable"] = sys.executable
    for k, v in info.items():
        click.echo(f"{k}: {v}")

@cli.command("SUM-RANGE")
@click.argument("start", type=int)
@click.argument("end", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def sumrange(start, end, help):
    if help:
        click.echo("Calculate the sum of a range of numbers.")
        click.echo("Usage: sumrange START END")
        return
    total = sum(range(start, end + 1))
    click.echo(str(total))

@cli.command("TEXT-COUNT-TOOL")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def charcount(text, help):
    if help:
        click.echo("Count the number of characters in a text.")
        click.echo("Usage: character count")
        return
    click.echo(str(len(text)))

@cli.command("TO-BINARY-TOOL")
@click.argument("number", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
@click.option("--prefix", is_flag=True, help="Show '0b' prefix in output.")
def binary(number, help, prefix):
    if help:
        click.echo("Convert a decimal number to binary.")
        click.echo("Usage: binary NUMBER [--prefix]")
        return
    result = bin(number)
    if not prefix:
        # Remove '0b' prefix if not requested
        result = result[2:]
    click.echo(result)

@cli.command("TO-HEX-TOOL")
@click.argument("number", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
@click.option("--uppercase", is_flag=True, help="Show hexadecimal letters in uppercase.")
def hexnum(number, help, uppercase):
    if help:
        click.echo("Convert a decimal number to hexadecimal.")
        click.echo("Usage: hexnum NUMBER [--uppercase]")
        return
    result = hex(number)
    if uppercase:
        # Make sure to drop the '0x' prefix, convert to uppercase, and re-add prefix
        result = "0x" + result[2:].upper()
    click.echo(result)

@cli.command("TO-OCTAL-TOOL")
@click.argument("number", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def octnum(number, help):
    if help:
        click.echo("Convert a decimal number to octal.")
        click.echo("Usage: octnum NUMBER")
        return
    click.echo(oct(number))

@cli.command("ENCODE-BASE64")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def encodebase64(text, help):
    if help:
        click.echo("Encode a string to Base64.")
        click.echo("Usage: encodebase64 TEXT")
        return
    encoded = text.encode("utf-8")
    b64 = itertools.accumulate(encoded, lambda a, b: a + b)
    final_bytes = functools.reduce(lambda x, y: x + bytes([y]), b64, b"")
    result = ""
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    index = 0
    while index < len(final_bytes):
        block = final_bytes[index : index + 3]
        bits = 0
        pad = 0
        for i, bt in enumerate(block):
            bits = (bits << 8) + bt
        if len(block) < 3:
            pad = 3 - len(block)
            bits <<= 8 * pad
        output = []
        for i in range(4):
            shift = 18 - 6 * i
            val = (bits >> shift) & 0x3F
            output.append(base64_chars[val])
        for _ in range(pad):
            output[-1 - _] = "="
        result += "".join(output)
        index += 3
    click.echo(result)

@cli.command("FILE-HASH")
@click.argument("filename")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def filehash(filename, help):
    if help:
        click.echo("Calculate the SHA-256 hash of a file.")
        click.echo("Usage: filehash FILENAME")
        return
    if not os.path.isfile(filename):
        click.echo("File not found")
        return
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    click.echo(h.hexdigest())

@cli.command("RANDOM-NUMBER-GENERATOR")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
@click.option("--max-val", type=int, default=1000000, help="Maximum random value.")
def randnum(help, max_val):
    if help:
        click.echo("Generate a random integer within a specified range.")
        click.echo("Usage: randnum [--max-val INT]")
        return
    click.echo(str(random.randint(0, max_val)))

@cli.command("PI-APPROXIMATION")
@click.argument("iterations", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def piapprox(iterations, help):
    if help:
        click.echo("Approximate π using a Monte Carlo method.")
        click.echo("Usage: piapprox ITERATIONS")
        return
    inside = 0
    for _ in range(iterations):
        xval = random.random()
        yval = random.random()
        if xval*xval + yval*yval <= 1:
            inside += 1
    pi_estimate = 4.0 * inside / iterations
    click.echo(str(pi_estimate))

@cli.command("RANDOM-RANGE")
@click.argument("start", type=int)
@click.argument("end", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def randomrange(start, end, help):
    if help:
        click.echo("Generate a random integer between START and END.")
        click.echo("Usage: randomrange START END")
        return
    click.echo(str(random.randint(start, end)))

@cli.command("ROUND-NUMBER")
@click.argument("value", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def roundnum(value, help):
    if help:
        click.echo("Round a floating-point value to the nearest integer.")
        click.echo("Usage: roundnum VALUE")
        return
    click.echo(str(round(value)))

@cli.command("ENCODE-HEX")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def encodehex(text, help):
    if help:
        click.echo("Encode a string into hexadecimal.")
        click.echo("Usage: encodehex TEXT")
        return
    encoded = text.encode("utf-8").hex()
    click.echo(encoded)

@cli.command("DECODE-HEX")
@click.argument("hexstring")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def decodehex(hexstring, help):
    if help:
        click.echo("Decode a hexadecimal string back into text.")
        click.echo("Usage: decodehex HEXSTRING")
        return
    try:
        decoded = bytes.fromhex(hexstring).decode("utf-8")
        click.echo(decoded)
    except:
        click.echo("Invalid hex input")

@cli.command("GENERATE-UUIDS")
@click.argument("count", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def genuuids(count, help):
    if help:
        click.echo("Generate a specified number of UUIDs.")
        click.echo("Usage: genuuids COUNT")
        return
    cu = CryptoUtility()
    for _ in range(count):
        click.echo(cu.generate_uuid())

@cli.command("CALCULATE-AVERAGE")
@click.argument("values", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def average(values, help):
    if help:
        click.echo("Calculate the average of given integer values.")
        click.echo("Usage: average VALUE [VALUE ...]")
        return
    if not values:
        click.echo("No values given")
        return
    avg = sum(values) / len(values)
    click.echo(str(avg))

@cli.command("CALCULATE-POWER")
@click.argument("base", type=float)
@click.argument("exponent", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def power(base, exponent, help):
    if help:
        click.echo("Raise BASE to the power of EXPONENT.")
        click.echo("Usage: power BASE EXPONENT")
        return
    result = base ** exponent
    click.echo(str(result))

@cli.command("COUNTDOWN-TIMER")
@click.argument("seconds", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def countdown(seconds, help):
    if help:
        click.echo("Count down from a specified number of seconds.")
        click.echo("Usage: countdown SECONDS")
        return
    while seconds > 0:
        click.echo(str(seconds))
        time.sleep(1)
        seconds -= 1
    click.echo("Done")

@cli.command("FIBONACCI-LIST")
@click.argument("capacity", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def fiblist(capacity, help):
    if help:
        click.echo("Generate all Fibonacci numbers up to a specified capacity.")
        click.echo("Usage: fiblist CAPACITY")
        return
    mu = MathUtility()
    seq = mu.fibonacci_sequence(capacity)
    click.echo(",".join(map(str, seq)))

@cli.command("CONVERT-BASE")
@click.argument("base", type=int)
@click.argument("number", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def convertbase(base, number, help):
    if help:
        click.echo("Convert a decimal number to a specified base (2 to 36).")
        click.echo("Usage: convertbase BASE NUMBER")
        return
    if base < 2 or base > 36:
        click.echo("Base must be between 2 and 36")
        return
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number == 0:
        click.echo("0")
        return
    negative = number < 0
    if negative:
        number = -number
    result = ""
    while number > 0:
        digit = number % base
        result = digits[digit] + result
        number //= base
    if negative:
        result = "-" + result
    click.echo(result)

@cli.command("MIN-MAX")
@click.argument("items", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def minmax(items, help):
    if help:
        click.echo("Find the minimum and maximum in a series of integers.")
        click.echo("Usage: minmax ITEM [ITEM ...]")
        return
    if not items:
        click.echo("No input")
        return
    minimum = min(items)
    maximum = max(items)
    click.echo(f"Min: {minimum}, Max: {maximum}")

@cli.command("CALCULATE-VARIANCE")
@click.argument("values", nargs=-1, type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def variance(values, help):
    if help:
        click.echo("Calculate the variance of a series of floating-point values.")
        click.echo("Usage: variance VALUE [VALUE ...]")
        return
    vals = list(values)
    n = len(vals)
    if n == 0:
        click.echo("No input")
        return
    mean = sum(vals) / n
    var = sum((x - mean)**2 for x in vals) / n
    click.echo(str(var))

@cli.command("CALCULATE-STDEV")
@click.argument("values", nargs=-1, type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def stdev(values, help):
    if help:
        click.echo("Calculate the standard deviation of a series of floating-point values.")
        click.echo("Usage: stdev VALUE [VALUE ...]")
        return
    vals = list(values)
    n = len(vals)
    if n == 0:
        click.echo("No input")
        return
    mean = sum(vals) / n
    var = sum((x - mean)**2 for x in vals) / n
    sd = math.sqrt(var)
    click.echo(str(sd))

@cli.command("ROT13-ENCODER")
@click.argument("message")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def rot13(message, help):
    if help:
        click.echo("Encode a message using ROT13.")
        click.echo("Usage: rot13 MESSAGE")
        return
    result = []
    for ch in message:
        c = ord(ch)
        if 65 <= c <= 90:
            c = ((c - 65 + 13) % 26) + 65
        elif 97 <= c <= 122:
            c = ((c - 97 + 13) % 26) + 97
        result.append(chr(c))
    click.echo("".join(result))

@cli.command("CALCULATE-MEDIAN")
@click.argument("values", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def median(values, help):
    if help:
        click.echo("Calculate the median of a series of integers.")
        click.echo("Usage: median VALUE [VALUE ...]")
        return
    arr = sorted(values)
    length = len(arr)
    if length == 0:
        click.echo("No input")
        return
    mid = length // 2
    if length % 2 == 0:
        m = (arr[mid - 1] + arr[mid]) / 2
        click.echo(str(m))
    else:
        click.echo(str(arr[mid]))

@cli.command("EVEN-NUMBERS")
@click.argument("start", type=int)
@click.argument("end", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def evens(start, end, help):
    if help:
        click.echo("List even numbers in a given range.")
        click.echo("Usage: evens START END")
        return
    nums = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            nums.append(i)
    click.echo(",".join(map(str, nums)))

@cli.command("ODD-NUMBERS")
@click.argument("start", type=int)
@click.argument("end", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def odds(start, end, help):
    if help:
        click.echo("List odd numbers in a given range.")
        click.echo("Usage: odds START END")
        return
    nums = []
    for i in range(start, end + 1):
        if i % 2 == 1:
            nums.append(i)
    click.echo(",".join(map(str, nums)))

@cli.command("HEX-TO-DECIMAL")
@click.argument("value", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def hex2dec(value, help):
    if help:
        click.echo("Interpret a decimal value as hexadecimal, then convert to decimal.")
        click.echo("Usage: hex2dec VALUE")
        return
    hex_str = hex(value)[2:]
    dec_val = int(hex_str, 16)
    click.echo(str(dec_val))

@cli.command("DECIMAL-TO-HEX")
@click.argument("value", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def dec2hex(value, help):
    if help:
        click.echo("Convert a decimal value to hexadecimal.")
        click.echo("Usage: dec2hex VALUE")
        return
    hex_str = hex(value)
    click.echo(hex_str)

@cli.command("BINARY-TO-DECIMAL")
@click.argument("val", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def bin2dec(val, help):
    if help:
        click.echo("Interpret a decimal value as binary, then convert to decimal.")
        click.echo("Usage: bin2dec VAL")
        return
    bin_str = bin(val)[2:]
    dec_val = int(bin_str, 2)
    click.echo(str(dec_val))

@cli.command("DECIMAL-TO-BINARY")
@click.argument("val", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def dec2bin(val, help):
    if help:
        click.echo("Convert a decimal value to binary.")
        click.echo("Usage: dec2bin VAL")
        return
    bin_str = bin(val)
    click.echo(bin_str)

@cli.command("CURRENT-TIME")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def timenow(help):
    if help:
        click.echo("Show the current time in YYYY-MM-DD HH:MM:SS format.")
        click.echo("Usage: timenow")
        return
    now_val = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    click.echo(now_val)

@cli.command("LINE-COUNT")
@click.argument("filename")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def linescount(filename, help):
    if help:
        click.echo("Count the number of lines in a file.")
        click.echo("Usage: linescount FILENAME")
        return
    if not os.path.isfile(filename):
        click.echo("File not found")
        return
    count = 0
    with open(filename, "r", encoding="utf-8") as f:
        for _ in f:
            count += 1
    click.echo(str(count))

@cli.command("WORD-COUNT")
@click.argument("filename")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def wordcount(filename, help):
    if help:
        click.echo("Count the number of words in a file.")
        click.echo("Usage: wordcount FILENAME")
        return
    if not os.path.isfile(filename):
        click.echo("File not found")
        return
    total_words = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            total_words += len(line.split())
    click.echo(str(total_words))

@cli.command("SIN-VALUE")
@click.argument("x", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def sinval(x, help):
    if help:
        click.echo("Calculate the sine of a value (radians).")
        click.echo("Usage: sinval X")
        return
    click.echo(str(math.sin(x)))

@cli.command("COS-VALUE")
@click.argument("x", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def cosval(x, help):
    if help:
        click.echo("Calculate the cosine of a value (radians).")
        click.echo("Usage: cosval X")
        return
    click.echo(str(math.cos(x)))

@cli.command("TAN-VALUE")
@click.argument("x", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def tanval(x, help):
    if help:
        click.echo("Calculate the tangent of a value (radians).")
        click.echo("Usage: tanval X")
        return
    click.echo(str(math.tan(x)))

@cli.command("ARCSIN-VALUE")
@click.argument("x", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def arcsinval(x, help):
    if help:
        click.echo("Calculate the arcsine of a value, must be between -1 and 1.")
        click.echo("Usage: arcsinval X")
        return
    if x < -1 or x > 1:
        click.echo("Out of domain")
    else:
        click.echo(str(math.asin(x)))

@cli.command("ARCCOS-VALUE")
@click.argument("x", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def arccosval(x, help):
    if help:
        click.echo("Calculate the arccosine of a value, must be between -1 and 1.")
        click.echo("Usage: arccosval X")
        return
    if x < -1 or x > 1:
        click.echo("Out of domain")
    else:
        click.echo(str(math.acos(x)))

@cli.command("ARCTAN-VALUE")
@click.argument("x", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def arctanval(x, help):
    if help:
        click.echo("Calculate the arctangent of a value.")
        click.echo("Usage: arctanval X")
        return
    click.echo(str(math.atan(x)))

@cli.command("LOG2-VALUE")
@click.argument("x", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def log2val(x, help):
    if help:
        click.echo("Calculate the base-2 logarithm of a value.")
        click.echo("Usage: log2val X")
        return
    if x <= 0:
        click.echo("Out of domain")
    else:
        click.echo(str(math.log2(x)))

@cli.command("LOG10-VALUE")
@click.argument("x", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def log10val(x, help):
    if help:
        click.echo("Calculate the base-10 logarithm of a value.")
        click.echo("Usage: log10val X")
        return
    if x <= 0:
        click.echo("Out of domain")
    else:
        click.echo(str(math.log10(x)))

@cli.command("WRITE-LINES")
@click.argument("filename")
@click.argument("content", nargs=-1)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def writelines(filename, content, help):
    if help:
        click.echo("Write multiple lines to a file.")
        click.echo("Usage: writelines FILENAME [LINE ...]")
        return
    with open(filename, "w", encoding="utf-8") as f:
        for line in content:
            f.write(line + "\n")
    click.echo("Lines written")

@cli.command("READ-LINES")
@click.argument("filename")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def readlines(filename, help):
    if help:
        click.echo("Read all lines from a file.")
        click.echo("Usage: readlines FILENAME")
        return
    if not os.path.isfile(filename):
        click.echo("File not found")
        return
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            click.echo(line.strip())

@cli.command("PYTHON-INFO")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def pythoninfo(help):
    if help:
        click.echo("Show basic Python environment information.")
        click.echo("Usage: pythoninfo")
        return
    info = {}
    info["version"] = platform.python_version()
    info["compiler"] = platform.python_compiler()
    info["implementation"] = platform.python_implementation()
    for k, v in info.items():
        click.echo(f"{k}: {v}")

@cli.command("DISTANCE")
@click.argument("x", type=float)
@click.argument("y", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def distance(x, y, help):
    if help:
        click.echo("Calculate the distance from (0,0) to (x,y) in a 2D plane.")
        click.echo("Usage: distance X Y")
        return
    dist = math.hypot(x, y)
    click.echo(str(dist))

@cli.command("FACTOR")
@click.argument("number", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def factor(number, help):
    if help:
        click.echo("List all positive factors of a number.")
        click.echo("Usage: factor NUMBER")
        return
    if number < 1:
        click.echo("Number must be positive")
        return
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    factors.sort()
    for f in factors:
        click.echo(str(f))

@cli.command("SQUARE")
@click.argument("value", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def square(value, help):
    if help:
        click.echo("Calculate the square of a number.")
        click.echo("Usage: square VALUE")
        return
    click.echo(str(value * value))

@cli.command("CUBE")
@click.argument("value", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def cube(value, help):
    if help:
        click.echo("Calculate the cube of a number.")
        click.echo("Usage: cube VALUE")
        return
    click.echo(str(value * value * value))

@cli.command("CHECK-PATH")
@click.argument("path")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def checkpath(path, help):
    if help:
        click.echo("Check if a path exists in the filesystem.")
        click.echo("Usage: checkpath PATH")
        return
    if os.path.exists(path):
        click.echo("Exists")
    else:
        click.echo("Does not exist")

@cli.command("SUM-DIGITS")
@click.argument("num", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def sumdigits(num, help):
    if help:
        click.echo("Sum the digits of an integer (ignores sign).")
        click.echo("Usage: sumdigits NUM")
        return
    s = str(abs(num))
    total = sum(int(ch) for ch in s)
    click.echo(str(total))

@cli.command("INTERLEAVE-LISTS")
@click.argument("list1", nargs=-1, type=int)
@click.argument("list2", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def interleave(list1, list2, help):
    if help:
        click.echo("Interleave two lists of integers into one sequence.")
        click.echo("Usage: interleave-lists [INT ...] [INT ...]")
        return
    result = []
    max_len = max(len(list1), len(list2))
    for i in range(max_len):
        if i < len(list1):
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
    click.echo(",".join(map(str, result)))

@cli.command("COLLATZ-SEQUENCE")
@click.argument("val", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def collatz(val, help):
    if help:
        click.echo("Generate the Collatz sequence for a given integer.")
        click.echo("Usage: collatz-sequence VAL")
        return
    sequence = []
    current = val
    while current != 1 and current > 0:
        sequence.append(current)
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
    sequence.append(1)
    click.echo(",".join(map(str, sequence)))

@cli.command("RANDOM-LIST-GENERATOR")
@click.argument("size", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
@click.option("--max-val", type=int, default=1000, help="Maximum random value in the list.")
def randomlist(size, help, max_val):
    if help:
        click.echo("Generate a list of random integers of a specified size.")
        click.echo("Usage: randomlist SIZE [--max-val INT]")
        return
    arr = [random.randint(0, max_val) for _ in range(size)]
    click.echo(",".join(map(str, arr)))

@cli.command("SEARCH-FILE")
@click.argument("filename")
@click.argument("text")
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def searchfile(filename, text, help):
    if help:
        click.echo("Search for TEXT within a file's lines.")
        click.echo("Usage: searchfile FILENAME TEXT")
        return
    if not os.path.isfile(filename):
        click.echo("File not found")
        return
    line_num = 1
    found = False
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if text in line:
                click.echo(f"Line {line_num}: {line.strip()}")
                found = True
            line_num += 1
    if not found:
        click.echo("No match")

@cli.command("SET-RANDOM-SEED")
@click.argument("value", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def randomseed(value, help):
    if help:
        click.echo("Set the seed for Python's random module.")
        click.echo("Usage: set-random-seed VALUE")
        return
    random.seed(value)
    click.echo("Random seed set")

@cli.command("FLOOR-VALUE")
@click.argument("val", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def floorval(val, help):
    if help:
        click.echo("Apply the floor function to a floating-point value.")
        click.echo("Usage: floorval VAL")
        return
    click.echo(str(math.floor(val)))

@cli.command("CEIL-VALUE")
@click.argument("val", type=float)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def ceilval(val, help):
    if help:
        click.echo("Apply the ceiling function to a floating-point value.")
        click.echo("Usage: ceilval VAL")
        return
    click.echo(str(math.ceil(val)))

@cli.command("IDENTITY-MATRIX")
@click.argument("size", type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def matrixid(size, help):
    if help:
        click.echo("Generate a size×size identity matrix.")
        click.echo("Usage: matrixid SIZE")
        return
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append("1")
            else:
                row.append("0")
        click.echo(" ".join(row))

@cli.command("PARTIAL-SUM")
@click.argument("values", nargs=-1, type=int)
@click.option("--help", "-h", is_flag=True, help="Show this help message and exit.")
def partialsum(values, help):
    if help:
        click.echo("Compute a running total (partial sums) of given integers.")
        click.echo("Usage: partialsum VALUE [VALUE ...]")
        return
    total = 0
    for val in values:
        total += val
        click.echo(str(total))

def main():
    cli()

if __name__ == "__main__":
    main()