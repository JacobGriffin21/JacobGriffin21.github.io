//============================================================================
// Name        : BinarySearchTree.cpp
// Author      : Jacob Griffin
// Version     : 1.0
// Copyright   : Copyright � 2017 SNHU COCE
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <time.h>

#include "CSVparser.hpp"

using namespace std;

//============================================================================
// Global definitions visible to all methods and classes
//============================================================================

// forward declarations
double strToDouble(string str, char ch);

// define a structure to hold bid information
struct Bid {
    string bidId; // unique identifier
    string title;
    string fund;
    double amount;
    Bid() {
        amount = 0.0;
    }
};

// Internal structure for tree node
struct Node {
    Bid bid;
    Node* left;
    Node* right;

    // default constructor
    Node() {
        left = nullptr;
        right = nullptr;
    }

    // initialize with a bid
    Node(Bid aBid) :
        Node() {
        bid = aBid;
    }
};

//============================================================================
// Binary Search Tree class definition
//============================================================================

/**
 * Define a class containing data members and methods to
 * implement a binary search tree
 */
class BinarySearchTree {

private:
    Node* root;

    void addNode(Node* node, Bid bid);
    void inOrder(Node* node);
    void preOrder(Node* node);
    void postOrder(Node* node);
    Node* removeNode(Node* node, string bidId);

public:
    BinarySearchTree();
    virtual ~BinarySearchTree();
    void InOrder();
    void PostOrder();
    void PreOrder();
    void Insert(Bid bid);
    void Remove(string bidId);
    Bid Search(string bidId);
};

/**
 * Default constructor
 */
BinarySearchTree::BinarySearchTree() {
    // FixMe (1): initialize housekeeping variables
    //root is equal to nullptr
    root = nullptr;

}

/**
 * Destructor
 */
BinarySearchTree::~BinarySearchTree() {
    // recurse from root deleting every node
}

/**
 * Traverse the tree in order
 */
void BinarySearchTree::InOrder() {
    // FixMe (2): In order root
    // call inOrder fuction and pass root
    inOrder(root);
}

/**
 * Traverse the tree in post-order
 */
void BinarySearchTree::PostOrder() {
    // FixMe (3): Post order root
    // postOrder root
    postOrder(root);
}

/**
 * Traverse the tree in pre-order
 */
void BinarySearchTree::PreOrder() {
    // FixMe (4): Pre order root
    // preOrder root
    preOrder(root);
}

/**
 * Insert a bid
 */
void BinarySearchTree::Insert(Bid bid) {
    // FIXME (5) Implement inserting a bid into the tree

    // if root equarl to null ptr
    if (root == nullptr) {
        root = new Node(bid); // root is equal to new node bid
    }
    // else
    else {
        this->addNode(root, bid); // add Node root and bid
    }
}

/**
 * Remove a bid
 */
void BinarySearchTree::Remove(string bidId) {
    // FIXME (6) Implement removing a bid from the tree
    // remove node root bidID
    this->removeNode(root, bidId);
}

/**
 * Search for a bid
 */
Bid BinarySearchTree::Search(string bidId) {
    // FIXME (7) Implement searching the tree for a bid
    // set current node equal to root
    Node* cur = root;
    while (cur != nullptr) {
        if (cur->bid.bidId.compare(bidId) == 0) {
            return cur->bid; // if match found, return current bid
        }
        else if (bidId.compare(cur->bid.bidId) < 0) { // if bid is smaller than current node then traverse left
            cur = cur->left;
        }
        else {
            cur = cur->right; // else larger so traverse right
        }
    }
    Bid bid;
    return bid; 
}

/**
 * Add a bid to some node (recursive)
 *
 * @param node Current node in tree
 * @param bid Bid to be added
 */
void BinarySearchTree::addNode(Node* node, Bid bid) {
    // FIXME (8) Implement inserting a bid into the tree
    // if node is larger then add to left         
    if (node != nullptr && node->bid.bidId.compare(bid.bidId) > 0) {
        if (node->left == nullptr) {  // if no left node
            node->left = new Node(bid);  // this node becomes left
            return;
        }
        // else
        else {
            this->addNode(node->left, bid); // else recurse down the left node
        }
    }
    else if (node != nullptr && node->bid.bidId.compare(bid.bidId) < 0) {
        if (node->right == nullptr) // if no right node
        {
            node->right == new Node(bid); // this node becomes right
            return;
        }
        //else
        else {
            this->addNode(node->right, bid);  // recurse down the right node
        }
    }
}
void BinarySearchTree::inOrder(Node* node) {
    // FixMe (9): Pre order root
    //if node is not equal to null ptr
    if (node != nullptr) {
        inOrder(node->left); //InOrder not left
        cout << node->bid.bidId << " : " << node->bid.title << " | " << node->bid.amount << " | " << node->bid.fund << endl; //output bidID, title, amount, fund
        inOrder(node->right); //InOder right
            
    }

}
void BinarySearchTree::postOrder(Node* node) {
    // FixMe (10): Pre order root
    //if node is not equal to null ptr
    if (node != nullptr) {
        postOrder(node->left); //postOrder not left
        postOrder(node->right); //postOder right
        cout << node->bid.bidId << " : " << node->bid.title << " | " << node->bid.amount << " | " << node->bid.fund << endl; //output bidID, title, amount, fund
    }

}


void BinarySearchTree::preOrder(Node* node) {
    // FixMe (11): Pre order root
    //if node is not equal to null ptr 
    if (node != nullptr) {
        cout << node->bid.bidId << " : " << node->bid.title << " | " << node->bid.amount << " | " << node->bid.fund << endl; //output bidID, title, amount, fund
        preOrder(node->right); //preOrder right
        preOrder(node->right); //preOrder right
    }

}



