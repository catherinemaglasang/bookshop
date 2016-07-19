import csv
from oscar.apps.partner.models import *
from oscar.apps.catalogue.models import *
from decimal import *

def import_data(csv_file='deploy/data/books/imported_books_data.csv'):
    """
    {
        'name': title
        'author':  
        'published': 
        'isbn': 
        'image': 
        'price':
        'status':
        'description': 
        'category_name': 
        'category1':
        'category2': 
        'category3': 
    }
    """

    """ Run command in a fresh db installation """
    """ Create root for all categories """
    root = Category.add_root(name='All')
    """ Create initial partner """ 
    primary_partner = Partner(name='Store')
    primary_partner.save()
    """ Create initial product class """ 
    product_class = ProductClass(name='Book')
    product_class.save()
    """ Create product attributes for our primary product class: book """
    author_attribute = ProductAttribute(product_class=product_class, name='Author', code='author')
    author_attribute.save() 
    publisher_attribute = ProductAttribute(product_class=product_class, name='Published', code='published')
    publisher_attribute.save()
    isbn_attribute = ProductAttribute(product_class=product_class, name='ISBN', code='isbn')
    isbn_attribute.save()

    try:
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                title = unicode(row[0],'utf-8')
                author = unicode(row[1],'utf-8')
                publisher = unicode(row[2],'utf-8')
                isbn = unicode(row[3],'utf-8')
                image = row[4]
                price = row[5]
                stocks = row[6]
                description = unicode(row[7], 'utf-8')
                category_col = [row[8], row[9], row[10], row[11]]

                print "Adding product %s..." % (title)

                """ Create product and add attribute for product""" 
                if not Product.objects.filter(title=title).exists():
                    product = Product(title=title, description=description, product_class=product_class)
                    product.attr.author = author
                    product.attr.publisher = publisher
                    product.attr.isbn = isbn
                    product.save()

                    """ Add images """
                    product_image = ProductImage(product=product, original='images/products/2016/02/' + image)
                    product_image.save()

                    """ Add stock records """
                    if price == '': 
                        price = 0.0
                    if stocks == '': 
                        stocks = 0
                    stock = StockRecord(product=product, partner=primary_partner, partner_sku= product.id, price_currency='DKK', price_excl_tax=price, price_retail=price, cost_price=price, num_in_stock=stocks)
                    stock.save()

                    """ Create and Assign Category To Product """
                    for category in category_col:
                        try: 
                            if category or not category == '':
                                if not Category.objects.filter(name=category).exists():
                                    cat = root.add_sibling(name=category)
                                cat = Category.objects.filter(name=category)[0]
                                product_category = ProductCategory(product=product, category=cat)
                                product_category.save()
                        except: 
                            pass

        root = Category.objects.filter(name='All')[0]
        root.delete()
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))    


# Run the ff in shell:
# from utils import import_data
# import_data()
