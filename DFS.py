from BinaryTree import BinaryTree

a_node=BinaryTree(1)
a_node.insert_left(2)
a_node.insert_right(5)

two_node=a_node.left_child
two_node.insert_left(3)
two_node.insert_right(4)

five_node=a_node.right_child
five_node.insert_left(6)
five_node.insert_right(7)

three_node=two_node.left_child
three_node.insert_left(20)

a_node.pre_order()
print("In Order ******")
a_node.in_order()

print("Post Order ******")
a_node.post_order()


# print(a_node.value)
# print(two_node.value)
# print(a_node.right_child.value)
# print(two_node.left_child.value)
# print(two_node.right_child.value)
# print(five_node.left_child.value)
# print(five_node.right_child.value)