Node* BinarySearchTree::removeNode(Node* node, string bidId) {
    //if the node is empty
    if (node == nullptr) {
        return node; //return the node
    }
    //if the bid is smaller
    else if (bidId.compare(node->bid.bidId) < 0) {
        node->left = removeNode(node->left, bidId); //proceed left in the bst
    }
    //if the bid is larger
    else if (bidId.compare(node->bid.bidId) > 0) { 
        node->right = removeNode(node->right, bidId); //proceeed right in the bst
    }
    //else
    else {
        if (node->left == nullptr && node->right == nullptr) { //if the node has no children
            delete node; 
            node = nullptr;
        }
        else if (node->left != nullptr && node->right == nullptr) { //if the node only has a left child
            Node* tmp = node; //store a temp node
            node = node->left; //move the left child up
            delete tmp; //delete temp node
            tmp = nullptr;
        }
        else if (node->right != nullptr && node->left == nullptr) { //if the node only has a right child
            Node* tmp = node; //store temp node
            node = node->right; //move the right child up
            delete tmp; //delete temp node
            tmp = nullptr;
        }
        else { //node has both a left and right child
            Node* tmp = node->right; //temp store right child
            Node* parent = nullptr; //parent node

            while (tmp->left != nullptr) { //left most node in right bst
                parent = tmp;
                tmp = tmp->left;
            }

            node->bid = tmp->bid; //copy leftmost node

            //remove leftmost node
            if (parent != nullptr) {
                parent->left = removeNode(parent->left, tmp->bid.bidId);
            }
            else {
                node->right = removeNode(node->right, tmp->bid.bidId);
            }
        }
    }
    return node;
}


//============================================================================
// Static methods used for testing
//============================================================================

/**
 * Display the bid information to the console (std::out)
 *
 * @param bid struct containing the bid info
 */
void displayBid(Bid bid) {
    cout << bid.bidId << ": " << bid.title << " | " << bid.amount << " | "
        << bid.fund << endl;
    return;
}

/**
 * Load a CSV file containing bids into a container
 *
 * @param csvPath the path to the CSV file to load
 * @return a container holding all the bids read
 */
void loadBids(string csvPath, BinarySearchTree* bst) {
    cout << "Loading CSV file " << csvPath << endl;

    // initialize the CSV Parser using the given path
    csv::Parser file = csv::Parser(csvPath);

    // read and display header row - optional
    vector<string> header = file.getHeader();
    for (auto const& c : header) {
        cout << c << " | ";
    }
    cout << "" << endl;

    try {
        // loop to read rows of a CSV file
        for (unsigned int i = 0; i < file.rowCount(); i++) {

            // Create a data structure and add to the collection of bids
            Bid bid;
            bid.bidId = file[i][1];
            bid.title = file[i][0];
            bid.fund = file[i][8];
            bid.amount = strToDouble(file[i][4], '$');

            //cout << "Item: " << bid.title << ", Fund: " << bid.fund << ", Amount: " << bid.amount << endl;

            // push this bid to the end
            bst->Insert(bid);
        }
    }
    catch (csv::Error& e) {
        std::cerr << e.what() << std::endl;
    }
}

/**
 * Simple C function to convert a string to a double
 * after stripping out unwanted char
 *
 * credit: http://stackoverflow.com/a/24875936
 *
 * @param ch The character to strip out
 */
double strToDouble(string str, char ch) {
    str.erase(remove(str.begin(), str.end(), ch), str.end());
    return atof(str.c_str());
}

/**
 * The one and only main() method
 */
int main(int argc, char* argv[]) {

    // process command line arguments
    string csvPath, bidKey;
    switch (argc) {
    case 2:
        csvPath = argv[1];
        bidKey = "97988";
        break;
    case 3:
        csvPath = argv[1];
        bidKey = argv[2];
        break;
    default:
        csvPath = "eBid_Monthly_Sales_Dec_2016.csv";
        bidKey = "97988";
    }

    // Define a timer variable
    clock_t ticks;

    // Define a binary search tree to hold all bids
    BinarySearchTree* bst;
    bst = new BinarySearchTree();
    Bid bid;

    int choice = 0;
    while (choice != 9) {
        cout << "Menu:" << endl;
        cout << "  1. Load Bids" << endl;
        cout << "  2. Display All Bids" << endl;
        cout << "  3. Find Bid" << endl;
        cout << "  4. Remove Bid" << endl;
        cout << "  9. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {

        case 1:

            // Initialize a timer variable before loading bids
            ticks = clock();

            // Complete the method call to load the bids
            loadBids(csvPath, bst);

            //cout << bst->Size() << " bids read" << endl;

            // Calculate elapsed time and display result
            ticks = clock() - ticks; // current clock ticks minus starting clock ticks
            cout << "time: " << ticks << " clock ticks" << endl;
            cout << "time: " << ticks * 1.0 / CLOCKS_PER_SEC << " seconds" << endl;
            break;

        case 2:
            bst->InOrder();
            break;

        case 3:
            ticks = clock();

            bid = bst->Search(bidKey);

            ticks = clock() - ticks; // current clock ticks minus starting clock ticks

            if (!bid.bidId.empty()) {
                displayBid(bid);
            }
            else {
                cout << "Bid Id " << bidKey << " not found." << endl;
            }

            cout << "time: " << ticks << " clock ticks" << endl;
            cout << "time: " << ticks * 1.0 / CLOCKS_PER_SEC << " seconds" << endl;

            break;

        case 4:
            bst->Remove(bidKey);
            break;
        }
    }

    cout << "Good bye." << endl;

    return 0;
}
