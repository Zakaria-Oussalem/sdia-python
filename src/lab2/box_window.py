from lab2.utils import get_random_number_generator, np


class BoxWindow:
    """[summary]"""

    def __init__(self, bounds=np.array([[0, 1], [0, 1], [0, 1]])):
        """[summary]

        Args:
            args ([type]): [description]
        """

        self.bounds = bounds

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """
        return ""

    def __len__(self):
        return

    def __contains__(self, point):
        assert len(point) == self.dimension()
        for i in range(self.dimension()):
            if not (self.bounds[i, 0] <= point[i] <= self.bounds[i, 1]):
                return False
        return True

    def dimension(self):
        """[summary]"""
        return len(self.bounds)

    def volume(self):
        """[summary]"""
        V = 1
        for [a, b] in self.bounds:
            V *= b - a
        return V

    def indicator_function(self, point):
        """[summary]

        Args:
            args ([type]): [description]
        """
        return point in self

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        pointArray = np.array(
            [[rng.random() * (b - a) + a for [a, b] in self.bounds] for i in range(n)]
        )
        return pointArray


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(center)
