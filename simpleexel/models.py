import re
import helpers


class SimpleExcel:
    _cells = {}
    tools = {}
    _deps = {}

    def __init__(self):
        pass

    def __setitem__(self, key, formula):
        self._cells[key] = helpers.convert_reverse_polish_to_infix(formula)
        # self.__check_deps__()

    def __check_deps__(self):
        pattern = '[A-Z]+\d'

        for key in self._cells.keys():
            if key not in self._deps:
                self._deps[key] = set()
            f = self.__getformula__(key)
            find_cells = re.findall(pattern=pattern, string=str(f))
            self._deps[key].update(find_cells)
            for c in find_cells:
                if c in self._deps:
                    if key in self._deps[c]:
                        raise ValueError("Circular dependency between {0} and {1} detected".format(c, key))

    def __getformula__(self, key):
        return self._cells[key]

    def __getitem__(self, key):
        return eval(self._cells[key], SimpleExcel.tools, self)

    def __repr__(self):
        output = ''
        for key in self._cells.keys():
            output += str(key) + '\n' + str(self.__getitem__(key)) + '\n'
        return output

