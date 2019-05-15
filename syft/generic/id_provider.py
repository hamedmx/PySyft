import random


def create_random_id():
    return int(10e10 * random.random())


class IdProvider:
    """Provides Id to all syft objects.

    Generate id and store the list of ids generated
    Can take a pre set list in input and will complete
    when it's empty.

    An instance of IdProvider is accessbile via sy.ID_PROVIDER.
    """

    def __init__(self, given_ids=list()):
        self.given_ids = given_ids
        self.generated = (
            []
        )  # TODO: use sorted container to quickly check whether a value is contained

    def pop(self, *args) -> int:
        """Provides random ids and store them.

        The syntax .pop() mimics the list syntax for convenience
        and not the generator syntax.

        Returns:
            Random Id.
        """
        if len(self.given_ids):
            random_id = self.given_ids.pop(-1)
        else:
            random_id = create_random_id()
            while random_id in self.generated:
                random_id = create_random_id()
        self.generated.append(random_id)
        return random_id
