import attr
import pythonping

from npdk.protocol import icmp


class HostTestCase(icmp.TestCase):

    def tearDown(self):
        print('+', attr.asdict(self.record))


if __name__ == "__main__":
    HostTestCase()
