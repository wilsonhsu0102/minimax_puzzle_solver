"""
Taken From Class
Tree class and functions
"""


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    === Attributes ===
    @param object value: value of root node
    @param list[Tree|None] children: child nodes
    """
    def __init__(self, value=None, children=None):
        """
        Create Tree self with content value and 0 or more children
        @param Tree self: this tree
        @param object value: value contained in this tree
        @param list[Tree|None] children: possibly-empty list of children
        @rtype: None
        """
        self.value = value
        # copy children if not None
        # NEVER have a mutable default parameter...
        self.children = children[:] if children is not None else []

    def __repr__(self):
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        @param Tree self: this tree
        @rtype: str

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return ('{}({}, {})'.format(self.__class__.__name__, repr(self.value),
                                    repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))


if __name__ == '__main__':
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
