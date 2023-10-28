from application.abstract.application import Context
class Pr(Context):
    def __init__(self, name: str, realm: str, etls: [str], sensors: [str] ):
        super().__init__(name, realm, etls, sensors)
        pass



if __name__ == '__main__':
    print(Pr('x','re',[], []).name)