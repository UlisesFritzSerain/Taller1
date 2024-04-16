class Node:
    def __init__(self):
        self.is_leaf = False
        self.ptr = [None] * (bucket_size + 1)  # Pointers to child nodes
        self.key = [None] * bucket_size  # Keys stored in the node
        self.size = 0  # Number of keys currently in the node


class BTree:
    def __init__(self):
        self.root = None  # Root node of the B-tree

    def get_root(self):
        return self.root  # Getter for the root node

    def insert(self, x):
        if self.root is None:
            # B-tree is empty, create a new root
            self.root = Node()
            self.root.key[0] = x
            self.root.is_leaf = True
            self.root.size = 1
        else:
            current = self.root
            parent = None

            # Traverse the tree to find the appropriate leaf node for insertion
            while not current.is_leaf:
                parent = current

                for i in range(current.size):
                    if current.key[i] is None or x < current.key[i]:
                        current = current.ptr[i]
                        break

                    if i == current.size - 1:
                        current = current.ptr[i + 1]
                        break

            if current.size < bucket_size:
                # Insert into a non-full leaf node
                i = 0

                while i < current.size and (current.key[i] is not None and x > current.key[i]):
                    i += 1

                # Shift keys and pointers to make space for the new key
                for j in range(current.size, i, -1):
                    current.key[j] = current.key[j - 1]

                current.key[i] = x
                current.size += 1

                current.ptr[current.size] = current.ptr[current.size - 1]
                current.ptr[current.size - 1] = None
            else:
                # Split the leaf node if it is full
                new_leaf = Node()
                temp_node = [None] * (bucket_size + 1)

                # Copy keys to temporary array
                for i in range(bucket_size):
                    temp_node[i] = current.key[i]

                i = 0

                while i < bucket_size and (temp_node[i] is not None and x > temp_node[i]):
                    i += 1

                # Shift keys in the temporary array to make space for the new key
                for j in range(bucket_size, i, -1):
                    temp_node[j] = temp_node[j - 1]

                temp_node[i] = x

                # Update sizes of the current and new_leaf nodes
                new_leaf.is_leaf = True
                current.size = (bucket_size + 1) // 2
                new_leaf.size = bucket_size + 1 - (bucket_size + 1) // 2

                # Update pointers
                current.ptr[current.size] = new_leaf
                new_leaf.ptr[new_leaf.size] = current.ptr[bucket_size]
                current.ptr[new_leaf.size] = current.ptr[bucket_size]
                current.ptr[bucket_size] = None

                # Copy keys from the temporary array to the current and new_leaf nodes
                for i in range(current.size):
                    current.key[i] = temp_node[i]

                for i in range(current.size, bucket_size):
                    new_leaf.key[i - current.size] = temp_node[i]

                if current == self.root:
                    # Update the root if splitting the root
                    new_root = Node()
                    new_root.key[0] = new_leaf.key[0]
                    new_root.ptr[0] = current
                    new_root.ptr[1] = new_leaf
                    new_root.is_leaf = False
                    new_root.size = 1
                    self.root = new_root
                else:
                    # Propagate the split upwards
                    self.shift_level(new_leaf.key[0], parent, new_leaf)

    def shift_level(self, x, current, child):
        # Helper method to handle splitting of non-leaf nodes
        if current.size < bucket_size:
            i = 0
            while i < current.size and (current.key[i] is not None and x > current.key[i]):
                i += 1

            # Shift keys and pointers to make space for the new key and child
            for j in range(current.size, i, -1):
                current.key[j] = current.key[j - 1]

            for j in range(current.size + 1, i + 1, -1):
                current.ptr[j] = current.ptr[j - 1]

            current.key[i] = x
            current.size += 1
            current.ptr[i + 1] = child
        else:
            # Split the non-leaf node if it is full
            new_internal = Node()
            temp_key = [None] * (bucket_size + 1)
            temp_ptr = [None] * (bucket_size + 2)

            # Copy keys and pointers to temporary arrays
            for i in range(bucket_size):
                temp_key[i] = current.key[i]

            for i in range(bucket_size + 1):
                temp_ptr[i] = current.ptr[i]

            i = 0

            while i < bucket_size and (temp_key[i] is not None and x > temp_key[i]):
                i += 1

            # Shift keys in the temporary array to make space for the new key
            for j in range(bucket_size, i, -1):
                temp_key[j] = temp_key[j - 1]

            temp_key[i] = x

            # Shift pointers in the temporary array to make space for the new child
            for j in range(bucket_size + 1, i + 1, -1):
                temp_ptr[j] = temp_ptr[j - 1]

            temp_ptr[i + 1] = child
            new_internal.is_leaf = False
            current.size = (bucket_size + 1) // 2
            new_internal.size = bucket_size - (bucket_size + 1) // 2

            # Copy keys and pointers from the temporary arrays to the current and new_internal nodes
            for i in range(current.size + 1, bucket_size + 1):
                new_internal.key[i - current.size - 1] = temp_key[i]

            for i in range(current.size + 1, bucket_size + 2):
                new_internal.ptr[i - current.size - 1] = temp_ptr[i]

            if current == self.root:
                # Update the root if splitting the root
                new_root = Node()
                new_root.key[0] = current.key[current.size]
                new_root.ptr[0] = current
                new_root.ptr[1] = new_internal
                new_root.is_leaf = False
                new_root.size = 1
                self.root = new_root
            else:
                # Propagate the split upwards
                self.shift_level(current.key[current.size], self.find_parent(self.root, current), new_internal)

    def search(self, x):
        # Search for a key in the B-tree
        if self.root is None:
            return -1  # B-tree is empty
        else:
            current = self.root
            while not current.is_leaf:
                for i in range(current.size):
                    if x < current.key[i]:
                        current = current.ptr[i]
                        break

                    if i == current.size - 1:
                        current = current.ptr[i + 1]
                        break

            for i in range(current.size):
                if current.key[i] == x:
                    return 1  # Key found

            return 0  # Key not found

    def display(self, current):
        # Display the B-tree
        if current is None:
            return

        q = [current]

        while q:
            l = len(q)

            for _ in range(l):
                t_node = q.pop(0)

                for j in range(t_node.size):
                    if t_node.key[j] is not None:
                        print(t_node.key[j], end=' ')

                for j in range(t_node.size + 1):
                    if t_node.ptr[j]:
                        q.append(t_node.ptr[j])

                print('\t', end='')

            print('\n')

    def find_parent(self, current, child):
        # Helper method to find the parent of a given node
        parent = None

        if current.is_leaf or current.ptr[0].is_leaf:
            return None  # No parent for leaf nodes

        for i in range(current.size + 1):
            if current.ptr[i] == child:
                parent = current
                return parent
            else:
                parent = self.find_parent(current.ptr[i], child)
                if parent:
                    return parent

        return parent


bucket_size = 3  # Set the bucket size for the B-tree

btree = BTree()  # Create a new B-tree

print('The size of bucket is', bucket_size, '!')

# Insert elements into the B-tree
btree.insert(1)
btree.insert(2)
btree.insert(3)
btree.display(btree.get_root())

btree.insert(4)
btree.insert(5)
btree.display(btree.get_root())
