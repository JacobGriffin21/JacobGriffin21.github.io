import csv

# Bid class created with arguements for the 'bid_id', 'title', 'fund' and 'amount'
# Assigning values to the  class level variables based on the arguments passed through the parameters
class Bid:
    def __init__(self, bid_id='', title='', fund='', amount=0.0):
        self.bid_id = bid_id
        self.title = title
        self.fund = fund
        self.amount = amount

# Node class created
# This is also where I set a boolean to flag the 'lazy deletion' method
# The flag will indicate whether the node has been flagged as 'deleted' but not actually removed so that the tree maintains structure
class Node:
    def __init__(self, bid=None):
        self.bid = bid if bid else Bid()
        self.left = None
        self.right = None
        self.is_deleted = False

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Fucntion for inserting a bid into the system
    def insert(self, bid):
        if self.root is None:
            self.root = Node(bid)
        else:
            self._add_node(self.root, bid)
            
    # Function for adding a node since we are using a BST
    def _add_node(self, node, bid):
        if bid.bid_id < node.bid.bid_id:
            if node.left is None:
                node.left = Node(bid)
            else:
                self._add_node(node.left, bid)
        else:
            if node.right is None:
                node.right = Node(bid)
            else:
                self._add_node(node.right, bid)

    # Function for searching for bid
    # The Function will make sure my new lazy deletion method is has not flagged the 'bid_id' as deleted
    def search(self, bid_id):
        node = self._search_node(self.root, bid_id)
        if node and not node.is_deleted:  
            return node.bid 
        return Bid()  


    # Fucntion for searching through the node to find the 'bid_id' that we are specifically searching for
    def _search_node(self, node, bid_id):
        if node is None:
            return None
        if node.bid.bid_id == bid_id:
            return node 
        if bid_id < node.bid.bid_id:
            return self._search_node(node.left, bid_id)
        return self._search_node(node.right, bid_id)


    # This is where the node is actually marked as deleted and will flip the boolean value to 'True" 
    def remove(self, bid_id):
        node = self._search_node(self.root, bid_id)
        if node:  # Checking if the node actually exist
            node.is_deleted = True  # Mark the node as deleted and flip the boolean to 'True'
            print(f"Bid {bid_id} has been marked as deleted.") # Print statements for myself so I know the function ran correctly
        else:
            print(f"Bid {bid_id} not found.") # When the user tries to find the bid_id again it should not be able to be found and print the statement


    # Function for traversing the tree from the root node
    def in_order(self):
        self._in_order(self.root)

    # Function to travers the tree 
    def _in_order(self, node):
        if node is not None:
            self._in_order(node.left) # Traverse from the left
            if not node.is_deleted:
                print(f"{node.bid.bid_id}: {node.bid.title} | {node.bid.amount} | {node.bid.fund}")
            self._in_order(node.right) # Traverse from the right

    
    # Function to load bids from the 'CSV' file
    def load_bids(self, csv_path):
        print(f"Loading CSV file {csv_path}")
        with open(csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            print(" | ".join(headers))
            for row in reader:
                bid = Bid(
                    bid_id=row[1],
                    title=row[0],
                    fund=row[8],
                    amount=float(row[4].replace('$', '').replace(',', ''))
                )
                self.insert(bid)

# The csv path is hardcoded into the code so that program knows where to pull the data  from
# 'Bid_Key' is hardcoded as a dummy 'bidId' so that I can ensure the fucntions are operating correctly
# Creating an instance of the 'BinarySearcTree' class
if __name__ == "__main__":
    csv_path = "eBid_Monthly_Sales_Dec_2016.csv"
    bid_key = "97988"
    bst = BinarySearchTree()

# While loop to dislplay the 'Menu' options
# Taking in the user input so they can select an option
    while True:
        print("Menu:")
        print("  1. Load Bids")
        print("  2. Display All Bids")
        print("  3. Find Bid")
        print("  4. Remove Bid")
        print("  9. Exit")
        choice = input("Enter choice: ")

        # Operations to perform based off of what the user selects in the 'Menu' options
        # Break statement if the user chooses choice 9 and wants to exit the program
        if choice == "1":
            bst.load_bids(csv_path)
        elif choice == "2":
            bst.in_order()
        elif choice == "3":
            bid = bst.search(bid_key)
            if bid.bid_id:
                print(f"{bid.bid_id}: {bid.title} | {bid.amount} | {bid.fund}")
            else:
                print(f"Bid Id {bid_key} not found.")
        elif choice == "4":
            bst.remove(bid_key)
        elif choice == "9":
            print("Goodbye.")
            break
