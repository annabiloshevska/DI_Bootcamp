# Define a class called Pagination to represent paginated content.
# It should optionally accept a list of items and a page size when initialized.
# Accept two optional parameters:
# items (default None): a list of items
# page_size (default 10): number of items per page
# Behavior:
# If items is None, initialize it as an empty list.
# Save page_size and set current_idx (current page index) to 0.
# Calculate total number of pages using math.ceil.
import math

class Pagination:
    def __init__(self,items = None, page_size = 10):
        if items == None:
            self.items = []
        else:
            self.items = items
        self.page_size = page_size #amount of items on a page
        self.current_idx = 0 #page number
        self.total_pages = math.ceil(len(self.items)/self.page_size) #all items in the list devived to pages according to amount of items per page
# This method returns the list of items visible on the current page.
# Use slicing based on the current_idx and page_size.
    def get_visible_items(self): 
        start = self.current_idx * self.page_size
        end = start + self.page_size
        visible_items = self.items[start:end] 
        return visible_items
# These methods should help navigate through pages:
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError ('Page number out of range')
        self.current_idx = page_num - 1
        return self
# → Goes to the specified page number (1-based indexing).
# → If page_num is out of range, raise a ValueError.
    def first_page(self):
        self.current_idx = 0
        return self
# → Navigates to the first page.
    def last_page(self):
        self.current_idx = self.total_pages -1 
        return self
# → Navigates to the last page.
    def next_page(self):
        if self.current_idx < self.total_pages -1:
            self.current_idx += 1
        return self
# → Moves one page forward (if not already on the last page).
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
# → Moves one page backward (if not already on the first page).

# Pages are indexed internally from 0, but user input is expected to start at 1.
# All navigation methods (except go_to_page) should return self to allow method chaining.
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(str(p))
# Output:
# a
# b
# c
# d
# Use the following test cases:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_idx + 1)
# Output: ValueError

p.go_to_page(0)
# Raises ValueError
