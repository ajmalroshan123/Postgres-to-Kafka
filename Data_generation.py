import random
from faker import Faker

# Initialize Faker for generating realistic product names
fake = Faker()

# Generate mock data
num_records = 5  # You can adjust this as needed
products = []

for i in range(1, num_records + 1):
    product = {
        'id': i,
        'name': fake.word(ext_word_list=['Laptop', 'Smartphone', 'T-shirt', 'Watch', 'Headphones']),
        'category': fake.word(ext_word_list=['Electronics', 'Gadgets', 'Apparel', 'Accessories', 'Health & Wellness']),
        'price': round(random.uniform(5.0, 100.0), 2),
        'last_updated': fake.date_time_this_year(before_now=True, after_now=False),
    }
    products.append(product)

# Print the mock data
for product in products:
    print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Price: ${product['price']:.2f}, Last Updated: {product['last_updated']}")
